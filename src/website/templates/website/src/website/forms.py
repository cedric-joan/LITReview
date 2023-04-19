from django import forms
from django.contrib.auth import get_user_model
from . import models


class TicketForm(forms.ModelForm):
    update_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mx-auto w-50 mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mx-auto w-50 mb-3'})}


class DeleteForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    
    
class ReviewForm(forms.ModelForm):
    update_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'comment']
        CHOICES = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)]
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control mx-auto w-50 mb-3'}),
            'rating': forms.RadioSelect(choices=CHOICES, attrs={'class': 'form-check-label mx-3 '
                                                                         'd-flex justify-content-center'}),
            'body': forms.Textarea(attrs={'class': 'form-control mx-auto w-50 mb-3'})
        }

class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    

User = get_user_model()

class FollowUsersForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['follows']