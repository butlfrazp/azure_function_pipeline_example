import os

class Config:
  def __init__(self):
    self._BLOB_STORAGE_CONN_STR = self._get_env_variable('BLOB_STORAGE_CONN_STR')
    self._SERVICE_BUS_CONN_STR = self._get_env_variable('SERVICE_BUS_CONN_STR')
    self._EVENT_HUB_CONN_STR = self._get_env_variable("EVENT_HUB_CONN_STR")

  def _get_env_variable(self, env_var: str, is_required: bool = True) -> str:
    value = os.environ.get(env_var)
    
    if value == None and is_required:
      raise ValueError(f"{env_var} cannot be empty")

    return value

  def get_blob_storage_connection_str(self) -> str:
    return self._BLOB_STORAGE_CONN_STR

  def get_service_bus_connection_str(self) -> str:
    return self._SERVICE_BUS_CONN_STR

  def get_event_hub_connection_str(self) -> str:
    return self._EVENT_HUB_CONN_STR

config = Config()  
