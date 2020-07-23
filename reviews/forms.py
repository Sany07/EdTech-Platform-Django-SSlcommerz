from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
    # content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    content      = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Review
        fields = [         
        # 'user',
        # 'content_type',
        'object_id',
        'content'

        ]

    def clean(self, *args, **kwargs):
        # c_type = self.cleaned_data.get("content_type")
        object_id = self.cleaned_data.get("object_id")
        content = self.cleaned_data.get("content")


        return super(ReviewForm, self).clean(*args, **kwargs)

