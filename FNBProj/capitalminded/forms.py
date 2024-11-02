# your_app/forms.py
from django.contrib.auth import get_user_model
from django import forms
from .models import MicroLoan
from .models import Post
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class MicroLoanApplicationForm(forms.ModelForm):
    class Meta:
        model = MicroLoan
        fields = ['amount_requested', 'term_months', 'purpose']
        widgets = {
            'purpose': forms.Textarea(attrs={'rows': 4}),
        }


# forms.py


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 7, 'placeholder': 'Share your business success story...'})
        }
