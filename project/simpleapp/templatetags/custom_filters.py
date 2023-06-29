from django import template

register = template.Library()

CURRENCIES_SYMBOLS = {
    'rub': 'Р',
    'usd': '$',
}


@register.filter()
def currency(value, code='rub'):
    """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """
    postfix = CURRENCIES_SYMBOLS[code]

    return f'{value} {postfix}'


@register.filter()
def cenzor(text):
    cenz = ['Дурак', 'дурак', 'бревно', 'Бревно', 'Негодяй', 'негодяй']
    new_text = text.split()
    for index, elem in enumerate(new_text):
        for i in cenz:
            if elem == i:
                new_text[index] = elem[-(len(elem))] + str('*') * (len(elem) - 1)
    return ' '.join(new_text)
