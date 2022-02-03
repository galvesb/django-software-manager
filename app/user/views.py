from rest_framework import exceptions


from rest_framework.response import Response
from rest_framework.views import APIView

from .authentication import JWTAuthentication

from .models import User

from .serializers import UserSerializer


class RegisterUser(APIView):
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Login(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if not user or not user.check_password(password):
            raise exceptions.AuthenticationFailed("Incorrect username or password!")

        token = JWTAuthentication.generate_access_token(user)

        response = Response()
        response.data = {"message": token}

        return response