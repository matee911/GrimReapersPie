#!/usr/bin/env/python
# coding: utf-8

import logging
import random
import sys
import time

from grimreaper import GrimReaper


def open_close(reaper, sleep, kill_after):
    # Register this process
    reaper.register(timeout=kill_after)

    # Run a long-running operation
    print("Will sleep for %s seconds." % sleep)
    time.sleep(sleep)

    # Unregister unless already killed by the GrimReaper
    reaper.unregister()


def main(args):
    reaper = GrimReaper()

    # How long this process will run
    sleep = random.randint(1, 10)

    # How many seconds must pass before the GrimReaper will kill this process
    kill_after = random.randint(1, 10)

    open_close(reaper, sleep, kill_after)


if __name__ == '__main__':
    grim_logger = logging.getLogger('grimreaper')
    grim_logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    grim_logger.addHandler(ch)

    main(sys.argv)
