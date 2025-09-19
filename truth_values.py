import tkinter as tk

# --- Mapeos simples ---
# De V/F a booleano y de booleano a V/F
def vf_to_bool(v):
    return True if v.strip().upper() == "V" else False

def bool_to_vf(b):
    return "V" if b else "F"

# Operadores lógicos básicos
def conjuncion(a, b):       # a ∧ b
    return a and b

def disyuncion(a, b):       # a ∨ b
    return a or b

def negacion(a):            # ¬a
    return (not a)

def condicional(a, b):      # a → b  (equivalente a (¬a) ∨ b)
    return (not a) or b

def bicondicional(a, b):    # a ↔ b  (a y b tienen el mismo valor)
    return a == b

def xor(a, b):              # a ⊕ b  (verdadero si son distintos)
    return a != b

# Construye frases para el formato textual
def frase_conjuncion(p_txt, q_txt):
    return f"{p_txt} y {q_txt}"

def frase_disyuncion(p_txt, q_txt):
    return f"{p_txt} o {q_txt}"

def frase_negacion(p_txt):
    # Agrega "no" al inicio de manera simple
    return f"No {p_txt}"

def frase_condicional(p_txt, q_txt):
    return f"Si {p_txt} entonces {q_txt}"

def frase_bicondicional(p_txt, q_txt):
    return f"{p_txt} si y solo si {q_txt}"

def frase_xor(p_txt, q_txt):
    return f"O {p_txt} o {q_txt}, pero no ambos"

# Acción principal del botón "Generar"
def generar_resultados():
    # Lee entradas de texto
    p_txt = entrada_p_texto.get().strip()
    q_txt = entrada_q_texto.get().strip()

    # Lee valores de verdad (V/F) y conviértelos a booleanos
    p_v = vf_to_bool(entrada_p_valor.get())
    q_v = vf_to_bool(entrada_q_valor.get())

    # --- Formato textual ---
    # Ensambla las frases pedidas en el ejemplo
    # p ^ q y p → q
    textual_p_and_q = f"p ∧ q: {frase_conjuncion(p_txt, q_txt)}"
    textual_p_imp_q = f"p → q: {frase_condicional(p_txt, q_txt)}"

    # Se puede mostrar también los demás operadores para que quede más completo
    textual_p_or_q  = f"p ∨ q: {frase_disyuncion(p_txt, q_txt)}"
    textual_not_p   = f"¬p: {frase_negacion(p_txt)}"
    textual_not_q   = f"¬q: {frase_negacion(q_txt)}"
    textual_p_iff_q = f"p ↔ q: {frase_bicondicional(p_txt, q_txt)}"
    textual_p_xor_q = f"p ⊕ q: {frase_xor(p_txt, q_txt)}"

    salida_textual.configure(state="normal")
    salida_textual.delete("1.0", "end")
    salida_textual.insert("end", textual_p_and_q + "\n")
    salida_textual.insert("end", textual_p_imp_q + "\n")
    # Extras (comentados si se quiere dejar mínimo):
    salida_textual.insert("end", textual_p_or_q + "\n")
    salida_textual.insert("end", textual_not_p + "\n")
    salida_textual.insert("end", textual_not_q + "\n")
    salida_textual.insert("end", textual_p_iff_q + "\n")
    salida_textual.insert("end", textual_p_xor_q + "\n")
    salida_textual.configure(state="disabled")

    # --- Formato de valores de verdad ---
    # Usa los operadores y convierte a V/F
    # p ^ q y p → q (como en el ejemplo)
    valores = []
    valores.append(f"p ∧ q: {bool_to_vf(conjuncion(p_v, q_v))}")
    valores.append(f"p → q: {bool_to_vf(condicional(p_v, q_v))}")
    # También mostramos los demás requeridos
    valores.append(f"p ∨ q: {bool_to_vf(disyuncion(p_v, q_v))}")
    valores.append(f"¬p: {bool_to_vf(negacion(p_v))}")
    valores.append(f"¬q: {bool_to_vf(negacion(q_v))}")
    valores.append(f"p ↔ q: {bool_to_vf(bicondicional(p_v, q_v))}")
    valores.append(f"p ⊕ q: {bool_to_vf(xor(p_v, q_v))}")

    salida_valores.configure(state="normal")
    salida_valores.delete("1.0", "end")
    salida_valores.insert("end", "\n".join(valores))
    salida_valores.configure(state="disabled")

def main():
    # Ventana principal (Tkinter básico, sin POO)
    global entrada_p_texto, entrada_q_texto, entrada_p_valor, entrada_q_valor, salida_textual, salida_valores

    root = tk.Tk()                 # Crea una nueva ventana
    root.title("Tabla de valores") # Le pone título
    root.geometry("700x520")       # Define el tamaño (ancho x alto)
    root.resizable(False, False)   # Evita redimensionar

    # --- Sección: Entradas ---
    marco_entradas = tk.LabelFrame(root, text="Entradas", padx=10, pady=10)
    marco_entradas.pack(fill="x", padx=10, pady=10)

    tk.Label(marco_entradas, text="p (texto):").grid(row=0, column=0, sticky="w")
    entrada_p_texto = tk.Entry(marco_entradas, width=40)
    entrada_p_texto.grid(row=0, column=1, padx=5, pady=3, sticky="w")

    tk.Label(marco_entradas, text="q (texto):").grid(row=1, column=0, sticky="w")
    entrada_q_texto = tk.Entry(marco_entradas, width=40)
    entrada_q_texto.grid(row=1, column=1, padx=5, pady=3, sticky="w")

    #var dropdowns
    tk.Label(marco_entradas, text="p (V/F):").grid(row=0, column=2, sticky="w", padx=(20,5))
    entrada_p_valor = tk.StringVar(marco_entradas)
    entrada_p_valor.set("F") # default value
    dropdown_p = tk.OptionMenu(marco_entradas, entrada_p_valor, "V", "F")
    dropdown_p.grid(row=0, column=3, pady=3, sticky="w")


    tk.Label(marco_entradas, text="q (V/F):").grid(row=1, column=2, sticky="w", padx=(20,5))
    entrada_q_valor = tk.StringVar(marco_entradas)
    entrada_q_valor.set("F") # default value
    dropdown_q = tk.OptionMenu(marco_entradas, entrada_q_valor, "V", "F")
    dropdown_q.grid(row=1, column=3, pady=3, sticky="w")

    boton_generar = tk.Button(marco_entradas, text="Generar", command=generar_resultados)
    boton_generar.grid(row=0, column=4, rowspan=2, padx=15)

    # --- Sección: Formato Textual ---
    marco_textual = tk.LabelFrame(root, text="Formato textual (frases)", padx=10, pady=10)
    marco_textual.pack(fill="both", expand=True, padx=10, pady=(0,10))

    salida_textual = tk.Text(marco_textual, height=7, state="disabled")
    salida_textual.pack(fill="both", expand=True)

    # --- Sección: Formato de valores de verdad ---
    marco_valores = tk.LabelFrame(root, text="Formato de valores de verdad (V/F)", padx=10, pady=10)
    marco_valores.pack(fill="both", expand=True, padx=10, pady=(0,10))

    salida_valores = tk.Text(marco_valores, height=7, state="disabled")
    salida_valores.pack(fill="both", expand=True)

    # Inicia la app
    root.mainloop()                # Mantiene la ventana abierta hasta que la cierres

if __name__ == "__main__":
    main()
