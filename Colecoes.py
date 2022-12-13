from abc import ABCMeta, abstractmethod

# Manipulando Arrays

print("Manipulação de Arrays:\n")


def iniciando_com_arrays():
    from time import sleep

    idades = [19, 38, 17, 26, 18, 26]
    novas_idades = [65, 90]

    print(f"Lista de idades: {idades}\nLista de novas idades: {novas_idades}\n")
    sleep(3)
    idades.insert(1, 39)
    print(f"Inserindo o numero 39 na posição 1 com metodo .insert(index, value): {idades}\n")
    sleep(3)
    print(f"Achando o index do numero 26 com o metodo .index(value): {idades.index(26)}\n")
    sleep(3)
    print(f"Achando o index do numero 26 a partir do elemento de index 5 "
          f"com o metodo .index(value, index): {idades.index(26, 5)}\n")
    sleep(3)
    idades.append(13)
    print(f"Adicionando 13 ao final da lista com metodo .append(value): {idades}\n")
    sleep(3)
    idades.remove(26)
    print(f"Removendo primeira aparição do 26 na lista com metodo .remove(value): {idades}\n")
    sleep(3)
    idades.pop(0)
    print(f"Retirando o item com index 0 da lista com metodo .pop(value): {idades}\n")
    sleep(3)
    idades.extend(novas_idades)
    print(f"Juntando as listas idades e novas_idades com metodo .extend(list): {idades}\n")
    idades.sort()
    print(f"Lista ordenada usando o metodo .sort() : {idades}")
    sleep(3)
    idades.clear()
    print(f"Limpando todos os elementos da lista com metodo .clear: {idades}\n")


# Aprendendo sobre List Comprehension
def manipulando_arrays():
    from time import sleep

    def adicionar_idade(idade):
        return idade + 1

    idades = [19, 38, 17, 26, 18]

    idades_mais_um = [(idade + 1) for idade in idades]
    idades_maiores_que_vinte = [idade for idade in idades if idade > 20]
    idades_maiores_que_vinte_mais_um = [adicionar_idade(idade) for idade in idades if idade > 20]

    print(f"Lista de idades: {idades}")
    sleep(3)
    print(f"Lista adicionando 1 a toda as idades: {idades_mais_um}")
    sleep(3)
    print(f"Lista de idades maiores que 20: {idades_maiores_que_vinte}")
    sleep(3)
    print(f"Lista de idades maiores que 20 e adicionando 1 a toda as idades: {idades_maiores_que_vinte_mais_um}")


# Aplicando Conceitos de orientação a objeto e usando Tuplas
class Conta(metaclass=ABCMeta):
    def __init__(self, titular, codigo_conta):
        self._titular = titular
        self._codigo_conta = str(codigo_conta)
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    # Foi criado um metodo abstrato que impede o instaciamento de novos objetos que não contenham uma implementação
    # própria desse mesmo metodo. Nesse exemplo: A classe ContaInvestimento ao herdar a classe Conta e não contenha
    # o metodo passa_o_mes não poderá ser instanciada enquanto as Classes ContaCorrente e ContaPoupanca podem ter
    # objetos instanciados.
    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"Titular da Conta: {self._titular}\nCódigo da conta: {self._codigo_conta}\nSaldo da conta: {self.saldo}"


#  Utilizando Herança, Polimorfismo e metodos abstratos
class ContaCorrente(Conta):
    def passa_o_mes(self):
        self.saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3


class ContaInvestimento(Conta):
    pass


# Utilizando Programação Procedural ========v
# Lista == conjunto de elementos do mesmo tipo ou mesmo tipo base(EX: Contas corrente e poupança) / Lista == mutáveis
# Tuplas == conjunto de elementos de tipos diferentes / Tupla == Imutável
# Exemplo de Tupla(utilizado para criar uma nova tupla a partir da original:
conta_do_yan = ("15", 10000)


def deposita(conta):
    valor_para_deposito = 1000
    novo_saldo = conta[1] + valor_para_deposito
    codigo = conta[0]
    return (codigo, novo_saldo)


def imprimir_resultado_deposita():
    print(conta_do_yan)
    print(deposita(conta_do_yan))


def exibir_operacao_com_tuplas():
    imprimir_resultado_deposita()


# Intercalando Listas, Tuplas e Objetos
def testando_conceitos_listas_e_tuplas():
    yan = ("Yan", 27, 1995)
    mayara = ("Mayara", 27, 1995)
    # roberto = ("Roberto", 15, 2007)

    usuarios = [yan, mayara]
    print(usuarios)
    usuarios.append(("Roberto", 15, 2007))
    print(usuarios)
    print(usuarios[0], usuarios[0][0])


