from django.urls import path
from quiz import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('quiz/',views.quiz,name='quiz'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('startquiz/',views.pre_quiz,name='pre_quiz')
]
