import os
import logging
import time
from flask import Flask
import dramatiq

flask_app = Flask(__name__)

global counter
counter = 0


@dramatiq.actor(max_retries=2)
def test_task(task_num):
    print("starting task {}".format(task_num))
    # access models on GPU here
    time.sleep(20)
    print("complete task {}".format(task_num))


@flask_app.route('/')
def run_task():
    global counter
    test_task.send(counter)
    counter = counter + 1
    return 'processing started'
