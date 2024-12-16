import asyncio, logging
from bot.dialogs import dialogs
from bot.db.base import Base
from sqlalchemy import text
from redis.asyncio import Redis
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.client.default import DefaultBotProperties
from bot.config.config_reader import Settings
from bot.handlers.commands import commands_router
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from aiogram_dialog import setup_dialogs


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


async def main():
    config = Settings()

    # Here is the connection to the DB
    engine = create_async_engine(url=str(config.db_dsn), echo=config.is_echo)
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    Sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    # Here is the connection to Redis
    storage = RedisStorage(
        redis=Redis.from_url(str(config.redis_dsn)),
        key_builder=DefaultKeyBuilder(with_destiny=True),
    )

    # Here is bot setup
    dp: Dispatcher = Dispatcher(storage=storage)
    setup_dialogs(dp)
    dp.include_routers(commands_router, *dialogs)
    bot: Bot = Bot(
        token=config.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await asyncio.gather(
            dp.start_polling(bot),
        )
    except Exception as e:
        logger.error(e)
    finally:
        await engine.dispose()
        logger.info("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())
