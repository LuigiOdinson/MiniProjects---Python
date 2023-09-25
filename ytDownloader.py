from pytube import YouTube
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import MessageDialog

pad_x = 40
pad_y = 7
TEXT_FONT = ('Arial Narrow', 18)

win = ttk.Window(themename='darkly')
win.geometry("700x400")
win.title("YtDownloader")

qualities = ["select", "Highest Resolution", "Lowest Resolution"]
qualities_var = ttk.StringVar(win)

# widgets
label1 = ttk.Label(win, text="Paste your Youtube link below:",
                   font=TEXT_FONT)
label1.grid(column=0, row=0, sticky=ttk.W, padx=pad_x, pady=pad_y)

place_holder = ttk.Label(win, text=" "*35, font=TEXT_FONT)
place_holder.grid(column=1, row=0, padx=pad_x, pady=pad_y)

link_input = ttk.Entry(win, font=TEXT_FONT)
link_input.grid(column=0, columnspan=2, row=1, sticky=ttk.EW, padx=pad_x, pady=pad_y)

label2 = ttk.Label(win, text="Enter the path to download to:",
                   font=TEXT_FONT)
label2.grid(column=0, row=2, sticky=ttk.W, padx=pad_x, pady=pad_y)

path_input = ttk.Entry(win, font=TEXT_FONT)
path_input.grid(column=0, columnspan=2, row=3, sticky=ttk.EW, padx=pad_x, pady=pad_y)

label3 = ttk.Label(win, text="Choose the quality:",
                   font=TEXT_FONT)
label3.grid(column=0, row=4, sticky=ttk.W, padx=pad_x, pady=pad_y)

qualities_menu = ttk.OptionMenu(win, qualities_var, *qualities)
qualities_menu.grid(column=0, row=5, sticky=ttk.EW, padx=pad_x, pady=pad_y)


def download():
    link = link_input.get()
    path = path_input.get()
    quality = qualities_var.get()

    info_full = True
    if link == "":
        dialog = MessageDialog("Enter the video link")
        dialog.show()
        info_full = False
    elif path == "":
        dialog = MessageDialog("Select a path")
        dialog.show()
        info_full = False

    yt_video = YouTube(link)

    if info_full:
        if quality == "Highest Resolution":
            yt_video = yt_video.streams.get_highest_resolution()
            print("downloading highest")
        elif quality == "Lowest Resolution":
            yt_video = yt_video.streams.get_lowest_resolution()
            print("downloading lowest")
        else:
            dialog = MessageDialog("Select a quality")
            dialog.show()

        yt_video.download(path)


# buttons
download_button = ttk.Button(win, text="Download", command=download)
download_button.grid(column=1, row=5, sticky=ttk.EW, padx=pad_x, pady=pad_y)

win.mainloop()
