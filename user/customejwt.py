from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import timedelta


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # refresh = self.get_token(self.user)
        # data['refresh'] = str(refresh)

        refresh = RefreshToken.for_user(self.user)
        access_token = refresh.access_token
        access_token.set_exp(lifetime=timedelta(days=10))
        data['token'] = str(access_token)
        # data['token'] = str(refresh.access_token)
        # Add extra responses here
        data['username'] = self.user.username
        data['role'] = 'admin'
        data['id'] = self.user.id
        data['firstName'] = 'Azmi'
        data['lastName'] = 'Refani'
        data['password'] = self.user.password

        # data['groups'] = self.user.groups.values_list('name', flat=True)
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)