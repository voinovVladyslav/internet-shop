from django.views import generic

from core.models import Category


class HomeView(generic.TemplateView):
    template_name = 'core/categories.html'
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
