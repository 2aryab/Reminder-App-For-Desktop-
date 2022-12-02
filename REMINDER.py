from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

t = Tk()
t.title('REMINDER APP FOR 3RD SEMESTER PROGRAMMERS')
t.geometry("500x300")
img = Image.open("notify-label-P.PNG")
tkimage = ImageTk.PhotoImage(img)

def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    # print(get_title,get_msg, tt)

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "PLEASE fill all the feilds !!!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("REMINDER IS SET", "If you are sure press ok to confirm")
        t.destroy()
        time.sleep(min_to_sec)
        

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Reminder",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)
            
img_label = Label(t, image=tkimage).grid()

t_label = Label(t, text="Title to Notify",font=("poppins", 10))
t_label.place(x=12, y=70)


title = Entry(t, width="25",font=("poppins", 13))
title.place(x=123, y=70)


m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)


msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)


time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)


time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=175)


time_min_label = Label(t, text="minutes", font=("poppins", 10))
time_min_label.place(x=175, y=180)


but = Button(t, text="SET REMINDER", font=("poppins", 10, "bold"), fg="#F0F0F8", bg="#F28C28", width=0,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()