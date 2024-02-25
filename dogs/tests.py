from django.test import TestCase
from dogs.models import Dog, Category
from dogs.serializers import DogSerializer


class DogModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name='Test_cat'
        )
        Dog.objects.create(
            id=1,
            name='test_name',
            category=category
        )

    def test_dog_name(self):
        dog = Dog.objects.get(pk=1)
        self.assertEqual(
            dog.name,
            'test_name'
        )


class DogSerializerTest(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name='Test_cat'
        )

    def test_dog_serializer(self):
        data = {'name': 'продам собачку',
                'category': 'Test_cat'}

        serializer = DogSerializer(data=data)
        self.assertFalse(
            serializer.is_valid()
        )

