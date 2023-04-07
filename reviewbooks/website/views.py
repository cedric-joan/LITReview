from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from authentication.models import User
from django.contrib.auth.decorators import login_required, permission_required
from website.models import Ticket
from . import forms


@login_required
# @permission_required('website.edit_ticket', raise_exception=True)
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, "website/view_ticket.html", context={'ticket': ticket})

@login_required
def flux_page(request):
    tickets = Ticket.objects.all()
    return render(request, "website/flux.html", context={'tickets': tickets})

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
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('flux-page')
    context = { 'edit_form': edit_form, }
    return render(request, 'website/edit_ticket.html', context=context)


@login_required
def delete_ticket(request, ticket_id):
    # ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('flux-page')




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