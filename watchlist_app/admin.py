from django.contrib import admin
from watchlist_app.models import WatchList, StreamPlatform, Review

# Register your models here.
#admin.site.register(WatchList)
@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    list_display = ['title','streamingPlatform']
    # def get_queryset(self, request):
    #     return super().get_queryset(request).prefetch_related('tags')
    # def get_tags(self, obj):
    #     return ", ".join(o for o in obj.tags.name())

admin.site.register(StreamPlatform)
admin.site.register(Review)
