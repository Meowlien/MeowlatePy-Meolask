from abc import ABC, abstractmethod
#from ast import Global
from enum import Enum, auto

# 容器界面
class IContainer(ABC):

    @abstractmethod # 添加元素
    def add(self, items: tuple) -> bool: pass

    @abstractmethod # 移除元素
    def remove(self, keys: list) -> bool: pass

    @abstractmethod # 根據 Key組 獲取 items >> 此方法不會注銷 items (字典中依舊存在)
    def get(self, keys: list) -> list: pass

    @abstractmethod # 根據 Key組 提取 items >> 此方法會使 items 解注冊 (注銷)
    def pop(self, keys: list) -> list: pass

# [ABC]: 容器
class Container(IContainer):

    class Type(Enum):
        Unknown = 0
        Object = auto()
        Reference = auto()

    '''
    param: <build_container: bool>: 是否創建容器
    '''
    def __init__(self, ref_container: dict=None) -> None:
        super().__init__()

        if ref_container == None:
            self._container: dict = {}
            self.type = Container.Type.Object
        else:
            self._container = ref_container          # 指向目標容器
            self.type = Container.Type.Reference


