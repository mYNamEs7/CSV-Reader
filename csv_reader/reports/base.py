from abc import ABC, abstractmethod
from typing import Any


class Report(ABC):
    name: str

    @abstractmethod
    def generate(self, records: list[Any]) -> list[list[Any]]:
        """Возвращает строки для tabulate"""
