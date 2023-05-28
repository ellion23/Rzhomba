import pyautogui as pag
from random import randint
from time import sleep
import tkinter as tk
import pyaudio
import wave
import threading
import pkg_resources
from PIL import Image, ImageTk

pag.FAILSAFE = False

# Build .exe
# pyinstaller --name=hello_mir --add-data="hello_mir.wav;." --add-data="hello_mir.ico;." --add-data="hello_mir.gif;." --ico "hello_mir.ico" --onefile --windowed hello_mir.py

def play_audio():
    while True:
        chunk = 1024
        sound = pkg_resources.resource_filename("__main__", "hello_mir.wav")
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


def update_image(canvas, frame_index):
    global frames
    global nframes
    while True:
        frame = frames[frame_index]
        canvas.create_image(0, 0, anchor=tk.NW, image=frame)

        frame_index += 1
        if frame_index == nframes:
            frame_index = 0
        sleep(0.1)


def create_window():
    root = tk.Tk()
    icon = pkg_resources.resource_filename("__main__", "hello_mir.ico")
    root.iconbitmap(icon)
    #
    # start
    #
    global nframes
    global gif
    global frames
    for i in range(nframes):
        gif.seek(i)
        frames.append(ImageTk.PhotoImage(gif))

    canvas = tk.Canvas(root, width=388, height=388)
    canvas.pack()

    frame_index = 0

    thread_img = threading.Thread(target=update_image, args=(canvas, frame_index))
    thread_img.start()

    #
    # end
    #
    root.title("Манера крутит мир")
    thread = threading.Thread(target=move, args=(root,))
    root.geometry(f'+{randint(1, 1500)}+{randint(1, 800)}')
    thread.start()
    root.mainloop()


if __name__ == "__main__":
    gif_path = pkg_resources.resource_filename("__main__", "hello_mir.gif")
    gif = Image.open(gif_path)
    frames = []
    nframes = gif.n_frames

    # thread1 = threading.Thread(target=mouse)
    thread2 = threading.Thread(target=play_audio)

    # thread1.start()
    thread2.start()
    l = threading.Thread(target=create_window)
    l.start()

    # thread1.join()
    thread2.join()
