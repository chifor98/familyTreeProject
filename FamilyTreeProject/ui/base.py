import reflex as rx

from .navbar import navbar_dropdown

def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    if not isinstance(child,rx. Component):
        child = rx.heading("this is not a valid child element")
    return rx.fragment(
        navbar_dropdown(),
        rx.box(
            child,
            bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
            id="my-content-area-el",
        ),
        child,
        rx.logo(),
        rx.color_mode.button(position="bottom-left", id='my-light-mode-btn'), 
        padding='10em',
        id="my-base-container",
    )
