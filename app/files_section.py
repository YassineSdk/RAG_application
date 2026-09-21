import reflex as rx 
from app.config import *
from app.components import *


def Files()->rx.Component:
    return rx.box(
        panel_header("Sources","file_text"),
            rx.hstack(
                rx.icon("plus",size=18),

                rx.button("add source",
                size="3",
                variant="soft",
                color_scheme="green",
                width="90%",
                radius="small"
                ),
                
            spacing="2",  
            align="center",
            width="100%"
                ),



        bg=section_bg,
        border_radius="5px",
        width="35%",
        height="100%")