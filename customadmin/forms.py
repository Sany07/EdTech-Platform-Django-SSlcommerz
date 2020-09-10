from django import forms
from django.forms import modelformset_factory


from customadmin.models import *




class GatewayForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        # self.fields['title'].label = "Course Title :"

        # self.fields['tags'].label = "Tags :"

        # self.fields['title'].widget.attrs.update(
        #     {
        #         'placeholder': 'Course Title',
        #     }
        # )




    class Meta:
        model = PaymentGatewaySettings
        fields = '__all__'


class FrontEndSettingsForm(forms.ModelForm):

        class Meta:
            model = FrontEndSettings
            fields = '__all__'




