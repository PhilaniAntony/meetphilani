from django.contrib import admin
from .models import Aboutme, Message, Collaboration, Project, Technologie, FileAdmin
# Register your models here.
admin.site.register(Aboutme)
admin.site.register(Message)
admin.site.register(Collaboration)
admin.site.register(Project)
admin.site.register(Technologie)
admin.site.register(FileAdmin)
