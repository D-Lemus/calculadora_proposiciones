#grafico.py
import tkinter as tk
from tkinter import messagebox
import logic

window = tk.Tk()
window.title("Calculadora Logica")

expression = "¬(p∧q)∧r"

def add(letter):
    global expression
    expression+=letter
    display.delete(0,tk.END)
    display.insert(0,expression)

def clear():
    global expression
    expression = ""
    display.delete(0,tk.END)

def backspace():
    global expression
    if expression == "":
        return
    expression = expression[:-1]
    display.delete(0,tk.END)
    display.insert(0,expression)


display = tk.Entry(window, width=40)
display.pack(pady=10)

fila1 = tk.Frame(window)
fila1.pack(pady=5)

fila2 = tk.Frame(window)
fila2.pack(pady=5)

#Variables
boton_p = tk.Button(fila1, text="p", width=2, command=lambda: add("p"))
boton_p.pack(side=tk.LEFT , padx=5)

boton_q = tk.Button(fila1, text="q", width=2, command=lambda: add("q"))
boton_q.pack(side=tk.LEFT , padx=5)

boton_r = tk.Button(fila1, text="r", width=2, command=lambda: add("r"))
boton_r.pack(side=tk.LEFT , padx=5)

#Boton de Borrar Todo
boton_clear = tk.Button(fila1, text="C",width=2, command=lambda:clear())
boton_clear.pack(side=tk.LEFT, padx=5)

#Boton de regresar 1
button_backspace = tk.Button(fila1, text="⌫", width=2, command=lambda:backspace())
button_backspace.pack(side=tk.LEFT,padx=5)

#Operadores Logicos 
boton_conjunction = tk.Button(fila1, text="∧",width=2, command=lambda:add('∧'))
boton_conjunction.pack(side=tk.LEFT, padx=5)

boton_disyunction = tk.Button(fila1, text="∨",width=2, command=lambda:add('∨'))
boton_disyunction.pack(side=tk.LEFT, padx=5)

boton_negation = tk.Button(fila1, text="¬",width=2, command=lambda:add('¬'))
boton_negation.pack(side=tk.LEFT, padx=5)

boton_entonces = tk.Button(fila1, text="→",width=2, command=lambda:add('→'))
boton_entonces.pack(side=tk.LEFT, padx=5)

boton_bicondicional = tk.Button(fila1, text="↔",width=2, command=lambda:add('↔'))
boton_bicondicional.pack(side=tk.LEFT, padx=5)

boton_parentesis_i = tk.Button(fila1, text="(",width=2, command=lambda:add('('))
boton_parentesis_i.pack(side=tk.LEFT, padx=5)

boton_parentesis_d = tk.Button(fila1, text=")",width=2, command=lambda:add(')'))
boton_parentesis_d.pack(side=tk.LEFT, padx=5)

boton_espacio= tk.Button(fila2, text="espacio",width=8, command=lambda:add(' '))
boton_espacio.pack(side=tk.LEFT, padx=5)

def definir_variables(root, vars_usadas, callback):
    """
    vars_usadas: set[str]  → {'p','q','r'}
    callback(dict)        → recibe {'p': True, 'q': False}
    """
    popup = tk.Toplevel(root)
    popup.title("Definir variables")
    popup.grab_set()   # modal

    valores = {}

    for var in vars_usadas:
        frame = tk.Frame(popup)
        frame.pack(pady=5)

        tk.Label(frame, text=f"{var} = ").pack(side=tk.LEFT)

        v = tk.StringVar(value="True")
        valores[var] = v

        tk.OptionMenu(frame, v, "True", "False").pack(side=tk.LEFT)

    def aceptar():
        resultado = {v: (valores[v].get() == "True") for v in valores}
        popup.destroy()
        callback(resultado)

    tk.Button(popup, text="OK", command=aceptar).pack(pady=10)




def proceso(expression):
    segregar = logic.segregate(expression)
    parentesis = logic.validar_parentesis(segregar)
    if parentesis:
        
        #variables_encontradas = logic.encontrar_variables()
        variables_usadas = logic.encontrar_variables(segregar)
        callback = continuar(variables_usadas)
        variables_definidas = definir_variables(window, variables_usadas,callback)

        def continuar(variables_definidas):
            traducción = logic.traducir_proposicion(expression,variables_definidas)
            resultado = logic.evaluar_proposicion(traducción)
            messagebox.showinfo("Resultado", f"RESULTADO: {resultado}")

#a_evaluar = display.get(expression)

#Boton Valores
boton_valores = tk.Button(fila2, text="EVALUAR",width=20, command=lambda:add('terminar'))
boton_valores.pack(side=tk.LEFT, padx=5)

#Boton Calcular 
boton_calcular = tk.Button(fila2, text="Calcular",width=20, command=lambda:proceso(expression))
boton_calcular.pack(side=tk.LEFT, padx=5)



window.mainloop()
