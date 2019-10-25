# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs['ignore_case'] if 'ignore_case' in kwargs else False
        self.unique_items = []
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

    def __next__(self):
        while True:
            item = self.items.__next__()
            if not self.ignore_case and type(item) is str:
                tmp_item = item.lower()
            else:
                tmp_item = item
            if tmp_item not in self.unique_items:
                self.unique_items.append(tmp_item)
                return item

    def __iter__(self):
        return self
