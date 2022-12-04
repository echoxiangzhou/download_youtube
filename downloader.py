from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as MsgBox
from pytube import YouTube
from pytube import Playlist

import shutil

#Functions
def select_path():
    #allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_field.delete(0,"end")
    path_field.insert(0,path)
#    path_label.config(text=path)

def select_url_file():
    #allows user to select a path from the explorer
    filetypes = (
        ('Text Files','*.txt'),
	    ('All Files','*.*')
    )
    path = askopenfilename(filetypes=filetypes)
    if path is not None:
      link_field.delete(0,END)
      url_field.delete(0,END)
      url_field.insert(0,path)

def handle_focus(event):
    if event.widget == link_field:
        url_field.delete(0,END)
    return

def download_video(url):
    print('download video:'+url)
    user_path = path_field.get()
    mp4_video = YouTube(url).streams.get_highest_resolution().download()
    shutil.move(mp4_video, user_path)

def download_file():
    #get user path
    get_link = link_field.get()
    #get selected path
    url_file = url_field.get()
#    print(len(url_file))

    if len(get_link) != 0:
        #url_field.delete(0,END)
        if "playlist?" in get_link:
            plist = Playlist(get_link)
            screen.title('Downloading Playlist:'+plist.title)
            for url in plist.video_urls:
                download_video(url)
            MsgBox.showinfo('提示','Download all videos of this playlist completely!')
        else:
            screen.title('Downloading single video...')
            #Download Video
            download_video(get_link)
    #        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    #        shutil.move(mp4_video, user_path)
            MsgBox.showinfo('提示','Download this video completely!')
        return

    if len(url_file) !=0 :
        with open(url_file,'r') as reader:
            for line in reader:
                line = line.strip() #delete blank line
                download_video(line)
            MsgBox.showinfo('提示', 'Download filelist video completely!')
        return
    MsgBox.showinfo('Information','Please Enter download link or playlist link or Select urlList file!')
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
link_label = Label(screen, text="Download Link: ", font=('Arial', 15))

#urllist file
url_field = Entry(screen, width=40, font=('Arial', 15) )
url_label = Label(screen, text="UrlList File: ", font=('Arial', 15))
url_btn =  Button(screen, text="Select File", width=3, bg='red', padx='20', pady='5',font=('Arial', 15), fg='#000', command=select_url_file)

#Select Path for saving the file
path_field = Entry(screen,width=30, text="", font=('Arial', 15))
path_label_title = Label(screen, text="File saving path:", font=('Arial', 15))
select_btn =  Button(screen, text="Select Path", width=3, bg='red', padx='22', pady='5',font=('Arial', 15), fg='#000', command=select_path)
#Add to window
canvas.create_window(280, 340, window=path_field)
canvas.create_window(70, 340, window=path_label_title)
canvas.create_window(450, 340, window=select_btn)

#Add urllist to window
canvas.create_window(60, 280, window=url_label)
canvas.create_window(290, 280, window=url_field)
canvas.create_window(450, 280, window=url_btn)

#Add widgets to window 
canvas.create_window(70, 220, window=link_label)
canvas.create_window(310, 220, window=link_field)

#Download btns
download_btn = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#000', command=download_file)
#add to canvas
canvas.create_window(250, 430, window=download_btn)

link_field.bind("<FocusIn>",handle_focus)

screen.mainloop()
