#!/usr/bin/env python

import colorama
from colorama import Fore, Back, Style

#Simple object for ease of note drawing.
class note:
  def __init__(self, name, octave, pitch, color):
    self.name = name
    self.octave = octave

    if pitch == 'sharp':
      self.body = '#()'
    elif pitch == 'flat':
      self.body = 'b()'
    else:
      self.body = ' ()'

    if color == 'green':
      self.color = Fore.GREEN
    elif color == 'red':
      self.color = Fore.RED
    else:
      self.color = Fore.BLACK