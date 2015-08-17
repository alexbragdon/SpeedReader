#!/usr/bin/env python

import colorama
from colorama import Fore, Back, Style

#Draws the entire grand staff.
def drawNotes(notesToDisplay):
 
#These are the default 'fill in the blank' variables to draw a complete empty staff.
  Note = {}
  Note['A',5] = '   '
  Note['G',5] = '   '
  Note['F',5] = '---'
  Note['E',5] = '   '
  Note['D',5] = '---'
  Note['C',5] = '   '
  Note['B',4] = '---'
  Note['A',4] = '   '
  Note['G',4] = '---'
  Note['F',4] = '   '
  Note['E',4] = '---'
  Note['D',4] = '   '
  Note['C',4] = '   '
  Note['B',3] = '   '
  Note['A',3] = '---'
  Note['G',3] = '   '
  Note['F',3] = '---'
  Note['E',3] = '   '
  Note['D',3] = '---'
  Note['C',3] = '   '
  Note['B',2] = '---'
  Note['A',2] = '   '
  Note['G',2] = '---'
  Note['F',2] = '   '
  Note['E',2] = '   '

#The stem for each not is set in the same way.
  Stem = {}
  Stem['A',5] = ' '
  Stem['G',5] = ' '
  Stem['F',5] = ' '
  Stem['E',5] = '-'
  Stem['D',5] = ' '
  Stem['C',5] = '-'
  Stem['B',4] = ' '
  Stem['A',4] = '-'
  Stem['G',4] = ' '
  Stem['F',4] = '-'
  Stem['E',4] = ' '
  Stem['D',4] = '-'
  Stem['C',4] = ' '
  Stem['B',3] = ' '
  Stem['A',3] = ' '
  Stem['G',3] = '-'
  Stem['F',3] = ' '
  Stem['E',3] = '-'
  Stem['D',3] = ' '
  Stem['C',3] = '-'
  Stem['B',2] = ' '
  Stem['A',2] = '-'
  Stem['G',2] = ' '
  Stem['F',2] = '-'
  Stem['E',2] = ' '


#The blank spots for the notes are then updated for each note to be drawn.
  for currentNote in notesToDisplay:
    Note[currentNote.name, currentNote.octave]= Style.BRIGHT + currentNote.color + currentNote.body + Style.RESET_ALL
    Stem[currentNote.name, currentNote.octave]= Style.BRIGHT + currentNote.color + '|' + Style.RESET_ALL

#An ASCII art representation of a grand staff, every possible note location corrisponds to a location in the 'note' collection. 
  print('                                              ' + Stem['A',5], end="\n", flush=True)
  print('|    __                                    ' + Stem['G',5] + Note['A',5], end="", flush=True)
  print('   \n', end="", flush=True)
  print('|   |  )                                 ' + Stem['F',5] + Note['G',5], end="", flush=True)
  print('      \n', end="", flush=True)
  print('|---|-/------------------------------' + Stem['E',5] + Note['F',5], end="", flush=True)
  print('---------\n', end="", flush=True)
  print('|   |/                            ' + Stem['D',5] + Note['E',5], end="", flush=True)
  print('            \n', end="", flush=True)
  print('|---/--------------------------' + Stem['C',5] + Note['D',5], end="", flush=True)
  print('---------------\n', end="", flush=True)
  print('|  /|                       ' + Stem['B',4] + Note['C',5], end="", flush=True)
  print('                  \n', end="", flush=True)
  print('|-/-|--------------------' + Stem['A',4] + Note['B',4], end="", flush=True)
  print('---------------------\n', end="", flush=True)
  print('|( /|\                ' + Stem['G',4] + Note['A',4], end="", flush=True)
  print('                        \n', end="", flush=True)
  print('|-\-|-)------------' + Stem['F',4] + Note['G',4], end="", flush=True)
  print('---------------------------\n', end="", flush=True)
  print('|  \|/          ' + Stem['E',4] + Note['F',4], end="", flush=True)
  print('                              \n', end="", flush=True)
  print('|---|--------' + Stem['D',4] + Note['E',4], end="", flush=True)
  print('---------------------------------\n', end="", flush=True)
  print('| (_|     ' + Stem['C',4] + Note['D',4], end="", flush=True)
  print('                                    \n', end="", flush=True)
  print('|       ' + Note['C',4], end="", flush=True)
  print('                                ' + Stem['B', 3] + '      \n', end="", flush=True)
  print('|                                       ' + Stem['A',3] + Note['B',3], end="", flush=True)
  print('      \n', end="", flush=True)
  print('|----_-------------------------------' + Stem['G',3] + Note['A',3], end="", flush=True)
  print('---------\n', end="", flush=True)
  print('|  /   \  *                       ' + Stem['F',3] + Note['G',3], end="", flush=True)
  print('            \n', end="", flush=True)
  print('|-|-----|----------------------' + Stem['E',3] + Note['F',3], end="", flush=True)
  print('---------------\n', end="", flush=True)
  print('|  \_/  | *                 ' + Stem['D',3] + Note['E',3], end="", flush=True)
  print('                  \n', end="", flush=True)
  print('|------/-----------------' + Stem['C',3] + Note['D',3], end="", flush=True)
  print('---------------------\n', end="", flush=True)
  print('|     /               ' + Stem['B',2] + Note['C',3], end="", flush=True)
  print('                        \n', end="", flush=True)
  print('|----/-------------' + Stem['A',2] + Note['B',2], end="", flush=True)
  print('---------------------------\n', end="", flush=True)
  print('|               ' + Stem['G',2] + Note['A',2], end="", flush=True)
  print('                              \n', end="", flush=True)
  print('|------------' + Stem['F',2] + Note['G',2], end="", flush=True)
  print('---------------------------------\n', end="", flush=True)
  print('|         ' + Stem['E',2] + Note['F',2], end="", flush=True)
  print('                                    \n', end="", flush=True)
  print('|       ' + Note['E',2], end="", flush=True)
  print('                                       \n', end="", flush=True)
  print('\n')


