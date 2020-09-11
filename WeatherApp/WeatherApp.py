from tkinter import *
from tkinter import messagebox
import requests
import json
from PIL import ImageTk, Image
from datetime import date

def getWeather():
    try:
        name = city_field.get()
        url = "https://api.openweathermap.org/data/2.5/weather?appid=5b0320570c420edbea631ccbceabc331&units=metric&q=" + name
        api_req = requests.get(url)
        api = json.loads(api_req.content)
        if api["cod"] != "404":

            description = api['weather'][0]["description"]
            icon = api['weather'][0]["icon"]
            cityName= api["name"]
            main = api['main']
            temp = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            country = api["sys"]["country"]
            img = Image.open("C:/Users/Sandeep/Desktop/Python/WeatherApp/OpenWeatherImages/" + str(icon) + "@4x.png")
            img = img.resize((100, 100), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            global panel
            panel= Label(root, image=img,bg="gray")
            panel.configure(image=img, width=img.width(), height=img.height())
            panel.image = img
            temp_field.insert(5, str(temp) + " Celsius")
            atm_field.insert(5, str(pressure) + " hPa")
            desc_field.insert(5, str(description))
            humid_field.insert(5, str(humidity) + "%")
            global text
            text = Label(root, text="Current Weather in " + cityName + " " + country ,bg="gray")
            panel.grid(row=1, column=2, sticky="E", rowspan=4, padx=5, pady=5)
            text.grid(row=2, column=1, sticky="W")

            timestamp = date.fromtimestamp(api["dt"])
            global statusBar
            statusBar= Label(root, text="Date: " + str(timestamp), anchor=W, font="Times 10 italic",bg="gray")
            statusBar.grid(row=7,column=2)
            city_field.delete(0, END)
            btn['state'] = DISABLED
            btn1["state"] = NORMAL
        else:
            messagebox.showerror("Error", "City Not Found \n"
                                          "Please enter valid city name")
            city_field.delete(0, END)
    except Exception as e:
        api = "Error"


def clearAll():
    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)
    text.destroy()
    panel.destroy()
    statusBar.destroy()
    # set focus on the city_field entry box
    city_field.focus_set()
    btn['state'] = NORMAL
if __name__ == "__main__":
    root = Tk()
    root.title("Weather App")
    root.iconbitmap("C:/Users/Sandeep/Desktop/Python/WeatherApp/favicon.ico")
    root.configure(bg="gray")
    root.minsize(width=585, height=300)
    root.maxsize(width=585, height=300)
    headlabel = Label(root, text="Weather Application", bg="DeepSkyBlue", fg="black",font="none 10 bold")
    label1 = Label(root, text="\nCity name : \n",bg="gray")
    text = Label(root, text="",bg="gray")
    label2 = Label(root, text="Temperature : \n",bg="gray")
    label3 = Label(root, text="Pressure : \n",bg="gray")
    label4 = Label(root, text="Humidity : \n",bg="gray")
    label5 = Label(root, text="Description  : \n",bg="gray")

    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0, sticky="E", ipadx="30")
    text.grid(row=2, column=1, sticky="W")
    label2.grid(row=3, column=0, sticky="E", ipadx="30")
    label3.grid(row=4, column=0, sticky="E", ipadx="30")
    label4.grid(row=5, column=0, sticky="E", ipadx="30")
    label5.grid(row=6, column=0, sticky="E", ipadx="30")

    city_field = Entry(root,bg="SlateGray",fg="white")
    city_field.insert(0, "Enter City Name")

    temp_field = Entry(root, bg="black", fg="white")
    atm_field = Entry(root, bg="black", fg="white")
    humid_field = Entry(root, bg="black", fg="white")
    desc_field = Entry(root, bg="black", fg="white")

    city_field.grid(row=1, column=1, ipadx="100")
    temp_field.grid(row=3, column=1, ipadx="100")
    atm_field.grid(row=4, column=1, ipadx="100")
    humid_field.grid(row=5, column=1, ipadx="100")
    desc_field.grid(row=6, column=1, ipadx="100")
    btn = Button(root, text="Get Weather", command=getWeather, bg="teal", activebackground="black",
                 activeforeground="white")
    btn.grid(row=7, column=1,pady=5, padx=10)
    btn1 = Button(root, text="Clear All", command=clearAll, bg="aquamarine",activebackground="black",activeforeground="black")
    btn1.grid(row=7, column=0, pady=5, padx=10)
    btn1["state"]=DISABLED
    root.mainloop()
