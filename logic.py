import re


def segregate(expr_internal: str) -> list[str]:
    expr_internal = expr_internal.split()
    return expr_internal

def validar_parentesis(segregacion: list[str]) -> bool:
    counter = 0

    for i in range(len(segregacion)):
        if counter >= 0:
            if segregacion[i] == "(":
                counter+=1
            elif segregacion[i] == ")":
                counter-=1
        else: return False

    return counter == 0

def encontrar_variables(segregacion: list[str]) -> list[str]:
    total_vars = ['p', 'q', 'r']
    seg_set = set(segregacion)
    vars_used = {var for var in total_vars if var in seg_set}
    return vars_used

def definir_variables(variables: list[str]) -> dict[str, str]:

    var_def = {}
    for var in variables:
        str_boolean_val = str(input(f'Enter "True" "False" for {var}: ')).lower().capitalize()
        

        while str_boolean_val not in ('True','False'):
            str_boolean_val = str(input(f'ONLY Enter "True" or "False" for {var}: ')).lower().capitalize()


        var_def[var] = str_boolean_val
    return var_def


def traducir_proposicion(proposicion:str, variables: dict[str, str]) -> bool:
    print(proposicion)
    for var, val in variables.items():
        proposicion = re.sub(rf"\b{var}\b",val,proposicion)
        print(f"variable {var} reformada")
        print(proposicion)
    return proposicion
        


proposicion = "not ( p and q ) or r"

segregacion = segregate(proposicion)
print(segregacion)

validador = validar_parentesis(segregacion)

variables = encontrar_variables(segregacion)
variables_definidas = definir_variables(variables)
print(variables_definidas)
print("==========================================\n")
traduccion = traducir_proposicion(proposicion,variables_definidas)
print(traduccion)


