from azure.servicebus import ServiceBusClient, ServiceBusMessage
from uuid import uuid1
from config import config


class ServiceBusService:
  def __init__(self, connection_str: str):
    with ServiceBusClient.from_connection_string(connection_str) as service_bus_client:
      self.service_bus_client = service_bus_client

  def send_message(self, queue_name: str, message: str):
    with self.service_bus_client.get_queue_sender(queue_name) as sender:
      session_id = str(uuid1())
      message = ServiceBusMessage(message, session_id=session_id)
      sender.send_messages(message)

service_bus_connection_str = config.get_service_bus_connection_str()
service_bus_service = ServiceBusService(service_bus_connection_str)
