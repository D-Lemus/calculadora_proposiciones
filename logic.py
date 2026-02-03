import re

def segregate(expr_internal: str) -> list[str]:
    return list(expr_internal.strip().replace(" ",""))

def validar_parentesis(characters: list[str]) -> bool:
    counter = 0

    for ch in range(len(characters)):
            
            if characters[ch] == "(":
                counter+=1
            
            elif characters[ch] == ")":
                counter-=1
                if counter < 0:
                    return False

    return counter == 0

def encontrar_variables(segregacion: list[str]) -> set[str]:
    total_vars = ['p', 'q', 'r']
    seg_set = set(segregacion)
    vars_used = {var for var in total_vars if var in seg_set}
    return vars_used


def traducir_proposicion(proposicion:str, var_def: dict[str, bool]) -> bool:
    print(proposicion)
    for var, val in var_def.items():
        proposicion = re.sub(rf"\b{var}\b",val,proposicion)

    proposicion = proposicion.replace('¬','not ')
    proposicion = proposicion.replace('∧',' and ')
    proposicion = proposicion.replace('∨',' or ')
    proposicion = proposicion.replace('→',' <= ')
    proposicion = proposicion.replace('↔',' == ')

    return proposicion

def evaluar_proposicion(traduccion:str) -> bool:
    print(f"Evaluando: {traduccion}:")
    return eval(traduccion)





        

###
proposicion = "¬(p∧q)∧r"

segregacion = segregate(proposicion)

validador = validar_parentesis(segregacion)

variables = encontrar_variables(segregacion)

variables_definidas = {'p':'True','q':'False','r':'True'}
print(variables_definidas)

print("==========================================\n")

traduccion = traducir_proposicion(proposicion,variables_definidas)

print("==========================================\n")

resultado = evaluar_proposicion(traduccion)
print(f"El resultado de la proposicion es: {resultado}")