#Draws only the treble cleft.
def drawTrebleNotes(notesToDisplay):
 
  Note = {}
  Note['A',5] = '   '
  Note['G',5] = '   '
  Note['F',5] = '---'
  Note['E',5] = '   '
  Note['D',5] = '---'
  Note['C',5] = '   '
  Note['B',4] = '---'
  Note['A',4] = '   '
  Note['G',4] = '---'
  Note['F',4] = '   '
  Note['E',4] = '---'
  Note['D',4] = '   '
  Note['C',4] = '   '

  Stem = {}
  Stem['C',6] = ' '
  Stem['G',5] = ' '
  Stem['F',5] = ' '
  Stem['E',5] = '-'
  Stem['D',5] = ' '
  Stem['C',5] = '-'
  Stem['B',4] = ' '
  Stem['A',4] = '-'
  Stem['G',4] = ' '
  Stem['F',4] = '-'
  Stem['E',4] = ' '
  Stem['D',4] = '-'
  Stem['C',4] = ' '


  for currentNote in notesToDisplay:
    Note[currentNote.name, currentNote.octave]= Style.BRIGHT + currentNote.color + currentNote.body + Style.RESET_ALL
    Stem[currentNote.name, currentNote.octave]= Style.BRIGHT + currentNote.color + '|' + Style.RESET_ALL

  print('\n', end="", flush=True)
  print('                                              ' + Stem['A',5], end="\n", flush=True)
  print('|    __                                    ' + Stem['G',5] + Note['A',5], end="", flush=True)
  print('   \n', end="", flush=True)
  print('|   |  )                                 ' + Stem['F',5] + Note['G',5], end="", flush=True)
  print('      \n', end="", flush=True)
  print('|---|-/------------------------------' + Stem['E',5] + Note['F',5], end="", flush=True)
  print('---------\n', end="", flush=True)
  print('|   |/                            ' + Stem['D',5] + Note['E',5], end="", flush=True)
  print('            \n', end="", flush=True)
  print('|---/--------------------------' + Stem['C',5] + Note['D',5], end="", flush=True)
  print('---------------\n', end="", flush=True)
  print('|  /|                       ' + Stem['B',4] + Note['C',5], end="", flush=True)
  print('                  \n', end="", flush=True)
  print('|-/-|--------------------' + Stem['A',4] + Note['B',4], end="", flush=True)
  print('---------------------\n', end="", flush=True)
  print('|( /|\                ' + Stem['G',4] + Note['A',4], end="", flush=True)
  print('                        \n', end="", flush=True)
  print('|-\-|-)------------' + Stem['F',4] + Note['G',4], end="", flush=True)
  print('---------------------------\n', end="", flush=True)
  print('|  \|/          ' + Stem['E',4] + Note['F',4], end="", flush=True)
  print('                              \n', end="", flush=True)
  print('|---|--------' + Stem['D',4] + Note['E',4], end="", flush=True)
  print('---------------------------------\n', end="", flush=True)
  print('| (_|     ' + Stem['C',4] + Note['D',4], end="", flush=True)
  print('                                    \n', end="", flush=True)
  print('|       ' + Note['C',4], end="", flush=True)
  print('                                       \n', end="", flush=True)
  print('\n')


