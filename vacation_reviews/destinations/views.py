from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from .models import Destination, Picture
from .forms import PictureUploadForm


def home(request):
    destinations = Destination.objects.all()
    return render(request, 'home.html', {'destinations': destinations})

@login_required
def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    reviews = destination.reviews.all()

    # Handle review submission
    if request.method == 'POST':
        # Handle picture upload
        picture_form = PictureUploadForm(request.POST, request.FILES)
        if picture_form.is_valid():
            picture = picture_form.save(commit=False)
            picture.destination = destination
            picture.save()
        
        # Handle review submission
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.destination = destination
            review.user = request.user
            review.save()

            return redirect('destination_detail', pk=destination.pk)  # Redirect after submitting the review and picture
    else:
        picture_form = PictureUploadForm()
        review_form = ReviewForm()

    return render(request, 'destination_detail.html', {
        'destination': destination,
        'reviews': reviews,
        'picture_form': picture_form,
        'review_form': review_form,
    })

from django.shortcuts import render, redirect
from .forms import DestinationForm  # Assuming you have a DestinationForm

@login_required
def add_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after adding the destination
    else:
        form = DestinationForm()

    return render(request, 'add_destination.html', {'form': form})

    reviews = destination.reviews.all()

@login_required   
def delete_destination(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect('home')  # Redirect to the home page after deletion
    return render(request, 'confirm_delete.html', {'destination': destination})