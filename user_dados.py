from tools.cpf import *
import datetime

nome = 'Maria Silva'
sobrenome = 'Oliveira'
idade = 30
cpf = gerar_cpf()
ano_nascimento = datetime.date.today().year - idade
e_maior = idade >= 18
altura = 1.75

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', e_maior)
print('Altura em metros:', altura)

if valida_cpf(cpf):
    print('CPF gerado:', cpf)
    print('CPF válido')
else:
    print('CPF gerado:', cpf)
    print('CPF inválido')
