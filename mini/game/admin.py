from django.contrib import admin
from .models import Game, Quiz, Reward, UserReward, UserProgress, UserProfile, Question, Answer

# Register models with default admin settings
admin.site.register(Game)
admin.site.register(Quiz)
admin.site.register(Reward)
admin.site.register(UserReward)
admin.site.register(UserProgress)
admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Answer)
