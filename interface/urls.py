from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
      path('submit_idea', views.submit_idea, name='submit_idea'),
        path("need-project/", views.need_project, name="need_project"),
]
