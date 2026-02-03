#grafico.py
import tkinter as tk
import logica as logic

window = tk.Tk()
window.title("Calculadora Logica")

expression = ""

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

#Variables
boton_p = tk.Button(window, text="p", width=2, command=lambda: add("p"))
boton_p.pack(side=tk.LEFT , padx=5)

boton_q = tk.Button(window, text="q", width=2, command=lambda: add("q"))
boton_q.pack(side=tk.LEFT , padx=5)

boton_r = tk.Button(window, text="r", width=2, command=lambda: add("r"))
boton_r.pack(side=tk.LEFT , padx=5)

#Boton de Borrar Todo
boton_clear = tk.Button(window, text="C",width=2, command=lambda:clear())
boton_clear.pack(side=tk.LEFT, padx=5)

#Boton de regresar 1
button_backspace = tk.Button(window, text="⌫", width=2, command=lambda:backspace())
button_backspace.pack(side=tk.LEFT,padx=5)

#Operadores Logicos 
boton_conjunction = tk.Button(window, text="∧",width=2, command=lambda:add('∧'))
boton_conjunction.pack(side=tk.LEFT, padx=5)

boton_disyunction = tk.Button(window, text="∨",width=2, command=lambda:add('∨'))
boton_disyunction.pack(side=tk.LEFT, padx=5)

boton_negation = tk.Button(window, text="¬",width=2, command=lambda:add('¬'))
boton_negation.pack(side=tk.LEFT, padx=5)

boton_entonces = tk.Button(window, text="→",width=2, command=lambda:add('→'))
boton_entonces.pack(side=tk.LEFT, padx=5)

boton_bicondicional = tk.Button(window, text="↔",width=2, command=lambda:add('↔'))
boton_bicondicional.pack(side=tk.LEFT, padx=5)

boton_parentesis_i = tk.Button(window, text="(",width=2, command=lambda:add('('))
boton_parentesis_i.pack(side=tk.LEFT, padx=5)

boton_parentesis_d = tk.Button(window, text="(",width=2, command=lambda:add(')'))
boton_parentesis_d.pack(side=tk.LEFT, padx=5)

#Boton Calcular 
boton_evlauar = tk.Button(window, text="EVALUAR",width=2, command=lambda:add('terminar'))
boton_evaluar.pack(side=tk.LEFT, padx=5)

#Enlace a Lógica
"""def usar_logica():
    evaluada = logic.evaluar(expression)
    display.delete(0,tk.END)
    display.insert(0,expression)

window.mainloop()"""