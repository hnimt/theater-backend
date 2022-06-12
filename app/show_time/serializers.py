from rest_framework import serializers

from show_time.models import ShowTime


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = ['id', 'value']
