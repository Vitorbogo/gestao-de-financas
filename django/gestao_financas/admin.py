from django.contrib import admin
from gestao_financas import models

admin.site.register(models.Expense)
admin.site.register(models.ExpenseCategory)
admin.site.register(models.Revenue)
admin.site.register(models.RevenueCategory)