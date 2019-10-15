from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
        }
    return render (request, 'articles/index.html', context)

def create(request):
    # POST 요청이면,
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        # valid?
        if article_form.is_valid():
            # valid하면, 저장
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    # GET 요청이면,
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article' : article,
        'comment_form' : comment_form,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article = article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'article_form' : article_form
    }
    return render(request, 'articles/form.html', context)

def comment_create(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail', article.pk)

def comment_del(request, pk, c_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=c_pk)
        comment.delete()
        return redirect('articles:detail', pk)
    