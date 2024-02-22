from django.http import Http404

class GuestOnlyMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)