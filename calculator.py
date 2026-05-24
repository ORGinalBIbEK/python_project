import tkinter


button_value=[
    ["AC","DEL","%","/"],
    ["7","8","9","X"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","+/-","="]
]
right_symbol=["/","X","-","+","="]
top_symbol=["AC","DEL","%"]

row_count=len(button_value) #5
column_count=len(button_value[0]) #4

#Background:
color_dark_charcoal="#1C1C1E"

#Number Keys:
color_light_greay="#3A3A3C"

#Function Keys (+, −, ×, ÷):
color_bright_color ="#FF9F0A"

#Clear/Modifier Keys (AC, +/-, %):
color_slate_gray="#A5A5A5"


#window setup
window=tkinter.Tk()
window.title("Calculator")
window.resizable(False,False)

frame=tkinter.Frame(window,bg=color_dark_charcoal)
label=tkinter.Label(frame,text="0",bg=color_dark_charcoal,fg="white",font=("Arial",30),anchor="e")

label.grid(row=0,column=0)

for row in range(row_count):
    for column in range(column_count):
        value=button_value[row][column]
        button=tkinter.Button(frame,text=value,bg=color_dark_charcoal,fg="white",font=("Arial",30),
                              width=column_count-1,height=1,
                              command=lambda value=value:button_clicked(value))
        button.grid(row=row+1,column=column,sticky="nsew",padx=1,pady=1) 
frame.pack()
def button_clicked(value):
    pass

window.mainloop()