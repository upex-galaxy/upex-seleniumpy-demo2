import pytest 
from tests.testbase import *

@pytest.mark.skip(reason="just created to test")
class TestDriverManager():
    
    def test_ex(self, setup:Test):
        web, get = setup

        get.page("https://demoqa.com/text-box")
        
if __name__ == '__main__':
    pytest.main()