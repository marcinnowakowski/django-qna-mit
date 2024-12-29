from .models import Answer, Question, SurveySubmission
from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    class Media:
        js = ('/media/fckeditor/fckeditor.js','/media/fckeditor/fckareas.js')

admin.site.register(Question, QuestionAdmin)

class SurveySubmissionAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/fckeditor/fckeditor.js','/media/fckeditor/fckareas.js')

admin.site.register(SurveySubmission, SurveySubmissionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    class Media:
        js = ('/media/fckeditor/fckeditor.js','/media/fckeditor/fckareas.js')

admin.site.register(Answer, AnswerAdmin)
