from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from dogs.models import Category, Dog
from dogs.permissions import IsModerator, IsDogPublic, IsDogOwner
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
    permission_classes = [~IsModerator]


class DogListView(generics.ListAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [AllowAny]


class DogRetrieveView(generics.RetrieveAPIView):
    serializer_class = DogDetailSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsModerator | IsDogOwner | IsDogPublic]


class DogUpdateView(generics.UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogDestroyView(generics.DestroyAPIView):
    queryset = Dog.objects.all()
    permission_classes = [~IsModerator]
