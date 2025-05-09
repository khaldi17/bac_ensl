from django import forms
from .models import BacRegistration

class BacRegistrationForm(forms.ModelForm):
    class Meta:
        model = BacRegistration
        fields = ['first_name', 'last_name', 'speciality', 'phone', 'payment_receipt']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'الاسم الأول (مثال: أحمد)',
                'class': 'form-control',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'الاسم الأخير (مثال: محمد)',
                'class': 'form-control',
            }),
            'speciality': forms.Select(attrs={
                'class': 'form-select',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'رقم الهاتف (مثال: 0612345678)',
                'class': 'form-control',
            }),
            'payment_receipt': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
            }),
        }
        labels = {
            'first_name': 'الاسم الأول',
            'last_name': 'الاسم الأخير',
            'speciality': 'التخصص',
            'phone': 'رقم الهاتف',
            'payment_receipt': 'إيصال الدفع',
        }
       
        error_messages = {
            'first_name': {
                'required': 'الاسم الأول مطلوب.',
            },
            'last_name': {
                'required': 'الاسم الأخير مطلوب.',
            },
            'speciality': {
                'required': 'التخصص مطلوب.',
            },
            'phone': {
                'required': 'رقم الهاتف مطلوب.',
                'invalid': 'الرجاء إدخال رقم هاتف صالح.',
            },
            'payment_receipt': {
                'required': 'إيصال الدفع مطلوب.',
            },
        }

class UsernameSearchForm(forms.Form):
    username = forms.IntegerField(
        label="رقم التسجيل",
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': 'أدخل رقم التسجيل',
            'class': 'form-control',
        }),
    )
