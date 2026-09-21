import reflex as rx
from app.config import *
from app.components import *


def History()->rx.Component:
    return rx.box(
        panel_header("History","History"),
        
        
        
        
        
        
        
        
        bg=section_bg,
        border_radius="5px",
        width="35%",
        height="100%")