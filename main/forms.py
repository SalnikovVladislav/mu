from django import forms
from django.contrib.auth.models import User
from .models import Tickets, Exhibition
from django.contrib.auth import authenticate, login


class SigUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
        }),
    )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают!"
            )
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "Данный логин уже зарегистрирован!"
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f"Пользователь '{username}' не зарегистрирован!"
            )
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError(
                    "Данный пароль не верный"
                )


class GetTicketForm(forms.Form):
    exhs = forms.ModelChoiceField(queryset=Exhibition.objects.filter(places__gte=1), required=False,
                                  widget=forms.Select(attrs={'class': 'choice'}))

    def save(self, username, number):
        ticket = Tickets()
        ticket.name = self.cleaned_data['exhs']
        ticket.buyer = username
        ticket.number_of_ticket = number
        return ticket
