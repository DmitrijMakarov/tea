from django import forms


class ReviewForm(forms.Form):
    str = forms.CharField(
        label='Отзыв',
        required=True,
        min_length=1,
        max_length=10000,
    )
