from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import api_model
from .serializers import APISerializer
from django.contrib.auth import authenticate

class UserApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        api_m = api_model.objects.filter(for_user = request.user.id)
        serializer = APISerializer(api_m, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'telegram_user_id': request.data.get('telegram_user_id'),
            'username': request.data.get('username'),
            'password': request.data.get('password')
        }
        
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            try:
                if api_model.objects.filter(telegram_user_id=data['telegram_user_id'], for_user=user.id).exists():
                    return Response({'success': True}, status=status.HTTP_200_OK)
            except api_model.DoesNotExist:
                return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)