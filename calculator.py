import tkinter


button_value=[
    ["AC","DEL","%","π"],
    ["7","8","9","X"],
    ["4","5","6","-"],
    ["1","2","3","+"],
    ["0",".","+/-","="]
]
right_symbol=["X","-","+","="]
top_symbol=["AC","DEL","%","π"]

row_count=len(button_value) #5
column_count=len(button_value[0]) #4

#Background:
color_dark_charcoal="#1C1C1E"

#Number Keys:
color_light_gray="#3A3A3C"

#Function Keys (+, −, ×, ÷):
color_bright_color ="#FF9F0A"

#Clear/Modifier Keys (AC, +/-, %):
color_slate_gray="#A5A5A5"


#window setup
window=tkinter.Tk()
window.title("Calculator")
window.resizable(False,False)

frame=tkinter.Frame(window,bg=color_dark_charcoal)
label=tkinter.Label(frame,text="0",bg=color_dark_charcoal,fg="white",font=("Arial",30),anchor="e"
                    ,width=column_count)

label.grid(row=0,column=0,columnspan=column_count,sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value=button_value[row][column]
        button=tkinter.Button(frame,text=value,bg=color_dark_charcoal,fg="white",font=("Arial",30),
                              width=column_count-1,height=1,
                              command=lambda value=value:button_clicked(value))
        if value in top_symbol:
            button.config(bg=color_slate_gray)
        elif value in right_symbol:
            button.config(bg=color_bright_color)
        else:
            button.config(bg=color_light_gray)


        button.grid(row=row+1,column=column,sticky="nsew",padx=1,pady=1)

frame.pack()

A="0"
operator=None
b=None

def clear_all():
    global A,B,operator
    A="0"
    B=None
    operator=None

def remove_zero_decimal(result):
    if result%1==0:
        return int(result)
    else:
        return result

def button_clicked(value):
    global right_symbol,top_symbol,A,operator,b

    if value in right_symbol:
        pass
    elif value in top_symbol:
        if value=="AC":
            clear_all()
            label["text"]="0"

        elif value == "DEL":
            text = label["text"]
            if len(text) > 1:
                text = text[:-1]
                if text == "-" or text == "":
                    text = "0"
            else:
                text = "0"

            label["text"] = text

        elif value=="%":
            result=float(label["text"])/100
            label["text"]=str(remove_zero_decimal(result))
        
        elif value == "π":
            if label["text"] == "0":
                label["text"] = "3.1415"
            else:
                label["text"] += "×3.1415"  # or however you want to chain it
    else: #digit or dot
        if value ==".":
            if "." not in label["text"]:
                label["text"]+=value

        elif value=="+/-":
            result=float(label["text"])*-1
            label["text"]=str(remove_zero_decimal(result))
        elif value in "0123456789":
            if label["text"]=="0":
                label["text"]=value
            else:
                label["text"]+=value


#center the window
window.update() #update the window to gets the new size dimesnsion
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()

window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(window_height/2))

#FORMAT "(width) x (height) +(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()