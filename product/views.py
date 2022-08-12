from datetime import datetime
from datetime import timedelta


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Product, UserProduct
from .serializers import ProductSerializers
from user.models import User


class ProductView(APIView):
    """
    프로덕트를 가져오고 생성하는 view
    """
    def get(self, request):
        products = Product.objects.all().exclude(is_active=False)
        return Response(ProductSerializers(products, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            product_id =  int(self.request.query_params.get("product_id"))
            cur_user = request.user
            cur_product = Product.objects.filter(id=product_id).get()
            user_product = UserProduct.objects.create(
                start_date = datetime.utcnow() + timedelta(days=1),
                end_date = datetime.utcnow() + timedelta(days=366),
                product = cur_product
            )
            cur_user.subscribe = user_product
            cur_user.save()
            return Response(
                {"detail": "구입이 완료 되었습니다."}, status= status.HTTP_200_OK
            )
        except TypeError:
            return Response(
                {"detail" : "입력값이 잘못되었습니다. 다시 시도해주세요."}
            )