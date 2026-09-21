from app.layout import Layout 
import reflex as rx





def index()-> rx.Component:
    return Layout()




app = rx.App(
    style={
        "font_family": "Inter, sans-serif",
    },
)
app.add_page(index, route="/")

