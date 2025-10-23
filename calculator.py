import tkinter as tk

# ---------------------------
# Modern Calculator by GPT-5
# ---------------------------

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("340x500")
root.config(bg="#1E1E1E")
root.resizable(False, False)

expression = ""
equation = tk.StringVar()


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except Exception:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


# -------- Entry Display --------
entry = tk.Entry(
    root,
    textvariable=equation,
    font=("Segoe UI", 26, "bold"),
    bg="#2D2D2D",
    fg="#00FF88",
    bd=0,
    justify="right",
)
entry.place(x=10, y=20, width=320, height=70)

# -------- Button Style --------
button_font = ("Segoe UI", 18, "bold")
button_bg = "#333333"
button_fg = "white"
active_bg = "#00FF88"
active_fg = "#000000"

# Helper to create styled buttons
def create_button(text, x, y, w=70, h=70, cmd=None, color=None):
    btn = tk.Button(
        root,
        text=text,
        font=button_font,
        fg=button_fg,
        bg=color if color else button_bg,
        activebackground=active_bg,
        activeforeground=active_fg,
        bd=0,
        command=cmd,
        relief="flat",
    )
    btn.place(x=x, y=y, width=w, height=h)
    btn.config(cursor="hand2", highlightthickness=0, borderwidth=0)
    return btn


# -------- Buttons --------
create_button("C", 10, 110, 150, 60, clear, "#FF3B30")
create_button("/", 180, 110, 70, 60, lambda: press("/"), "#00FF88")
create_button("*", 260, 110, 70, 60, lambda: press("*"), "#00FF88")

create_button("7", 10, 190, cmd=lambda: press("7"))
create_button("8", 90, 190, cmd=lambda: press("8"))
create_button("9", 170, 190, cmd=lambda: press("9"))
create_button("-", 260, 190, cmd=lambda: press("-"), color="#00FF88")

create_button("4", 10, 270, cmd=lambda: press("4"))
create_button("5", 90, 270, cmd=lambda: press("5"))
create_button("6", 170, 270, cmd=lambda: press("6"))
create_button("+", 260, 270, cmd=lambda: press("+"), color="#00FF88")

create_button("1", 10, 350, cmd=lambda: press("1"))
create_button("2", 90, 350, cmd=lambda: press("2"))
create_button("3", 170, 350, cmd=lambda: press("3"))
create_button("=", 260, 350, 70, 130, equalpress, "#00FF88")

create_button("0", 10, 430, 150, 50, lambda: press("0"))
create_button(".", 170, 430, 70, 50, lambda: press("."))

# -------- Run --------
root.mainloop()
