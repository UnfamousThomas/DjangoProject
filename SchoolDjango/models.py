from django import forms

class DiscordMessage(forms.Form):
    message = forms.CharField(label= 'Saada Discordi:', max_length=500)
