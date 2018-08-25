import pytest


# 测试题目
class TestAAA:
    @pytest.mark.parametrize("a,b",[(3,6)])
    def test_aaa(self,a,b):
        print(a)
        print(b)
        print("aa")



