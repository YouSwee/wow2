from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail

class URLTests(TestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_articles_list_url_resolves(self):
        url = reverse('articles-list')
        self.assertEqual(resolve(url).func.view_class, ArticleList)

    def test_article_category_list_url_resolves(self):
        url = reverse('articles-category-list', kwargs={'slug': 'example-category'})
        self.assertEqual(resolve(url).func.view_class, ArticleCategoryList)

    def test_article_detail_url_resolves(self):
        url = reverse('news-detail', kwargs={
            'year': 2024,
            'month': 9,
            'day': 15,
            'slug': 'example-article'
        })
        self.assertEqual(resolve(url).func.view_class, ArticleDetail)
