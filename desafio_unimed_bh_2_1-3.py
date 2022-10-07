# DICAS SOBRE PYTHON:
# FUN��O input(): Ela recebe como par�metro uma String que ser� vis�vel ao usu�rio, 
# onde geralmente informa que tipo de informa��o ele est� esperando receber;
# FUN��O print(): Ela � a respons�vel por imprimir os dados e informar os valores no terminal;
# M�TODO ord(): Retorna o valor  ASCII de cada letra ou s�mbolo do teclado;
# TODO: De acordo com a entrada, imprima a posi��o dessa letra no Alfabeto;

#DESAFIO:
#Dada a letra N do alfabeto, nos diga qual a sua posi��o.

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
    print("Digita��o inv�lida")
else:    
    #caso falso, mostra resultado
    print(ord(letra) - (ord(primeira_letra)-1))
