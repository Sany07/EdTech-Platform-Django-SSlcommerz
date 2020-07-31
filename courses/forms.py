from django import forms
from django.forms import modelformset_factory


from courses.models import *




class CourseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Course Title :"
        self.fields['price'].label = "Course Price :"
        self.fields['offer_price'].label = "Discount Price* :"
        self.fields['description'].label = "Course Description :"
        # self.fields['tags'].label = "Tags :"

        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Python Basic to Advance',
            }
        )

        self.fields['price'].widget.attrs.update(
            {
                'placeholder': '199.0',
            }
        )
        self.fields['offer_price'].widget.attrs.update(
            {
                'placeholder': '',
            }
        )

    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'price',
            'offer_price',
            'thumbnail',
            'category'

        ]

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Category is required")
        return category

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get('thumbnail')

        if not thumbnail:
            raise forms.ValidationError("Thumbnail is required")
        return thumbnail

    def save(self, commit=True):
        course = super(CourseModelForm, self).save(commit=False)
        if commit:
            course.save()
        return course


LessonFormset = modelformset_factory(
    Lesson,
    fields=('title', ),
    extra=1,
    widgets={
        'title': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Lesson Title Here'
            }
        )
    }

)
LessonContentFormset = modelformset_factory(
    LessonContent,
    fields=('title', 'video_link', ),
    extra=1,
    widgets={
        'title': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Video title here'

            }
        ),
        'video_link': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Video Link here'
            }
        )
    }
)
