import tkinter as tk
import random
from tkinter import PhotoImage
from PIL import Image, ImageTk

window = tk.Tk()

window.title("Slot Machine")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.resizable(False, False)
window["bg"] = "cadetblue3"

canvas = tk.Canvas(window, width=screen_width,
                   height=screen_height, background='cadetblue3')
canvas.pack()


# @@@@@@@@@
# 이미지
# @@@@@@@@@
# 안내박스
cherry_s = ImageTk.PhotoImage(Image.open("imge/cherry_s.png"))
cherry_s_label = tk.Label(window, image=cherry_s, relief="ridge")
cherry_s_label1 = tk.Label(window, image=cherry_s, relief="ridge")
cherry_s_label2 = tk.Label(window, image=cherry_s, relief="ridge")
cherry_s_label3 = tk.Label(window, image=cherry_s, relief="ridge")
cherry_s_label4 = tk.Label(window, image=cherry_s, relief="ridge")
lemon_s = ImageTk.PhotoImage(Image.open("imge/lemon_s.png"))
lemon_s_label = tk.Label(window, image=lemon_s, relief="ridge")
lemon_s_label1 = tk.Label(window, image=lemon_s, relief="ridge")
lemon_s_label2 = tk.Label(window, image=lemon_s, relief="ridge")
lemon_s_label3 = tk.Label(window, image=lemon_s, relief="ridge")
lemon_s_label4 = tk.Label(window, image=lemon_s, relief="ridge")
seveno_s = ImageTk.PhotoImage(Image.open("imge/seveno_s.png"))
seveno_s_label = tk.Label(window, image=seveno_s, relief="ridge")
seveno_s_label1 = tk.Label(window, image=seveno_s, relief="ridge")
seveno_s_label2 = tk.Label(window, image=seveno_s, relief="ridge")
seveno_s_label3 = tk.Label(window, image=seveno_s, relief="ridge")
seveno_s_label4 = tk.Label(window, image=seveno_s, relief="ridge")
logo = ImageTk.PhotoImage(Image.open("imge/logo4.png"))
logo_label = tk.Label(window, image=logo, background='cadetblue3')
one = ImageTk.PhotoImage(Image.open("imge/one.png"))
one_label = tk.Label(window, image=one, background='cadetblue3')
two = ImageTk.PhotoImage(Image.open("imge/two.png"))
two_label = tk.Label(window, image=two, background='cadetblue3')
three = ImageTk.PhotoImage(Image.open("imge/three.png"))
three_label = tk.Label(window, image=three, background='cadetblue3')
# 별
star = ImageTk.PhotoImage(Image.open("imge/star.png"))
star_label = tk.Label(window, image=star, background='white')
star_label2 = tk.Label(window, image=star, background='white')
star_label3 = tk.Label(window, image=star, background='white')
star_label4 = tk.Label(window, image=star, background='white')
star_label5 = tk.Label(window, image=star, background='white')
star_label6 = tk.Label(window, image=star, background='white')
star_label7 = tk.Label(window, image=star, background='white')
star_label8 = tk.Label(window, image=star, background='white')
star_label9 = tk.Label(window, image=star, background='white')
# 심볼
symbol_images = [
    "imge/symbol/seveno.png",
    "imge/symbol/cherry.png",
    "imge/symbol/lemon.png",
]
symbol_images_tk = [ImageTk.PhotoImage(
    Image.open(image)) for image in symbol_images]
label1 = tk.Label(window, image=random.choice(
    symbol_images_tk), borderwidth=10, relief="sunken")
label2 = tk.Label(window, image=random.choice(
    symbol_images_tk), borderwidth=10, relief="sunken")
label3 = tk.Label(window, image=random.choice(
    symbol_images_tk), borderwidth=10, relief="sunken")


# @@@@@@@@@
# 게임안내박스
# @@@@@@@@@
canvas.create_rectangle(4, 20, screen_width-10, 130,
                        outline='gray21', width=12)
canvas.create_rectangle(14, 30, screen_width-20, 123,
                        fill='cadetblue3', outline='indianred2', width=8)
logo_label.place(x=screen_width/2, y=2, anchor='n')
# 1
one_label.place(x=22, y=75, anchor='w')
cherry_s_label.place(x=62, y=35)
cherry_s_label1.place(x=142, y=35)
cherry_s_label2.place(x=222, y=35)
lemon_s_label.place(x=316, y=35)
lemon_s_label1.place(x=396, y=35)
lemon_s_label2.place(x=476, y=35)
# 2
two_label.place(x=610, y=75, anchor='w')
cherry_s_label3.place(x=660, y=35)
cherry_s_label4.place(x=740, y=35)
seveno_s_label3.place(x=820, y=35)
lemon_s_label3.place(x=914, y=35)
lemon_s_label4.place(x=994, y=35)
seveno_s_label4.place(x=1074, y=35)
# 3
three_label.place(x=1212, y=75, anchor='w')
seveno_s_label.place(x=screen_width-275, y=35)
seveno_s_label1.place(x=screen_width-195, y=35)
seveno_s_label2.place(x=screen_width-111, y=35)


