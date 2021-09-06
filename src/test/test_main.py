import pytest
import test.data.data as dt

from ..main import main

@pytest.fixture
def resource():
    # load data objects
    data_object = []
    for item in dt.data:
        temp = main(item)
        data_object.append(temp)

    yield data_object
    print("finalizer function")

class TestResource:

    def test_age(self, resource):
        data_object = []
        for item in dt.data:
            temp = main(item)
            data_object.append(temp)

        assert data_object[0]["age"] > 0, AssertionError("Age did not update!")
    
    def test_height(self, resource):
        data_object = []
        for item in dt.data:
            temp = main(item)
            data_object.append(temp)

        assert data_object[0]["height"] > 0, AssertionError("Height did not update!")