from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import CommentForm, PostForm

from .models import Post
from django.views.generic import ListView, DetailView, CreateView


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'djangoBlog/create_post.html'
    success_url = reverse_lazy('post-list')


class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
    template_name = 'djangoBlog/post_detail.html'
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('-created_at')
        if self.request.method == 'POST':
            context['form'] = CommentForm(self.request.POST)
        else:
            context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()

            if request.headers.get('HX-Request') == 'true':
                html = f"""
                <div>
                    <p>{comment.text}</p>
                    <small>Author: {comment.author_name} | {comment.created_at.strftime('%Y-%m-%d %H:%M')}</small>
                </div>
                """
                return HttpResponse(html)
            else:
                return redirect('post-detail', pk=self.object.pk)
        else:
            if request.headers.get('HX-Request') == 'true':
                return HttpResponse(status=400)
            else:
                context = self.get_context_data()
                context['form'] = form
                return self.render_to_response(context)


class AddCommentView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            if request.headers.get('HX-Request') == 'true':
                html = f"""
                <div>
                    <p>{comment.text}</p>
                    <small>Author: {comment.author_name} | {comment.created_at.strftime('%Y-%m-%d %H:%M')}</small>
                </div>
                """
                return HttpResponse(html)
            else:
                return redirect('post-detail', pk=pk)
        else:
            if request.headers.get('HX-Request') == 'true':
                return HttpResponse(status=400)
            else:
                return redirect('post-detail', pk=pk)
