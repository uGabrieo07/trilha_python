from random import randint
import time as t
import math as m

def PedraPapelTesoura ():
  jogarNovamente = "y"
  rodadas = 5
  pontosDoUsuario = 0
  pontosDaMaquina = 0
  listaDeOpcoes = ["PEDRA","PAPEL","TESOURA"]
  mensagensDeZoacao = [
        "Simplesmente, o inimigo da sorte hahahahaha",
        "Me manda mensagem depois pra eu te ensinar como joga kkkk",
        "Perde até pro vento!",
        "Mais uma e você vira freguês!",
        "Você devia se aposentar desse jogo!",
        "Não sabia que perder era sua especialidade!",
        "Tá precisando de um coach de pedra, papel e tesoura?",
    ]
  mensagensDeFelicitacao = [
        "Você é o mestre do pedra, papel e tesoura!",
        "Parabéns, você é brabo mesmo!",
        "Vai com calma calbreso, deixa eu ganhar também!",
        "Vitória merecida! Parabéns!",
        "Ganhou de mim ??? Isso é bruxaria!",
        "Grande vitória! Parabéns!",
        "Venceu de novo ??? Tá usando hack!!"
    ]
  while (str.upper(jogarNovamente) == "Y"):
    print ("\n\nOlá, jogador! Bem vindo ao nosso pedra papel e tesoura!\n\n")
    t.sleep(2)
    print (f"Você e eu começamos ambos com 0 pontos cada um.\n\n")
    t.sleep(2)
    print (f"Vamos jogar {rodadas} rodadas. O vencedor de cada uma delas leva 1 ponto. Em caso de empate, ninguem leva nada :(\n\n")
    t.sleep(2)
    while rodadas > 0:
      print(f"{rodadas} rodadas restantes!.\n\n")
      print(f"Você tem {pontosDoUsuario} pontos e a máquina tem {pontosDaMaquina} pontos.\n\n")
      t.sleep(2)
      jogadaDoUsuario = str.upper(input("Escolha entre Pedra, Papel ou Tesoura: "))

      if jogadaDoUsuario == "PEDRA" or jogadaDoUsuario == "PAPEL" or jogadaDoUsuario == "TESOURA":
        indexAleatorio = randint(0,2)
        jogadaDaMaquina = listaDeOpcoes[indexAleatorio]

        if jogadaDoUsuario == "PEDRA" and jogadaDaMaquina == "PAPEL":
          print(f"Você escolheu {jogadaDoUsuario} e a máquina escolheu {jogadaDaMaquina}. Você perdeu!")
          rodadas -= 1
          pontosDaMaquina += 1
        elif jogadaDoUsuario == "PAPEL" and jogadaDaMaquina == "PEDRA":
          print(f"Você escolheu {jogadaDoUsuario} e a máquina escolheu {jogadaDaMaquina}. Você ganhou!")
          rodadas -= 1
          pontosDoUsuario += 1
        elif jogadaDoUsuario == "PEDRA" and jogadaDaMaquina == "TESOURA":
          print(f"Você escolheu {jogadaDoUsuario} e a máquina escolheu {jogadaDaMaquina}. Você ganhou!")
          rodadas -= 1
          pontosDoUsuario += 1
        elif jogadaDoUsuario == "TESOURA" and jogadaDaMaquina == "PEDRA":
          print(f"Você escolheu {jogadaDoUsuario} e a máquina escolheu {jogadaDaMaquina}. Você perdeu!")
          rodadas -= 1
          pontosDaMaquina += 1
        elif jogadaDoUsuario == "PAPEL" and jogadaDaMaquina == "TESOURA":
          print(f"Você escolheu {jogadaDoUsuario} e a máquina escolheu {jogadaDaMaquina}. Você perdeu!")
          rodadas -= 1
          pontosDaMaquina += 1
        elif jogadaDoUsuario == "TESOURA" and jogadaDaMaquina == "PAPEL":
          print(f"Você escolheu {jogadaDoUsuario} e a máquina escolheu {jogadaDaMaquina}. Você ganhou!")
          rodadas -= 1
          pontosDoUsuario += 1
        elif jogadaDoUsuario == jogadaDaMaquina:
          print(f"Você escolheu {jogadaDoUsuario} e a máquina escolheu {jogadaDaMaquina}. Empate!")
        else:
          print("Jogada inválida, tente novamente.\n")
          continue
    if pontosDoUsuario == 3:
      indexMensagemFelicitacao = randint(0, 6) 
      print (mensagensDeFelicitacao[indexMensagemFelicitacao])
    if pontosDaMaquina == 3:
      indexMensagemZoacao = randint(0, 6) 
      print (mensagensDeZoacao[indexMensagemZoacao])
    jogarNovamente = str.upper(input("Deseja jogar novamente? (y/n): "))
    if jogarNovamente == "Y":
      rodadas = 5
      pontosDoUsuario = 0
      pontosDaMaquina = 0
  print("Obrigado por jogar e volta sempre, freguês :)")
  t.sleep(2)
  return None

def VerificaConvergencia():
    soma = 0
    n = 2
    termosMax = 10000
    
    for _ in range(termosMax):
        termo = 1 / (n * m.log(n)**2)
        soma += termo
        n += 1
        
    return soma < float('inf')

