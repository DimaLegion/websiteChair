from .models import Task
from django.forms import ModelForm, widgets


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "characteristic", "color"]
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'task': widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'characteristic': widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите характеристики'}),
            'color': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите цвет'}),
        }
