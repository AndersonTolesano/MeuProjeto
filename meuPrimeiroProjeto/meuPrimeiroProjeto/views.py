from django.http import HttpResponse

def hello(request):
    return HttpResponse('Ola mundo')

def articles(request, year):
    return HttpResponse('Meu ano de nascimento é: ' + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome':'Ana', 'idade': 23},
        {'nome':'Pedro', 'idade': 25},
        {'nome':'Maria', 'idade': 19}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'Nao encontrado', 'idade': 0}

def fname(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem: ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse('Pessoa nao encontrada')
