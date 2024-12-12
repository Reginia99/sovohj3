from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'home.html', {'destinations': destinations})

@login_required
def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    reviews = destination.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.destination = destination  # Link the review to the destination
            review.user = request.user       # Assign the logged-in user
            review.save()
            return redirect('destination_detail', pk=destination.pk)  # Redirect to the same page
    else:
        form = ReviewForm()

    reviews = destination.reviews.all()

    return render(request, 'destination_detail.html', {
        'destination': destination,
        'reviews': reviews,
        'form': form,
    })
