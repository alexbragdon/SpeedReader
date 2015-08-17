#!/usr/bin/env python
#Version 0.1: August 17th, 2015

import time, note, drawNotes, getch, random
from note import note
from getch import getch
from drawNotes import drawNotes, clearGrandStaff

#The core of the game; selects a note at random, draws it to the terminal and asks the player what it is. 
def promtForNote():
  #The drawNotes function can only handel certain notes, so we have to limit the selection.
  possibleNotes = ['E,2', 'F,2', 'G,2', 'A,2', 'B,2', 'C,3', 
	               'D,3', 'E,3', 'F,3', 'G,3', 'A,3', 'B,3', 'C,4',
	               'D,4', 'E,4', 'F,4', 'G,4', 'A,4', 'B,4', 'C,5',
	               'D,5', 'E,5', 'F,5', 'G,5', 'A,5']
  randomNote, randomOctave = random.choice(possibleNotes).split(',') #Break the note, octave pair apart.
  randomOctave = int(randomOctave)

  notesToPrint = []
  notesToPrint.append(note(randomNote, randomOctave, 'natural', 'green'))
  drawNotes(notesToPrint) #Function with all the fun ACSII art.
  notesToPrint.clear()
  print('What note is this? ', end="", flush=True)
  answer = getch().upper()
  print(answer, end="", flush=True)

  correctAnswer = False
  answerCount = 0

  while not correctAnswer:
    if answer == 'Q':
      return 0 
    elif answer == randomNote:
      correctAnswer = True
      print("")
      return 1 + answerCount
    else:
      CURSOR_UP_ONE = '\x1b[1A' #These two strings manipulate the terminal we're drawing to.
      ERASE_LINE = '\x1b[2K' #Second string
      answerCount += 1
      print(CURSOR_UP_ONE, end="\n", flush=True)
      print('Wrong!! Try again! ', end="", flush=True)
      answer = getch().upper()
      print(answer, end="", flush=True)


#
def printFinalStatistics(totalQuestions, totalAnswers):
    if totalAnswers:
      print("\nIt took you " + repr(totalAnswers) + " answer(s) to name " + repr(totalQuestions) + " note(s)!")
      print("That's a " + repr((totalQuestions / totalAnswers) * 100) + "% accuracy!")
      print("Thanks for playing! Goodbye!")
    else:
      print("\nSorry, you didn't answer any questions.")
      print("Goodbye!")
    quit()


#Main loop for the game, just triggers a prompt for a new note forever, or until it recvives a zero for a questions score. 
def main():
  print('Welcome to Speed Reader v0.1')
  print('Push the key for the note displayed, or hit q to exit.')

  totalAnswers = 0
  totalQuestions = 0
  returnedFromPrompt = 0 

  while 1:
    returnedFromPrompt = promtForNote()
    if not returnedFromPrompt == 0: #A zero back indicates the user would like to quit the program.
      totalQuestions += 1
      totalAnswers += returnedFromPrompt
      clearGrandStaff()
      CURSOR_UP_ONE = '\x1b[1A'
      ERASE_LINE = '\x1b[2K'
      print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE, end="\n", flush=True)
    else:
      printFinalStatistics(totalQuestions, totalAnswers)
  

if __name__ == '__main__':
  main()