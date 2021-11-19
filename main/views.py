from .models import Exhibition, Tickets
from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import SigUpForm, SignInForm, GetTicketForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    exhibitions = Exhibition.objects.all()
    if request.user.is_authenticated:
        move = "logout"
        username = request.user.username
        text = "Hello, "
        text2 = "logout"
        return render(request, 'main/index.html', {"username": username, "text": text, "text2": text2, "move": move, 'exhibitions': exhibitions})
    else:
        move = "signup"
        text = "Зарегистрироваться"
        text2 = "или войти!"
        return render(request, 'main/index.html', {"text": text, "move": move, "text2": text2, 'exhibitions': exhibitions})


def contacts(request):
    if request.user.is_authenticated:
        move = "logout"
        username = request.user.username
        text = "Hello, "
        text2 = "logout"
        return render(request, 'main/contacts.html', {"username": username, "text": text, "text2": text2, "move": move})
    else:
        move = "signup"
        text = "Зарегистрироваться"
        text2 = "или войти!"
        return render(request, 'main/contacts.html', {"text": text, "move": move, "text2": text2})


def news(request):
    exhibitions = Exhibition.objects.all()
    if request.user.is_authenticated:
        move = "logout"
        username = request.user.username
        text = "Hello, "
        text2 = "logout"
        return render(request, 'main/news.html',
                      {"username": username, "text": text, "text2": text2, "move": move, 'exhibitions': exhibitions})
    else:
        move = "signup"
        text = "Зарегистрироваться"
        text2 = "или войти!"
        return render(request, 'main/news.html',
                      {"text": text, "move": move, 'text2': text2, 'exhibitions': exhibitions})


class recordingView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            move = "logout"
            username = request.user.username
            text = "Hello, "
            text2 = "logout"
            exhibitions = Exhibition.objects.all()
            form = GetTicketForm()
            return render(request, 'main/recording.html',
                          {"username": username, "text": text, "text2": text2, "move": move,
                           'exhibitions': exhibitions, 'form': form})
        else:
            return HttpResponseRedirect('signup')

    def post(self, request, *args, **kwargs):
        form = GetTicketForm(request.POST)
        if form.is_valid():
            username = request.user
            number = 1
            ticket = form.save(username, number)
            exhibition_of = Exhibition.objects.get(name_of_exh=ticket.name)
            if Tickets.objects.filter(name=ticket.name, buyer=username).count() != 0:
                move = "logout"
                text = "Hello, "
                text2 = "logout"
                exhibitions = Exhibition.objects.all()
                message = "У вас уже есть билет!"
                return render(request, 'main/recording.html',
                              {"username": username, "text": text, "text2": text2, "move": move,
                               'exhibitions': exhibitions, 'form': form, 'message': message})
            exhibition_of.sold_tickets += 1
            exhibition_of.places -= 1
            exhibition_of.save()
            ticket = form.save(username, exhibition_of.sold_tickets)
            ticket.save()
            return HttpResponseRedirect('/mytickets')
        else:
            return HttpResponseRedirect('/recording')




class myTicketsView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('signup')
        else:
            username = request.user.id
            my_tickets = Tickets.objects.filter(buyer=username).order_by("id")
            return render(request, 'main/mytickets.html', {'mytickets': my_tickets})

    def post(self, request, *args, **kwargs):
        username = request.user.id
        my_tickets = Tickets.objects.filter(buyer=username).order_by("id")
        return render(request, 'main/mytickets.html', {'mytickets': my_tickets})



class SignUpView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/recording')
        form = SigUpForm()
        return render(request, 'main/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/recording')
        return render(request, 'main/signup.html', context={
            'form': form,
        })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/recording')
        form = SignInForm()
        return render(request, 'main/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/recording")
        return render(request, 'main/signin.html', context={
            'form': form,
        })
