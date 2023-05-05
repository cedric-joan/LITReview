from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from website.models import Ticket, Review , UserFollows
from django.contrib.auth.models import User
from authentication.models import User
from itertools import chain
from django.db.models import CharField, Value
from . import forms


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "website/view_ticket.html", context={'ticket': ticket})

@login_required
def flux_page(request):

    
    users_followed = UserFollows.objects.filter(user=request.user)
    reviews = Review.objects.filter(author__in=[user_followed.followed_user for user_followed
                                in users_followed])

    tickets = Ticket.objects.filter(author__in=[user_followed.followed_user for user_followed
                                in users_followed])

    
    tickets_and_reviews = sorted(chain(tickets, reviews),
                                 key=lambda instance: instance.date_created,
                                 reverse=True)
    
    paginator = Paginator(tickets_and_reviews, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'tickets_and_reviews': tickets_and_reviews, 'page_obj': page_obj}
    return render(request, "website/flux.html", context=context)




@login_required
def display_posts(request):
    tickets_user = Ticket.objects.filter(author=request.user)
    tickets_user = tickets_user.annotate(content_type=Value('TICKET', CharField()))
    reviews_user = Review.objects.filter(author=request.user)
    reviews_user = reviews_user.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(chain(tickets_user, reviews_user),
                   key=lambda instance: instance.date_created, reverse=True)
    
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts, 'page_obj': page_obj}
    return render(request, 'website/posts.html', context=context)


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
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid() and ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.author = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.author = request.user
            review.ticket = Ticket.objects.last()
            review.save()
            return redirect('flux-page')
    context = {'ticket_form': ticket_form,'review_form':review_form}
    return render(request, 'website/create_review.html', context=context)    


@login_required
def create_review_from_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            ticket.has_review = True
            ticket.save()
            review = review_form.save(commit=False)
            review.author = request.user
            review.ticket = Ticket.objects.get(id=ticket_id)
            review.ticket.has_review = True
            review.save()
            return redirect('flux-page')
    context={"ticket": ticket, "review_form": review_form}
    return render(request, 'website/create_review_from_ticket.html', context=context) 




@login_required
def follow_users(request):
    users_follow_you = [user_follow.user.username for user_follow in
                        UserFollows.objects.filter(followed_user=request.user.id)]
    users_followed = UserFollows.objects.filter(user_id=request.user)
    users_to_exclude = [user_followed.followed_user.username for user_followed in users_followed]
    users_to_exclude.append(request.user.username)
    users_to_follow = User.objects.exclude(username__in=users_to_exclude)
    if request.method == "POST":
        to_follow = User.objects.get(pk=request.POST["to_follow"])
        if to_follow in users_to_follow:
            UserFollows(user=request.user, followed_user=to_follow).save()
    users_followed = UserFollows.objects.filter(user_id=request.user)
    return render(request, 'website/follow_users.html', context={"users_followed": users_followed,
                                                                 "users_to_follow": users_to_follow,
                                                                 "users_follow_you": users_follow_you})
        


@login_required
def delete_follow_users(request, user_id):
    user_follow = UserFollows.objects.get(user=request.user, followed_user=user_id)
    if request.method == "POST":
        user_follow.delete()
        return redirect('follow_users')






