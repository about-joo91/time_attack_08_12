from calendar import c
from http import client
import json
from rest_framework.test import APITestCase, APIClient

from ..user.models import User
# Create your tests here.
class TestProductView(APITestCase):
    """
    ProductView를 검증하는 함수
    """

    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create(
            email= "test@gmail.com"
        )
    
    def test_product_post(self):
        client = APIClient()
        
        user = User.objects.get(email = "test@gmail.com")
        client.force_authenticate(user = user)
        url = "/product/"
        response = client.post(
            url,
            json.dumps({}),
            content_type="application/json"
        )
        result = response.json()
        
