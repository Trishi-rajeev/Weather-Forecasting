from tkinter import *
import tkinter as tk
from tkinter import messagebox  # Import messagebox from tkinter
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
import pytz
from PIL import Image, ImageTk
from datetime import datetime, timedelta

# Initialize main window
root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False, False)

def get_weather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="your_app_name_here")  # Update the user agent string
    try:
        location = geolocator.geocode(city)
        if location is None:
            raise ValueError("Location not found")
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        timezone.config(text=f"Timezone: {result}")
        long_lat.config(text=f"Coordinates: {round(location.latitude, 4)}N, {round(location.longitude, 4)}E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=f"Local Time: {current_time}")

        # Weather
        api = f"http://api.openweathermap.org/data/2.5/onecall?lat={location.latitude}&lon={location.longitude}&exclude=hourly,minutely&appid=api_id_from_open_weather_app&units=metric"

        json_data = requests.get(api).json()

        if json_data.get('cod') == 200:
            # Current weather data
            temp = json_data['current']['temp']
            humidity = json_data['current']['humidity']
            pressure = json_data['current']['pressure']
            wind_speed = json_data['current']['wind_speed']
            description = json_data['current']['weather'][0]['description']

            # Update weather labels
            t.config(text=f"{temp} °C")
            h.config(text=f"{humidity} %")
            p.config(text=f"{pressure} hPa")
            w.config(text=f"{wind_speed} m/s")
            d.config(text=f"{description}")

            daily_data = json_data['daily']
            firstdayimage = daily_data[0]['weather'][0]['icon']
            print(firstdayimage)
            
            # Days
            days = [datetime.now() + timedelta(days=i) for i in range(7)]
            day_labels = [day1, day2, day3, day4, day5, day6, day7]

            for i, day in enumerate(days):
                day_labels[i].config(text=day.strftime("%A"))

        else:
            messagebox.showerror("Error", "City not found")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Icon
image_icon = PhotoImage(file="c:/Users/Admin/Downloads/1680757947232weather-forecast-images/weather forecast images/Images/logo.png")
root.iconphoto(False, image_icon)

round_box = PhotoImage(file="c:/Users/Admin/Downloads/1680757947232weather-forecast-images/weather forecast images/Images/Rounded Rectangle 1.png")
Label(root, image=round_box, bg="#57adff").place(x=30, y=110)

# Labels
Label1 = Label(root, text="Temperature", font=('Helvetica', 11), fg="white", bg="#203243")
Label1.place(x=50, y=120)

Label2 = Label(root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243")
Label2.place(x=50, y=140)

Label3 = Label(root, text="Pressure", font=('Helvetica', 11), fg="white", bg="#203243")
Label3.place(x=50, y=160)

Label4 = Label(root, text="Wind Speed", font=('Helvetica', 11), fg="white", bg="#203243")
Label4.place(x=50, y=180)

Label5 = Label(root, text="Description", font=('Helvetica', 11), fg="white", bg="#203243")
Label5.place(x=50, y=200)

# Search Box
search_image = PhotoImage(file="c:/Users/Admin/Downloads/1680757947232weather-forecast-images/weather forecast images/Images/Rounded Rectangle 3.png")
myimage = Label(image=search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="c:/Users/Admin/Downloads/1680757947232weather-forecast-images/weather forecast images/Images/Layer 7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

search_icon = PhotoImage(file="c:/Users/Admin/Downloads/1680757947232weather-forecast-images/weather forecast images/Images/Layer 6.png")
search_button = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=get_weather)
search_button.place(x=645, y=125)

# Bottom box
Frame = Frame(root, width=900, height=180, bg="#212120")
Frame.pack(side=BOTTOM)

# Bottom boxes
firstbox = PhotoImage(file="c:/Users/Admin/Downloads/1680757947232weather-forecast-images/weather forecast images/Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="c:/Users/Admin/Downloads/1680757947232weather-forecast-images/weather forecast images/Images/Rounded Rectangle 2 copy.png")

Label(Frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(Frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(Frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(Frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(Frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(Frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(Frame, image=secondbox, bg="#212120").place(x=800, y=30)

# Clock (time display)
clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
clock.place(x=30, y=20)

# Timezone
timezone = Label(root, font=("Helvetica", 10, 'bold'), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 10, 'bold'), fg="white", bg="#57adff")
long_lat.place(x=700, y=40)

# Weather details labels
t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)

h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)

p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)

w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)

d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)

# First cell
firstframe = tk.Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=35, y=315)
day1 = Label(firstframe, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=5)
firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)

# Second cell
secondframe = tk.Frame(root, width=70, height=115, bg="#282829")
secondframe.place(x=305, y=325)
day2 = Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=10, y=5)
secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=7, y=20)

# Third cell
thirdframe = tk.Frame(root, width=70, height=115, bg="#282829")
thirdframe.place(x=405, y=325)
day3 = Label(thirdframe, bg="#282829", fg="#fff")
day3.place(x=10, y=5)
thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=7, y=20)

# Fourth cell
fourthframe = tk.Frame(root, width=70, height=115, bg="#282829")
fourthframe.place(x=505, y=325)
day4 = Label(fourthframe, bg="#282829", fg="#fff")
day4.place(x=10, y=5)
fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=7, y=20)

# Fifth cell
fifthframe = tk.Frame(root, width=70, height=115, bg="#282829")
fifthframe.place(x=605, y=325)
day5 = Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=10, y=5)
fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=7, y=20)

# Sixth cell
sixthframe = tk.Frame(root, width=70, height=115, bg="#282829")
sixthframe.place(x=705, y=325)
day6 = Label(sixthframe, bg="#282829", fg="#fff")
day6.place(x=10, y=5)
sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=7, y=20)

# Seventh cell
sevframe = tk.Frame(root, width=70, height=115, bg="#282829")
sevframe.place(x=805, y=325)
day7 = Label(sevframe, bg="#282829", fg="#fff")
day7.place(x=10, y=5)
sevenimage = Label(sevframe, bg="#282829")
sevenimage.place(x=7, y=20)

root.mainloop()
