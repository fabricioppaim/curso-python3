def valida_cpf(cpf):

    cpf_somente_numeros = cpf.replace('.', '').replace('-', '')
    multiplicados = 0

    if len(cpf_somente_numeros) == 11 or len(cpf_somente_numeros) == 9 and len(set(cpf_somente_numeros)) != 1:
    
        controle = 0
        while controle < 2:
            if controle == 0:
                cpf_digitos = cpf_somente_numeros[:9]
                multiplicador = 10
                controle += 1
            else:
                cpf_digitos = cpf_somente_numeros[:9] + str(digito)
                multiplicador = 11
                controle += 1

            multiplicados = 0
            for numero in cpf_digitos:
                multiplicados += int(numero) * multiplicador
                multiplicador -= 1

            digito = 0
            digito = (multiplicados * 10) % 11
            digito = digito if digito <= 9 else 0
        
        if cpf_somente_numeros in (cpf_digitos + str(digito)):
            return True, (cpf_digitos + str(digito))
        else:            
            return False, (cpf_digitos + str(digito))
    else:
        return False, cpf_somente_numeros

def gerar_cpf():
    import random

    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))
    *_, cpf = valida_cpf(cpf)
    return cpf
        
