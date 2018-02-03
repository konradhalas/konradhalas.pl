from django.shortcuts import render

from talks.models import Talk


def talks_list_view(request):
    talks = Talk.objects.all()
    return render(
        request=request,
        template_name='talks/talks_list.html',
        context={
            'talks': talks,
        }
    )
