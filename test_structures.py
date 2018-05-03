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

class TestStack:

    @pytest.fixture(scope='function')
    def test_stack(self):
        x = data_structures.Stack()
        x.push('lorem')
        x.push('dim')
        x.push('sum')
        x.push('Cha')
        x.push('siu')
        x.push('bao')
        return x

    def test_peek_return_type(self, test_stack):
        peeked = test_stack.peek()
        assert type(peeked) == data_structures.Node

    def test_peek_value(self, test_stack):
        peeked = test_stack.peek()
        assert peeked.data == 'bao'
        peeked = test_stack.peek()
        assert peeked.data == 'bao'
        peeked = test_stack.peek()
        assert peeked.data == 'bao'

    def test_peek_size(self, test_stack):
        test_stack.peek()
        assert test_stack.size == 6
        test_stack.peek()
        assert test_stack.size == 6
        test_stack.peek()
        assert test_stack.size == 6

    def test_pop_return_type(self, test_stack):
        popped = test_stack.pop()
        assert type(popped) == data_structures.Node

    def test_pop_value(self, test_stack):
        popped = test_stack.pop()
        assert popped.data == 'bao'
        popped = test_stack.pop()
        assert popped.data == 'siu'
        popped = test_stack.pop()
        assert popped.data == 'Cha'

    def test_pop_size(self, test_stack):
        test_stack.pop()
        assert test_stack.size == 5
        test_stack.pop()
        assert test_stack.size == 4
        test_stack.pop()
        assert test_stack.size == 3

    def test_pop_empty(self):
        test_stack = data_structures.Stack()
        try:
            popped = test_stack.pop()
        except:
            pass
        else:
            assert False, "Expected an exception; instead got a Node with value '{}'.".format(popped.data)

    def test_push_return_type(self, test_stack):
        pushed = test_stack.push('steamed')
        assert pushed == None

    def test_push_size(self, test_stack):
        test_stack.push('steamed')
        assert test_stack.size == 7
