from django.contrib import admin
from .models import Register
from .models import User
from .models import Point
# Register your models here.

admin.site.register(User)
admin.site.register(Point)
admin.site.register(Register)