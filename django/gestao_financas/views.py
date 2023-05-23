from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework import status

from gestao_financas.serializers import RevenueSerializer, RevenueCategorySerializer, ExpenseSerializer, ExpenseCategorySerializer
from gestao_financas.models import Revenue, RevenueCategory, Expense, ExpenseCategory

from common.response_helper import responseHelper


class RevenueView(ViewSet):
    """Revenue view to make the CRUD operations"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, pk: str = None):
        if not pk:
            return Revenue.objects.get(user_id=self.request.user.id, pk=pk)
        return Revenue.objects.filter(user_id=self.request.user.id)
    
    def list(self, request: Request):
        revenues = self.get_queryset()
        serializer = RevenueSerializer(revenues)
        return responseHelper.json_success_response(serializer.data,
                                                    "Receitas retornadas com sucesso!",
                                                    len(serializer.data))

    def retrieve(self, request: Request, pk: str = None):
        revenue = self.get_queryset(pk=pk)
        serializer = RevenueSerializer(revenue, many=True)
        if not serializer.data:
            return responseHelper.json_not_found_response(serializer.data)
        else:
            return responseHelper.json_success_response(serializer.data,
                                                        "Receita retornada com sucesso!",
                                                        1)

    def update(self, request: Request, pk: str = None):
        revenue = self.get_queryset(pk=pk)
        serializer = RevenueSerializer(revenue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responseHelper.json_success_response(serializer.data,
                                                        "Receita atualizada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao atualizar a receita!",
                                                      serializer.errors)

    def create(self, request: Request):
        serializer = RevenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responseHelper.json_success_response(serializer.data,
                                                        "Receita criada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao criar nova receita!",
                                                      serializer.errors)
        
    def destroy(self, request: Request, pk: str = None):
        if not pk:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Revenue ID é necessário nesta operação!",
                                                      "Revenue ID é requerido")
        
        revenue = self.get_queryset(pk=pk)
        if revenue:
            serializer = RevenueSerializer(revenue)
            revenue.delete()
            return responseHelper.json_success_response(serializer.data,
                                                        "Receita deletada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Receita não existe!",
                                                      "Revenue não existe ou ID inválido")


class RevenueCategoryView(ViewSet):
    """Revenue Category view to make CRUD operations"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, pk: str = None):
        if not pk:
            return RevenueCategory.objects.filter(user_id=self.request.user.id) 
        return RevenueCategory.objects.get(user_id=self.request.user.id, pk=pk)
    
    def list(self, request: Request):
        revenue_categorys = self.get_queryset()
        serializer = RevenueCategorySerializer(revenue_categorys)
        return responseHelper.json_success_response(serializer.data,
                                                    "Receitas retornadas com sucesso!",
                                                    len(serializer.data))
    
    def retrieve(self, request: Request, pk: str = None):
        revenue = self.get_queryset(pk=pk)
        serializer = RevenueCategorySerializer(revenue, many=True)
        if not serializer.data:
            return responseHelper.json_not_found_response(serializer.data)
        else:
            return responseHelper.json_success_response(serializer.data,
                                                        "Receita retornada com sucesso!",
                                                        1)
        
    def update(self, request: Request, pk: str = None):
        revenue = self.get_queryset(pk=pk)
        serializer = RevenueCategorySerializer(revenue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responseHelper.json_success_response(serializer.data,
                                                        "Receita atualizada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao atualizar a receita!",
                                                      serializer.errors)

    def create(self, request: Request):
        serializer = RevenueCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responseHelper.json_success_response(serializer.data,
                                                        "Receita criada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao criar nova receita!",
                                                      serializer.errors)
        
    def destroy(self, request: Request, pk: str = None):
        if not pk:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Revenue ID é necessário nesta operação!",
                                                      "Revenue ID é requerido")
        
        revenue = self.get_queryset(pk=pk)
        if revenue:
            serializer = RevenueCategorySerializer(revenue)
            revenue.delete()
            return responseHelper.json_success_response(serializer.data,
                                                        "Receita deletada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Receita não existe!",
                                                      "Revenue não existe ou ID inválido")
        
    
                        

