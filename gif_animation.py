import tkinter as tk
from PIL import Image, ImageTk
import threading
from time import sleep


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


root = tk.Tk()
gif = Image.open('hello_mir.gif')
frames = []

nframes = gif.n_frames

for i in range(nframes):
    gif.seek(i)
    frames.append(ImageTk.PhotoImage(gif))


canvas = tk.Canvas(root, width=388, height=388)
canvas.pack()

frame_index = 0

thread = threading.Thread(target=update_image, args=(canvas, frame_index))
thread.start()
root.mainloop()