# @@@@@@@@@
# 별박스
# @@@@@@@@@
canvas.create_rectangle(386, 166, 1134, 660, outline='gray21', width=15)
canvas.create_rectangle(396, 176, 1124, 650,
                        fill='white', outline='indianred2', width=15)
star_label.place(x=410, y=187)
star_label2.place(x=screen_width/2, y=187, anchor='n')
star_label3.place(x=1075, y=187)
star_label4.place(x=screen_width/4+205, y=187, anchor='n')
star_label5.place(x=935, y=187, anchor='n')
star_label6.place(x=410, y=597)
star_label7.place(x=1075, y=597)
star_label8.place(x=screen_width/4+205, y=597, anchor='n')
star_label9.place(x=935, y=597, anchor='n')

# @@@@@@@@@
# 포인트
# @@@@@@@@@
points = 0
points_label = tk.Label(window, text=f"Points: {points}", font=(
    "Times New Roman", 25), background='cadetblue3')
points_label.place(x=760, y=596, anchor='n')


def p_reset():
    global points
    points = 0
    points_label.config(text=f"Points: {points}")


button = tk.Button(window, text='reset', bg='indianred2',
                   relief='raised', overrelief='sunken', font=(
                       "Times New Roman", 20), command=p_reset)
button.place(x=760, y=700, anchor='n')


# @@@@@@@@@
# 라벨 박스
# @@@@@@@@@
canvas.create_rectangle(236, 236, 1284, 584, outline='gray21', width=15)
canvas.create_rectangle(246, 246, 1274, 574,
                        fill='cadetblue1', outline='indianred2', width=15)
canvas.create_rectangle(296, 296, 524, 524, outline='gray21', width=30)
canvas.create_rectangle(646, 296, 874, 524, outline='gray21', width=30)
canvas.create_rectangle(996, 296, 1224, 524, outline='gray21', width=30)
canvas.create_rectangle(296, 296, 524, 524, outline='indianred2', width=15)
canvas.create_rectangle(646, 296, 874, 524, outline='indianred2', width=15)
canvas.create_rectangle(996, 296, 1224, 524, outline='indianred2', width=15)

label1.place(x=300, y=300)
label2.place(x=650, y=300)
label3.place(x=1000, y=300)


# @@@@@@@@@
# 슬롯 설정
# @@@@@@@@@
rolling_symbols = [tk.Label(window, image=random.choice(
    symbol_images_tk), borderwidth=10, relief="sunken") for _ in range(3)]

for i, label in enumerate(rolling_symbols):
    label.place(x=300 + i * 350, y=300)

spinning = False


def start_spin():
    global spinning
    if not spinning:
        spinning = True
        spin_machine()


def stop_spin():
    global spinning
    spinning = False


def spin_machine():
    global points

    if spinning:
        for label in rolling_symbols:
            label.configure(image=random.choice(symbol_images_tk))
        window.after(100, spin_machine)

    else:
        label1_image = rolling_symbols[0].cget("image")
        label2_image = rolling_symbols[1].cget("image")
        label3_image = rolling_symbols[2].cget("image")

        if label1_image == label2_image == label3_image:
            if label1_image == str(symbol_images_tk[0]):
                points += 3
            elif label1_image == str(symbol_images_tk[1]):
                points += 1
            elif label1_image == str(symbol_images_tk[2]):
                points += 1
        elif (label1_image == label2_image == str(symbol_images_tk[1]) and label3_image == str(symbol_images_tk[0])) or (label1_image == label3_image == str(symbol_images_tk[1]) and label2_image == str(symbol_images_tk[0])) or (label3_image == label2_image == str(symbol_images_tk[1]) and label1_image == str(symbol_images_tk[0])):
            points += 2
        elif (label1_image == label2_image == str(symbol_images_tk[2]) and label3_image == str(symbol_images_tk[0])) or (label1_image == label3_image == str(symbol_images_tk[2]) and label2_image == str(symbol_images_tk[0])) or (label3_image == label2_image == str(symbol_images_tk[2]) and label1_image == str(symbol_images_tk[0])):
            points += 2

        points_label.config(text=f"Points: {points}")


# @@@@@@@@@
# 실행
# @@@@@@@@@
start_button = tk.Button(window, text='Start', command=start_spin,
                         bg='indianred2', font=("Times New Roman", 20))
start_button.place(x=650, y=700, anchor='n')

stop_button = tk.Button(window, text='Stop', command=stop_spin,
                        bg='indianred2', font=("Times New Roman", 20))
stop_button.place(x=860, y=700, anchor='n')


window.mainloop()
