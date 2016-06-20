#!/usr/bin/env python
# coding: utf-8
import logging
import os
import socket

__version__ = '0.1'

log = logging.getLogger(__name__)


class GrimReaper(object):
    def __init__(self, socket_path='/tmp/GrimReaper.socket', process_timeout=30):
        self._path = socket_path
        self._process_timeout = process_timeout
        self._connect()

    def _is_connected(self):
        try:
            self._socket.recv(0)
        except socket.error as e:
            if e.errno == socket.errno.EAGAIN:
                return True
            else:
                log.debug(e)
                return self._connect()
        else:
            log.debug('Connection is active')
            return True

    def _connect(self):
        self._socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._socket.setblocking(0)

        try:
            self._socket.connect(self._path)
        except socket.error as e:
            # Transport endpoint is already connected
            if e.errno == 106:
                return True

            log.error('Unable to connect to the socket "%s": %s', self._path, e)
            self.on_connection_error(e)

            if e.errno == socket.errno.ENOENT:
                # No such file or directory
                return False
            elif e.errno == socket.errno.ECONNREFUSED:
                # Connection refused
                return False
            elif e.errno == socket.errno.EPIPE:
                # Broken pipe
                return False

            raise
        return True

    def _close(self):
        self._socket.close()

    def register(self, timeout=None, pid=None):
        if timeout is None:
            timeout = self._process_timeout

        if pid is None:
            pid = os.getpid()

        if self._is_connected():
            msg = 'register:%s:%s' % (pid, timeout)
            try:
                self._socket.sendall(msg.encode('utf-8'))
            except socket.error as e:
                if e.errno == socket.errno.EPIPE:
                    self._close()
                    return
                log.debug(e)

            log.debug('Registered process (PID=%s; timeout=%s)', pid, timeout)
        else:
            log.warning('Unable to register the process (PID=%s).', pid)

    def unregister(self, pid=None):
        if pid is None:
            pid = os.getpid()

        if self._is_connected():
            msg = 'unregister:%s' % pid
            try:
                self._socket.sendall(msg.encode('utf-8'))
            except socket.error as e:
                if e.errno == socket.errno.EPIPE:
                    self._close()
                    return
                log.debug(e)

            log.debug('Unregistered process (PID=%s)', pid)
        else:
            log.warning('Unable to unregister the process (PID=%s).', pid)

    def on_connection_error(self, exc):
        pass
