from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from articles.feed import ArticlesRSSFeed, ArticlesAtomFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('misc.urls')),
    path('talks/', include('talks.urls')),
    path('projects/', include('projects.urls')),
    path('articles/', include('articles.urls')),
    path('rss/', ArticlesRSSFeed(), name='articles_rss'),
    path('atom/', ArticlesAtomFeed(), name='articles_atom'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
