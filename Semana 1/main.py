from semana_um import *

exercio = None
if __name__ == '__main__':
  exercio = input("Qual exercicio deseja rodar?(a ou b): ")
  if str.lower (exercio) == "a":
    PedraPapelTesoura()
  if str.lower (exercio) == "b":
    print (VerificaConvergencia())