from rest_framework.serializers import ModelSerializer

from gestao_financas.models import Revenue, RevenueCategory, Expense, ExpenseCategory


class RevenueSerializer(ModelSerializer):
    """Serializer to the Revenue view"""

    class Meta:
        model = Revenue
        fields = '__all__'


class RevenueCategorySerializer(ModelSerializer):
    """Serializer Class for the Revenue Catgoerys"""

    class Meta:
        model = RevenueCategory
        fields = '__all__'


class ExpenseSerializer(ModelSerializer):
    """Serializer to the Revenue view"""

    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseCategorySerializer(ModelSerializer):
    """Serializer Class for the Revenue Catgoerys"""

    class Meta:
        model = ExpenseCategory
        fields = '__all__'
