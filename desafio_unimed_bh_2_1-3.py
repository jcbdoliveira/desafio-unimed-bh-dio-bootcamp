# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;

#DESAFIO:
#Dada a letra N do alfabeto, nos diga qual a sua posição.

#leitura da letra digitada
letra = input()
#converteu para maiusculo
letra = letra.upper()
#definindo os limites 
primeira_letra = "A"
ultima_letra = "Z"
#testando os limites
if (ord(letra) < ord(primeira_letra)) or (ord(letra) > ord(ultima_letra)):
    #caso verdadeiro, apresenta erro 
    print("Digitação inválida")
else:    
    #caso falso, mostra resultado
    print(ord(letra) - (ord(primeira_letra)-1))
