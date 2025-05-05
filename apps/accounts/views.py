from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.accounts.serializers import CreaseUserSerializer, MyTokenObtainPairSerializer


class RegisterAPIView(APIView):
    serializer_class = CreaseUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'}, status=201)
        return Response(serializer.errors, status=400)


class MyTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
