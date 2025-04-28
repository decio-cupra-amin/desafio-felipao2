'''crie uma função que recebe como parametro a quantidade de vitorias e derrotas de um jogador,
depois retorne o resultado para uma variavel, o saldo de rankeadas são feitas pelo calculo:
se vitorias for menor que 10 = ferro
se vitorias for entre 11 e 20 = bronze
se vitorias for entre 21 e 50 = prata
se vitorias for entre 51 e 80 = ouro
se vitorias for entre 81 e 90 = diamante
se vitorias for entre 91 e 100 = lendario
se vitorias for acima ou igual a 101 = imortal'''

jogador = 70

def ranking(pontos):
    if pontos >= 51 and pontos <= 80:
        print("O ranking do jogador é ouro")
    if pontos >=81 and pontos <= 90:
        print("O jogador é ranking diamante") 
    if pontos >=91 and pontos <= 100:
        print("O jogador é ranking lendario")       

ranking(jogador)  
