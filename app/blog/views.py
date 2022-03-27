from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Article, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,
                  'blog/blog/detail_view.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})



def blog_home(request):
    blog_info = Article.objects.order_by('title')
    return render(request, 'blog/blog_home.html', {'blog_info': blog_info})



class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog/detail_view.html'
    context_object_name = 'article'


class BlogUpdateView(UpdateView):
    model = Article
    template_name = 'blog/create.html'

    form_class = ArticleForm


class BlogDeleteView(DeleteView):
    model = Article
    success_url = '/blog/'
    template_name = 'blog/blog-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = ArticleForm()

    data ={
        'form': form,
        'error': error
    }

    return render(request, 'blog/create.html', data)




