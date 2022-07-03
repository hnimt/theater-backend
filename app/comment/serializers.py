from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user_email = serializers.CharField(source='user.email')

    class Meta:
        model = Comment
        fields = ['id', 'user_email', 'movie', 'value', 'is_updated',
                  'is_deleted', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        res = Comment.objects.create(user=user, movie=validated_data['movie'],
                                     value=validated_data['value'], is_updated=False)
        return res

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.user == user:
            return super().update(instance, validated_data)
        raise serializers.ValidationError(_("Not permission to update comment."))
