import pytest, test_demo as g
@pytest.mark.parametrize("n1,n2,r",[(2022,12,5)])
def test_cal(n1,n2,r):
    if g.caln(n1,n2)==r:
        print(g.caln(n1,n2))
        return True
    else:
        return  False

@pytest.mark.parametrize("Value,r",[(50,"chocolate")])
def test_key(Value,r):
    if g.keys(Value)==r:
        return True
    else:
        return False
@pytest.mark.parametrize("l,r",[([43,99,56],[99,56,43])])
def test_desce(l,r):
    if g.desce(l)==r:
        return  True
    else:
        return False
@pytest.mark.parametrize("l,r",[([67,34,21],34)])
def test_min(l,r):
    if g.mymin(l)==r:
        return True
    else:
        return False