class ExpenseView(ViewSet):
    """Expense view to make CRUD operations"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, pk: str = None):
        if not pk:
            return Expense.objects.filter(user_id=self.request.user.id) 
        return Expense.objects.get(user_id=self.request.user.id, pk=pk)
    
    def list(self, request: Request):
        revenue_categorys = self.get_queryset()
        serializer = ExpenseSerializer(revenue_categorys)
        return responseHelper.json_success_response(serializer.data,
                                                    "Despesas retornadas com sucesso!",
                                                    len(serializer.data))
    
    def retrieve(self, request: Request, pk: str = None):
        revenue = self.get_queryset(pk=pk)
        serializer = ExpenseSerializer(revenue, many=True)
        if not serializer.data:
            return responseHelper.json_not_found_response(serializer.data)
        else:
            return responseHelper.json_success_response(serializer.data,
                                                        "Despesas retornada com sucesso!",
                                                        1)
        
    def update(self, request: Request, pk: str = None):
        revenue = self.get_queryset(pk=pk)
        serializer = ExpenseSerializer(revenue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responseHelper.json_success_response(serializer.data,
                                                        "Despesas atualizada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao atualizar a despesa!",
                                                      serializer.errors)

    def create(self, request: Request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responseHelper.json_success_response(serializer.data,
                                                        "Despesa criada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao criar nova despesa!",
                                                      serializer.errors)
        
    def destroy(self, request: Request, pk: str = None):
        if not pk:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Expense ID é necessário nesta operação!",
                                                      "Expense ID é requerido")
        
        revenue = self.get_queryset(pk=pk)
        if revenue:
            serializer = ExpenseSerializer(revenue)
            revenue.delete()
            return responseHelper.json_success_response(serializer.data,
                                                        "Despesa deletada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Despesa não existe!",
                                                      "Despesa não existe ou ID inválido")


class ExpenseCategoryView(ViewSet):
    """Expense Category view to make CRUD operations"""
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, pk: str = None):
        if not pk:
            return ExpenseCategory.objects.filter(user_id=self.request.user.id) 
        return ExpenseCategory.objects.get(user_id=self.request.user.id, pk=pk)
    
    def list(self, request: Request):
        revenue_categorys = self.get_queryset()
        serializer = ExpenseCategorySerializer(revenue_categorys)
        return responseHelper.json_success_response(serializer.data,
                                                    "Categoria de despesas retornadas com sucesso!",
                                                    len(serializer.data))
    
    def retrieve(self, request: Request, pk: str = None):
        revenue = self.get_queryset(pk=pk)
        serializer = ExpenseCategorySerializer(revenue, many=True)
        if not serializer.data:
            return responseHelper.json_not_found_response(serializer.data)
        else:
            return responseHelper.json_success_response(serializer.data,
                                                        "Categoria de despesa retornada com sucesso!",
                                                        1)
        
    def update(self, request: Request, pk: str = None):
        revenue = self.get_queryset(pk=pk)
        serializer = ExpenseCategorySerializer(revenue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responseHelper.json_success_response(serializer.data,
                                                        "Categoria de despesa atualizada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao atualizar a categoria de despesa!",
                                                      serializer.errors)

    def create(self, request: Request):
        serializer = ExpenseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return responseHelper.json_success_response(serializer.data,
                                                        "Categoria de despesa criada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Erro ao criar nova categoria de despesa!",
                                                      serializer.errors)
        
    def destroy(self, request: Request, pk: str = None):
        if not pk:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Expense Category ID é necessário nesta operação!",
                                                      "Expense Catgory ID é requerido")
        
        revenue = self.get_queryset(pk=pk)
        if revenue:
            serializer = ExpenseCategorySerializer(revenue)
            revenue.delete()
            return responseHelper.json_success_response(serializer.data,
                                                        "Categoria de despesa deletada com sucesso!",
                                                        1)
        else:
            return responseHelper.json_error_response(status.HTTP_400_BAD_REQUEST,
                                                      "Categoria de despesa não existe!",
                                                      "Categoria de despesa não existe ou ID inválido")
