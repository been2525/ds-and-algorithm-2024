# file : ds27_Sierprinski.py
# desc : 시에르핀 삼각형 그리기

from tkinter import *
import random

def drawTriangle(x, y, size):
    if size >= 30:
        drawTriangle(x, y, size/2)# 왼쪽 아래 삼각
        drawTriangle(x+size/2, y, size/2) # 오른쪽 아래 삼각
        drawTriangle(x+size/4, int(y-size*(3**0.5)/4), size/2) # 위쪽 작은삼각
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2, fill='red', outline='red')

# 전역변수
wSize = 1000

# 메인코드
window = Tk()
window.title('시에르핀 삼각형 그리기')
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawTriangle(wSize/5, wSize/5*4, wSize*2/3)

canvas.pack()
window.mainloop()