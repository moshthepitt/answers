from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin  # , PolymorphicChildModelAdmin
from sorl.thumbnail.admin import AdminImageMixin

from questions.models import Quiz, Question, MultipleChoiceQuestion, MultipleChoiceOption
from questions.models import RatingQuestion, TextQuestion, EssayQuestion, BooleanQuestion
from questions.models import Category, Sitting

from core.utils import image_file


class QuizAdmin(AdminImageMixin, admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'image_thumb', 'category', 'draft']
    image_thumb = image_file('obj.image', short_description='Image')


class CategoryAdmin(admin.ModelAdmin):
    pass


class SittingAdmin(admin.ModelAdmin):
    pass


class MultipleChoiceOptionInline(AdminImageMixin, admin.TabularInline):
    model = MultipleChoiceOption


class MultipleChoiceQuestionAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['title', 'category', 'quiz']
    list_filter = ['quiz']
    inlines = [MultipleChoiceOptionInline, ]


class MultipleChoiceOptionAdmin(AdminImageMixin, admin.ModelAdmin):
    pass


class RatingQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['quiz']


class TextQuestionAdmin(admin.ModelAdmin):
    pass


class EssayQuestionAdmin(admin.ModelAdmin):
    pass


class BooleanQuestionAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(PolymorphicParentModelAdmin):
    base_model = Question

    child_models = (
        (MultipleChoiceQuestion, MultipleChoiceQuestionAdmin),
        (RatingQuestion, RatingQuestionAdmin),
        (TextQuestion, TextQuestionAdmin),
        (EssayQuestion, EssayQuestionAdmin),
        (BooleanQuestion, BooleanQuestionAdmin),
    )

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sitting, SittingAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(MultipleChoiceQuestion, MultipleChoiceQuestionAdmin)
admin.site.register(MultipleChoiceOption, MultipleChoiceOptionAdmin)
admin.site.register(RatingQuestion, RatingQuestionAdmin)
admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(EssayQuestion, EssayQuestionAdmin)
admin.site.register(BooleanQuestion, BooleanQuestionAdmin)
