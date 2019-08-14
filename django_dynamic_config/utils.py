import json
from types import MappingProxyType, SimpleNamespace
from .models import DynamicConfig, VALUE_TYPE_LIST


class Config:
    @staticmethod
    def _string_to_data(value_type: str, value: str):
        assert value_type in VALUE_TYPE_LIST, f"{value_type} type not in {VALUE_TYPE_LIST}"

        if value_type == 'int':
            return int(value)
        if value_type == 'float':
            return float(value)
        if value_type == 'str':
            return str(value)
        if value_type == 'json':
            return json.loads(value)
        if value_type == 'bool':
            return bool(value)

    @classmethod
    def all(cls, is_show: bool = True, is_dict: bool = False):
        return cls._get_config(is_show=is_show, is_dict=is_dict)

    @classmethod
    def _get_config(cls, is_show: bool = True, is_dict: bool = False):
        queryset = DynamicConfig.objects.filter(is_show=is_show)
        config = {item.key: cls._string_to_data(item.value_type, item.value)
                  for item in queryset}
        return config if is_dict else SimpleNamespace(**config)

    def __getattr__(self, item):
        config = self.all(is_dict=True)
        if item not in config:
            raise AttributeError(f"'Config' object has no attribute '{item}'")
        return config[item]
