from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from authentication.models import User
from django.contrib.auth.decorators import login_required
from website.models import Ticket, Review
from . import forms


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "website/view_ticket.html", context={'ticket': ticket})

@login_required
def flux_page(request):
    tickets = Ticket.objects.order_by('date_created')[::-1]
    reviews = Review.objects.order_by('date_created')[::-1]
    context = {'tickets': tickets, 'reviews': reviews}
    return render(request, "website/flux.html", context=context)

@login_required
def create_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST,request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            return redirect('flux-page')
    context = {'ticket_form': ticket_form}
    return render(request, 'website/create_ticket.html', context=context)    

@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteForm()
    if request.method == 'POST':
        if 'update_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST,request.FILES, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('flux-page')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('flux-page')

    context = { 'edit_form': edit_form, 'delete_form': delete_form, }
    return render(request, 'website/update_ticket.html', context=context)


@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review_form = forms.ReviewForm(instance=review)
    delete_review = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'update_review' in request.POST:
            review_form = forms.ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect('flux-page')
        if 'delete_review' in request.POST:
            delete_review = forms.DeleteReviewForm(request.POST)
            if delete_review.is_valid():
                review.delete()
                return redirect('flux-page')   
    context = {'review_form': review_form, 'delete_review': delete_review} 
    return render(request, 'website/update_review.html', context=context)



@login_required
def create_review(request):
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid() :
            review = review_form.save(commit=False)
            review.author = request.user
            review.ticket = Ticket.objects.last()
            review.save()
            return redirect('flux-page')
    context = {'review_form':review_form}
    return render(request, 'website/create_review.html', context=context)    


@login_required
def create_review_from_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.ticket = Ticket.objects.get(id=ticket_id)
            review.save()
            return redirect('flux-page')
    context={"ticket": ticket, "review_form": review_form}
    return render(request, 'website/create_review_from_ticket.html', context=context) 





# @login_required
# def view_posts(request, ticket_id):
#     ticket = get_object_or_404(Ticket, id=ticket_id)  
#     # tickets = Ticket.objects.all()
#     # tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
#     # reviews = Review.objects.filter(user=request.user)
#     # reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
#     # posts = sorted(chain(reviews, tickets),
#     #                key=lambda post: post.time_created, reverse=True)
#     return render(request, 'website/posts.html', context={"ticket": ticket})



@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('plux-page')
    return render(request, 'website/follow_users.html', context={'form':form})    
