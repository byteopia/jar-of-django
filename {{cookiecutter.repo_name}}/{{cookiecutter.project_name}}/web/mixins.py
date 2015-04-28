from django.views.generic import base
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class PageTitleMixin(base.ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['page_title'] = self.title
        except AttributeError:
            context['page_title'] = "Title"
        return context


class StatusContextMixin(base.ContextMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = {'slug': "Healthy", 'detail': "All services are operational with no known issues."}
        context['status'] = status
        return context
