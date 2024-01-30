from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, Tag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        flag = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    flag += 1
            if flag > 1:
                raise ValidationError('Основным может быть только один раздел')
            else:
                pass
        if flag == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    pass
