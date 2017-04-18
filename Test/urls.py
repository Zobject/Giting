from django.conf.urls import url
from Test import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    #url(r'^snippets/', views.snippet_detail),
]