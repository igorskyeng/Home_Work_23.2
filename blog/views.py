from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog

from pytils.translit import slugify

from main.forms import BlogForm


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    permission_required = 'blog.add_blog'
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Blog
    permission_required = 'blog.view_blog'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        blogs = Blog.objects.all()

        context_data['object_list'] = blogs
        context_data['title'] = 'Блог'

        return context_data


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    permission_required = 'blog.change_blog'
    fields = ('title', 'body', 'image_preview')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

    def test_func(self):
        return self.request.user.is_superuser


def switching_publications(request, pk):
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.publication_sign:
        blog_item.publication_sign = False
    else:
        blog_item.publication_sign = True

    blog_item.save()

    return redirect(reverse('blog:list'))
