import logging
import json
import azure.functions as func
from azure.eventhub import EventHubProducerClient, EventData
from services.blob_service import blob_service
from config import config


def main(event: func.EventHubEvent):
    logging.info('Triggered source to staged azure function...')

    message_data_str = event.get_body().decode('utf-8')
    message_data_json = json.loads(message_data_str)

    container = message_data_json["container"]
    source_path = message_data_json["source_path"]
    target_path = message_data_json["target_path"]

    blob_data = blob_service.download_blob(container, source_path)
    blob_service.upload_blob(container, target_path, json.dumps(blob_data))

    triggering_message = {
        "container": message_data_json["container"],
        "source_path": message_data_json["target_path"],
        "target_path": "sample.json"
    }

    triggering_message_str = json.dumps(triggering_message)
    return triggering_message_str
