from .models import Category


def category_list(request):
    cat_list = {'cat_list': Category.objects.all()}
    return cat_list