from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext as _
from django.utils.html import format_html

from datatableview.views import DatatableView
from core.mixins import AdminMixin

from answers.models import Sitting
from answers.forms import SittingForm


class SittingDatatableView(AdminMixin, DatatableView):
    """
    Allows you to manage sittings
    """

    model = Sitting
    template_name = "answers/sitting_list.html"
    datatable_options = {
        'structure_template': "datatableview/bootstrap_structure.html",
        'columns': [
            'title',
            (_("Actions"), 'id', 'get_actions'),
        ],
        'search_fields': ['title'],
        'unsortable_columns': ['id'],
    }

    def get_actions(self, instance, *args, **kwargs):
        return format_html(
            '<a href="{}">Edit</a>', reverse(
                'answers:sitting_edit', args=[instance.pk])
        )


class SittingUpdate(AdminMixin, UpdateView):
    model = Sitting
    form_class = SittingForm
    template_name = "answers/sitting_edit.html"
    success_url = reverse_lazy('answers:sitting_list')


class SittingAdd(AdminMixin, CreateView):
    model = Sitting
    form_class = SittingForm
    template_name = "answers/sitting_add.html"
    success_url = reverse_lazy('answers:sitting_list')
