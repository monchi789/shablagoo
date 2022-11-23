from django.contrib import admin
from .models import User, Role, Category, Event, EventPlanner

# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(EventPlanner)
admin.site.register(Event)