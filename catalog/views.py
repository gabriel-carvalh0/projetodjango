from django.shortcuts import get_object_or_404, render
from django.views import generic
import catalog

from .models import Product, Category

class ProductListView(generic.ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

product_list = ProductListView.as_view()

class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)