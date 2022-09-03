from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy

from posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('posts.list')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'text']

    def get_success_url(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk != None:
            return reverse_lazy('posts.detail', args=(pk,))
        else:
            return reverse_lazy('posts.detail', args=(self.object.id,))


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('posts.list')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
