from abc import ABC, abstractmethod
from ast import Global
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

    def __init__(self, build_container: bool=True, container_ptr: dict=None) -> None:
        super().__init__()
        self._container: dict = None
        self.type: Container.Type = Container.Type.Unknown

        # 創建容器
        if build_container == True:
            self._container: dict = {}
            self.type = Container.Type.Object
        # 不創建容器則
        else:
            # 必須提供容器指標
            if container_ptr == None:
                # >>> 請在第一次實例化前，設定容器引用對象(即：請先先呼叫 initialize(obj: dict) 進行初始化)
                raise Exception("\n\n>>>> Pls setup container's reference before first instance!\n")
            else:
                # 指向目標容器
                self._container = container_ptr
                self.type = Container.Type.Reference