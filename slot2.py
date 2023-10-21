import tkinter as tk
import random

window = tk.Tk()
window.title("Slot Machine")
window.geometry("1000x450+300+50")
window.resizable(False, False)
window["bg"] = "black"

symbol_images = {
    'Cherry': 'symbol/cherry.png',
    'Lemon': 'symbol/lemon.png',
    'Orange': 'symbol/orange.png',
    'Plum': 'symbol/plum.png',
    'Bell': 'symbol/bell.png',
    'Bar': 'symbol/bar.png',
    'Seven': 'symbol/seven.png',
}


def spin_reels():
    results = [random.choice(list(symbol_images.keys())) for _ in range(3)]
    update_display(results)


def update_display(results):
    for i in range(3):
        img = tk.PhotoImage(file=symbol_images[results[i]])
        img = img.subsample(5)
        labels[i].config(image=img)
        labels[i].image = img


frame = tk.Frame(window, bg="black", padx=10, pady=10)
frame.grid(row=0, column=0, columnspan=3)

labels = []
for i in range(3):
    img = tk.PhotoImage(file="symbol/blank.png")
    img = img.subsample(4)
    label = tk.Label(frame, image=img, anchor="center", bg="black")
    label.grid(row=0, column=i, sticky="nsew")
    labels.append(label)

spin_button = tk.Button(
    window, text="Spin", font=("Franklin Gothic Medium", 20), command=spin_reels, bg='red', fg='white', padx=20, pady=10)
spin_button.grid(row=1, column=0, columnspan=3, pady=20)

window.mainloop()
