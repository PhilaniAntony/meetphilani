from django import forms
from .models import Message, Collaboration


class MessageModelForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class CollaborationModelForm(forms.ModelForm):
    class Meta:
        model = Collaboration
        fields = '__all__'
