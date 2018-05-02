import pytest

import data_structures

class TestLinkedList:

    @pytest.fixture(scope='function')
    def test_list(self):
        x = data_structures.LinkedList()
        x.insert('lorem')
        x.insert('dim')
        x.insert('sum')
        x.insert('Cha')
        x.insert('siu')
        x.insert('bao')
        return x

    def test_size(self, test_list):
        assert test_list.size == 6
        test_list.insert('bacon')
        assert test_list.size == 7

    def test_search_success(self, test_list):
        query = 'Cha'
        result_node = test_list.search(query)
        assert type(result_node) == data_structures.Node
        assert result_node.data == query

    def test_search_fail(self, test_list):
        try:
            test_list.search('sandwich')
        except:
            pass
        else:
            assert False, 'Expected an Exception, but one was not raised.'

    def test_delete_head(self, test_list):
        query = 'bao'
        test_list.delete(query)
        assert test_list.size == 5
        try:
            test_list.search(query)
        except:
            pass
        else:
            assert False, 'Node with data={} was not deleted.'.format(query)

    def test_delete_other(self, test_list):
        query = 'sum'
        test_list.delete(query)
        assert test_list.size == 5
        try:
            test_list.search(query)
        except:
            pass
        else:
            assert False, 'Node with data={} was not deleted.'.format(query)

    def test_delete_fail(self, test_list):
        try:
            test_list.delete('pizza')
        except:
            pass
        else:
            assert False, 'Expected an Exception, but one was not raised.'
