from typing import overload


class Base(object):
    @overload
    def __init__(self) -> None: ...

    @overload
    def test(self) -> None: ...

    @overload
    def set_work(self, status: bool) -> None: ...

    @overload
    def is_work(self) -> bool: ...


class A(Base):

    def __init__(self) -> None:
        self.__name__ = 'A'
        self.__is_work__ = False

    def test(self) -> None:
        print(f'{self.__name__} {id(self)}')

    def set_work(self, status: bool) -> None:
        self.__is_work__ = status

    def is_work(self) -> bool:
        return self.__is_work__


class B(Base):

    def __init__(self) -> None:
        self.__name__ = 'B'
        self.__is_work__ = False

    def test(self) -> None:
        print(f'{self.__name__} {id(self)}')

    def set_work(self, status: bool) -> None:
        self.__is_work__ = status

    def is_work(self) -> bool:
        return self.__is_work__


class mgr(object):

    def __init__(self):
        self.__Base_obj__: dict[str, list[Base]] = {}
        self.__Base_cls__: dict = {}

    # 注册管理任务线类， cls 是一个类的实现
    def register_class(self, cls) -> bool:

        if self.__Base_cls__.get(cls.__name__) is None:
            self.__Base_cls__[cls.__name__] = cls

        return False

    def get_by_name(self, name: str) -> Base:

        objlists: list[Base] = self.__Base_obj__.get(name)

        if objlists is not None:
            for obj in objlists:
                if obj is not None and obj.is_work() is False:
                    return obj
                else:
                    continue

        obj = self.__Base_cls__[name]()

        if objlists is None:
            self.__Base_obj__[name] = [obj]
        else:
            self.__Base_obj__[name].append(obj)

        return obj


if __name__ == '__main__':
    obj_mgr = mgr()
    obj_mgr.register_class(A)
    obj_mgr.register_class(B)

    obj1: Base = obj_mgr.get_by_name(A.__name__)

    obj1.test()
    obj1.set_work(True)

    obj2: Base = obj_mgr.get_by_name(A.__name__)
    obj3: Base = obj_mgr.get_by_name(B.__name__)

    obj2.test()
    obj3.test()

    obj4: Base = obj_mgr.get_by_name(A.__name__)
    obj4.test()
