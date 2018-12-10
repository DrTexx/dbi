from source import demo

class TestDemo():
    def test_run_demo(self):
        assert demo.run_demo() == None