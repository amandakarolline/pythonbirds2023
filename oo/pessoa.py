class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    amanda = Pessoa(nome='Amanda')
    karolline = Pessoa(amanda, nome='Karolline')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(karolline.olhos)
    print(amanda.olhos)
    print(id(Pessoa.olhos), id(karolline.olhos), id(amanda.olhos))
