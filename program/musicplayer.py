import os

import tkinter

import tkinter.filedialog

import random

import time

import threading

import pygame

folder = ''

def play():

    # folder用来表示存放MP3音乐文件的文件夹

    global folder

    

    musics = [folder+'\\'+music

              for music in os.listdir(folder) \

              if music.endswith(('.mp3', '.wav', '.ogg'))]

    

    # 初始化混音器设备

    pygame.mixer.init()

    while playing:

        if not pygame.mixer.music.get_busy():

            # 随机播放一首歌曲

            nextMusic = random.choice(musics)

            pygame.mixer.music.load(nextMusic.encode())

            # 播放一次

            pygame.mixer.music.play(1)

            musicName.set('playing....'+nextMusic)

        else:

            time.sleep(0.3)

                

root = tkinter.Tk()

root.title('音乐播放器v1.0---董付国')

root.geometry('280x70+400+300')

root.resizable(False, False)

# 关闭程序时执行的代码

def closeWindow():

    # 修改变量，结束线程中的循环

    global playing

    playing = False

    time.sleep(0.3)

    

    try:

        # 停止播放，如果已停止，

        # 再次停止时会抛出异常，所以放在异常处理结构中

        pygame.mixer.music.stop()

        pygame.mixer.quit()

    except:

        pass

    root.destroy()

root.protocol('WM_DELETE_WINDOW', closeWindow)

pause_resume = tkinter.StringVar(root, value='NotSet')

playing = False

# 播放按钮

def buttonPlayClick():

    # 选择要播放的音乐文件夹

    global folder

    if not folder:

        folder = tkinter.filedialog.askdirectory()

    if not folder:

        return

    

    global playing

    playing = True

    # 创建一个线程来播放音乐，当前主线程用来接收用户操作

    t = threading.Thread(target=play)

    t.start()

    

    # 根据情况禁用和启用相应的按钮

    buttonPlay['state'] = 'disabled'

    buttonStop['state'] = 'normal'

    buttonPause['state'] = 'normal'    

    buttonNext['state'] = 'normal'

    

    pause_resume.set('Pause')

buttonPlay = tkinter.Button(root,

                            text='Play',

                            command=buttonPlayClick)

buttonPlay.place(x=20, y=10, width=50, height=20)

# 停止按钮

def buttonStopClick():

    global playing

    playing = False

    

    pygame.mixer.music.stop()

    musicName.set('暂时没有播放音乐')

    buttonPlay['state'] = 'normal'

    buttonStop['state'] = 'disabled'

    buttonPause['state'] = 'disabled'

    buttonNext['state'] = 'disabled'

    global folder

    folder = ''

buttonStop = tkinter.Button(root,

                            text='Stop',

                            command=buttonStopClick)

buttonStop.place(x=80, y=10, width=50, height=20)

buttonStop['state'] = 'disabled'

# 暂停与恢复，两个功能共用一个按钮

def buttonPauseClick():

    if pause_resume.get() == 'Pause':

        pygame.mixer.music.pause()

        pause_resume.set('Resume')

    elif pause_resume.get() == 'Resume':

        pygame.mixer.music.unpause()

        pause_resume.set('Pause')

buttonPause = tkinter.Button(root,

                             textvariable=pause_resume,

                             command=buttonPauseClick)

buttonPause.place(x=140, y=10, width=50, height=20)

buttonPause['state'] = 'disabled'

# 下一首音乐

def buttonNextClick():

    global playing

    playing = False

    pygame.mixer.music.stop()

    pygame.mixer.quit()

    buttonPlayClick()

buttonNext = tkinter.Button(root,

                            text='Next',

                            command=buttonNextClick)

buttonNext.place(x=200, y=10, width=50, height=20)

buttonNext['state'] = 'disabled'

musicName = tkinter.StringVar(root,

                              value='暂时没有播放音乐...')

labelName = tkinter.Label(root,

                          textvariable=musicName)

labelName.place(x=0, y=40, width=270, height=20)

# 启动消息循环

root.mainloop()