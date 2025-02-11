from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy, render
from django.shortcuts import get_object_or_404

from .models import Cours, Lesson, Review


class CoursMixin:
    model = Cours
    fields = '__all__'
    template_name = 'cours/cours.html'
    success_url = reverse_lazy('cours:cours_list')


class CoursListView(ListView):
    model = Cours
    ordering = 'start_date'
    paginate_by = 10


class LessonListView(ListView):
    model = Lesson
    ordering = 'id'
    paginate_by = 10


class ReviewListView(ListView):
    model = Review
    ordering = 'id'


class CoursCreateView(CreateView, CoursMixin):
    pass


class CoursUpdateView(UpdateView, CoursMixin):
    pass


def course_detail(request, pk):
    cours = get_object_or_404(Cours, pk)
    context = {"cours": cours}
    return render(request, 'cours_detail.html', context)