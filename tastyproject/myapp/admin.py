from django.contrib import admin
from .models import Restaurant, Voting, Voting2

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Voting)
admin.site.register(Voting2)