from django.urls import path
from .views import SocListView,\
                   SocDetailView,\
                   SocCreateView


urlpatterns = [
    path('posts/', SocCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', SocDetailView.as_view(), name='post_detail'),
    path('', SocListView.as_view(), name='home'),
]
