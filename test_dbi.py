import pytest
from dbi import Dbi
dbi = Dbi(3,True)
dpm = dbi.print_message

class TestDbi():
    def test_verb_type(self):
        with pytest.raises(TypeError):
            dpm("yes","sir")
        with pytest.raises(TypeError):
            dpm(3.4,"yes","sir")
    def test_verb_limits(self):
        with pytest.raises(ValueError):
            dpm(-1,"hello","chap")
        with pytest.raises(ValueError):
            dpm(0,"mr.","zero")
    def test_arg_type(self):
        with pytest.raises(TypeError):
            dpm(3,"I'm",45)
        with pytest.raises(TypeError):
            dpm(3,2,"turtle doves and a partridge in a pair tree")
            