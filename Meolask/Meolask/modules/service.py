from MeowkitPy.logging.logger import log
from abc import ABC, abstractmethod
from typing import Union
from Meolask.template import IRegister
from Meolask.modules.container import Container

# (模板) 服務項
class ServiceTemplate(ABC):

    def __init__(self, id: str=None, name: str=None) -> None:
        self.id = id
        self.name = name

# (容器) 服務項
class ServiceContainer(Container):

    # [abs:override]: 添加服務項(注冊) -> dict[服務對象ID, 注冊狀態]
    def add(self, services: list[ServiceTemplate]) -> dict[str, str]:
        out: dict[str, str] = {}
        for svc in services:
            if self._container.get(svc.id, None) is None:
                self._container[svc.id] = svc
                out[svc.id] = 'success'
            else:
                log.LogWarning(f'{svc.id} is already add | registered.')
                out[svc.id] = 'fail'
        return out

    # [abs:override]: 移除服務項(注銷)
    def remove(self, collect: Union[list[str], list[ServiceTemplate]]) -> bool:

        if isinstance(collect, list[str]) == True:
            for _key, val in self._container.items():
                for key in collect:
                    if _key == key:
                        del self._container[_key]
            return True

        elif isinstance(collect, list[ServiceTemplate]) == True:
            for _key, val in self._container.items():
                for svc in collect:
                    if _key == svc.id:
                        del self._container[_key]
            return True

        else: # 不可能有 Flase >> 因爲參數形態被指定了
            return False

    # [abs:override]: 根據 Key組 獲取 items >> 此方法不會注銷 items (字典中依舊存在)
    def get(self, keys: list[str]) -> list[ServiceTemplate]:
        output: list[ServiceTemplate] = []
        for _key, val in self._container.items():
            for key in keys:
                if _key == key:
                    output.append(self._container[_key])
        return output

    # [abs:override]: 根據 Key組 提取 items >> 此方法會使 items 解注冊 (注銷)
    def pop(self, keys: list[str]) -> list[ServiceTemplate]:
        output: list[ServiceTemplate] = []
        for _key, val in self._container.items():
            for key in keys:
                if _key == key:
                    output.append(self._container.pop(_key))
        return output

# 服務注冊器
class ServiceRegister(IRegister):

    def __init__(self, container_ptr: dict) -> None:
        super().__init__() 
        self._container = ServiceContainer(False, container_ptr) # 設定參考對象

    # 注冊服務項 -> dict[服務對象ID, 注冊狀態]
    def register(self, services: list[ServiceTemplate]) -> dict[str, str]:
        return self._container.add(services)
