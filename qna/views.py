from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Question
from .forms import QuestionForm

# List view to display all questions
class QuestionListView(ListView):
    model = Question
    template_name = 'qna/question_list.html'
    context_object_name = 'questions'
    ordering = ['-pub_date']  # Optional: Order by publication date

# Detail view to display a single question
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'qna/question_detail.html'
    context_object_name = 'question'

# Create view to create a new question
class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'qna/question_create.html'

    def get_success_url(self):
        return reverse_lazy('question_detail', kwargs={'slug': self.object.slug})

# Edit view to update an existing question
class QuestionEditView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'qna/question_edit.html'

    def get_success_url(self):
        return reverse_lazy('question_detail', kwargs={'slug': self.object.slug})
