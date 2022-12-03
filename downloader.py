from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as MsgBox
from pytube import YouTube
from pytube import Playlist

import shutil


#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    user_path = path_label.cget("text")
    if "playlist?" in get_link:
        plist = Playlist(get_link)
        screen.title('Downloading Playlist:'+plist.title)
        for url in plist.video_urls:
            mp4_video = YouTube(url).streams.get_highest_resolution().download()
    	    #move file to selected directory
            shutil.move(mp4_video, user_path)
        MsgBox.showinfo('提示','Download all videos of this playlist completely!')
    else:
        screen.title('Downloading single video...')
        #Download Video
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    	#move file to selected directory
        shutil.move(mp4_video, user_path)
        MsgBox.showinfo('提示','Download this video completely!')

screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#image logo
logo_img = PhotoImage(file='yt.png')
#resize
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

#link field
link_field = Entry(screen, width=40, font=('Arial', 15) )
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))

#Select Path for saving the file
path_label = Label(screen, text="", font=('Arial', 15))
path_label_title = Label(screen, text="File saving path:", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#000', command=select_path)
#Add to window
canvas.create_window(300, 280, window=path_label)
canvas.create_window(100, 280, window=path_label_title)
canvas.create_window(250, 330, window=select_btn)

#Add widgets to window 
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#000', command=download_file)
#add to canvas
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
