from django.shortcuts import render

from projects.models import Project


def projects_list_view(request):
    projects = Project.objects.all()
    return render(
        request=request,
        template_name='projects/projects_list.html',
        context={'projects': projects},
    )
