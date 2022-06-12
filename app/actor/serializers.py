from rest_framework.serializers import ModelSerializer

from actor.models import Actor


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'description', 'avatar', 'created_at', 'updated_at']