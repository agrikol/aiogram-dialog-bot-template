from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram_dialog import DialogManager, StartMode
from bot.states.states import StartSG
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram_dialog.api.entities import ShowMode

commands_router: Router = Router()


@commands_router.message(CommandStart())
async def process_start_command(
    message: Message,
    dialog_manager: DialogManager,
) -> None:
    await dialog_manager.start(
        StartSG.START, mode=StartMode.RESET_STACK, show_mode=ShowMode.DELETE_AND_SEND
    )
