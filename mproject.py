import speedtest  
from tkinter import *

def checkSpeed():
    try:
        sp = speedtest.Speedtest()  # Corrected the class name
        sp.get_best_server()
        download_speed = str(round(sp.download() / (10 ** 6), 3)) + " Mbps"
        upload_speed = str(round(sp.upload() / (10 ** 6), 3)) + " Mbps"
        label_down.config(text=download_speed)
        label_up.config(text=upload_speed)
    except Exception as e:
        label_down.config(text="Error: " + str(e))
        label_up.config(text="Error: " + str(e))

st = Tk()
st.title("Internet Speed Test")
st.geometry("500x650")
st.config(bg="Black")

label = Label(st, text="Internet Speed Test", font=("Times New Roman", 33, "bold"), bg="Black", fg="White")
label.place(x=60, y=40, height=50, width=380)

label = Label(st, text="Download Speed", font=("Times New Roman", 25, "bold"), bg="Black", fg="White")
label.place(x=40, y=130, height=50, width=380)

label_down = Label(st, text="00", font=("Times New Roman", 25, "bold"))
label_down.place(x=40, y=200, height=50, width=380)

label = Label(st, text="Upload Speed", font=("Times New Roman", 25, "bold"), bg="Black", fg="White")
label.place(x=40, y=290, height=50, width=380)

label_up = Label(st, text="00", font=("Times New Roman", 25, "bold"))
label_up.place(x=40, y=360, height=50, width=380)

check = Button(st, text="Check Speed", font=("Times New Roman", 25, "bold"), relief=RAISED, bg="Red", fg="Black", command=checkSpeed) 
check.place(x=40, y=460, height=50, width=380)

st.mainloop()
