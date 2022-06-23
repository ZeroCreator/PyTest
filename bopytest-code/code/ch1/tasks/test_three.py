"""Test the Task data type. Проверим тип данных Task."""


from collections import namedtuple

import pytest

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None) # Вы можете использовать __new __.__ defaults__ для создания объектов Task без указания всех полей.

# ест test_defaults() предназначен для демонстрации и проверки того, как работают умолчания.

def test_defaults():
    """Using no parameters should invoke defaults.
    Без использования параметров, следует ссылаться
    на значения по умолчанию. """
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

# Тест test_member_access() должен продемонстрировать, как обращаться к членам по имени nd не по индексу,
# что является одной из основных причин использования namedtuples.
@pytest.mark.run_these_please
def test_member_access():
    """Check .field functionality of namedtuple.
    Проверка свойства .field (поля) namedtuple. """
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)
