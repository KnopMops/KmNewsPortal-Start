from django.urls import path
from django.contrib.auth.views import LoginView

from news.views import IndexView, ArticleDetailView, RegisterView, Logout, news_like, CommentView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),

    path('article/<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('article/<int:pk>/like/', news_like, name="news_like"),
    path('article/<int:pk>/comment/', CommentView.as_view(), name="article_comment"),

    path('auth/register/', RegisterView.as_view(), name="register"),
    path('auth/login/', LoginView.as_view(template_name="auth/login.html"), name="login"),
    path('auth/logout/', Logout, name="logout")
]
