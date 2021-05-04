from django.shortcuts import render
from authapp.forms import UserLoginForm

# Create your views here.
def login(request):
    form = UserLoginForm()
    context = {'title': 'Geekshop - Авторизация', 'form': form}
    return render(request, 'authapp/login.html', context)