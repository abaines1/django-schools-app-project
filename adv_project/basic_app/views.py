from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        
        return context
    

# Function Based Views
# def index(request):
#   return render(request, 'index.html')

# Class Based Template Views
# class IndexView(TemplateView):
#   template_name = 'index.html'
#

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    model = models.School
    template_name = 'basic_app/school_list.html'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

    def get_success_url(self):
        return reverse_lazy('basic_app:school_detail', kwargs={'pk': self.object.pk})
    

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

    def get_success_url(self):
        return reverse_lazy('basic_app:school_detail', kwargs={'pk': self.object.pk})
    

class SchoolDeleteView(DeleteView):
    model = models.School
    
    def get_success_url(self):
        return reverse_lazy('basic_app:list')  # redirect to list page

class StudentDetailView(DetailView):
    model = models.Student
    template_name = 'basic_app/student_detail.html'

class StudentCreateView(CreateView):
    fields = ('name', 'age', 'school')
    model = models.Student

    def get_success_url(self):
        return reverse_lazy('basic_app:school_detail', kwargs={'pk': self.object.school.pk})
    

class StudentUpdateView(UpdateView):
    fields = ('name', 'age', 'school')
    model = models.Student

    def get_success_url(self):
        return reverse_lazy('basic_app:student_detail', kwargs={'pk': self.object.pk})