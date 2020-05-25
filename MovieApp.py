import tkinter
import requests
from PIL import Image, ImageTk
from config import api_key

url = "http://www.omdbapi.com/?apikey=" + api_key + "&t="
data = ""

root = tkinter.Tk()
root.winfo_toplevel().wm_geometry("")
root.geometry("1000x600")
root.title("MovieApp")

def get_series():
    series = search.get()
    data = requests.get(url+series).json()

    search.destroy()
    search_btn.destroy()

    f = open('poster.jpg','wb')
    f.write(requests.get(data["Poster"]).content)
    f.close()

    canvas = tkinter.Canvas(root, width=300, height=400)
    im = Image.open("poster.jpg")
    canvas.image = ImageTk.PhotoImage(im)
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    canvas.pack(side=tkinter.LEFT)
    
    tkinter.Label(root, text=data["Title"], font=("Helvetica", 25)).pack(side=tkinter.TOP)

    info_list = tkinter.Listbox(root, width=0, height=30, bd=0)
    info_list.insert(tkinter.END, "Years: "+data["Year"])
    info_list.insert(tkinter.END, "Released: "+data["Released"])
    info_list.insert(tkinter.END, "Writers: "+data["Writer"])
    info_list.insert(tkinter.END, "Plot: "+data["Plot"])
    info_list.insert(tkinter.END, "Languages: "+data["Language"])
    info_list.insert(tkinter.END, "Countries: "+data["Country"])
    info_list.pack(side=tkinter.RIGHT)

    root.update()

search = tkinter.Entry(root)
search.pack()

search_btn = tkinter.Button(root, text="Search", command=get_series)
search_btn.pack()

root.mainloop()