from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"Категория ({self.name} - {self.id})"
    

class News(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=f"uploads/news/%d/%m/%Y/")
    image_url = models.URLField(blank=True, null=True)
    source = models.CharField(max_length=20, blank=True, null=True)
    likes = models.ManyToManyField(get_user_model(), related_name='news_like')

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"{self.title}"
    
    def number_of_likes(self):
        return self.likes.count()
    

class Comment(models.Model):
    article = models.ForeignKey(News, on_delete=models.PROTECT)
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    posted_at = models.DateTimeField(default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return f"{self.article.__str__()}: {self.posted_by}"
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Banner(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads/news/banner/%d/%m/%Y/")
    url = models.URLField()
    posted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}: {self.url}"

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"