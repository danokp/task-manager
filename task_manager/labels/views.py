from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from task_manager.mixins import UserLoginRequiredMixin
from .models import Label
from .forms import LabelCreationForm
from task_manager.tasks.models import Task


class LabelView(UserLoginRequiredMixin, ListView):
    '''Show list of labels.'''

    model = Label


class LabelCreateView(UserLoginRequiredMixin, CreateView):
    '''Create new label.'''

    model = Label
    form_class = LabelCreationForm
    success_url = reverse_lazy('show_labels')
    template_name = 'labels/create_label.html'
    extra_context = {'button_text': _('Create')}

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Label has been created successfully'),
        )
        return super().form_valid(form)


class LabelUpdateView(UserLoginRequiredMixin, UpdateView):
    '''Update label.'''

    model = Label
    form_class = LabelCreationForm
    success_url = reverse_lazy('show_labels')
    template_name = 'labels/update_label.html'
    extra_context = {'button_text': _('Update')}

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Label has been updated successfully'),
        )
        return super().form_valid(form)


class LabelDeleteView(UserLoginRequiredMixin, DeleteView):
    '''Delete label.'''

    model = Label
    success_url = reverse_lazy('show_labels')
    template_name = 'labels/delete_label.html'
    extra_context = {'button_text': _('Delete')}

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        related_tasks = Task.objects.filter(labels=self.object)
        if related_tasks.exists():
            messages.error(
                request,
                _('Cannot delete label. There are related tasks.'),
            )
            return redirect('show_labels')
        messages.success(self.request, _('Label has been deleted'))
        return super().post(request)
