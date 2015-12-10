from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.html import format_html

from datatableview.views import DatatableView
from core.mixins import AdminMixin, CustomerQuerysetMixin
from saas.mixins import CustomerSaveMixin, CustomerListViewMixin, CustomerCheckMixin

from reviews.models import Review
from reviews.mixins import ReviewMixin
from reviews.forms import ReviewForm, PeerReviewForm
from questions.forms import quiz_form_helper, save_quiz_form, make_custom_cleaned_quiz_form


class ReviewView(CustomerCheckMixin, ReviewMixin, FormMixin, DetailView):
    model = Review

    def get_success_url(self):
        return reverse('dashboard')

    def get_form_class(self):
        return make_custom_cleaned_quiz_form(self.object.quiz)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        save_quiz_form(self.object.quiz, form, self.request.user, self.object)
        return super(ReviewView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        form = self.get_form()
        context['form'] = form
        context['form_helper'] = quiz_form_helper(self.object.quiz)
        return context

    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        return super(ReviewView, self).dispatch(*args, **kwargs)


class ReviewUpdate(AdminMixin, CustomerCheckMixin, CustomerSaveMixin, CustomerQuerysetMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_edit.html"
    success_url = reverse_lazy('reviews:review_list')


class ReviewAdd(AdminMixin, CustomerSaveMixin, CustomerQuerysetMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_add.html"
    success_url = reverse_lazy('reviews:review_list')


PeerReviewUpdate = ReviewUpdate.as_view(
    form_class=PeerReviewForm,
    success_url=reverse_lazy('reviews:peer_review_list')
)
PeerReviewAdd = ReviewAdd.as_view(
    form_class=PeerReviewForm,
    success_url=reverse_lazy('reviews:peer_review_list')
)


class ReviewDatatableView(AdminMixin, CustomerListViewMixin, DatatableView):
    model = Review
    template_name = "reviews/review_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            'title',
            'sitting',
            'quiz',
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['title', 'sitting__title'],
        'unsortable_columns': ['id'],
    }
    review_type = None

    def get_queryset(self):
        queryset = super(ReviewDatatableView, self).get_queryset()
        return queryset.filter(userprofile=None)

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Report</a>', reverse(
                'reviews:review_edit', args=[instance.pk]), reverse('reports:review', args=[instance.pk])
        )


class PeerReviewDatatableView(AdminMixin, CustomerListViewMixin, DatatableView):
    model = Review
    template_name = "reviews/peer_review_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            'title',
            'sitting',
            'quiz',
            (_("User"), 'userprofile', 'get_user'),
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['title', 'userprofile__user__last_name', 'userprofile__user__first_name', 'userprofile__user__username', 'sitting__title'],
        'unsortable_columns': ['id'],
    }
    review_type = None

    def get_queryset(self):
        queryset = super(PeerReviewDatatableView, self).get_queryset()
        return queryset.exclude(userprofile=None)

    def get_user(self, instance, *args, **kwargs):
        return instance.userprofile.get_display_name()

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Report</a>', reverse(
                'reviews:peer_review_edit', args=[instance.pk]), reverse('reports:peer_review', args=[instance.pk])
        )
