from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),

    #CRUD
    path('dashboard/',views.dasboard_view,name="dashboard"),
    path('create-record/',views.create_record,name="create-record"),
    path('update-record/<int:pk>',views.update_record,name="update-record"),
    path('record/<int:pk>',views.singular_record,name="record"),
    path('delete-record/<int:pk>',views.delete_record,name="delete-record")
]