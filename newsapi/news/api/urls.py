from django.urls import path
from news.api.views import (ArticleListCreateAPIView,
                            ArticleDetailAPIView,
                            JournalistCreateAPIView)

urlpatterns=[
    path('articles/',ArticleListCreateAPIView.as_view(),name = "article-list"),
    path('articles/<int:pk>',ArticleDetailAPIView.as_view(),name="article-detail"),
    path('journalist/',JournalistCreateAPIView.as_view(),name="journalist-list")
]