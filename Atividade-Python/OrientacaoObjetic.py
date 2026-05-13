# nuber = [4,5,6,7,8,4]

# print(nuber)

# Exemplo Class é o model (Planta Baixa)
# class Carro:
#     def __init__(self, marca, modelo):
#         self.marca = marca  # Atributo
#         self.modelo = modelo # Atributo

#     def acelerar(self):     # Método
#         print(f"A marca {self.marca} do modelo {self.modelo} está acelerando...")

# # Criando um objeto (instanciando)
# meu_carro = Carro("Toyota", "Corolla")
# meu_carro.acelerar()



# self.atributo = Publico (Qualquer parte do código pode ler e alterar o valor diretamente.)
# self._atributo = Protegido (Serve como um aviso de "uso interno apenas". É muito respeitado em ambientes profissionais e por bibliotecas famosas.)
# self.__atributo = Privado (O Python altera o nome internamente para impedir acessos acidentais.)
# class Usuario:
#     def __init__(self, nome, email, senha):
#         self.nome = nome          # 🟢 Verde: Público
#         self._email = email       # 🟡 Amarelo: Protegido (só mude se souber o que está fazendo)
#         self.__senha = senha      # 🔴 Vermelho: Privado (bloqueado por fora)

# usuario = Usuario("Ana", "ana@email.com", "1234")

# # Testando os acessos por fora da classe:
# print(usuario.nome)     # 🟢 Funciona perfeitamente
# print(usuario._email)   # 🟡 Funciona, mas você quebrou a boa prática do Python
# print(usuario.__senha)  # 🔴 Dá ERRO! O Python protege o dado


# ##
# 1. Definimos a categoria/molde usando 'class'
class Notebook:
    
    # 2. O primeiro 'def' constrói o objeto e define seus atributos
    def __init__(self, marca, memoria_ram):
        self.marca = marca               # Atributo Público 🟢
        self._memoria = memoria_ram      # Atributo Protegido 🟡
        self.__ligado = False            # Atributo Privado 🔴

    # 3. Os próximos 'def' criam os métodos (ações do notebook)
    def ligar(self):
        self.__ligado = True
        print(f"O notebook {self.marca} está inicializando...")

    def exibir_status(self):
        # O método consegue ler o atributo privado vermelho livremente
        status = "Ligado" if self.__ligado else "Desligado"
        print(f"Marca: {self.marca} | RAM: {self._memoria}GB | Status: {status}")

# Criando o objeto baseado no molde da classe
meu_note = Notebook("Dell", 16)

# Executando os métodos definidos com 'def'
meu_note.ligar()
meu_note.exibir_status()
