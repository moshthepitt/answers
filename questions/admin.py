from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin  # , PolymorphicChildModelAdmin

from questions.models import Quiz, Question, MultipleChoiceQuestion, MultipleChoiceOption
from questions.models import RatingQuestion, TextQuestion, EssayQuestion, BooleanQuestion
from questions.models import Category


class QuizAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    pass


class MultipleChoiceOptionInline(admin.TabularInline):
    model = MultipleChoiceOption


class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    inlines = [MultipleChoiceOptionInline, ]


class MultipleChoiceOptionAdmin(admin.ModelAdmin):
    pass


class RatingQuestionAdmin(admin.ModelAdmin):
    pass


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
admin.site.register(Question, QuestionAdmin)
admin.site.register(MultipleChoiceQuestion, MultipleChoiceQuestionAdmin)
admin.site.register(MultipleChoiceOption, MultipleChoiceOptionAdmin)
admin.site.register(RatingQuestion, RatingQuestionAdmin)
admin.site.register(TextQuestion, TextQuestionAdmin)
admin.site.register(EssayQuestion, EssayQuestionAdmin)
admin.site.register(BooleanQuestion, BooleanQuestionAdmin)
