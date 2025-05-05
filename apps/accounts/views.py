from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.serializers import CreaseUserSerializer


class RegisterAPIView(APIView):
    serializer_class = CreaseUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'massage': 'success'}, status=201)
        return Response(serializer.errors, status=400)
