import tkinter as tk
from pytube import YouTube
import time

root = tk.Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title("POGCHAMP YOUTUBE DOWNLOADER")


title_label=tk.Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()


yt_link = tk.StringVar()

link_label=tk.Label(root, text = 'DROP THE LINK HERE: ', font = 'arial 15 bold').place(x= 32 , y = 60)
yt_link_enter = tk.Entry(root, width = 70,textvariable = yt_link).pack(fill=tk.X,pady=60)


def Yt_Downloader():
    try:
        yt_url =YouTube(str(yt_link.get()))
        yt_video = url.streams.first()
        yt_video.download()
        finished=tk.Label(root, text = 'DOWNLOADED COMPLETE  POGGERS!', font = 'arial 15').place(x= 50 , y = 210)
    except:
        error=tk.Label(root,text="You have either put in a wrong URL or you didn't enter anything.Please try again with a valid youtube video URL.")




button=tk.Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'white', padx = 5,pady=5, command = Yt_Downloader).pack(fill=tk.X,pady=20)



root.mainloop()
