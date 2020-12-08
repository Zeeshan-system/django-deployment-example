from django.contrib import admin
from first_app.models import Topic,Webpage,AccessRecords,Users

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecords)
admin.site.register(Users)
