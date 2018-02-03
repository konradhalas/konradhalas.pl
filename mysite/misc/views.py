from django.shortcuts import render


def home_view(request):
    return render(
        request=request,
        template_name='misc/home.html',
    )


def about_view(request):
    return render(
        request=request,
        template_name='misc/about.html',
    )
