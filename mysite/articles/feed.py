import datetime

from django.contrib.gis.feeds import Feed
from django.urls import reverse_lazy
from django.utils.feedgenerator import Atom1Feed

from articles.models import Article


class ArticlesRSSFeed(Feed):
    title = 'Konrad Hałas - software engineer, speaker and trainer'
    link = reverse_lazy('articles_list')
    description = 'Latest articles by Konrad Hałas'

    def items(self):
        return Article.objects.filter(is_public=True)

    def item_title(self, item: Article):
        return item.title

    def item_description(self, item: Article):
        return item.text_summary

    def item_link(self, item: Article):
        return item.get_absolute_url()

    def item_pubdate(self, item: Article):
        return datetime.datetime(item.publish_date.year, item.publish_date.month, item.publish_date.day)

    def item_updateddate(self, item: Article):
        return datetime.datetime(item.update_date.year, item.update_date.month, item.update_date.day)


class ArticlesAtomFeed(ArticlesRSSFeed):
    feed_type = Atom1Feed
    subtitle = ArticlesRSSFeed.description
