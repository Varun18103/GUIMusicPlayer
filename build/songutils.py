from pygame import *
from tkinter import filedialog

songList = []
songIndex = -1


# C:\Users\shams\Desktop\Songs\bedard.mp3

def loadsingle():
    global songIndex
    path = filedialog.askopenfilename()
    songList.append(path)
    songIndex = songIndex + 1
    mixer.init()
    mixer.music.load(songList[songIndex])
    print(songIndex)
    print(songList[songIndex])


def play():
    if mixer.music.get_pos() > 0:
        mixer.music.unpause()
    else:
        mixer.music.play()


def pause():
    mixer.music.pause()


def stop():
    mixer.music.stop()


def loadPlaylist():
    global songIndex
    songList.clear()
    songIndex = 0
    filePaths = filedialog.askopenfilenames()
    for fileName in filePaths:
        songList.append(fileName)
    mixer.init()
    mixer.music.load(songList[songIndex])
    mixer.music.play()
    print(songList)


def nextSong():
    global songIndex
    songIndex = songIndex + 1
    if (songIndex >= len(songList)):
        songIndex = 0
    mixer.music.load(songList[songIndex])
    mixer.music.play()


def prevSong():
    global songIndex
    songIndex = songIndex - 1
    if (songIndex < 0):
        songIndex = len(songList)-1
    mixer.music.load(songList[songIndex])
    mixer.music.play()


# if __name__ == '__main__':
#    while True:
#        print("1.Load Single 2.Play 3.Pause 4.Stop 5.Load Playlist 6.Next 7.Previous")
#        ch = int(input(""))
#        if ch == 1:
#            loadsingle()
#        elif ch == 2:
#            play()
#        elif ch == 3:
#            pause()
#        elif ch == 4:
#            stop()
#        elif ch == 5:
#            loadPlaylist()
#       elif ch == 6:
#            nextSong()
#        elif ch == 7:
#            prevSong()