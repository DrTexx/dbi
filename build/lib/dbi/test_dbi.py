import pytest
from dbi.dbi import Dbi,DbiErrors
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
        assert dpm(dbi.verb + 1,"outside limit","show nothing!") == DbiErrors.VerbTooLow
    def test_honour_debug_flag(self):
        dbi.debug = False
        assert dpm(3,"should get nothing","debugging is disabled") == DbiErrors.DebugOff
        dbi.debug = True
    def test_arg_type(self):
        with pytest.raises(TypeError):
            dpm(3,"I'm",45)
        with pytest.raises(TypeError):
            dpm(3,2,"turtle doves and a partridge in a pair tree")
    def test_submessages(self):
        assert "parent message | sub-message" in dpm(3,"parent message","sub-message",return_string=True)
        