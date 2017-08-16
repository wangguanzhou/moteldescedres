from django import forms

ROOM_TYPES = (
    ('Economic', 'Economic(1 Double bed)'),
    ('Standard', 'Standard(1 Queen bed)'),
    ('Standard', 'Standard(2 Double bed)'),
    ('Superior', 'Superior(1 Queen bed)'),
)

class ReserveForm(forms.Form):
    checkin_date = forms.CharField(widget=forms.TextInput(attrs={'class':
        'form-control', 'id': 'checkin-datepicker', 'placeholder': 'Date of check-in'}))
    checkout_date = forms.CharField(widget=forms.TextInput(attrs={'class':
        'form-control', 'id': 'checkout-datepicker', 'placeholder': 'Date of check-out'}))
    room_type = forms.ChoiceField(label='Room Type', choices=ROOM_TYPES, widget=forms.Select(attrs={'class': 'form-control'}))
    num_of_rooms = forms.ChoiceField(label='Number of rooms', choices=((1,'1'), (2, '2'), (3, '3'), (4,
        '4')), widget=forms.Select(attrs={'class': 'form-control'}))
    client_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    client_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}))
    client_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    client_message = forms.CharField(widget=forms.Textarea(attrs={'class':
        'form-control', 'placeholder': 'Please leave your message here'}), required=False)
 
