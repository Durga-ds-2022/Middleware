from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from User_account.models import UserFunction

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= UserFunction
        fields= '__all__'
        
    def validate_password(self, password):
        if len(password)> 3 and len(password)<12:
            if not password.isidentifier():
                return password
            raise ValidationError("Password should be contain speical Charactor")
        raise ValidationError("Password length should between 3 to 12")
    
    
            