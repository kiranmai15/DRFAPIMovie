# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all() # Complex Queryset Result
#     data = {
#         'movies': list(movies.values())
#        }# Python Dictionary
#     return JsonResponse(data) # JSON Response


# # Individual JSON responses for specific movies
# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.desc,
#         'active': movie.active
#     }
#     return JsonResponse(data) # JSON Response