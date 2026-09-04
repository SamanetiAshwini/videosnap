from django.contrib import admin
from .models import *

admin.site.register(Video)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Playlist)
admin.site.register(VideoComment)
admin.site.register(VideoLike)
admin.site.register(VideoShare)
admin.site.register(WatchHistory)
admin.site.register(SavedVideo)
admin.site.register(Subscription)
