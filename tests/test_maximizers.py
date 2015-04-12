from pytest import fixture
from collections import Counter

from libextract.pruners import prune_by_child_count
from libextract.maximizers import node_counter_argmax


@fixture
def pairs(etree):
    return prune_by_child_count(etree)


@fixture
def argmax_pairs(pairs):
    return node_counter_argmax(pairs)


def test_node_counter_argmax(argmax_pairs):
    u = {elem.tag: counter for elem, counter in argmax_pairs}
    u.pop('head')
    assert u['article'] == ('div', 9)
    for key in u:
        assert key in {'article', 'body', 'html'}