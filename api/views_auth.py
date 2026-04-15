from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password']
    )
    return Response({"message": "User created"})


@api_view(['POST'])
def login(request):
    from django.contrib.auth import authenticate

    user = authenticate(
        username=request.data['username'],
        password=request.data['password']
    )

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
        })
    return Response({"error": "Invalid credentials"}, status=400)
