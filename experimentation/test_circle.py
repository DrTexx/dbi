import pytest
from circles import circle_area
from math import pi

class TestCircleArea():
    def test_area(self):
        # test areas when radius >= 0
        assert circle_area(1) == pi
        assert circle_area(0) == 0
        assert circle_area(2.1) == pi*2.1**2
    def test_values(self):
        with pytest.raises(ValueError):
            circle_area(-2)
    def test_types(self):
        with pytest.raises(TypeError):
            circle_area(3+5j)
        with pytest.raises(TypeError):
            circle_area(True)
        with pytest.raises(TypeError):
            circle_area("radius")
            