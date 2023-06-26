from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _

from .models import Task
from .filters import TaskFilter

from task_manager.statuses.models import Status
from task_manager.users.models import User


class TaskListView(View):
    '''Show list of tasks'''

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        filtered_tasks = TaskFilter(
            request.GET,
            queryset=tasks,
            request=request,
        )
        button_text = _('Show')
        return render(
            request,
            'tasks/show_tasks.html',
            context={
                'filtered_tasks': filtered_tasks,
                'button_text': button_text,
            },
        )


class TaskView(View):
    '''Show task.'''

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = Task.objects.get(id=task_id)
        return render(
            request,
            'tasks/task.html',
            context={'task': task}
        )


class TaskCreateView(View):
    '''Create new task.'''

    pass


class TaskUpdateView(View):
    '''Update task.'''

    pass


class TaskDeleteView(View):
    '''Delete task.'''

    pass
