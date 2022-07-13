from django import forms
from .models import Feedback
# class FeedbackForm(forms.Form):
#     name = forms.CharField(max_length=20, min_length=2, error_messages={
#         'max_length': 'Too many symbols',
#         'min_length': 'Too few symbols',
#         'required': 'Please, insert form 2 to 20 symbols',
#     })
#     surname = forms.CharField(max_length=20, min_length=2)
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
#     rating = forms.IntegerField(max_value=10, min_value=1)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'rating']
        fields = '__all__'
        # exclude = ['rating']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name': {
                'max_length': 'Too many symbols',
                'min_length': 'Too few symbols',
                'required': 'Field must not be empty',
            },
            'surname': {
                'max_length': 'Too many symbols',
                'min_length': 'Too few symbols',
                'required': 'Field must not be empty',
            },
        }