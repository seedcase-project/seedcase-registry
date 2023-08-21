from django.shortcuts import render
from .models import Variable, Project, Request
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializer import RequestSerializer
from .serializer import VariableSerializer


def home(request):
    """
    Render the home page
    """
    return render(request, "home.html")


def VariableList(request):
    """
    Create variable list for the table view for the html page
    """
    variables = Variable.objects.filter(availability=True)
    context = {"variables": variables}
    return render(request, "variable_list.html", context)


@api_view(["GET"])
def all_variables(request):
    """
    API endpoint to get all variables
    """
    variables = Variable.objects.all()
    serializer = VariableSerializer(variables, many=True)
    return Response(serializer.data)


class ProjectList(ListView):
    """
    Create basic list view from the model to render tha html page
    """

    model = Project
    template_name = "project_list.html"
    context_object_name = "projects"


@api_view(["POST"])
def create_request(request):
    """
    API endpoint to create a new request and associated variables.

    Parameters:
    - request.data: JSON payload containing request information and variables.

    Returns:
    - 201 Created: If the request is successfully created.
    - 400 Bad Request: If the payload data is invalid.

    Example JSON payload:
    {
        "request_id": "123456",
        "status": "PENDING",
        "username": "richard",
        "contact_email": "richard@email.com",
        "variables": [1, 2]
    }
    """
    payload = request.data
    variables_ids = payload.pop("variables")

    try:
        request_obj = Request.objects.create(**payload)
        variables = Variable.objects.filter(id__in=variables_ids)
        request_obj.variables.set(variables)

        response_data = {
            "request_id": request_obj.request_id,
            "status": request_obj.status,
            "username": request_obj.username,
            "contact_email": request_obj.contact_email,
            "variables": variables_ids,
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
