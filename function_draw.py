import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import *
from PIL import Image

def graph_function():
    try:
        function = entry_function.get()
        start_value = float(entry_start_value.get())
        end_value = float(entry_end_value.get())

        x = np.linspace(start_value, end_value, 400)
        y = eval(function, {"__builtins__": None}, {"x": x, "np": np})
        
        fig.clear()
        ax = fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title("Function Graph")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True)
        canvas.draw()
    except Exception as e:
        error = CTk()
        error.title("WARNING")
        error.geometry("350x100")
        error.resizable(False,False)
        lbl_error=CTkLabel(master=error, text="Please fill in all the blanks.", font=("Arial",20))
        lbl_error.place(relx=0.5, rely=0.3, anchor="center")
        btn_tm=CTkButton(error, text="OK", command=error.destroy )
        btn_tm.place(relx=0.5, rely=0.8, anchor="center")
        error.mainloop()


app = CTk()
app.title("Function Graph Drawer")
app.geometry("800x785")
app.resizable(False, False)

set_appearance_mode("dark")

lbl_function = CTkLabel(app, text="Function Expression:", font=("Arial", 15))
lbl_function.pack()
entry_function = CTkEntry(app, width=500, justify="center", height=28, font=("Arial", 14))
entry_function.pack()

lbl_start_value = CTkLabel(app, text="X's Start Value:", font=("Arial",15))
lbl_start_value.pack()
entry_start_value = CTkEntry(app, width=500, justify="center", height=28, font=("Arial", 14))
entry_start_value.pack()

lbl_end_value = CTkLabel(app, text="X's End Value:", font=("Arial",15))
lbl_end_value.pack()
entry_end_value = CTkEntry(app, width=500, justify="center", height=28, font=("Arial", 14))
entry_end_value.pack()

btn_draw = CTkButton(app, text="Draw Graph", command=graph_function, height=35, width=215, corner_radius=32,
                    hover_color="#C850C0", border_color="#808080", border_width=2)
btn_draw.pack()

fig = plt.Figure(figsize=(8, 7))
canvas = FigureCanvasTkAgg(fig, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

app.mainloop()
