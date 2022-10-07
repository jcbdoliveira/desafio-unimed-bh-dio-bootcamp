# DICAS SOBRE PYTHON:
# FUN��O input(): Ela recebe como par�metro uma String que ser� vis�vel ao usu�rio, 
# onde geralmente informa que tipo de informa��o ele est� esperando receber;
# FUN��O print(): Ela � a respons�vel por imprimir os dados e informar os valores no terminal;
# M�TODO split(): permite dividir o conte�do da vari�vel de acordo com as condi��es especificadas 
# em cada par�metro da fun��o ou com os valores predefinidos por padr�o;
# while True significa que, enquanto houver entradas, o c�digo ap�s o try continuar� sendo executado

#Desafio
#Humberto tem um papagaio muito esperto. Quando est� com as duas pernas no ch�o, o papagaio fala em portugu�s. 
#Quando levanta a perna esquerda, fala em ingl�s. Por fim, quando levanta a direita fala em franc�s. 
#Nico, amigo de Humberto, ficou fascinado com o animal. Em sua emo��o perguntou: �E quando ele levanta as duas?�. 
#Antes que Humberto pudesse responder, o papagaio gritou: �A� eu caio, idiota!�.

#funcao para avaliar qual perna levantou
#e definir qual idioma ser� utilizado
def analisa_perna(perna):
    switcher = {
        "esquerda": "ingles",
        "direita": "frances",
        "nenhuma": "portugues",
        "ambas":"caiu",
    }
    return switcher.get(perna, "nothing")

#loop infinito para entrada at� sair com exception
while True: 
    try: 
      perna_escolhida = input()
      print(analisa_perna(perna_escolhida))
    except EOFError: 
        break