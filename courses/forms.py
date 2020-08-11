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
                'placeholder': 'Course Title',
            }
        )

        self.fields['description'].widget.attrs.update(
            {
                'placeholder': 'Course Description',
            }
        )

        self.fields['price'].widget.attrs.update(
            {
                'placeholder': 'Leave Blank You If Free ',
            }
        ) 
        self.fields['offer_price'].widget.attrs.update(
            {
                'placeholder': 'Offer Price If you Have',
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
    fields=('curriculum_title', ),
    extra=1,
    widgets={
        'curriculum_title': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Lesson Title Here',
                'required': 'required'
            }
        )
    }

)
LessonContentFormset = modelformset_factory(
    LessonContent,
    fields=('title', 'video_link', 'text_content'),
    extra=1,
    widgets={
        'title': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Video title here',
                'required': 'required'

            }
        ),
        'video_link': forms.TextInput(
            attrs={
                'class': 'form-control lesson-video',
                'placeholder': 'Enter Video Link here',
                'value': 'html://',
                # 'required': 'required'

            }
        ),        
        'text_content': forms.TextInput(
            attrs={
                'style': 'display: none',
                'class': 'form-control lesson-text',
                'placeholder': 'Enter Text Content here',
                # 'required': 'required'
            }
        )
    }
)
