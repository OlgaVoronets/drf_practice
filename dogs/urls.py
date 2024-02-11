from django.urls import path
from rest_framework import routers

from dogs.views import CategoryViewSet, DogListView, DogCreateView, DogRetrieveView, DogDestroyView, DogUpdateView

app_name = 'dogs'

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [
    path('', DogListView.as_view()),
    path('create/', DogCreateView.as_view()),
    path('update/<int:pk>/', DogUpdateView.as_view()),
    path('destroy/<int:pk>/', DogDestroyView.as_view()),
    path('detail/<int:pk>/', DogRetrieveView.as_view()),
]
urlpatterns += router.urls
