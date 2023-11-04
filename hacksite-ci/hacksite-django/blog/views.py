import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Blog, Comment

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, 'index.html', context)


@login_required
def detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    comments = Comment.objects.filter(blog=blog)
    logger.info(f'request.method: {request.method}')
    if request.method == 'POST':
        data = {'comment': request.POST['comment'],
                'blog': blog,
                'user': request.user}
        form = CommentForm(data)
        if form.is_valid():
            logger.info('Is valid!')
            # form.blog = blog
            # form.user = request.user
            form.save()
        else:
            logger.info(f'Else!: {form.errors}')
    else:
        form = CommentForm()
    context = {'blog': blog, 'form': form, 'comments': comments}
    return render(request, 'blog/_id.html', context)
