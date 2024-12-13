from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255, null=True, blank=True)
    grade = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.user.username

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Quiz(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1=models.CharField(max_length=255, default='Default Option 1')
    option2=models.CharField(max_length=255, default='Default Option 2')
    option3=models.CharField(max_length=255, default='Default Option 3')
    option4=models.CharField(max_length=255, default='Default Option 4')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.answer_text
  
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='user_progress')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='user_progress')
    score = models.IntegerField()
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

class Reward(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='user_rewards')
    earned_at = models.DateTimeField(auto_now_add=True)


