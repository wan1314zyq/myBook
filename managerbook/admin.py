from django.contrib import admin

# Register your models here.

from managerbook.models import *

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(TypeBook)
admin.site.register(Details)