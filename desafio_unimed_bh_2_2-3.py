# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado

#Desafio
#Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português. 
#Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. 
#Nico, amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. 
#Antes que Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.

#funcao para avaliar qual perna levantou
#e definir qual idioma será utilizado
def analisa_perna(perna):
    switcher = {
        "esquerda": "ingles",
        "direita": "frances",
        "nenhuma": "portugues",
        "ambas":"caiu",
    }
    return switcher.get(perna, "nothing")

#loop infinito para entrada até sair com exception
while True: 
    try: 
      perna_escolhida = input()
      print(analisa_perna(perna_escolhida))
    except EOFError: 
        break