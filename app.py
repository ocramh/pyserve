import os
import logging
import time
from flask import Flask
import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
import torch
from yolov3.yolov3 import Darknet

rabbitmq_broker = RabbitmqBroker(host="35.204.126.101", port=5672)
dramatiq.set_broker(rabbitmq_broker)

flask_app = Flask(__name__)

global counter
counter = 0

### Object detection
# prepare model
device = torch.device("cuda")
global model
model = Darknet('./yolov3/yolov3.cfg')
model.load_darknet_weights('./yolov3/yolov3.weights')
model.to(device)
model.eval()

@dramatiq.actor(max_retries=2)
def test_task(task_num):
    print("starting task {}".format(task_num))

    # access models on GPU here
    dummy_pred = model(torch.rand((1,3,128,128)).to(device))
    print(dummy_pred)

    time.sleep(20)
    print("complete task {}".format(task_num))


@flask_app.route('/')
def run_task():
    global counter
    test_task.send(counter)
    counter = counter + 1
    return 'processing started'
