from django.urls import path
from game import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('quizList/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz_view'),
    path('check_answer/', views.check_answer, name='check_answer'),
    path('hangman/', views.hangman_view, name='hangman_view'),
    path('story/', views.story, name='story'),
    path('tictactoe/', views.TTT, name='TicTacToe'),
    path('Saniastory/',views.sania, name='Sanstory'),
    path('Rihaanstory/',views.rihaan, name='Rihstory'),
    path('Videos/', views.videos, name='vids'),
    path('register/', views.register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='game/login.html'), name='login'),
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),
]
