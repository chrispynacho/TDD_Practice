from linkedList import *
import sure


def test_get_count_of_list_items():
    myList = UnorderedList()
    (myList.size()).should.equal(0)

    myList.add(1)
    (myList.size()).should.equal(1)

    myList.add(1)
    myList.add(1)
    (myList.size()).should.equal(3)


def test_search_list():
    myList = UnorderedList()

    (myList.search("b")).shouldnt.be.ok

    myList.add("b")
    (myList.search("b")).should.be.ok

    myList.add("c")
    myList.add("d")
    (myList.search("d")).should.be.ok
    (myList.search("f")).shouldnt.be.ok

def test_remove_item():
    myList = UnorderedList()

    myList.add("b")
    myList.add("d")
    myList.add("c")

    myList.remove("c")
    (myList.search("c")).shouldnt.be.ok