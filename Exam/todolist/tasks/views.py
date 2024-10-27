from django.views import generic
from .models import Task, Category
from django.db.models import Q
from django.shortcuts import render


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')
        search_query = self.request.GET.get('search')

        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if search_query:
            queryset = queryset.filter(Q(title__icontains=search_query))

        return queryset


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

# tasks/views.py
from django.views.generic import CreateView
from .models import Task
from .forms import TaskForm

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = '/tasks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        print(context['categories'])
        return context
