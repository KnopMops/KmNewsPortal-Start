from django.conf import settings
from newsapi import NewsApiClient
from datetime import timedelta
from django.utils import timezone

from news.models import News, Category


def fetch_news():
    client = NewsApiClient(api_key=settings.NEWSAPI_API_KEY)
    date_from = timezone.now().date() - timedelta(days=1)

    for category in Category.objects.all():
        response = client.get_everything(q=category.name, language="ru", from_param=date_from)
        article = response.get("articles")[1]

        content = article.get("content").split("[")[0]
        content += f"<a href='{article.get('url')}' target='_blank'>Посмотреть полностью</a>"

        db_article = News(
            source=article["source"].get("name"),
            title=article.get("author"),
            description=content,
            image_url=article.get("urlToImage"),
            category=category,
        )
        db_article.save()