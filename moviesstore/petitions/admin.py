from django.contrib import admin
from .models import MoviePetition, PetitionVote

@admin.register(MoviePetition)
class MoviePetitionAdmin(admin.ModelAdmin):
    list_display = ['movie_title', 'year', 'title', 'created_by', 'created_at']
    list_filter = ['year', 'genre', 'created_at']
    search_fields = ['movie_title', 'title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']

@admin.register(PetitionVote)
class PetitionVoteAdmin(admin.ModelAdmin):
    list_display = ['petition', 'user', 'vote_type', 'created_at']
    list_filter = ['vote_type', 'created_at']
    search_fields = ['petition__movie_title', 'user__username']
    ordering = ['-created_at']