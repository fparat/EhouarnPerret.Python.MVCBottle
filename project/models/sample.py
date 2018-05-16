from project.helpers.argcheck import check_value_type


# id is builtin... whining noooo :-)
class Sample(object):
    def __init__(self, no: int, x: float, y: float):
        if not check_value_type(no, int):
            raise ValueError(no)
        if not check_value_type(x, float):
            raise ValueError(x)
        if not check_value_type(y, float):
            raise ValueError(y)
        self._no = no
        self._x = x
        self._y = y

    @property
    def no(self) -> int:
        return self._no

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y
