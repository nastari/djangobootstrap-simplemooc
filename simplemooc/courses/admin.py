from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','id']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('created_at',) 


admin.site.register(Course, CourseAdmin)


#Django é muito mairo que o ADMIN. ADMIN é um administrador de CRUD's.