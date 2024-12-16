from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Button
from bot.states.states import StartSG


start_dialog = Dialog(
    Window(
        Const("This is a bot template"),
        Button(Const("Plug button"), id="plug_button"),
        state=StartSG.START,
    ),
)
