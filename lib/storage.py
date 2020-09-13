from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class AbstractStorage(ABC):
    """
    Abstract storage class.
    You can use it with database or with standart python collections and save interface
    """

    @abstractmethod
    async def add(self, element: Any):
        """
        Method used to add/insert element to storage
        :param element: element to insert
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    async def get(self) -> Any:
        """
        Method used to get all elements that were inserted to storage
        :return:
        """
        raise NotImplementedError


@dataclass
class ListStorage(AbstractStorage):
    storage: List = field(default_factory=list)

    async def add(self, element):
        self.storage.append(element)

    async def get(self) -> List:
        return self.storage
