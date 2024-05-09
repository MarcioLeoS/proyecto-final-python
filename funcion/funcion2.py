import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class PlotterApp:
    def __init__(self, master):
        self.master = master
        master.title("Plotter")

        self.label = ttk.Label(master, text="Inserta una función:")
        self.label.grid(row=0, column=0, sticky="w")

        self.entry = ttk.Entry(master, width=50)
        self.entry.grid(row=1, column=0, padx=5, pady=5)

        self.plot_button = ttk.Button(master, text="Graficar", command=self.plot)
        self.plot_button.grid(row=1, column=1, padx=5, pady=5)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.plot_canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.plot_canvas.get_tk_widget().grid(row=2, column=0, columnspan=2)

    def plot(self):
        function = self.entry.get()

        try:
            x = np.linspace(-10, 10, 100)
            y = eval(function)
            ax = self.fig.add_subplot(111)
            ax.clear()
            ax.plot(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title('Gráfico de ' + function)
            ax.grid(True)
            self.plot_canvas.draw()
        except Exception as e:
            tk.messagebox.showerror("Error", "Ha ocurrido un error al graficar la función: " + str(e))


def main():
    root = tk.Tk()
    app = PlotterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
