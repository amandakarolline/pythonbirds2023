class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'


class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    amanda = Mutante(nome='Amanda')
    karolline = Mulher(amanda, nome='Karolline')
    print(Pessoa.cumprimentar(karolline))
    print(id(karolline))
    print(karolline.cumprimentar())
    print(karolline.nome)
    print(karolline.idade)
    for filho in karolline.filhos:
        print(filho.nome)
    karolline.sobrenome = 'Sousa'
    del karolline.filhos
    karolline.olhos = 1
    del karolline.olhos
    print(amanda.__dict__)
    print(karolline.__dict__)
    print(Pessoa.olhos)
    print(karolline.olhos)
    print(amanda.olhos)
    print(id(Pessoa.olhos), id(karolline.olhos), id(amanda.olhos))
    print(Pessoa.metodo_estatico(), karolline.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), karolline.nome_e_atributos_de_classes())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Mulher))
    print(isinstance(amanda, Pessoa))
    print(isinstance(amanda, Mulher))
    print(amanda.olhos)
    print(karolline.cumprimentar())
    print(amanda.cumprimentar())
