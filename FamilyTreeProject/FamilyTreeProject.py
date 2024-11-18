import reflex as rx
from rxconfig import config
from .ui.navbar import navbar_dropdown
from .ui.base import base_page
from . import pages

class State(rx.State):
     """ The app state."""
     label= "Welcome to Reflex!"
     
     def handle_title_input_change(self, val):
         self.label = val
     def did_click(self):
         print("Hello world did click")
         
def index() -> rx.Component:
    return base_page(rx.vstack())

app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, route='/about')