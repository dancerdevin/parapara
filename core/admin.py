from django.contrib import admin
from .models import User, Character, Arc, Paradigm, Parameter, EventLog

# Register your models here.
admin.site.register(User)
admin.site.register(Character)
admin.site.register(Arc)
admin.site.register(Paradigm)
admin.site.register(Parameter)
admin.site.register(EventLog)