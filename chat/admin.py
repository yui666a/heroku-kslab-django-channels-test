from django.contrib import admin

from .models import Question, Choice, Message, Room

admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Question)
admin.site.register(Choice)


