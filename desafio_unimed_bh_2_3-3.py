# DICAS SOBRE PYTHON:
# FUN��O input(): Ela recebe como par�metro uma String que ser� vis�vel ao usu�rio, 
# onde geralmente informa que tipo de informa��o ele est� esperando receber;
# FUN��O print(): Ela � a respons�vel por imprimir os dados e informar os valores no terminal;
# M�TODO split(): permite dividir o conte�do da vari�vel de acordo com as condi��es especificadas 
# em cada par�metro da fun��o ou com os valores predefinidos por padr�o;

#A empresa que voc� trabalha resolveu conceder um aumento salarial a todos funcion�rios, de acordo com a tabela abaixo:
#Sal�rio	Percentual de Reajuste
#0        -   600.00   17%
#600.01   -   900.00   13%
#900.01   -  1500.00   12%
#1500.01  -  2000.00   10%
#Acima de    2000.00    5%
#Leia o sal�rio do funcion�rio e calcule e mostre o novo sal�rio, bem como o valor de reajuste ganho e o �ndice reajustado, em percentual.

salario = int(input()) 
novo_salario = 0
aumento_salario = 0
percentual_reajuste = 0

#procedimento que recebe o salario e devolve o % de reajuste
def define_percentual(salario):
  percentual_aplicado = 0
  
  if (salario <= 600):
    percentual_aplicado = 17.00
  elif ((salario >= 600.01) and (salario <= 900)):
    percentual_aplicado = 13.00
  elif ((salario >= 900.01) and (salario <= 1500)):
    percentual_aplicado = 12.00
  elif ((salario >= 1500.01) and (salario <= 2000)):
    percentual_aplicado = 10.00
  else: 
    percentual_aplicado = 5.00
  return percentual_aplicado

#procedimento que recebe o salario e devolve o salario reajustado
def reajusta_salario(salario):
  percentual = define_percentual(salario)
  return salario + (salario * (percentual / 100))

#invoca o procedimento de reajuste de salario
novo_salario = reajusta_salario(salario)
aumento_salario = novo_salario - salario

#prepara as variaveis para exibi��o
percentual_reajuste = '{:.0f}'.format(((novo_salario / salario) * 100) - 100)
novo_salario = "{:.2f}".format(novo_salario)
aumento_salario = '{:.2f}'.format(aumento_salario)
#exibe resultados
print(f'Novo salario: {novo_salario}\nReajuste ganho: {aumento_salario}\nEm percentual: {percentual_reajuste} %')