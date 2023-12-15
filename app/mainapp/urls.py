from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('reg', views.reg_page),
    path('log', views.login_page),
    path('lg', views.log_out),
    path('postnote', views.post_note),
    path('clear/<str:note_id>', views.delete_note)
]