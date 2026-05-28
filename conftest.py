import pytest

from main import BooksCollector


@pytest.fixture(autouse=True)
def collector():
    collector = BooksCollector()
    return collector