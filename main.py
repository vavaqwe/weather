import pyowm
from pyowm import OWM
from pyowm.utils.config import get_default_config
from tkinter import *
import customtkinter
from datetime import date, timedelta

owm = OWM('69be55df671a26b648a0b198c0739f9e')
config_dict = get_default_config()
config_dict['language'] = 'uk'
mgr = owm.weather_manager()


def gettext():
    try:
        place =textbox.get('1.0', END).strip()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        print(w)
        temp = w.temperature('celsius')["temp"]
        status = w.detailed_status
        detail_status = f'Температура {str(temp)} {status}'
        label1.configure(text=detail_status)
    except pyowm.commons.exceptions.NotFoundError:
        label1.configure(text="Місто не було знайдено ")
    except pyowm.commons.exceptions.APIRequestError:
        label1.configure(text="Місто не було знайдено ")


app = customtkinter.CTk()
app.title("weather")
app.geometry("240x200")


textbox = customtkinter.CTkTextbox(app, width=200, height=20)
label = customtkinter.CTkLabel(app, text="Введіть місто")
label1 = customtkinter.CTkLabel(app, text="", fg_color="transparent")
button = customtkinter.CTkButton(app, text="Пошук", command=gettext)

label.grid(padx=5, pady=5)
label1.grid(padx=0, pady=0)
textbox.grid(padx=5, pady=5)
button.grid(padx=50, pady=10)
app.mainloop()

today = date.today()
next_week = today + timedelta(weeks=1)