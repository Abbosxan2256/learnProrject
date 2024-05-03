from django.contrib.auth.views import LoginView
from django.urls import path

from apps.views import IndexListView, RegisterCreateView, ProfileDetailView

urlpatterns = [
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='prof'),
    path('', IndexListView.as_view(), name='index_x'),
    path('register', RegisterCreateView.as_view(), name='registers'),
    path('login', LoginView.as_view(
        template_name='apps/login.html',
        redirect_authenticated_user=True,
        next_page='index_x'
    ), name='login'),
]
