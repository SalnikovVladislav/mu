from django.urls import path
from . import views
from .views import SignUpView, SignInView, myTicketsView, recordingView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('news', views.news, name='news'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('recording', recordingView.as_view(), name='recording'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('signin/', SignInView.as_view(), name="signin"),
    path('mytickets', myTicketsView.as_view(), name='mytickets')
]
