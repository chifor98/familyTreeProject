import reflex as rx
from rxconfig import config
from .pages.navbar import navbar_dropdown


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
def navbar() -> rx.Component:
    return navbar_dropdown()


def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    print([type(x) for x in args])
    return rx.container(
        navbar(),
        child,
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
    )

def index() -> rx.Component:
    return base_page(
        rx.vstack(
        )
    )

app = rx.App()
app.add_page(index)