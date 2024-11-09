from django import forms
import datetime
from .models import *

class FormEx(forms.Form):
    name = forms.CharField(max_length=100)
    comment= forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    email = forms.EmailField(required=False, label="Please enter your email")
    agree = forms.BooleanField()
    BirthDate = forms.DateField(initial= datetime.date.today,widget=forms.NumberInput(attrs={"type" : "datetime-loacl"}))
    BIRTH_DAY_CHOICE = ["1999", "2001", "2002", "2003", "2004"]
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_DAY_CHOICE))
    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    fav_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    fav_color1 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    model = forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all(), initial=0)
    last_modified = models.DateTimeField(auto_now_add=True)

class Prac(forms.ModelForm):
    class Meta:
        model = PracModel
        fields = "__all__"