#!/bin/bash
echo "=> creating dramatiq-test conda env"
conda create -n dramatiq-test python=3.6
conda activate dramatiq-test
pip install -r requirements.txt