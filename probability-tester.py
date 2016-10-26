"""

Script to prove (or disprove) that just because you throw heads 3 times in a row, 
it doesn't make you any more or less likely to throw tails on the next throw - the
probability is always the same.

.. which we already knew, but just to prove it - but more importantly, it proves
that Martingale betting systems are a risky business. You can be wrong 10 times in a row.

Usage: 

python probability-tester.py
  (perform default 1000 iterations)

python probability-tester.py 1000000
  (perform a million iterations)
  

"""

import sys, random
from time import time

startTime = time()

# record total number of wins and losses
wins   = 0
losses = 0

# record total number of coin tosses, just for fun
tosses = 0

try:
    iterations = int(sys.argv[1])
except IndexError:
    iterations = 1000

for i in range(0, iterations):

    # list to record throws
    throws = []

    # keep appending heads or tails (1 or 0) to list until last 3 throws were all heads (1) or all tails (0)
    while throws[-3:] != [1, 1, 1] and throws[-3:] != [0, 0, 0]:
        throws.append(random.choice((0, 1)))
        tosses += 1

    # now bet the opposite way and check if our bet matches another random coin toss.
    # if so, we win!
    if (int(throws[-1:] == [0]) == random.choice((0, 1))):
        wins += 1
    else:
        losses += 1

    # record the final throw
    tosses += 1

executionTime = time() - startTime

print "Performed %s iterations (%s coin tosses) in %.2f secs." \
    % (format(iterations, ',d'), format(tosses, ',d'), executionTime)

print "Wins: %s" % format(wins, ',d')
print "Losses: %s" % format(losses, ',d')