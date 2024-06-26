from typing import Optional, List

from django import forms

# Инструменты для формы

def get_default_attrs(extra: Optional[dict] = None):
    if extra:
        attrs = extra
    else:
        attrs = {'class': 'form-input form-control'}
    return attrs


def get_attrs_with_classes(classes: List[str]):
    """
    Возвращает атрибуты со своими классами

    Пример использования: get_attrs_with_classes(["form-input", "form-control"])
    """
    attrs = {
        "class": " ".join(classes)
    }
    return attrs


class LoginUserForm(forms.Form):
    attrs = get_default_attrs()
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs=attrs))


class RegisterUserForm(forms.Form):
    attrs = get_default_attrs()
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs=attrs))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs=attrs))

class ReviewForm(forms.Form):
    str = forms.CharField(
        label='Отзыв',
        required=True,
        min_length=1,
        max_length=10000,
    )
