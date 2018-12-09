import pytest
from dbi import Dbi
dbi = Dbi(3,True)
dpm = dbi.print_message

class TestDbi():
    def test_verblvl(self):
        with pytest.raises(TypeError):
            dpm("yes","sir")
        with pytest.raises(TypeError):
            dpm(3.4,"yes","sir")
        with pytest.raises(TypeError):
            dpm(3,"actually","this should work")