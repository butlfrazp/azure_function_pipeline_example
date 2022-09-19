import logging
import json
import azure.functions as func
from services.blob_service import blob_service
from services.service_bus_service import service_bus_service

"""
expected payload example:
{
    "container": "test",
    "source_path": "source/sample2.json",
    "target_path": "stage/sample2.json"
}
"""
def main(msg: func.ServiceBusMessage):
    logging.info('Triggered source to target azure function...')

    message_data_str = msg.get_body().decode('utf-8')
    message_data_json = json.loads(message_data_str)

    container = message_data_json["container"]
    source_path = message_data_json["source_path"]
    target_path = message_data_json["target_path"]

    blob_data = blob_service.download_blob(container, source_path)
    blob_service.upload_blob(container, target_path, json.dumps(blob_data))

    target_service_bus_queue = "staged-to-target"

    triggering_message = {
        "container": message_data_json["container"],
        "source_path": message_data_json["target_path"],
        "target_path": "sample.json"
    }

    service_bus_service.send_message(target_service_bus_queue, json.dumps(triggering_message))
