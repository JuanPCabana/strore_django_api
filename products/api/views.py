
from rest_framework import viewsets, status, permissions

from products.api.serializers import ProductSerializer, ShortProductSerializer
from products.adapters.repository.django_products import DjangoProductRepository
from products.core.services import ProductService
from products.utils import response_error_handler, body_validator, handle_response


class ProductViewSet(viewsets.ViewSet):
    repo = DjangoProductRepository()
    service = ProductService(repo)
    queryset = service.list_products()
    permission_classes = [permissions.AllowAny]
    productSerializer = ProductSerializer
    shortProductSerializer = ShortProductSerializer

    #metodo get
    def list(self, request):
        """"Lista los productos"""
        
        products = self.service.list_products()
        serializer = self.shortProductSerializer(products, many=True)
        
        return handle_response(serializer.data)

    #metodo get de un solo producto
    def retrieve(self, request, pk=None):
        """"Retorna un producto"""
        
        product = self.service.get_product(pk)
        if not product:
            return response_error_handler("Producto no encontrado", status.HTTP_404_NOT_FOUND)

        serializer = self.productSerializer(product)
        
        return handle_response(serializer.data)

    #metodo post
    def create(self, request):
        """"Crea un producto"""
        
        product_data: dict = request.data

        valid = body_validator(data=product_data, required_fields=[
                               'reference', 'name', 'description', 'base_price', 'tax_rate'])
        if not valid:
            return response_error_handler("Faltan campos requeridos", status.HTTP_400_BAD_REQUEST)

        try:
            product = self.service.create_product(
                reference=product_data['reference'],
                name=product_data['name'],
                description=product_data['description'],
                base_price=product_data['base_price'],
                tax_rate=product_data['tax_rate']
            )
        except Exception as e:
            return response_error_handler("Bad Request", status.HTTP_400_BAD_REQUEST)

        serializer = self.productSerializer(product)

        return handle_response(serializer.data, status_code=status.HTTP_201_CREATED)

    #metodo put
    def update(self, request, pk=None):
        """actualiza un producto"""
        
        product_data: dict = request.data

        valid = body_validator(data=product_data)
        if not valid:
            return response_error_handler("Faltan campos requeridos", status.HTTP_400_BAD_REQUEST)

        try:
            product = self.service.update_product(
                pk,
                reference=product_data.get('reference'),
                name=product_data.get('name'),
                description=product_data.get('description'),
                base_price=product_data.get('base_price'),
                tax_rate=product_data.get('tax_rate')
            )
        except Exception as e:
            return response_error_handler("Bad Request", status.HTTP_400_BAD_REQUEST)

        if not product:
            return response_error_handler("Producto no encontrado", status.HTTP_404_NOT_FOUND)

        serializer = self.productSerializer(product)

        return handle_response(serializer.data, status_code=status.HTTP_200_OK)

    #metodo patch
    def partial_update(self, request, *args, **kwargs):
        """actualiza parcialmente un producto"""
        
        return self.update(request, *args, **kwargs)
