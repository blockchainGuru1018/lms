from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .forms import *
from .models import *


class LessonDetailView(DetailView):
    queryset = Lesson.objects.all()
    template_name = 'lesson/lesson_detail.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Lesson, pk=pk)
        return obj

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        #context['form'] = SectionModelForm
        context['form_2'] = LectureForm
        return context


class LessonUpdateView(UpdateView):
    template_name = 'lesson/lesson_update.html'
    queryset = Lesson.objects.all()
    form_class = LessonForm

    def get_success_url(self):
        return reverse ('lesson:lesson_detail', kwargs={'pk': self.object.pk})


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = "lesson/lesson_delelet.html"
    success_url = reverse_lazy('course:course_list')


class LectureCreateView(SuccessMessageMixin, CreateView):
    form_class = LectureForm
    template_name = 'lesson/lecture_detail.html'
    success_message = "%(name)s wurde erfolgreich erstellt"

    def get_success_url(self):
        return reverse ('lesson:lecture_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        #object = form.instance.lecture = Lesson.objects.get(pk=self.kwargs['pk'])
        self.object = form.save()
        return super().form_valid(form)



class LectureDetailView(DetailView):
    model = Lecture
    template_name = 'lesson/lecture_detail.html'

    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Lecture, pk=pk)
        return obj


class LectureUpdateView(UpdateView):
    template_name = 'lesson/lecture_update.html'
    queryset = Lecture.objects.all()
    form_class = LectureFormUpdate

    def get_success_url(self):
        return reverse ('lesson:lesson_detail', kwargs={'pk': self.object.pk})
