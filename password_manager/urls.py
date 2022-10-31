from django.urls import path, include

urlpatterns = [
    path('api/', include('password_manager.api.urls'))
]
