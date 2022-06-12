from rest_framework import serializers

from show_date.models import ShowDate


class ShowDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowDate
        fields = ['id', 'value']