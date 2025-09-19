import tkinter as tk
from functools import partial


class LogicGame:
    OPERATORS = {
        "∧": lambda a, b: a and b,
        "v": lambda a, b: a or b,
        "→": lambda a, b: (not a) or b,
        "↔": lambda a, b: ((not a) or b) and ((not b) or a),
        "⊕": lambda a, b: a != b
    }

    DEFAULT_TEXT = "Seleccionar"
    OP_OPTIONS = [DEFAULT_TEXT] + list(OPERATORS.keys())
    VAR_OPTIONS = ["V", "F"]

    PROPOSITION_TOKENS = ["(", "p", "q", ")", "(", "r", "s", ")"]
    VAR_POSITIONS = [1, 3, 7, 9]  # indices de las variables en PROPOSITION_TOKENS
    OP_POSITIONS = [2,5,8] # indices de los operadores en PROPOSITION_TOKENS  
    init_time = 120 #seconds for the timer


    def __init__(self, root):
        self.root = root
        self.root.title("Mini Game")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        self.root.configure(bg="lightblue")

        self.main_label = tk.Label(root, text="Jugador 1, ingresa los operadores lógicos", font=("Arial", 18), bg="lightblue")
        self.main_label.pack(pady=20)

        self.proposition_frame = tk.Frame(root, bg="lightblue")
        self.proposition_frame.pack(expand=True)

        self.operator_vars = [tk.StringVar(value=self.OP_OPTIONS[0]) for _ in range(3)] #las stringvar son variables de tkinter especiales que actualizan automáticamente los widgets asociados
        self.tries = 1


        #go back button
        import main
        self.back_button = tk.Button(root, text="Volver", font=("Arial", 12), command= lambda: main.open_new_window_and_close_old(root, 'main'))
        self.back_button.place(x=10, y=10)


        self._build_operator_selection()
        self.confirm_button = tk.Button(root, text="Confirmar", font=("Arial", 16), bg="green", fg="black")
        self.confirm_button.pack(pady=20)
        self.confirm_button.bind("<Button-1>", self.start_guessing_phase)


    def _show_results(self):
        self.confirm_button.destroy()
        self.timer_label.destroy()

        for col in self.OP_POSITIONS:
            label = self.proposition_frame.grid_slaves(row=0, column=col)[0]
            label.configure(text=self.selected_ops[self.OP_POSITIONS.index(col)])

            dropdwon = self.proposition_frame.grid_slaves(row=1, column=col)[0]
            dropdwon.destroy()
 

    # UI

    def _update_timer(self):
        """actualiza el temporizador cada segundo"""
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Tiempo restante: {self.time_left} s")
            self.timer_label.after(1000, self._update_timer)
        else:
            self._popup("Tiempo agotado", "Se acabó el tiempo. ¡Juego terminado!")
            self._show_results()



    def _build_operator_selection(self):
        """construye la expresión con espacios para dropdowns de operadores"""
        col = 0
        for idx, token in enumerate(self.PROPOSITION_TOKENS):
            label = tk.Label(self.proposition_frame, text=token, font=("Arial", 16), bg="lightblue")
            label.grid(row=0, column=col, padx=5, pady=5)

            if idx in [1, 5]:  # después de p y r va un operador
                op_menu = tk.OptionMenu(self.proposition_frame, self.operator_vars[0 if idx == 1 else 2], *self.OP_OPTIONS)
                op_menu.grid(row=0, column=col + 1, padx=5, pady=5)
                col += 1

            if idx == 3:  # entre (p op q) y (r op s)
                op_menu = tk.OptionMenu(self.proposition_frame, self.operator_vars[1], *self.OP_OPTIONS)
                op_menu.grid(row=0, column=col + 1, padx=5, pady=5)
                col += 1

            col += 1

    # LOGIC
    def start_guessing_phase(self, _):
        """jugador 2 empieza a adivinar las operaciones"""
        if any(var.get() == self.DEFAULT_TEXT for var in self.operator_vars):
            self._popup("Atención", "Selecciona todas las operaciones")
            return
 
        self.selected_ops = [var.get() for var in self.operator_vars]
        self.main_label.config(text="Jugador 2, deduce las operaciones lógicas")

        # Dropdowns de variables
        self.var_vars = []
        self.boolean_values = [True] * 4

        self._set_dropdown_str(self.operator_vars, self.DEFAULT_TEXT) # resetear dropdowns de operadores a la opción por defecto

        for col, idx in zip([1, 3, 7, 9], range(4)):
            old_label = self.proposition_frame.grid_slaves(row=0, column=col)[0] # obtener la etiqueta antigua
            old_label.destroy()

            var_str = tk.StringVar(value=self.VAR_OPTIONS[0])
            var_str.trace_add("write", partial(self._on_var_change, idx)) #partial es para pasar argumentos extra a la función callback
            self.var_vars.append(var_str)

            dd = tk.OptionMenu(self.proposition_frame, var_str, *self.VAR_OPTIONS)
            dd.grid(row=0, column=col, padx=5, pady=5)

        for col in self.OP_POSITIONS:
            #move down the operator dropdowns 
            op_widget = self.proposition_frame.grid_slaves(row=0, column=col)[0]
            op_widget.grid_forget()
            op_widget.grid(row=1, column=col, padx=5, pady=5)

            # add a question mark label in place of the operator dropdowns
            label = tk.Label(self.proposition_frame, text="?", font=("Arial", 16), bg="lightblue")
            label.grid(row=0, column=col, padx=5, pady=5)

        # Resultado
        tk.Label(self.proposition_frame, text="=", font=("Arial", 16), bg="lightblue").grid(row=0, column=11, padx=5, pady=5)

        self.result_label = tk.Label(self.proposition_frame, text="", font=("Arial", 16), bg="lightblue")
        self.result_label.grid(row=0, column=12, padx=5, pady=5)
        self._update_result()

        # Preparar temporizador
        self.time_left = self.init_time
        self.timer_label = tk.Label(self.root, text=f"Tiempo restante: {self.time_left} s", font=("Arial", 14), bg="lightblue")
        self.timer_label.pack(pady=10)
        self.timer_label.after(1000, self._update_timer)


        # Preparar botón Confirmar
        self.confirm_button.unbind("<Button-1>")
        self.confirm_button.bind("<Button-1>", self.check_guess)


    def _on_var_change(self, idx, *_):
        """callback cuando cambia un dropdown de variable"""
        self.boolean_values[idx] = (self.var_vars[idx].get() == "V")
        self._update_result()


    def _set_dropdown_str(self, dropdown_strs, str):
        """establece el valor de múltiples StringVars (usadas en dropdowns) a str"""
        for str_var in dropdown_strs:
            str_var.set(str)

    def _update_result(self):
        """actualiza el resultado mostrado basado en las selecciones actuales"""
        first = self.OPERATORS[self.selected_ops[0]](self.boolean_values[0], self.boolean_values[1])
        second = self.OPERATORS[self.selected_ops[2]](self.boolean_values[2], self.boolean_values[3])
        result = self.OPERATORS[self.selected_ops[1]](first, second)
        self.result_label.config(text="V" if result else "F")

    def check_guess(self, _):
        """verifica si el jugador 2 adivinó correctamente las operaciones"""
        if any(var.get() == self.DEFAULT_TEXT for var in self.operator_vars):
            self._popup("Atención", "Selecciona todas las operaciones")
            return

        guess = [var.get() for var in self.operator_vars]
        msg = ""

        if guess == self.selected_ops:
            msg = f"¡Correcto! Lo lograste en {self.tries} intento(s)"
            #self.confirm_button.config(text="Salir", command=self.root.destroy)
            self._show_results()
        else:
            msg = f"Incorrecto, llevas {self.tries} intento(s)"

        self.tries += 1
        tk.Label(self.proposition_frame, text=msg, font=("Arial", 16), bg="lightblue").grid(row=3, column=0, columnspan=13, pady=10)


    def _popup(self, title, text):
        """crea una ventana emergente modal con un mensaje"""
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("300x150")

        tk.Label(popup, text=text).pack(pady=20)
        tk.Button(popup, text="Cerrar", command=popup.destroy).pack(pady=10)

        popup.transient(self.root)
        popup.grab_set() # hace que la ventana sea modal, modal es que no se puede interactuar con la ventana padre hasta cerrar la hija
        self.root.wait_window(popup) #espera a que se cierre la ventana hija para continuar con la ejecución del código


def main():
    root = tk.Tk()
    game = LogicGame(root)
    root.mainloop()
