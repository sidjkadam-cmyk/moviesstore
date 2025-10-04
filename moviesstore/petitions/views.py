from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Q
from .models import MoviePetition, PetitionVote
from .forms import MoviePetitionForm

def petition_list(request):
    """Display all movie petitions"""
    petitions = MoviePetition.objects.annotate(
        yes_votes=Count('votes', filter=Q(votes__vote_type='yes')),
        no_votes=Count('votes', filter=Q(votes__vote_type='no')),
        total_votes=Count('votes')
    ).order_by('-created_at')
    
    template_data = {
        'title': 'Movie Petitions',
        'petitions': petitions
    }
    return render(request, 'petitions/index.html', template_data)

@login_required
def create_petition(request):
    """Create a new movie petition"""
    if request.method == 'POST':
        form = MoviePetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            messages.success(request, 'Your petition has been created successfully!')
            return redirect('petitions.index')
    else:
        form = MoviePetitionForm()
    
    template_data = {
        'title': 'Create Movie Petition',
        'form': form
    }
    return render(request, 'petitions/create.html', template_data)

def petition_detail(request, petition_id):
    """Display petition details and voting"""
    petition = get_object_or_404(MoviePetition, id=petition_id)
    
    # Check if user has already voted
    user_vote = None
    if request.user.is_authenticated:
        try:
            user_vote = PetitionVote.objects.get(petition=petition, user=request.user)
        except PetitionVote.DoesNotExist:
            pass
    
    # Get vote counts
    yes_votes = petition.votes.filter(vote_type='yes').count()
    no_votes = petition.votes.filter(vote_type='no').count()
    total_votes = petition.votes.count()
    
    template_data = {
        'title': f'Petition: {petition.movie_title}',
        'petition': petition,
        'user_vote': user_vote,
        'yes_votes': yes_votes,
        'no_votes': no_votes,
        'total_votes': total_votes
    }
    return render(request, 'petitions/detail.html', template_data)

@login_required
@require_POST
def vote_petition(request, petition_id):
    """Vote on a petition"""
    petition = get_object_or_404(MoviePetition, id=petition_id)
    vote_type = request.POST.get('vote_type')
    
    if vote_type not in ['yes', 'no']:
        messages.error(request, 'Invalid vote type.')
        return redirect('petitions.detail', petition_id=petition_id)
    
    # Check if user already voted
    vote, created = PetitionVote.objects.get_or_create(
        petition=petition,
        user=request.user,
        defaults={'vote_type': vote_type}
    )
    
    if not created:
        # User already voted, update their vote
        vote.vote_type = vote_type
        vote.save()
        messages.info(request, 'Your vote has been updated.')
    else:
        messages.success(request, 'Your vote has been recorded!')
    
    return redirect('petitions.detail', petition_id=petition_id)

@login_required
def my_petitions(request):
    """Display petitions created by the current user"""
    petitions = MoviePetition.objects.filter(created_by=request.user).annotate(
        yes_votes=Count('votes', filter=Q(votes__vote_type='yes')),
        no_votes=Count('votes', filter=Q(votes__vote_type='no')),
        total_votes=Count('votes')
    ).order_by('-created_at')
    
    template_data = {
        'title': 'My Petitions',
        'petitions': petitions
    }
    return render(request, 'petitions/my_petitions.html', template_data)