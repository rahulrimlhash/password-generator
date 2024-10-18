from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'home.html')

def password_generate(request):
    character = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))
        
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*'))
        
    password = ''
    for i in range(length):
        password += random.choice(character)
    return render(request, 'password.html', {'password': password})