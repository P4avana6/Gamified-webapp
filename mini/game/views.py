from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Quiz, Question, UserProfile
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'game/quiz_list.html', {'quizzes': quizzes})

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, 'game/quiz.html', {'quiz': quiz, 'questions': questions})


@csrf_exempt
def check_answer(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        option_selected = body.get('option')
        question_id = body.get('question_id')
        question = get_object_or_404(Question, id=question_id)
        correct_answer = question.answers.filter(is_correct=True).first()

        if option_selected == correct_answer.answer_text:
            response = {'result': 'Correct answer!!!😎', 'correct': True, 'correct_answer': correct_answer.answer_text}
        else:
            response = {'result': 'Incorrect answer! 🥲', 'correct': False, 'correct_answer': correct_answer.answer_text}

        return JsonResponse(response)

    return JsonResponse({'result': 'Invalid request.'})

@login_required
def home_view(request):
    return render(request, 'game/Home.html')

def about_view(request):
    return render(request, 'game/About.html')

def TTT(request):
    return render(request, 'game/TicTacToe.html')

def hangman_view(request):
    return render(request, 'game/hangman.html')

def story(request):
    return render(request, 'game/story.html')

def sania(request):
    return render(request, 'game/sania.html')

def rihaan(request):
    return render(request, 'game/rihaan.html')

def videos(request):
    return render(request, 'game/videos.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserRegisterForm()
    return render(request, 'game/register.html', {'form': form})

from django.http import HttpResponse
from gtts import gTTS
import os

def text_to_speech(request):
    text = request.GET.get('text', '')
    if not text:
        return HttpResponse("No text provided", status=400)

    tts = gTTS(text=text, lang='en')
    audio_file = "audio.mp3"
    tts.save(audio_file)

    with open(audio_file, 'rb') as f:
        response = HttpResponse(f.read(), content_type="audio/mpeg")
        response['Content-Disposition'] = f'attachment; filename="{audio_file}"'

    os.remove(audio_file)
    return response
