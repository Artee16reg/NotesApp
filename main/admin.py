# superUser name= artee password= artee

from django.contrib import admin

from .models import Task

admin.site.register(Task)
