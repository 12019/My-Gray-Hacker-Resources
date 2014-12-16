#!/usr/bin/env python

__author__ = "bt3"


import os
import socket
import select
from time import sleep
import binascii
from subprocess import Popen,STDOUT,PIPE
import os
from math import *
import string



def next_line(stdout):
  # read inputs in lines
  line = ""
  while True:
    r = stdout.read(1)
    if r == '\n':
      break
    line += r
  return line


def write(stdin,val):
  # write outputs
  stdin.write(val)


def nl():
  # shorter next line for iteration
  return next_line(p.stdout)


def wr(val):
  # shorter write for iteration
  write(p.stdin,val)


def ntext():
  line = ""
  while "psifer text:" not in line:
    line = nl()
  return line[len("psifer text:") + 1:]



def main():
  SHELL_COMMAND = "nc 54.209.5.48 12345"

  p = Popen(SHELL_COMMAND, shell=True, cwd="./", stdin=PIPE,
    stdout=PIPE, stderr=STDOUT,close_fds=True)


  while True:
    text = ntext()
    text += " -> just an example"
    wr(ans + '\n')

  ret = p.wait()
  print "Return code: %d" % ret



if __name__ == '__main__':
  main()