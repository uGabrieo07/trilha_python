class Filme:
    def __init__(self, titulo, duracao, classificacao):
        self.titulo = titulo
        self.duracao = duracao  # em minutos
        self.classificacao = classificacao  # classificação indicativa

    def __str__(self):
        return f"{self.titulo} ({self.duracao} min, {self.classificacao})"

class Sala:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    def __str__(self):
        return f"Sala {self.numero} (Capacidade: {self.capacidade})"

class Sessao:
    def __init__(self, filme, sala, horario):
        self.filme = filme
        self.sala = sala
        self.horario = horario

    def __str__(self):
        return f"{self.filme} na {self.sala} às {self.horario}"

class Cinema:
    def __init__(self, nome):
        self.nome = nome
        self.salas = []
        self.sessoes = []

    def adicionar_sala(self, sala):
        self.salas.append(sala)

    def adicionar_sessao(self, sessao):
        self.sessoes.append(sessao)

    def __str__(self):
        resultado = f"Cinema {self.nome}\n"
        resultado += "Salas:\n"
        for sala in self.salas:
            resultado += f"  {sala}\n"
        resultado += "Sessões:\n"
        for sessao in self.sessoes:
            resultado += f"  {sessao}\n"
        return resultado


