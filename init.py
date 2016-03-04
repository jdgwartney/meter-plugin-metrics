#!/usr/bin/env python

from sys import stdout
from time import sleep

while True:
    stdout.write("PULSE_METRIC_LOAD 100 DEFAULT\n")
    sleep(5)

