import time as t
from random import randint

def JogoDaForca():
    listaDeAnimais = ["Cachorro", "Gato", "Elefante", "Leao", "Tigre", "Girafa", "Zebra", "Rinoceronte", "Hipopotamo", "Canguru",
        "Koala", "Panda", "Urso", "Lobo", "Raposa", "Esquilo", "Coelho", "Veado", "Gorila", "Macaco",
        "Jacare", "Crocodilo", "Tartaruga", "Serpente", "Iguana", "Peixe", "Tubarao", "Baleia", "Golfinho", "Polvo",
        "Camelo", "Lhama", "Alpaca", "Pinguim", "Avestruz", "Pavao", "Coruja", "Falcao", "Águia", "Papagaio",
        "Borboleta", "Abelha", "Joaninha", "Formiga", "Caracol", "Lesma", "Lagarto", "Sapo", "Ra", "Javali"]
        
    listaDePaises = ["Brasil", "Estados Unidos", "Canadá", "Argentina", "Chile", "México", "Alemanha", "França", "Reino Unido", "Italia",
        "Espanha", "Portugal", "Russia", "China", "Japao", "Coreia do Sul", "India", "Australia", "Nova Zelandia", "Africa do Sul",
        "Egito", "Nigeria", "Turquia", "Arabia Saudita", "Ira", "Iraque", "Grecia", "Noruega", "Suecia", "Dinamarca",
        "Finlandia", "Holanda", "Belgica", "Suiça", "Austria", "Polonia", "Ucrania", "Hungria", "Republica Tcheca", "Eslovaquia",
        "Romenia", "Bulgaria", "Croacia", "Servia", "Eslovenia", "Estonia", "Letonia", "Lituania", "Israel", "Indonesia"]

    listaDeAlimentos = ["Arroz", "Feijao", "Carne", "Frango", "Peixe", "Ovo", "Leite", "Queijo", "Iogurte", "Pao",
        "Massa", "Batata", "Cenoura", "Tomate", "Alface", "Espinafre", "Brocolis", "Couve", "Abobora", "Abobrinha",
        "Maça", "Banana", "Laranja", "Uva", "Morango", "Manga", "Pera", "Melancia", "Abacaxi", "Limao",
        "Amendoa", "Noz", "Castanha", "Avela", "Amendoim", "Cafe", "Cha", "Chocolate", "Açucar", "Mel",
        "Sal", "Pimenta", "Azeite", "Manteiga", "Margarina", "Farinha", "Cereal", "Aveia", "Iogurte", "Salsicha"]

    print("Olá, jogador!")
    t.sleep(2)
    print("Vamos jogar um jogo da forca!")
    t.sleep(2)
    categoria = input("Primeiro, escolha uma categoria para as palavras que você vai ter que advinhar (animais, países ou alimentos): ")

    while True:
        if categoria.lower() == "animais":
            palavraSorteada = listaDeAnimais[randint(0, len(listaDeAnimais) - 1)].upper()
            break
        elif categoria.lower() == "países" or categoria.lower() == "paises":
            palavraSorteada = listaDePaises[randint(0, len(listaDePaises) - 1)].upper()
            break
        elif categoria.lower() == "alimentos":
            palavraSorteada = listaDeAlimentos[randint(0, len(listaDeAlimentos) - 1)].upper()
            break
        else:
            print("Você não escolheu uma categoria válida!")
            t.sleep(2)
            categoria = input("Escolha uma categoria válida para as palavras que você vai ter que advinhar (animais, países ou alimentos): ")

    print(f"Beleza! Você escolheu a categoria {categoria}.")
    t.sleep(2)
    print("Sem mais enrolações, vamos jogar!\n\n")
    t.sleep(2)

    espacosDaPalavra = palavraSorteada.count(" ")
    caracteresOcultos = ["_" if char != " " else " " for char in palavraSorteada]
    tentativas = len(palavraSorteada) - espacosDaPalavra

    while tentativas > 0:
        print(" ".join(caracteresOcultos))
        t.sleep(2)
        print(f"\nTentativas restantes: {tentativas}\n1. Chutar letra\n2. Chutar palavra")
        escolha = input("--> ")

        if escolha == "1":
            letraEscolhida = input("Escolha uma letra: ").lower()

            if letraEscolhida in palavraSorteada.lower():
                for i in range(len(palavraSorteada)):
                    if palavraSorteada[i].lower() == letraEscolhida:
                        caracteresOcultos[i] = palavraSorteada[i]
            else:
                tentativas -= 1
                print(f"Você errou! Você tem {tentativas} tentativa(s) restante(s).")
                t.sleep(2)

        elif escolha == "2":
            palavraChutada = input("Chute uma palavra: ").lower()

            if palavraChutada == palavraSorteada.lower():
                print(f"Você acertou a palavra {palavraSorteada}!")
                t.sleep(2)
                jogarNovamente = input("Deseja jogar novamente? (y/n): ").lower()
                if jogarNovamente == "y":
                    JogoDaForca()
                else:
                    print("Obrigado por jogar :)")
                    t.sleep(2)
                    return
            else:
                print(f"Você errou! A palavra correta era {palavraSorteada}.")
                t.sleep(2)
                jogarNovamente = input("Deseja jogar novamente? (y/n): ").lower()
                if jogarNovamente == "y":
                    JogoDaForca()
                else:
                    print("Obrigado por jogar :)")
                    t.sleep(2)
                    return

        if "_" not in caracteresOcultos:
            print(f"Parabéns, jogador! Você adivinhou a palavra {palavraSorteada}.")
            t.sleep(2)
            jogarNovamente = input("Deseja jogar novamente? (y/n): ").lower()
            if jogarNovamente == "y":
                JogoDaForca()
            else:
                print("Obrigado por jogar :)")
                t.sleep(2)
                return

    print(f"Você perdeu! A palavra secreta era {palavraSorteada}.")
    t.sleep(2)
    jogarNovamente = input("Deseja jogar novamente? (y/n): ").lower()
    if jogarNovamente == "y":
        JogoDaForca()
    else:
        print("Obrigado por jogar :)")
        t.sleep(2)
