from abc import ABC, abstractmethod
from api_client.api.client import APIClient, ConcreteAPIClientFactory

class APIBuilder(ABC):
    @abstractmethod
    def build_client(self) -> APIClient:
        pass

class ConcreteAPIBuilder(APIBuilder):
    def build_client(self) -> APIClient:
        factory = ConcreteAPIClientFactory()
        return factory.create_client()
