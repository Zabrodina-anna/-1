from abc import ABC, abstractmethod


class Furniture(ABC):
    """Абстрактный класс для мебели"""

    def __init__(self, material: str, height: float, width: float) -> None:
        if height <= 0:
            raise ValueError(f"Высота должна быть положительным числом, получено: {height}")
        if width <= 0:
            raise ValueError(f"Ширина должна быть положительным числом, получено: {width}")
        self.material = material
        self.height = height
        self.width = width

    @abstractmethod
    def assemble(self) -> None:
        """Собрать мебель"""
        ...

    @abstractmethod
    def disassemble(self) -> None:
        """Разобрать мебель"""
        ...


class Table(Furniture):
    """Класс Стол, наследующий от Furniture"""

    def __init__(self, material: str, height: float, width: float, legs_number: int) -> None:
        super().__init__(material, height, width)
        if legs_number <= 0:
            raise ValueError(f"Количество ножек должно быть положительным числом, получено: {legs_number}")
        self.legs_number = legs_number

    def assemble(self) -> None:
        """Собрать стол"""
        ...

    def disassemble(self) -> None:
        """Разобрать стол"""
        ...

    def extend(self, length: float) -> None:
        """Увеличить длину стола

        :param length: Новая длина стола
        :return: None
        :raises ValueError: если длина не положительная

        >>> table = Table("дерево", 1.0, 2.0, 4)
        >>> table.extend(3.0)
        >>> table.width
        3.0
        """
        if length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        self.width = length  # Увеличиваем ширину стола до нового значения


class Tree(ABC):
    """Абстрактный класс для дерева"""

    def __init__(self, species: str, age: int) -> None:
        if age < 0:
            raise ValueError(f"Возраст не может быть отрицательным, получено: {age}")
        self.species = species
        self.age = age

    @abstractmethod
    def grow(self) -> None:
        """Дерево растет"""
        ...

    @abstractmethod
    def shed_leaves(self) -> None:
        """Сбросить листья"""
        ...


class Oak(Tree):
    """Класс Дуб, наследующий от Tree"""

    def grow(self) -> None:
        """Дуб растет"""
        ...

    def shed_leaves(self) -> None:
        """Дуб сбрасывает листья"""
        ...

    def age_tree(self, years: int) -> None:
        """Увеличить возраст дерева

        :param years: Количество лет для увеличения возраста
        :return: None
        :raises ValueError: Если количество лет не положительное

        >>> oak = Oak("Дуб", 10)
        >>> oak.age_tree(5)
        ...
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным числом")
        self.age += years
        ...


class Stack(ABC):
    """Абстрактный класс для стека"""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError(f"Вместимость должна быть положительным числом, получено: {capacity}")
        self.capacity = capacity
        self.items = []

    @abstractmethod
    def push(self, item) -> None:
        """Добавить элемент в стек"""
        ...

    @abstractmethod
    def pop(self):
        """Извлечь элемент из стека"""
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        """Проверить, пуст ли стек"""
        ...


class ArrayStack(Stack):
    """Класс Стек на массиве, наследующий от Stack"""

    def push(self, item) -> None:
        """Добавить элемент в стек

        :param item: Элемент для добавления
        :return: None
        :raises OverflowError: если стек переполнен

        >>> stack = ArrayStack(3)
        >>> stack.push(1)
        ...
        """
        if len(self.items) >= self.capacity:
            raise OverflowError("Стек переполнен")
        self.items.append(item)

    def pop(self):
        """Извлечь элемент из стека

        :return: Элемент, извлеченный из стека
        :raises IndexError: если стек пуст

        >>> stack = ArrayStack(3)
        >>> stack.push(1)
        >>> stack.pop()
        1
        """
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def is_empty(self) -> bool:
        """Проверить, пуст ли стек

        :return: True, если стек пуст, иначе False

        >>> stack = ArrayStack(3)
        >>> stack.is_empty()
        True
        """
        return len(self.items) == 0
