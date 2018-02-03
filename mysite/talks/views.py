from django.db.models import Min
from django.shortcuts import render

from talks.models import Talk


def talks_list_view(request):
    talks = Talk.objects.annotate(
        last_event_date=Min('events__date'),
    ).order_by('-last_event_date').prefetch_related('events')
    return render(
        request=request,
        template_name='talks/talks_list.html',
        context={
            'talks': talks,
        }
    )
