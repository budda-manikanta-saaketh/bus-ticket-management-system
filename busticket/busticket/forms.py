from django import forms

class Booktickets(forms.Form):
    Full_name=forms.CharField()
    Aadhar_number=forms.CharField()
    From=forms.CharField()
    To=forms.CharField()
    date = forms.DateField()
    Number_of_seats=forms.IntegerField()
class Ticketid_form(forms.Form):
    Ticket_Id=forms.CharField()