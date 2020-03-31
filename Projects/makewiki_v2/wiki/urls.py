from django.urls import path
from wiki.views import PageListView, PageDetailView, create_page, PostCreateView
from wiki.forms import PageForm


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('w/create/', create_page, name="wiki-create-page"),
    path('p/create/', PostCreateView.as_view(), name='post-create-page')
]
