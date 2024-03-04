import speedtest
import tkinter as tk
from tkinter import Label, Button

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test")

        self.download_label = Label(root, text="Download Speed: ")
        self.download_label.pack()

        self.upload_label = Label(root, text="Upload Speed: ")
        self.upload_label.pack()

        self.test_button = Button(root, text="Run Speed Test", command=self.run_speed_test)
        self.test_button.pack()

    def run_speed_test(self):
        st = speedtest.Speedtest()
        download_speed = st.download() / 1024 / 1024  # Convert to Mbps
        upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

        self.download_label.config(text=f"Download Speed: {download_speed:.2f} Mbps")
        self.upload_label.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()