#Draws only the bass cleft.
def drawBassNotes(notesToDisplay):
 
  Note = {}
  Note['C',4] = '   '
  Note['B',3] = '   '
  Note['A',3] = '---'
  Note['G',3] = '   '
  Note['F',3] = '---'
  Note['E',3] = '   '
  Note['D',3] = '---'
  Note['C',3] = '   '
  Note['B',2] = '---'
  Note['A',2] = '   '
  Note['G',2] = '---'
  Note['F',2] = '   '
  Note['E',2] = '   '

  Stem = {}
  Stem['C',4] = ' '
  Stem['B',3] = ' '
  Stem['A',3] = ' '
  Stem['G',3] = '-'
  Stem['F',3] = ' '
  Stem['E',3] = '-'
  Stem['D',3] = ' '
  Stem['C',3] = '-'
  Stem['B',2] = ' '
  Stem['A',2] = '-'
  Stem['G',2] = ' '
  Stem['F',2] = '-'
  Stem['E',2] = ' '


  for currentNote in notesToDisplay:
    Note[currentNote.name, currentNote.octave]= Style.BRIGHT + currentNote.color + currentNote.body + Style.RESET_ALL
    Stem[currentNote.name, currentNote.octave]= Style.BRIGHT + currentNote.color + '|' + Style.RESET_ALL

  print('\n', end="", flush=True)
  print('                                              ' + Stem['C',4], end="\n", flush=True)
  print('|                                          ' + Stem['B',3] + Note['C',4], end="", flush=True)
  print('   \n', end="", flush=True)
  print('|                                       ' + Stem['A',3] + Note['B',3], end="", flush=True)
  print('      \n', end="", flush=True)
  print('|----_-------------------------------' + Stem['G',3] + Note['A',3], end="", flush=True)
  print('---------\n', end="", flush=True)
  print('|  /   \  *                       ' + Stem['F',3] + Note['G',3], end="", flush=True)
  print('            \n', end="", flush=True)
  print('|-|-----|----------------------' + Stem['E',3] + Note['F',3], end="", flush=True)
  print('---------------\n', end="", flush=True)
  print('|  \_/  | *                 ' + Stem['D',3] + Note['E',3], end="", flush=True)
  print('                  \n', end="", flush=True)
  print('|------/-----------------' + Stem['C',3] + Note['D',3], end="", flush=True)
  print('---------------------\n', end="", flush=True)
  print('|     /               ' + Stem['B',2] + Note['C',3], end="", flush=True)
  print('                        \n', end="", flush=True)
  print('|----/-------------' + Stem['A',2] + Note['B',2], end="", flush=True)
  print('---------------------------\n', end="", flush=True)
  print('|               ' + Stem['G',2] + Note['A',2], end="", flush=True)
  print('                              \n', end="", flush=True)
  print('|------------' + Stem['F',2] + Note['G',2], end="", flush=True)
  print('---------------------------------\n', end="", flush=True)
  print('|         ' + Stem['E',2] + Note['F',2], end="", flush=True)
  print('                                    \n', end="", flush=True)
  print('|       ' + Note['E',2], end="", flush=True)
  print('                                       \n', end="", flush=True)
  print('\n')

#Erases the appropriate number of lines to erase the whole grand staff.  
def clearGrandStaff():
  CURSOR_UP_ONE = '\x1b[1A'
  ERASE_LINE = '\x1b[2K'
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + 
	    ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + 
	    CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + 
	    ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + 
	    CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + 
	    ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + 
	    CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + 
	    ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + CURSOR_UP_ONE, end="", flush=True)

#Erases the appropriate number of lines to clear a single cleft, bass or treble.
def clearSingleStaff():
  CURSOR_UP_ONE = '\x1b[1A'
  ERASE_LINE = '\x1b[2K'
  print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + 
	    ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + 
	    CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + 
	    ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + 
	    CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE, end="", flush=True)
