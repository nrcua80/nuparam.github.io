from django.urls import path
from .import views


urlpatterns = [
   # path('admin/', admin.site.urls),
   path('',views.index, name='index'),
  #  path('index/', views.index1, name='index1'),
  path('register', views.register, name='register'),
  path('login', views.login, name ='login'),
  path('logout', views.logout, name = 'logout'),
  path('post/<str:pk>', views.post, name = 'post'),
  path('counter', views.counter, name = 'counter'),
  
]