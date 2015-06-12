from django.contrib import admin

from polymorphic.admin import PolymorphicParentModelAdmin

from answers.models import Answer, TextAnswer, MultipleChoiceAnswer, EssayAnswer, RatingAnswer, BooleanAnswer


class TextAnswerAdmin(admin.ModelAdmin):
    pass


class MultipleChoiceAnswerAdmin(admin.ModelAdmin):
    pass


class EssayAnswerAdmin(admin.ModelAdmin):
    pass


class RatingAnswerAdmin(admin.ModelAdmin):
    pass


class BooleanAnswerAdmin(admin.ModelAdmin):
    pass


class AnswerAdmin(PolymorphicParentModelAdmin):
    base_model = Answer
    child_models = (
        (TextAnswer, TextAnswerAdmin),
        (MultipleChoiceAnswer, MultipleChoiceAnswerAdmin),
        (EssayAnswer, EssayAnswerAdmin),
        (RatingAnswer, RatingAnswerAdmin),
        (BooleanAnswer, BooleanAnswerAdmin)
    )


admin.site.register(Answer, AnswerAdmin)
admin.site.register(TextAnswer, TextAnswerAdmin)
admin.site.register(MultipleChoiceAnswer, MultipleChoiceAnswerAdmin)
admin.site.register(EssayAnswer, EssayAnswerAdmin)
admin.site.register(RatingAnswer, RatingAnswerAdmin)
admin.site.register(BooleanAnswer, BooleanAnswerAdmin)
