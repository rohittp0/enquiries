import pytest

from enquiries import choices


@pytest.fixture
def clist():
    cl = choices.ChoiceList(['abcd', 'efgh', 'ijkl'])
    return cl


def test_list_length(clist):
    assert len(clist) == 3


def test_get_item(clist):
    assert clist[1] == "efgh"


def test_contains(clist):
    assert 'efgh' in clist
    assert 'refwe' not in clist


def test_set_item(clist):
    assert clist[1] == 'efgh'
    clist[1] = 'mnop'
    assert clist[1] == 'mnop'


def test_del_item(clist):
    del clist[1]
    assert clist[1] != 'abcd'
    assert len(clist) == 2


def test_iterate(clist):
    choices_list = iter(clist)
    assert next(choices_list) == 'abcd'
    assert next(choices_list) == 'efgh'
    assert next(choices_list) == 'ijkl'
    with pytest.raises(StopIteration):
        next(choices_list)


def test_reverse(clist):
    choices_list = reversed(clist)
    assert next(choices_list) == 'ijkl'


def test_no_choices():
    with pytest.raises(ValueError):
        choices.ChoiceList([])
