from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from blog.models import Post

# Create your views here.

class HomeView(generic.ListView):
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    # queryset = User.objects.all()
    queryset = Post.objects.all()

    # def get_context_data(self):
    #     return {"posts": posts}

    # def get(self, request):
    #     context = {"posts": posts}
    #     return render(request, 'blog/home.html', context=context)


class AboutView(generic.View):
    
    def get(self, request):
        context = {"name":"Sample about template"}
        return render(request, 'blog/about.html', context=context)