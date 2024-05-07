from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from news.models import News
from news.forms import NewUserForm, CommentForm


class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()
        return context
    

class ArticleDetailView(TemplateView):

    template_name = "news/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = News.objects.get(pk=kwargs.get("pk"))
        context["comment_form"] = CommentForm
        return context
    

class RegisterView(FormView):

    template_name = "auth/register.html"
    form_class = NewUserForm

    def form_valid(self, form):
        form.save()
        return super().form_valid()
    

class CommentView(FormView):

    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.posted_by = self.request.user
        comment.article_id = self.kwargs.get("pk")
        comment.save()

        return HttpResponseRedirect(reverse("article_detail"), args=[self.kwargs.get("pk")])
    

def Logout(request):
    logout(request)
    return redirect('index')


def news_like(request, pk):
    news = get_object_or_404(News, pk=pk)

    if news.likes.filter(id=request.user.id).exists():
        news.likes.remove(request.user)
    else:
        news.likes.add(request.user)

    return HttpResponseRedirect(reverse("article_detail", args=[str(pk)]))