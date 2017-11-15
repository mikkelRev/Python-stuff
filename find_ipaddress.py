#!/usr/bin/env python
import socket
import fcntl
import struct


def get_ip(if_name):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
	s.fileno(),
	0x8915,
	struct.pack('256s', if_name[:15])
	)[20:24])


print get_ip('wlan0')
