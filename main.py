import tkinter as tk

def open_new_window_and_close_old(old_window, new_window):
    old_window.destroy()  # close the old window
    new_window = __import__(new_window)  # import the new window module
    new_window.main()  # open the new window



def main():
    root = tk.Tk()
    root.title("Proyecto Lógica")
    root.geometry("1000x600")
    root.resizable(False, False)
    root.configure(bg="lightyellow")
    mainLabel = tk.Label(root, text="Bienvenido al Proyecto de Lógica", font=("Arial", 24), bg="lightyellow")
    mainLabel.pack(pady=20)

    start_minigame = tk.Button(root, text="Iniciar Mini Juego", font=("Arial", 16), bg="green", fg="black", command=lambda: open_new_window_and_close_old(root, 'minigame'))
    start_minigame.pack(pady=20)

    start_truth_tables_text = tk.Button(root, text="Tablas de Verdad formato textual", font=("Arial", 16), bg="orange", fg="black") 
    start_truth_tables_text.pack(pady=20)

    start_truth_tables_gui = tk.Button(root, text="Tablas de Verdad Valores de Verdad", font=("Arial", 16), bg="orange", fg="black")
    start_truth_tables_gui.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()