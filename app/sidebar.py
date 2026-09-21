import reflex as rx 
from app.config import *
from app.components import dark_mode_toggle





def sidebar()->rx.Component:
    return rx.box(

        rx.hstack(
            rx.flex(
                rx.heading("Rag Application"),
                align="center",
                height="100%",
                padding="1em"
                ),

                rx.flex(
                dark_mode_toggle(),
                align="center",
                height="100%",
                padding="1em",
                justify="end",
                spacing="5",
                flex="1"
            )
        ),



        border_radius="10px",
        width="100%",
        height="60px"
    )