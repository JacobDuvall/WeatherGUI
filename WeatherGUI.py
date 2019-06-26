import tkinter as tk  # GUI for project
import requests  # used to make web requests
from PIL import Image, ImageTk  # used for icons

# format the string to display after searching for a city
# @weather_json - the json file returned from weather API
def format_response(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (city, conditions, temp)
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str


# request weather from weather API
# @city - the city to search from the weather API
def get_weather(city):
    weather_key = '1eac61168b8d6a2fc184d0165a89ee2a'  # my personal key
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': 'edffd1bf975a74d5d10e58c5ac8be2d3', 'q': city, 'units': 'imperial'}  # dictionary used to query
    response = requests.get(url, params=params)  # ask API for the goods
    print(response.json())
    weather_json = response.json()

    results['text'] = format_response(response.json())

    icon_name = weather_json['weather'][0]['icon']  # The correct icon to display
    open_image(icon_name)


# display the icon for the current weather in the current city
# @icon - the name of the icon used to search saved icon images
def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('C:/Users/jdduval1/PycharmProjects/WeatherGUI/img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


app = tk.Tk()  # the tk window

HEIGHT = 500  # height of window
WIDTH = 600  # width of window

# The main block of code
C = tk.Canvas(app, height=HEIGHT, width=WIDTH)  # the full background canvas
background_image = tk.PhotoImage(file='C:/Users/jdduval1/Desktop/images/landscape.png')  # the background
background_label = tk.Label(app, image=background_image)  # create label and put it inside of the tk app
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()

frame = tk.Frame(app,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

textbox = tk.Entry(frame, font=40)
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather(textbox.get()))
submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

app.mainloop()  # loop and run GUI forever
