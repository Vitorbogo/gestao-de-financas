from django.urls import path, include
from rest_framework.routers import DefaultRouter

from gestao_financas.views import RevenueView, ExpenseView, RevenueCategoryView, ExpenseCategoryView


router = DefaultRouter()
router.register('revenue', RevenueView, basename='revenue')
router.register('revenue-category', RevenueCategoryView, basename='revenue-category')
router.register('expense', ExpenseView, basename='expense')
router.register('expense-category', ExpenseCategoryView, basename='expense-category')

urlpatterns = [
    path('', include(router.urls)),
]
