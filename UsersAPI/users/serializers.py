from rest_framework import serializers
from .models import UsersData

class UsersSerializer(serializers.ModelSerializer):
    """
    Returns users list.
    """
    class Meta:
        model = UsersData
        fields = ['id','full_name','emp_code', 'status', 'email', 'status', 'crd', 'upd']

class CreateUsersSerializer(serializers.ModelSerializer):
    """

    """
    email = serializers.EmailField()
    emp_code = serializers.IntegerField()
    class Meta:
        model= UsersData
        fields = ['id','full_name','emp_code', 'email', 'status', 'crd', 'upd']

    def create(self, validated_data):
        if UsersData.objects.filter(email =validated_data['email']).exists():
            user_data = UsersData.objects.get(email__iexact=validated_data['email'].strip())
            user_data.full_name = validated_data['full_name'].strip()
            user_data.emp_code = validated_data['emp_code']
            user_data.save()
        else:
            user_data = UsersData.objects.create(full_name=validated_data['full_name'].strip(),email =validated_data['email'].lower(),emp_code = validated_data['emp_code'])

        return user_data