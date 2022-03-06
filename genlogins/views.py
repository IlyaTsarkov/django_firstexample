from django.shortcuts import render
import random


# Create your views here.

def start(request):
    return render(request, 'genlogins/index.html')


def login(request):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщэюя'
    length = int(request.GET.get('hard_length'))

    your_login = ''

    for x in range(length):
        your_login += random.choice(alphabet)

    return render(request, 'genlogins/login.html',
                  {'login': your_login})


def rand_login(request):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщэюя'
    your_rand_login = ''

    from_char = int(request.GET.get('from_char'))
    to_char = int(request.GET.get('to_char'))
    random_length = random.randint(from_char, to_char)

    for x in range(random_length):
        your_rand_login += random.choice(alphabet)

    return render(request, 'genlogins/random_login.html',
                  {'rand_login': your_rand_login})
