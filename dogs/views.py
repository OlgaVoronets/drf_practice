from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from dogs.models import Category, Dog
from dogs.serializers import CategorySerializer, DogSerializer, DogDetailSerializer, CategoryDetailSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializers = {
        'retrieve': CategoryDetailSerializer,
        'list': CategorySerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_class)


class DogCreateView(generics.CreateAPIView):
    serializer_class = DogSerializer


class DogListView(generics.ListAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogRetrieveView(generics.RetrieveAPIView):
    serializer_class = DogDetailSerializer
    queryset = Dog.objects.all()


class DogUpdateView(generics.UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogDestroyView(generics.DestroyAPIView):
    queryset = Dog.objects.all()
