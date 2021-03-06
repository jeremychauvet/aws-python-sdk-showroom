#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

import secrets
import sys
import boto3
import json
from time import sleep
from faker import Faker
from faker_credit_score import CreditScore

# This function insert fake datas in queue defined bellow.
client = boto3.client("sqs", region_name="eu-central-1")

# Variables.
QUEUE_NAME = "order.fifo"
NUMBER_OF_MESSAGES_TO_SEND = 1


def insert_messages_in_queue():
    try:
        get_queue_url_response = client.get_queue_url(QueueName=QUEUE_NAME)
        queue_url = get_queue_url_response["QueueUrl"]

        # Import library to insert fake datas.
        fake = Faker()
        fake.add_provider(CreditScore)

        for message_number in range(NUMBER_OF_MESSAGES_TO_SEND):
            payload = {
                "credit_score": {
                    "name": str(fake.credit_score_name()),
                    "provider": str(fake.credit_score_provider()),
                    "score": str(fake.credit_score()),
                }
            }
            # Convert dictionnary in JSON.
            payload = json.dumps(payload)
            # Create hash for MessageDeduplicationId as queue is FIFO.
            hash = secrets.token_hex(nbytes=16)
            print('[INFO] Message : ' + str(payload))
            print('[INFO] Hash : ' + hash)
            # Sent message to queue.
            send_message_response = client.send_message(
                QueueUrl=queue_url,
                MessageBody=payload,
                MessageGroupId=hash,
                MessageDeduplicationId=hash,
            )

            if send_message_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print(
                    "[INFO] Message "
                    + str(message_number)
                    + " of "
                    + str(NUMBER_OF_MESSAGES_TO_SEND)
                    + " sent successfully."
                )
                sleep(2)
            else:
                print(
                    "[ERROR] Message not sent successfully. Output : "
                    + str(send_message_response)
                )
                sys.exit(1)

    except:
        print("[ERROR] " + str(sys.exc_info()[1]))

if __name__ == "__main__":
    insert_messages_in_queue()
