from django.db import models
from django.contrib.auth.models import User

class MoviePetition(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    movie_title = models.CharField(max_length=255, help_text="The title of the movie you want to see added")
    year = models.IntegerField(help_text="Year the movie was released")
    genre = models.CharField(max_length=100, blank=True, help_text="Movie genre (optional)")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_petitions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.movie_title} ({self.year}) - {self.title}"

class PetitionVote(models.Model):
    VOTE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    id = models.AutoField(primary_key=True)
    petition = models.ForeignKey(MoviePetition, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=3, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['petition', 'user']  # One vote per user per petition
    
    def __str__(self):
        return f"{self.user.username} voted {self.vote_type} on {self.petition.movie_title}"