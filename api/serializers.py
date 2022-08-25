from rest_framework import serializers
from .models import Car
from django.contrib.auth.models import User


        
# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     mark = serializers.CharField(max_length=100)
#     model = serializers.CharField(max_length=100)
#     broken = serializers.BooleanField(required=False, 
#                                    default=False,)
#     power = serializers.IntegerField()
# 	# created = serializers.DateTimeField()
	
#     def create(self, validated_data):
#         print(validated_data)
#         return Car.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.mark = validated_data.get('mark', instance.mark)
#         instance.model = validated_data.get('model', instance.model)
#         instance.broken = validated_data.get('broken', instance.broken)
#         instance.power = validated_data.get('power', instance.power)
#         instance.save()
#         return instance
    
class CarSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Car
        fields = ['url', 'id', 'mark', 'model', 'broken', 'power', 'owner']
        
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    cars = serializers.HyperlinkedRelatedField(many=True, 
                                              view_name='car-detail', 
                                              read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'cars']