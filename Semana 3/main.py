from analise_dados import *
from classes import *
import time as t

if __name__ == '__main__':
      print ("Primeiro testaremos a função analisar_dados.")
      t.sleep(2)
      print ("Selecione o arquivo .csv contendo os dados a serem analisados.")
      t.sleep(2)
      analisar_dados()

      # Exemplo de uso da classe Cinema
      print ("Agora testaremos a classe Cinema.")
      t.sleep(2)
      print ("Vamos criar um cinema com duas salas e duas sessões.")
      t.sleep(2)
      filme1 = Filme("O Poderoso Chefão", 175, "18 anos")
      filme2 = Filme("Vingadores: Ultimato", 181, "12 anos")

      sala1 = Sala(1, 100)
      sala2 = Sala(2, 80)

      sessao1 = Sessao(filme1, sala1, "15:00")
      sessao2 = Sessao(filme2, sala2, "18:00")
      sessao3 = Sessao(filme1, sala2, "21:00")

      cinema = Cinema("Kinoplex")
      cinema.adicionar_sala(sala1)
      cinema.adicionar_sala(sala2)
      cinema.adicionar_sessao(sessao1)
      cinema.adicionar_sessao(sessao2)
      cinema.adicionar_sessao(sessao3)

      print(cinema)
    
