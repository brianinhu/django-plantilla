from django.shortcuts import render
from django.contrib import messages
from myapp.models import Article, Category
# Create your views here.


def index(request):
    start = 10
    end = 20
    range_numbers = range(start, end+1)
    return render(request, 'index.html',
                  {'title': 'Home',
                   'variable': 'This is a variable for index.html',
                   'start': 10,
                   'end': 20,
                   'range_numbers': range_numbers})


def about(request):
    team = ['John', 'Jane', 'Jack', 'Jill']
    return render(request, 'about.html',
                  {'title': 'About',
                   'variable': 'This is a variable for about.html',
                   'team': None})


def contact(request):
    return render(request, 'contact.html',
                  {'title': 'Contact',
                   'variable': 'This is a variable for contact.html'})


def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html',
                  {'title': 'Articles',
                   'articles': articles})


def v_create_article(request):
    return render(request, 'create_article.html',
                  {'title': 'Create Article'})


def f_create_article(request):
    try:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            image = request.POST['image']
            published_time = request.POST['published_time']

            article = Article(title=title, content=content,
                              image=image, published_time=published_time)
            article.save()
            messages.success(request, 'Article created successfully.')
    except:
        messages.error(request, 'Article created failed.')

    articles = Article.objects.all()
    return render(request, 'articles.html',
                  {'title': 'Articles',
                   'articles': articles})


def v_edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'edit_article.html',
                  {'title': 'Edit Article',
                   'article': article})


def f_edit_article(request):
    if request.method == 'POST':
        article_id = request.POST['id']
        title = request.POST['title']
        content = request.POST['content']
        image = request.POST['image']
        published_time = request.POST['published_time']

        article = Article.objects.get(id=article_id)
        article.title = title
        article.content = content
        article.image = image
        article.published_time = published_time
        article.save()

    articles = Article.objects.all()
    return render(request, 'articles.html',
                  {'title': 'Articles',
                   'articles': articles})


def f_delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()

    articles = Article.objects.all()
    return render(request, 'articles.html',
                  {'title': 'Articles',
                   'articles': articles})
