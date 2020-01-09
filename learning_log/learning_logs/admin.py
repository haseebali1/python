from django.contrib import admin

# Register your models here.

# .models tells Django to look in the same directory
from .models import Topic, Entry

#manage our model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)

