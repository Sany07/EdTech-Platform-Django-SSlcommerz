from django import forms
from django.forms import modelformset_factory
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from accounts.models import CustomUser
from courses.models import *


class StudentRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter User Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        for field in self.fields:
            self.fields[field].required = True

        self.fields['password1'].error_messages.update({
            'required': 'Password is required'
        })
        self.fields['password2'].error_messages.update({
            'required': 'Confirm Password is required'
        })

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name',
                  'last_name',  'password1', 'password2', ]

    def save(self, commit=True):
        user = UserCreationForm.save(self, commit=False)
        user.role = "stu"
        if commit:
            user.save()
        return user


class TeacherRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(TeacherRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter User Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        for field in self.fields:
            self.fields[field].required = True

        self.fields['password1'].error_messages.update({
            'required': 'Password is required'
        })
        self.fields['password2'].error_messages.update({
            'required': 'Confirm Password is required'
        })

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name',
                  'last_name',  'password1', 'password2', ]

    def save(self, commit=True):
        user = UserCreationForm.save(self, commit=False)
        user.role = "tea"
        if commit:
            user.save()
        return user


class StudentChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name',  'password']


class UserLoginForm(forms.Form):
    email_or_username = forms.CharField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def clean(self, *args, **kwargs):
        email_or_username = self.cleaned_data.get("email_or_username")
        password = self.cleaned_data.get("password")

        if email_or_username and password:
            try:
                user = CustomUser.objects.get(username=email_or_username)
                self.user = authenticate(username=user, password=password)

            except:
                try:
                    user = CustomUser.objects.get(email=email_or_username)
                    self.user = authenticate(email=user, password=password)

                except CustomUser.DoesNotExist:

                    raise forms.ValidationError("User Does Not Exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")

            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


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
            'category',
            'language'

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
