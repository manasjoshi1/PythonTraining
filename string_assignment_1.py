import collections


class Item:
    ch = ''
    freq = 0

    def __init__(self, ch, freq):
        self.ch, self.freq = ch, freq

    def __str__(self):
        return f'{self.ch} : {self.freq}'

    def __gt__(self, other):
        return self.freq > other.freq

    def __lt__(self, other):
        return self.freq < other.freq


def heapify(items: list, size: int = None, node_index: int = None):
    if size is None:
        size = len(items)
    if node_index is None:
        node_index = len(items[:size]) // 2 + 1
    if node_index > 0:
        max_index = node_index
        for child in [node_index * 2 + 1, node_index * 2 + 2]:
            if child >= len(items):
                continue
            if items[max_index] >= items[child]:
                max_index = child
        if node_index != max_index:
            items[node_index], items[max_index] = items[max_index], items[node_index]
        return heapify(items, size, node_index - 1)


def rearrange(text: str):

    res = [''] * len(text)
    items = []
    for ch, freq in collections.Counter(text).items():
        items.append(Item(ch, freq))
    heapify(items)

    i = 0
    while items:
        if items[0] == items[-1] and items[0].freq > 1:
            return 'Not Possible'
        items[0], items[-1] = items[-1], items[0]

        res[i] = items[-1].ch
        items[-1].freq -= 1
        i += 1
        if items[-1].freq == 0:
            items.pop()
            heapify(items)
        else:
            heapify(items, len(items) - 1)

    return ''.join(res)


assert rearrange('aaabc') in ['abaca', 'acaba']
assert rearrange('aaabb') == 'ababa'
assert rearrange('aa') == 'Not Possible'
assert rearrange('aaaabc') == 'Not Possible'