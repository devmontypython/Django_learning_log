from django.contrib import admin
#Para registrar Topic junto ao site de administração, digite:
from applearning_logs.models import Topic, Entry
admin.site.register(Topic)
admin.site.register(Entry)

# Register your models here.
