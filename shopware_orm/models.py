from datetime import datetime

from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass


class ApiModelMeta(ModelMetaclass):
    def __new__(cls, name, bases, dct):
        new_class: type = super().__new__(cls, name, bases, dct)
        new_class.api = ShopwareAPIManager(new_class)
        return new_class


class ShopwareApiQuery:

    def __init__(self, model: type) -> None:
        self._model = model
        self._query = {}

    def all(self) -> "ShopwareApiQuery":
        """
        Return a new ShopwareApiQuery that is a copy of the current one.
        """
        return self._clone()

    def filter(self, *args, **kwargs) -> "ShopwareApiQuery":
        """
        Return a new ShopwareApiQuery that is a copy the current one extended with additional
        filters.
        """
        query = self._clone()

        for key, value in kwargs.items():
            query._query[key] = value

        return query

    def get(self):
        pass

    def first(self):
        pass

    def latest(self):
        pass

    def order_by(self):
        pass

    def _clone(self):
        """
        Return a copy of the current ShopwareApiQuery.
        """
        clone = self.__class__(
            model=self._model,
        )
        clone._query = self._query
        return clone

    def __str__(self):
        return f"ShopwareApiQuery[{self._model.__name__}] {self._query}"


class ShopwareAPIManager:

    def __init__(self, model: type, api_query: type = ShopwareApiQuery) -> None:
        self._model = model
        self._api_query = api_query

    def create(self, **kwargs) -> "ShopwareModel":
        instance = self._model(**kwargs)
        return instance

    def _create_query(self):
        return self._api_query(self._model)

    def all(self):
        return self._create_query()

    def filter(self, *args, **kwargs):
        return self._create_query().filter(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self._create_query().get(*args, **kwargs)


class ShopwareModel(BaseModel, metaclass=ApiModelMeta):
    pass


class TestShopwareModel(ShopwareModel):
    id: int
    name: str
    active: bool
    created_at: datetime = datetime.now()





