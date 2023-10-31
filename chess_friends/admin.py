from django.contrib import admin

# Register your models here.
from chess_friends.models import Chess, Category

admin.site.register(Chess)
admin.site.register(Category)