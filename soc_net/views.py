from django.shortcuts import render, redirect
from django.views.generic import DetailView, View
from .models import Post

from .forms import PostForm

from datetime import date


class SocListView(View):
    def get(self, request):
        post = Post.objects.filter(publication_date__lte=date.today()).filter(moderation=True)
        return render(request, 'home.html', {'list_post': post})


class SocDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class SocCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post_new.html', {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.author = request.user
                if request.user.groups.filter(name='my_editors').exists() or request.user.groups.filter(name='my_admin').exists():
                    new_post.moderation = True
                    new_post.save()
                return redirect(new_post)
            return render(request, 'post_new.html', {'form': form})
