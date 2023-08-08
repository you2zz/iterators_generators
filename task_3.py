class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.stack = [[0, self.list_of_list]]
        return self

    def __next__(self):
        while self.stack:
            count, self.list_of_list = self.stack[-1]
            if count < len(self.list_of_list):
                self.stack[-1][0] += 1
                if type(self.list_of_list[count]) is not list:
                    return self.list_of_list[count]
                self.stack.append([0, self.list_of_list[count]])
            else:
                self.stack.pop()
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()