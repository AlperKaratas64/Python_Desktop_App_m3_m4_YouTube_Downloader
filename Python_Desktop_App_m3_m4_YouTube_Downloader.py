import pytube
import os
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("700x500+350+100")
window.title("YOUTUBE İNDİRİCİ")
window.configure(bg="black")

def show_downloading_message(format_choice):
    if format_choice == "mp3":
        messagebox.showinfo(title="Downloader", message="İndiriliyor... Lütfen bekleyin. MP3 olarak indirilecek.")
    else:
        messagebox.showinfo(title="Downloader", message="İndiriliyor... Lütfen bekleyin. Yüksek kalitede indirilecek.")

def download_video(format_choice):
    try:
        url = my_entry.get()
        path = "Desktop"

        video = pytube.YouTube(url)
        
        show_downloading_message(format_choice)  # İndirme işlemi başlamadan önce mesajı göster

        if format_choice == "mp3":
            streams = video.streams.filter(only_audio=True)
            stream = streams.first()
            stream.download(path)
            original_file_path = os.path.join(path, stream.default_filename)
            new_file_path = os.path.splitext(original_file_path)[0] + ".mp3"
            os.rename(original_file_path, new_file_path)
            messagebox.showinfo(title="Downloader", message="MP3 olarak indirildi.")
        else:
            highest_res_stream = video.streams.get_highest_resolution()
            highest_res_stream.download(path)
            messagebox.showinfo(title="Downloader", message="Yüksek kalitede indirildi.")

    except:
        messagebox.showerror(title="Error", message="Uygulamayı yeniden başlatın.")

def add_spacing(x):
    frame = Frame()
    frame.pack(pady=x)

add_spacing(50)

label = Label(text="YOUTUBE URL'Sİ GİRİN:", font="Kablammo", fg="red", bg="black")
label.pack()

add_spacing(10)

my_entry = Entry(width=50)
my_entry.pack()

add_spacing(20)

mp3_button = Button(text="Download as MP3", width=20, height=2, fg="red", bg="black", command=lambda: download_video("mp3"))
mp3_button.pack()

high_quality_button = Button(text="Download in High Quality", width=20, height=2, fg="red", bg="black", command=lambda: download_video("mp4"))
high_quality_button.pack()

window.mainloop()
