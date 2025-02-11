from django.contrib import admin

from .models import Cours, Lesson, Review


@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_at',
        'start_date',
        'end_date',
        'logo'
    )
    search_fields = ('title', 'description')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'text', 'cours')
    search_fields = ('title', 'description', 'cours')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment', 'cours')
    search_fields = ('comment', 'cours')