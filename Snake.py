import tkinter as tk

window = tk.Tk()
window.title("SHMS PTO EP")

label = tk.Label(window, text="{}", foreground="red", height=3, font="courier")
label.pack()

button = tk.Button(window, text="Move this by using the arrow keys", command=lambda: print("Button clicked"))
button.pack()

window.mainloop()