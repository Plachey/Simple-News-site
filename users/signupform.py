from .models import CustomUser
from django import forms as frm


class SignUpForm(frm.Form):
    email = frm.EmailField(required=True)
    first_name = frm.CharField(max_length=30, label='First Name', required=False)
    last_name = frm.CharField(max_length=30, label='Last Name', required=False)
    age = frm.IntegerField(min_value=0, required=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'age',)

    def signup(self, user):
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']

        user.save()
        return user
