#!/usr/bin/env python
# coding: utf-8
import logging
import os
import socket

__version__ = '0.1.0a1'

log = logging.getLogger(__name__)


class GrimReaper(object):
    def __init__(self, socket_path='/tmp/grimreaper.socket', process_timeout=30):
        self._path = socket_path
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._process_timeout = process_timeout
        self._connect()

    def _is_connected(self):
        try:
            self._socket.recv(0)
        except socket.error:
            return self._connect()
        else:
            return True

    def _connect(self):
        try:
            self._socket.connect(self._path)
        except socket.error as e:
            log.error('Unnable to connect to the socket "%s": %s', self._path, e)
            self.on_connection_error(e)

            if e.errno == socket.errno.ENOENT:
                # No such file or directory
                return False
            elif e.errno == socket.errno.ECONNREFUSED:
                # Connection refused
                return False

            raise
        return True

    def register(self, timeout=None, pid=None):
        if timeout is None:
            timeout = self._process_timeout

        if pid is None:
            pid = os.getpid()

        if self._is_connected():
            msg = 'register:%s:%s' % (pid, timeout)
            self._socket.sendall(msg.encode('utf-8'))
            log.debug('Registered process (PID=%s; timeout=%s)', pid, timeout)
        else:
            log.warning('Unnable to register the process (PID=%s).', pid)

    def unregister(self, pid=None):
        if pid is None:
            pid = os.getpid()

        if self._is_connected():
            msg = 'unregister:%s' % pid
            self._socket.sendall(msg.encode('utf-8'))
            log.debug('Unregistered process (PID=%s)', pid)
        else:
            log.warning('Unnable to unregister the process (PID=%s).', pid)

    def on_connection_error(self, exc):
        pass