from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins  import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .models import Post, Comment
# Create your views here.


class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'

class BLogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'postDetail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'newPost.html'
    fields = ['title', 'author', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'postEdit.html'
    fields = ['body']

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'postDelete.html'
    success_url = reverse_lazy('home')
'''
def BlogDetailView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Comments = posts.commments.all()
    newComment = None
    template_name = 'postDetail.html'
    context_object_name = allBlogsList
    
    if requests.method=='Post':
        commentForm = CommentForm(data=request.POST)
    
        if comment_form.is_valid():
            newComment = comment_form.save(commit=False)
            newComment.post = post
            newComment.save()
            return redirect ('postDetail', pk=pk)

    else:
        comment_form = CommentForm()
        template_name = 'postComment'

    context = {'post': post, 'CommentForm': CommentForm, 'comments': comments, 'newComment': newComment}
    return render(request, template_name, context)
    '''