def lista_com_tuplas():  # Não Podemos alterar a tupla mas podemos alterar os objetos que ela referência
    conta_yan = Conta("Yan", 5334)
    conta_mayara = Conta("Yan", 90012)

    contas = (conta_yan, conta_mayara)

    for conta in contas:
        print(conta)

    conta_yan.deposito(300)

    for conta in contas:
        print(conta)
# Encerrando o uso de programação Procedural ======/\


def teste_duck_typing():
    conta_yan = ContaCorrente("Yan", 16)
    conta_mayara = ContaPoupanca("Mayara", 17)

    conta_mayara.deposito(1000)
    conta_yan.deposito(1000)

    contas = [conta_yan, conta_mayara]

    print(f"Contas antes do uso do metodo passa_o_mes:")
    for conta in contas:
        print(f"{conta}\n")

    print("\nContas após do uso do metodo passa_o_mes:")

    for conta in contas:
        conta.passa_o_mes()  # Por possuirem o mesmo metodo, é possivel chamar esse metodo em uma lista
        print(f"{conta}\n")


def testando_biblioteca_array():
    import array as arr
    # Uma vez que usamos uma array, precisamos declarar o tipo de dado que será usado e uma vez esses dados sendo
    # definidos, não é mais possivel alterar o tipo de dados que essa array irá receber. O "d" é referente ao tipo
    # da array que nesse caso é float.
    array1 = arr.array("d", [1, 3.5])
    print(array1)


def testando_biblioteca_numpy():
    # Utilizando a biblioteca numpy, temos uma melhor eficiencia na utilização de calculos matemáticos
    import numpy as np
    array1 = np.array([1, 3.5])
    print(array1)


def testando_metodo_equals():
    class ContaSalario:
        def __init__(self, codigo_conta):
            self.__codigo_conta = codigo_conta
            self.__saldo = 0

        def depositar(self, valor):
            self.saldo += valor

        def __str__(self):
            return f"Codigo da conta: {self.codigo_conta}\n" \
                   f"Saldo: {self.saldo}"

        def __eq__(self, outro):
            # Testa se os objetos são do mesmo tipo. Classes que herdam outra classe possuem o mesmo tipo da classe
            # herdada
            if type(outro) != ContaSalario:
                return False
            return self.codigo_conta == outro.codigo_conta and self.saldo == outro.__saldo

        @property
        def codigo_conta(self):
            return self.__codigo_conta

        @property
        def saldo(self):
            return self.__saldo

        @saldo.setter
        def saldo(self, valor):
            self.__saldo = valor

    class ContaDeposito(ContaSalario):
        pass

    class ContaVirtual:
        pass

    conta1 = ContaSalario(13)
    conta2 = ContaDeposito(13)

    print(conta2)
    print(conta1)

    print(f"Compara se os valores contidos nos objetos são os mesmos: {conta2 == conta1}")
    print(f"Compara se o endereço na memória dos objetos é o mesmo{conta2 is conta1}")
    print(f"Compara se um objeto do tipo Conta Salario é do tipo Conta Salario: {isinstance(conta1, ContaSalario)}")
    print(f"Compara se um objeto do tipo Conta Deposito é do tipo Conta Salario: {isinstance(conta2, ContaSalario)}")
    print(f"Compara se um objeto do tipo Conta Salario é do tipo Conta Virtual: {isinstance(conta1, ContaVirtual)}")


def testando_enumerate():
    lista_idades = [13, 29, 50, 47, 32, 50, 71, 48]

    # Sem usar o método enumerate, podemos criar um laço utilizando o metodo range para imprimir o indice e o valor
    # de dados dentro de uma lista
    for i in range(len(lista_idades)):
        print(i, lista_idades[i])
    print("\n")

    # O Comando list(enumerate()) é utilizada para retornar o indice e o valor contido naquele indice em
    # formato de uma lista
    print(list(enumerate(lista_idades)))
    print("\n")

    # Dessa forma, o laço for irá imprimir em forma de tuplas, o agrupamento de indice e valor contido nesse indice
    for valor in enumerate(lista_idades):
        print(valor)
    print("\n")

    # Usando a função for x, y in enumarate(list), temos como saída o indice e o valor contido nesse indice agrupados
    # e fora de uma tupla. Dessa forma, evitamos o uso da função range
    for indice, idade in enumerate(lista_idades):
        print(indice, "x", idade)
    print("\n")

    usuarios = [("Yan", 27, 1995), ("Mayara", 26, 1995), ("Fabio", 53, 1971)]

    for usuario in usuarios:  # Desempacotando dados da lista
        print(usuario)

    for nome, idade, ano_nascimento in usuarios:  # Desempacotando dados da lista e imprimindo o 1 elemento
        print(nome)

    for _, idade, _ in usuarios:  # Desempacotando dados da lista e imprimindo o 2 elemento
        print(idade)

    # Nota: Todas as formas são válidas para todos os tipos de desempacotamento


