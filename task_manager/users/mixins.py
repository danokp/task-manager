from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class UserAccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.id == self.kwargs.get('pk')

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                _('You are not logged in! Log in, please.'),
            )
            return redirect('login')
        messages.error(
            self.request,
            _("You do not have permission to modify another user."),
        )
        return redirect('show_users')
