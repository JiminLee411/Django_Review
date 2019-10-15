from django.urls import path
from . import views

app_name = 'articles' # 처음부터 url app name

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/comment/create/', views.comment_create, name='comment_create'),
    path('<int:pk>/comment/<int:c_pk>/delete/', views.comment_del, name='comment_del'),
]


# url은 사용자가 보낸 요청!!!!!!!!!!!!!