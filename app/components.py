import reflex as rx
from reflex.style import set_color_mode, color_mode


def dark_mode_toggle() -> rx.Component:
    return rx.segmented_control.root(
        rx.segmented_control.item(
            rx.icon(tag="monitor", size=20),
            value="system",
        ),
        rx.segmented_control.item(
            rx.icon(tag="sun", size=20),
            value="light",
        ),
        rx.segmented_control.item(
            rx.icon(tag="moon", size=20),
            value="dark",
        ),
        on_change=set_color_mode,
        variant="classic",
        radius="large",
        value=color_mode,
    )

def panel_header(title:str,icon:str)->rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(title,weight="medium", size="4", color="#e8eaed"),
            rx.icon(icon,size=18),
            width="100%",
            justify="between"
        ),
        rx.divider(),
        padding="1em",
        width="100%",

    )