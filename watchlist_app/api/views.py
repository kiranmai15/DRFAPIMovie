from rest_framework.response import Response
from watchlist_app.models import WatchList, Review
from watchlist_app.api.serializers import WatchListSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#no need of decorators in Class Based Views of APIView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


#Concrete View Class
class ReviewList(generics.ListCreateAPIView):
    #queryset = Review.objects.all()
    # overwrite the QuerySet TO get reviews for a specific movie
   serializer_class = ReviewSerializer
   permission_classes = [IsAuthenticated]
   
   def get_queryset(self):
       pk = self.kwargs['pk']
       return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class WatchListAV(APIView):
  #define a get method
    def get(self, request):
        movies = WatchList.objects.all()
        #Utilise the serializer n return the response
        serializer = WatchListSerializer(movies,many=True) 
              # when we have multiple objects ,serializer should map each object
        return Response(serializer.data)
    def post(self, request):
        serilizer = WatchListSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors)

    
class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error' : 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk) 
        #serialize the data send by the user
        # get the particular movie id 
        serializer = WatchListSerializer(movie, data=request.data)
        #check if it is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self, request, pk):
       movie = WatchList.objects.get(pk = pk)
       movie.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)


from watchlist_app.models import StreamPlatform
from watchlist_app.api.serializers import StreamPlatformSerializer

# Serializer for StreamPlatform
class StreamPlatformAV(APIView):
    def get(self, request):
        movies = StreamPlatform.objects.all()
        #Utilise the serializer n return the response
        serializer = StreamPlatformSerializer(movies,many=True, context={'request': request}) 
              # when we have multiple objects ,serializer should map each object
        return Response(serializer.data)
    def post(self, request):
        serilizer = StreamPlatformSerializer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors)
        
# Particular streaming details
class StreamDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error' : 'Streaming Platform not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(movie, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = StreamPlatform.objects.get(pk=pk) 
        #serialize the data send by the user
        # get the particular movie id 
        serializer = StreamPlatformSerializer(movie, data=request.data)
        #check if it is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self, request, pk):
       movie = StreamPlatform.objects.get(pk = pk)
       movie.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)





# Function Based Views --------------------------------
# # what type of view this is: add the decorator for GET Requests
# @api_view(['GET','POST'])
# def movie_list(request):
    
#     if request.method == 'GET':
#        movies = Movie.objects.all()
#        serializer = MovieSerializer(movies,many=True) 
#        # when we have multiple objects ,serializer should map each object
#        return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error' : 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk) 
#         #serialize the data send by the user
#         # get the particular movie id 
#         serializer = MovieSerializer(movie, data=request.data)
#         #check if it is valid
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#        movie = Movie.objects.get(pk = pk)
#        movie.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
    
