from django import forms
from customadmin.models import *
from courses.models import *




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


# class FrontEndSettingsForm(forms.ModelForm):

#         class Meta:
#             model = FrontEndSettings
#             fields = '__all__'

class GeneralSettingsForm(forms.ModelForm):

        class Meta:
            model = FrontEndSettings
            fields = '__all__'


class CategoryForm(forms.ModelForm):

        class Meta:
            model = Category
            fields = '__all__'




