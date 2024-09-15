from django.urls import path
from .views import HomePageView, ArticleDetail, ArticleList, ArticleCategoryList

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Головна сторінка
    path('articles/', ArticleList.as_view(), name='articles-list'),  # Список публікацій
    path(r'articles/category/<slug>', ArticleCategoryList.as_view(),name='articles-category-list'),  # Категорії
    path('articles/<int:year>/<int:month>/<int:day>/<slug>/', ArticleDetail.as_view(), name='news-detail'),  # Деталі публікації
]
