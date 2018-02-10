from django.shortcuts import render, get_object_or_404

from articles.models import Article


def articles_list_view(request):
    articles = Article.objects.filter(is_public=True)
    return render(
        request=request,
        template_name='articles/articles_list.html',
        context={'articles': articles},
    )


def article_details_view(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(
        request=request,
        template_name='articles/article_details.html',
        context={'article': article},
    )
