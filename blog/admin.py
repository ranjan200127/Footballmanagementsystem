from django.contrib import admin
from .models import team,point_table,goal,match
# Register your models here.
admin.site.register(team)
admin.site.register(point_table)
admin.site.register(goal)
admin.site.register(match)