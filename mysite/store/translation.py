from .models import Product, Category
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)