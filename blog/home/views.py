# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializer import BlogPostSerializer
from .models import BlogPost


class BlogView(APIView):
    permission_classes     = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        blogs      = BlogPost.objects.all()
        serializer = BlogPostSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)        
        return Response(
            {
                "message": "Blog post created successfully.",
                "data":    serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )
    def patch(self, request, pk):
        try:
            instance = BlogPost.objects.get(id=pk)
            serializer = BlogPostSerializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BlogPost.DoesNotExist:
            return Response({"error": "Blog post not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response({"error": "You do not have permission to delete this blog post."}, status=status.HTTP_403_FORBIDDEN)
        try:
            instance = BlogPost.objects.get(id=pk)
            instance.delete()
            return Response({"message": "Blog post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        except BlogPost.DoesNotExist:
            return Response({"error": "Blog post not found."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

