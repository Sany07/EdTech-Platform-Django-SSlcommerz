from django import forms



from billings.models import Billing


class BillingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BillingForm, self).__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )

        for field in self.fields:
            self.fields[field].required = True

        # self.fields['password1'].error_messages.update({
        #     'required': 'Password is required'
        # })


    class Meta:
        model = Billing
        # fields = ['email', 'username', 'first_name',
        #           'last_name',  'password1', 'password2', ]

        exclude = ('user', 'timestamp', 'products')         





