def SubstituirPalavras (palavraOriginal, novaPalavra, texto):
   "Função que, dado um texto, substitui uma palavra por outra."
   texto = texto.replace(palavraOriginal, novaPalavra)
   
   return texto


def OrdenarPalavras (string):
   "Função que, dado uma lista de palavras, retorna uma lista ordenada."
   listaASerOrdenada = string.split(',')
   listaASerOrdenada.sort()
   string_ordenada = ", ".join(listaASerOrdenada)
   
   return string_ordenada