from rest_framework.serializers import ModelSerializer

from director.models import Director


class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'description', 'avatar', 'created_at', 'updated_at']