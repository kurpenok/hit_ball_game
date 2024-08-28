#!/usr/bin/env python3

import time
from tkinter import Canvas, Tk

from ball import Ball
from paddle import Paddle


def close_window(event):
    tk.destroy()


if __name__ == "__main__":
    tk = Tk()
    tk.title("Hit Ball!")
    tk.bind("<q>", close_window)
    tk.resizable(False, False)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()

    paddle = Paddle(canvas, "blue")
    ball = Ball(canvas, paddle, "red")

    while True:
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
