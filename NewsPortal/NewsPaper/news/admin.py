from django.contrib import admin
from .models import Post, Subscriber

def nullfy_rating(modeladmin, request, queryset):
    queryset.update(rating=0)
nullfy_rating.short_description = 'Обнулить рейтинг'
class PostAdmin(admin.ModelAdmin):
    list_display = ["categoryType", "author", "dateCreation", "title", "rating"]
    list_filter = ["categoryType", "author", "dateCreation", "rating"]
    search_fields = ["categoryType", "author", "dateCreation", "rating"]
    actions = [nullfy_rating]

admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber)


