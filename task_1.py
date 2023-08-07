class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.list_of_list_i = -1
        self.sublist = []
        self.sublist_i = -1
        return self

    def __next__(self):
        self.sublist_i += 1
        if self.sublist_i >= len(self.sublist):
            self.list_of_list_i += 1
            if self.list_of_list_i >= len(self.list_of_list):
                raise StopIteration
            self.sublist = self.list_of_list[self.list_of_list_i]
            self.sublist_i = 0
        return self.sublist[self.sublist_i]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()