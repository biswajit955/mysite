from tkinter import E
from django.contrib import admin
from .models import Blog,Author,Entry ,Dog

# Register your models here.
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Dog)