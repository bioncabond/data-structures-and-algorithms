import pytest
from code_challenges.graph_business_trip.business_trip import Graph


def test_one_way_trip():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    graph.add_edge(a, b, 105)
    actual = graph.business_trip([a,b])
    expected = (True , "$105")
    assert actual == expected

def test_connecting_flight():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    graph.add_edge(a, b, 105)
    graph.add_edge(b, c, 250)
    actual = graph.business_trip([a,b,c])
    expected = (True , "$355")
    assert actual == expected

def test_no_flight():
    graph = Graph()
    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    graph.add_edge(b, c, 250)
    actual = graph.business_trip([a,b])
    expected = (False , "$0")
    assert actual == expected
