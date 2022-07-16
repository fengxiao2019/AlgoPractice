import pytest
from data_structure.heap.heap import MinHeap


TEST_DATA = [{'input': [], 'expected': []}]


@pytest.fixture(scope='module')
def heap():
    yield MinHeap()


@pytest.fixture(params=[])
def insert_sample(request):
    return request.params


@pytest.mark.parametrize("test_input,expected", [(5, [None, 5]), (4, [None, 4, 5]), (3, [None, 3, 5, 4])])
def test_insert(heap, test_input, expected):
    heap.insert(test_input)
    assert heap.check_valid()
    assert heap.values == expected


def test_remove():
    pass