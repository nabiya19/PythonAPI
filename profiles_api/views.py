from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """returns a list of API view features"""
        an_apiview = ['Uses HTTP methods as function(get, post, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manially to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
