import tkinter as tk
from tkinter import font
import time

def fake_bsod():
    root = tk.Tk()
    root.attributes("-fullscreen", True)       # Vollbild
    root.attributes("-topmost", True)          # immer im Vordergrund
    root.configure(bg="#000088")               # dunkles Blau 

    # Größere, fette Schrift
    title_font = font.Font(family="Consolas", size=72, weight="bold")
    text_font  = font.Font(family="Consolas", size=28)
    small_font = font.Font(family="Consolas", size=18)

    # Haupt-Text
    lbl_title = tk.Label(root, text=":(", fg="white", bg="#000088",
                         font=title_font)
    lbl_title.pack(pady=(80, 20))

    lbl_main = tk.Label(root,
        text="your PC ran into a Problem please restart your PC\n"
             "we are finding the issuses\n"
             "",
        fg="white", bg="#000088", font=text_font, justify="center")
    lbl_main.pack(pady=10)

    lbl_code = tk.Label(root,
        text="Stoppcode: CRITICAL_PROCESS_DIED\n\n"
             "your OS is corrupted and needs to be repaired!\n",
        fg="#99ccff", bg="#000088", font=small_font, justify="center")
    lbl_code.pack(pady=40)
    
    # Kleiner Hinweis unten 
    lbl_hint = tk.Label(root, text="infos? -> github.com/border001",
                        fg="#5555ff", bg="#000088", font=("Consolas", 12))
    lbl_hint.place(relx=0.5, rely=0.98, anchor="s")

    
    root.after(10000, root.destroy)

    root.mainloop()


if __name__ == "__main__":
    fake_bsod()