from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from .models import Chel, Note
from django.contrib.auth.models import AnonymousUser


def reg_page(request):
    if request.method == "GET":
        return render(request, "reg_page.html")
    else:
        data = request.POST
        username = data.get("username")
        password1, password2 = data.get("password1"), data.get("password2")
        if username is None:
            return render(request, "reg_page.html", {'error': 'Введите имя пользователя'})
        elif password1 is None or password2 is None:
            return render(request, "reg_page.html", {'error': 'Введите пароль'})
        elif password1 != password2:
            return render(request, "reg_page.html", {'error': 'Пароли должны совпадать'})
        else:
            try:
                newuser = Chel()
                newuser.create_user(username, password1)
                user = authenticate(request, username=username, password=password1)
                login(request, user)
                return redirect('http://127.0.0.1:8000/')
            except Exception:
                return render(request, "reg_page.html", {'error': 'Пользователь с таким логином уже существует'})



def login_page(request):
    if request.method == "GET":
        return render(request, "login_page.html")
    else:
        data = request.POST
        try:
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is None:
                return render(request, "login_page.html", {'error': 'Такого пользователя нет'})
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        except KeyError:
            return HttpResponse("<h3>Заполните все поля</h3>")

# Create your views here.
def start(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        notes = Note.objects.filter(chel=request.user).all()
        return render(request, "index.html", {"notes" : notes})
    return redirect('http://127.0.0.1:8000/reg')

def post_note(request):
    if request.method == "POST":
        user = request.user
        if request.POST['data']:
            user.create_note(request.POST['data'])
        return redirect("http://127.0.0.1:8000/")
    
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect("http://127.0.0.1:8000/")
    
    

def log_out(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/")