"""djangorestframeworkproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from webproj.views import todo_viewset, users_viewset
ROUTER = DefaultRouter()
ROUTER.register(r'todos', todo_viewset.TodoItemListViewSet, base_name='todos')

users = users_viewset.UsersViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'docs/', include_docs_urls(title='XXXX', )),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(ROUTER.urls)),
    url(r'^users/', users),

    # url(r'api-token', views.obtain_auth_token),
    url(r'^jwt$', obtain_jwt_token),
    url(r'^jwt_verify$', verify_jwt_token),


    # path(r'^index/', TemplateView.as_view(template_name='index.html'), name='index')
]

