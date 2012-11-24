##### Global Imports #####
from django.contrib import admin

##### Local Imports #####
from models import *

class LevelAdmin(admin.ModelAdmin):
    list_display = ('guided_reading','grade_level','dra',)
    search_fields = ('guided_reading',)
    list_filter = ('guided_reading','grade_level','dra',)

admin.site.register(Level, LevelAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','level','grade_level','dra',)
    search_fields = ('title',)
    list_filter = ('title','level','grade_level','dra',)

admin.site.register(Book, BookAdmin)