def testando_sort_sorted_reversed():
    idades = [13, 2, 29, 47, 33, 44, 29]

    lista_ordenada = sorted(idades)  # O método sorted() faz a ordenação de uma lista sem alterar a lista original
    lista_ordenada_invertida = sorted(idades, reverse=True)
    lista_invertida = list(reversed(idades))  # O método reversed() necessariamente precisa ser instanciado em uma lista
    lista_invertida_ordenada = list(reversed(sorted(idades)))

    print("Os metodos Sorted() e Reversed() não alteram a lista original")
    print(f"Lista Original: {idades}\n"
          f"Listas alteradas pelos metodos: \n"
          f"{lista_ordenada}\n{lista_ordenada_invertida}\n{lista_invertida}\n{lista_invertida_ordenada}\n")

    print(f"Lista original: {idades}")
    idades.sort()
    print(f"Lista original após ser alterada com o metodo .sort(): {idades}")


def testando_metodo_less_than():
    from operator import attrgetter

    class ContaSalario:
        def __init__(self, codigo_conta):
            self.__codigo_conta = codigo_conta
            self.__saldo = 0

        def depositar(self, valor):
            self.saldo += valor

        def __str__(self):
            return f"Codigo da conta: {self.codigo_conta}\n" \
                   f"Saldo: {self.saldo}"

        def __eq__(self, outro):
            # Testa se os objetos são do mesmo tipo. Classes que herdam outra classe possuem o mesmo tipo da classe
            # herdada
            if type(outro) != ContaSalario:
                return False
            return self.codigo_conta == outro.codigo_conta and self.saldo == outro.saldo

        def __lt__(self, outro):
            return self.saldo < outro.saldo

        @property
        def saldo(self):
            return self.__saldo

        @saldo.setter
        def saldo(self, valor):
            self.__saldo += valor

        @property
        def codigo_conta(self):
            return self.__codigo_conta

    conta1 = ContaSalario(13120)
    conta1.depositar(1000)
    conta2 = ContaSalario(13129)
    conta2.depositar(800)

    lista_de_contas = [conta1, conta2]

    lista_ordenada_pelo_saldo = sorted(lista_de_contas)

    # Implementando a operação __lt__ a classe Conta Salario podemos comparar 2 objetos da mesma classe
    # O reverse= pode ou não ser usado para inverter a ordem
    for conta in sorted(lista_de_contas, reverse=False):  # Podemos usar: for conta in lista_ordenadas_pelo_saldo:
        print(conta)

    # Utilizando a biblioteca operator para usar o attrgetter
    # Deve ser passado como key attrgetter("parametro") e pode ser ou não usado o reverse=
    for conta in sorted(lista_de_contas, key=attrgetter("saldo"), reverse=True):
        print(conta)


def testando_total_ordering():

    from functools import total_ordering

    @total_ordering
    class ContaSalario:
        def __init__(self, codigo_conta):
            self.__codigo_conta = codigo_conta
            self.__saldo = 0

        def depositar(self, valor):
            self.saldo += valor

        def __str__(self):
            return f"Codigo da conta: {self.codigo_conta}\n" \
                   f"Saldo: {self.saldo}"

        def __eq__(self, outro):
            # Testa se os objetos são do mesmo tipo. Classes que herdam outra classe possuem o mesmo tipo da classe
            # herdada
            if type(outro) != ContaSalario:
                return False
            return self.codigo_conta == outro.codigo_conta and self.saldo == outro.saldo

        def __lt__(self, outro):
            # O método __lt__ foi incrementado para que primeiro compare se o valor do saldo da conta seja diferente da
            # outra conta, ele retorna que o self.saldo é menor que o outro.saldo. Se esse condicional não for verda-
            # deira, a função retorna que o self.codigo_conta é menor que o outro.codigo_conta
            if self.saldo != outro.saldo:
                return self.saldo < outro.saldo
            return self.codigo_conta < outro.codigo_conta

        @property
        def saldo(self):
            return self.__saldo

        @saldo.setter
        def saldo(self, valor):
            self.__saldo += valor

        @property
        def codigo_conta(self):
            return self.__codigo_conta

    conta1 = ContaSalario(200)
    conta1.depositar(800)
    conta2 = ContaSalario(5)
    conta2.depositar(800)
    conta3 = ContaSalario(133)
    conta3.depositar(800)

    lista_contas = [conta1, conta2, conta3]

    # Ordena as contas de acordo com o metodo __lt__ (less than)
    for conta in sorted(lista_contas):
        print(conta)

    # Após implementar a biblioteca functools e importar o total_ordering, a classe passa a conseguir fazer operações
    # comparativas entre objetos criados a partir dela pois possui as funções __lt__ e __eq__ (less than e equals)
    print(conta1 >= conta2)
    print(conta1 == conta2 == conta3)
    print(conta1 < conta3)
    print(conta2 < conta1)
