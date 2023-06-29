import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config
from tkinter import *
import customtkinter

owm = OWM('69be55df671a26b648a0b198c0739f9e')
config_dict = get_default_config()
config_dict['language'] = 'ru'
mgr = owm.weather_manager()


def gettext():
    try:
        observation = mgr.weather_at_place(textbox.get('1.0', END))
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        print(temp)
    except pyowm.commons.exceptions.NotFoundError:
        print("Не поняла")


app = customtkinter.CTk()
app.title("weather")
app.geometry("400x150")


textbox = customtkinter.CTkTextbox(app)
label = customtkinter.CTkLabel(app, text="Введите город")
button = customtkinter.CTkButton(app, text="Принять", command=gettext)

label.grid(padx=10, pady=10)
textbox.grid(padx=10, pady=10)
button.grid(padx=50, pady=10)

app.mainloop()
