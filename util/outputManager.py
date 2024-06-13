﻿
import math
import datetime as dt
from token import PERCENT

def printProgress( message, completed, total, startTime, barLen=30, messagePad=30, padChar='.', startAmount=0 ):
  #'█' '▓' '▒' '░'

  timeElapsed = dt.datetime.now() - startTime
  percentage = 0 if total == 0 else completed / total
  timePercentage = 0 if total - startAmount == 0 else (completed - startAmount) / (total-startAmount)

  timeLeft = "Estimating Time"

  if timePercentage > 0 and timeElapsed.total_seconds() > 1:
    secondsLeft = ( timeElapsed.total_seconds() / timePercentage ) - timeElapsed.total_seconds() if timePercentage > 0 else 0
    m, s = divmod(secondsLeft, 60)
    h, m = divmod(m, 60)
    timeLeft = f'~{int(h):d}:{int(m):02d}:{int(s):02d}'

  blockCount = barLen * percentage 

  solidBlocks = math.floor(blockCount)
  remainder = blockCount - solidBlocks
  lastBlock = '' if completed == total else '▓' if remainder > 0.75 else '▒' if remainder > 0.5 else '░' if remainder > 0.25 else ' ' 

  blockTxt = '█' * solidBlocks + lastBlock + ' ' * (barLen - solidBlocks - 1)
  
  print( 
    message + padChar * (messagePad - len(message)),
    F'[{blockTxt}]',
    F'({completed}/{total}; {percentage:.1%}; {timeLeft} Remaining)',
    end='\r')

  if completed >= total:
    print(
      message + padChar * (messagePad - len(message)),
      F'[{blockTxt}]',
      F'({completed}/{total}; {percentage:.1%})'
    )
    return False
  return True
  
