from rest_framework import serializers
from . import models 
from hellogram.users import models as user_models


class SmallImageSerializer(serializers.ModelSerializer):
    
    """ Used for the notifications """

    class Meta:
        model = models.Image
        fields = (
            'file',
        )

class UserProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'file',
            'comment_count',
            'like_count',
        )


class FeedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = user_models.User 
        fields = (
            'username',
            'profile_image'
        )



class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id',
            'message',
            'creator',
        )



class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = (
            'creator'
        )




class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image 
        fields = (
            'id',
            'creator',
            'file',
            'location',
            'caption',
            'comments',
            'like_count',
            'created_at'
            
        )


class InputImageSerializer(serializers.ModelSerializer):

    file = serializers.FileField(required=False)

    class Meta:
        model = models.Image
        fields = (
            'file',
            'location',
            'caption'
        )
