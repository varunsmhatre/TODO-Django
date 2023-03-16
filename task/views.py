from django.shortcuts import render
from .models import Task
from datetime import date
from  django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime
# Create your views here.




@login_required
def home(request):
    data_list = []
    col_names = ('id', 'title', 'start_date', 'end_date')
    for row in Task.objects.filter(status='ongoing', creator=request.user).order_by('end_date').values_list(*col_names):
        # print(row)
        data_dict = {}
        for i in range(0, len(col_names)):
            data_dict[col_names[i]] = row[i]
        data_dict['breached'] = date.today() > row[-1]
        data_list+=[data_dict]
    # print(data_list)
    # print(request.user.username)
    return render(request, 'task/home.html', {'tasks':data_list})


class TaskDetailView(DetailView, LoginRequiredMixin):
    model = Task


class TaskCreateView(CreateView, LoginRequiredMixin):
    model = Task
    fields = ['title', 'start_date', 'end_date']

    def get_form(self, form_class=None):
        form = super(TaskCreateView, self).get_form(form_class)
        form.fields['start_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        form.fields['end_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form
    
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    fields = ['title', 'start_date', 'end_date', 'status', 'comments']

    def get_form(self, form_class=None):
        form = super(TaskUpdateView, self).get_form(form_class)
        form.fields['start_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        form.fields['end_date'].widget = AdminDateWidget(attrs={'type': 'date'})
        form.fields['comments'].label += " (Add Reason for Closing or Completed Comments if Required)"
        return form

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        task = self.get_object()
        if self.request.user == task.creator:
            return True
        return False

@login_required
def task_history(request):
    data_list = []
    col_names = ('title', 'date_created', 'start_date', 'end_date', 'status', 'comments', 'date_cc')
    for row in Task.objects.exclude(status='ongoing').filter(creator=request.user).order_by('start_date').values_list(*col_names):
        # print(row)
        data_dict = {}
        for i in range(0, len(col_names)):
            data_dict[col_names[i]] = row[i]
        data_dict['breached'] = row[-1].date() > row[3]
        data_list+=[data_dict]
    return render(request, 'task/history.html', {'tasks':data_list})


def about(request):
    return render(request, 'task/about.html', {'title':'About'})