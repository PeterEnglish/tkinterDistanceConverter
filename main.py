from tkinter import *


window = Tk()
window.configure(bg="lightblue")
window.title("Distance Converter")#must go before mainloop()
window.minsize(350, 120)
def convert():
    option=v.get()
    if (option=="km"):
        km_to_miles()
    else:
        miles_to_km()

def get_first_input():
    return float(first_input.get())

def miles_to_km():
    miles = get_first_input()
    km = round(miles* 1.689, 4)
    result_label.config(text=f"{km} Km")

def km_to_miles():
    km = get_first_input()
    miles = round(km/1.689, 4)
    result_label.config(text=f"{miles} Miles")

option = ""
def selection():
    option = v.get()
    result_label["text"]=0
    if (option=="km"):
        input_label["text"] = "Km"
        result_label["text"]=0
       
    else:
        input_label["text"] = "Miles"
       
        
        

first_input = Entry(bg="white", width=30)
first_input.place(x=60, y=60)
input_label = Label(bg="lightblue", text="Km")
input_label.place(x=250, y=60)
is_equal_label = Label(bg="lightblue", text="Is Equal To:")
is_equal_label.place(x=60, y=90)
result_label = Label(bg="lightblue", text="0 ")
result_label.place(x=150, y=90)

calculate_button = Button(text="Calculate", command=convert, width=30)
calculate_button.place(x=60, y=120)
v = StringVar(value="km")

radio_one = Radiobutton( 
    bg="lightblue",
               text="Km to Miles",
               padx = 20, 
               variable=v, 
               value="km",
               command=selection).place(x=40, y=20)

radio_two = Radiobutton(
               bg="lightblue", 
               text="Miles to Km",
               padx = 20, 
               variable=v, 
               value="miles",
               command=selection).place(x=200, y=20)

window.mainloop() #keeps window on screen

