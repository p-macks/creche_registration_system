from django.urls import path
from . views import StudentList,StudentDetail,StudentCreate,StudentUpdate,StudentDelete,AppLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('login/',AppLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',RegisterPage.as_view(), name='register'),
    path('',StudentList.as_view(),name='students'),
    path('student/<int:pk>/',StudentDetail.as_view(),name='student'),
    path('student_create/',StudentCreate.as_view(),name='student_create'),
    path('student_update/<int:pk>/',StudentUpdate.as_view(),name='student_update'),
    path('student_delete/<int:pk>/',StudentDelete.as_view(),name='student_delete'),
]