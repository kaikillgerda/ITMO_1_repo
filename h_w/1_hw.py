def test_well():
    assert ('home', 'work') == ('home', 'work')


def test_not():
    assert 'QA' != 'QC'


def test_bad():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)