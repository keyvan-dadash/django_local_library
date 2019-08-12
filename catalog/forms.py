from django import forms
import datetime

class ReNewBookForm(forms.Form):
    renewal_date = forms.DateField(label="Renewal Date:",widget=forms.TextInput(attrs={"class":"form-control ml-2"}) ,help_text="Enter a date between now and 4 weeks(default:3)")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise forms.ValidationError("Invalid date - renewal in past")
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError("Invalid date - renewal more than 4 weeks")

        return data
