from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic import View

from .forms import *
from lesson.forms import LessonForm
from lesson.models import Lesson, LessonVenue
from .models import Category, Course

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http.response import Http404
from django.contrib.auth.decorators import login_required


##### -------- Cours -------- #####
class CourseUpdateView(UpdateView):
    model = Course
    queryset = Course.objects.all()
    template_name = 'cours/cours_update.html'
    form_class = CourseForm

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['btn_title'] = 'Änderung Speichern'
        return context

    def form_valid(self, form):
        # form = CourseForm(request.POST, request.FILES)
        form.instance.user_id = self.request.user
        form.instance.display_name = form.cleaned_data['name']
        form.save()
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'cours/cours_delete.html'
    success_url = reverse_lazy('course:course_list')


class CourseListView(ListView):
    queryset = Course.objects.all()
    model = Course
    template_name = 'cours/cours_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class CourseCreateView(CreateView):
    model = Course
    template_name = 'cours/cours_creat.html'
    form_class = CourseForm
    # success_message = "%(name)s was created successfully"

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['user_id'] = self.request.user.pk
        context['btn_title'] = 'Create Course'
        return context

    def form_valid(self, form):
        # form = CourseForm(request.POST, request.FILES)
        form.instance.user_id = self.request.user
        form.instance.display_name = form.cleaned_data['name']
        form.save()
        return super(CourseCreateView, self).form_valid(form)


class CourseMaterialView(SuccessMessageMixin, View):
    template_name = 'cours/cours_user_view.html'
    error_message = 'Error saving the Doc, check fields below.'

    def get_object(self):
        try:
            obj = Course.objects.get(pk=self.kwargs['pk'])
        except Course.DoesNotExist:
            raise Http404('Course not found!')
        return obj

    def get_context_data(self, **kwargs):
        kwargs['course'] = self.get_object()
        if 'categoryform' not in kwargs:
            kwargs['categoryform'] = CategoryForm()
            kwargs['btn_title'] = 'Create Category'
        if 'lessonform' not in kwargs:
            kwargs['lessonform'] = LessonForm()
            kwargs['btn_title_2'] = 'Create Lesson'
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
            ctxt = {}
            
            if 'categoryform' in request.POST:
                categoryform = CategoryForm(request.POST, request.FILES)
                if categoryform.is_valid():
                    # categoryform = form.save(commit=False)
                    categoryform.save()
                    # success_message = 'Your name has been changed.'
                    messages.add_message(request, messages.INFO, 'wurde erfolgreich erstellt')
                else:
                    ctxt['lessonform'] = categoryform

            elif 'lessonform' in request.POST:

                if request.method == "POST":
                    form = LessonForm(request.POST, request.FILES)
                    if form.is_valid():
                        lesson = form.save(commit=False)
                        lesson.course = self.get_object()
                        lesson.save()
                        messages.add_message(request, messages.INFO, 'wurde erfolgreich erstellt')
                    else:
                        print('form error:', form.errors)
                        
            return render(request, self.template_name, self.get_context_data(**ctxt))


##### -------- Category -------- #####
class CategoryUpdateView(UpdateView):
    template_name = 'category/category_update.html'
    queryset = Category.objects.all()
    form_class = CategoryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_title'] = 'Category Update'
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category/category_delelet.html"
    success_url = reverse_lazy('/')


# User Course
class CourseUserSingleView(DetailView):
    model = Course
    template_name = "cours_user/cours_user_singel.html"

    def get_object(self):
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Course, pk=pk)
        return obj


# User view
@login_required
def user_view(request, lesson_id=None):
    lessons = LessonVenue.get_student_available_lesson(request.user)
    current_lesson_qs = lessons
    if lesson_id:
        current_lesson_qs = lessons.filter(pk=lesson_id)
    current_lesson = current_lesson_qs.first()
    if not current_lesson:
        Http404('Not available lesson yet!')
        
    return render(request,
                  'cours_user/user_lesson_view.html',
                  {'lessons': lessons,
                   'current_lesson': current_lesson})
