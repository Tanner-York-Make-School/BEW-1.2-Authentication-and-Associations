from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.models import User

from wiki.models import Page
from wiki.forms import PageForm, PostForm


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })


class PostCreateView(CreateView):
    """ Renders the create post form """
    def get(self, request, *args, **kwargs):
        context = {'form': PostForm()}
        return render(request, 'create-post.html', context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.save()
          return HttpResponseRedirect('/')
        return render(request, 'create-post.html', {'form': form})
    

def create_page(request):
  """ Gets data from the user to create a new page"""
  if request.method == 'POST' and request.user.is_authenticated:
    form  = PageForm(data=request.POST)
    if form.is_valid():
      new_page = form.save(commit=False)
      new_page.author = request.user
      new_page.save()
      return HttpResponseRedirect('/')
    else:
      form = PageForm()
    return render(request, 'create-page.html', {'form': form})
  else: 
    form = PageForm()
    return render(request, 'create-page.html', {'form': form, 'error_message': 
                  'You need to be authenticated to create new pages'})