from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from dogs.models import Dog, Category
from dogs.validators import validator_words


class DogSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    name = serializers.CharField(validators=[validator_words])

    class Meta:
        model = Dog
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DogDetailSerializer(serializers.ModelSerializer):
    category_count = SerializerMethodField()
    category = CategorySerializer()

    def get_category_count(self, instance):
        return Dog.objects.filter(category=instance.category).count()

    class Meta:
        model = Dog
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_dogs = DogSerializer(source='dog_set', many=True)

    class Meta:
        model = Category
        fields = '__all__'
