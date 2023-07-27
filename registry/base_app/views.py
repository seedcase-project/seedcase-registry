from django.shortcuts import render, redirect
from .models import Variable, Project
from django.views.generic import ListView


def home(request):
    """
    Render the home page
    """
    return render(request, 'home.html')


def VariableList(request):
    """
    Create variable list for the table view for the html page
    """
    variables = Variable.objects.filter(availability=True)
    return render(request, 'variable_list.html', {'variables': variables})


class ProjectList(ListView):
    """
    Create basic list view from the model to render tha html page
    """
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'
