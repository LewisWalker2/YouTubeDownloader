import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_bar.pack(pady=(10, 5))
    (progress_label.pack(pady=(10, 5)))
    status_label.pack(pady=(10, 5))

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()
        title = ctk.CTkLabel(content_frame, text=f"{yt.title}")
        title.pack(pady=(10, 5))

        #download the video into a specific directory
        os.path.join("Downloads", f"{yt.title}.mp4")
        stream.download(output_path="Downloads")
        status_label.configure(text=f"Downloaded", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error{str(e)}", text_color="white", fg_color="red")


def on_progress(stream, chunk, byte_remaining):
    total_size = stream.filesize
    byte_downloaded = total_size - byte_remaining
    percentage_completed = byte_downloaded/total_size * 100

    progress_label.configure(text= str(int(percentage_completed)) + "%")
    progress_label.update()

    progress_bar.set(float(percentage_completed / 100))


# create a root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# title of the window
root.title("Youtube Downloader By Lewis")

# set min and max width and the height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

# create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady = 10)

# create a label and the entry widget from the video url
url_label = ctk.CTkLabel(content_frame, text="Enter the YouTube Link: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10, 5))
entry_url.pack(pady=(10, 5))

# create a download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=(10, 5))

# create a resoulution combo box
resolution = ["720p", "360p", "240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolution, textvariable=resolution_var)
resolution_combobox.pack(pady=(10, 5))
resolution_combobox.set("720p")


# create a label and the progress bar to display the download progress
progress_label = ctk.CTkLabel(content_frame, text="0%")

#progress_label.pack(pady=(10, 5))
progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)
#progress_bar.pack(pady=(10, 5))


# create a status label
status_label = ctk.CTkLabel(content_frame, text="")
#status_label.pack(pady=(10, 5))




#to start the app
root.mainloop()