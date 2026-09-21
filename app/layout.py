import reflex as rx 
from app.chat_section import chat
from app.files_section import Files
from app.history_section import History
from app.sidebar import sidebar
from app.config import *

def Layout():
    """
    the application shell 
    """
    return rx.flex(
        sidebar(),
        rx.flex(
            Files(),
            chat(),
            History(),
            direction="row",
            spacing="4",
            flex="1",
            width="100%",
            ),
        bg=app_bg,
        spacing="4",
        padding="1em",
        direction="column",
        height="920px",
        width="100%"
        )
