from django.forms.utils import ErrorList
from django import forms


class FormUserMixin:
    def form_valid(self, form):
        if not self.request.user.is_authenticated():
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["Stupid user is not logged in","Or just stupid"])
            return self.form_invalid(form)

        form.instance.user = self.request.user
        return super(FormUserMixin, self).form_valid(form)


class AllowedUserMixin:
    def form_valid(self, form):
        if  form.instance.user != self.request.user:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["You are not allowed to do that"])
            return self.form_invalid(form)
        return super(AllowedUserMixin, self).form_valid(form)
