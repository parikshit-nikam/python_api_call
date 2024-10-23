import requests
from api_client.models.user import User
from abc import ABC, abstractmethod
from typing import List

class APIClient(ABC):
    BASE_URL = "https://api.restful-api.dev"

    @abstractmethod
    def get_users(self) -> List[User]:
        pass

class ConcreteAPIClient(APIClient):
    def get_users(self) -> List[User]:
        response = requests.get(f"{self.BASE_URL}/objects")
        response.raise_for_status()
        users_data = response.json()
        return [User(**user) for user in users_data]

# Factory Method
class APIClientFactory(ABC):
    @abstractmethod
    def create_client(self) -> APIClient:
        pass

class ConcreteAPIClientFactory(APIClientFactory):
    def create_client(self) -> APIClient:
        return ConcreteAPIClient()
