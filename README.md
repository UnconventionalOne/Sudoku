# Sudoku

Originally I tried figuring out on my own how I might be  able to solve and 
generate Sudokus. I realize I should use dictionaries or something other than lists,
but that would seem to require a complete redesign. The scripts here are the best things 
that have come out of that so far. 

lookout_testing.py

This is the closest thing I currently have to a Sudoku generator. Currently, it should 
either create a completed, valid Sudoku board or raises an exception. Regarding the failures,
it seems likely to be faster just to scratch a failure and try again, rather than try to backtrack
or something. 
To make an actual puzzle, I would still need to do something like randomly deleting cells, while 
checking that the board still only has one solution, which would require a very fast solver. 
It basically works using a combination between random number assignment and the two most simple
logical solving techniques (identifying naked singles and hiden singles).

brute_force_attempt1.py

My crazy backtracking solver. Because of the way data is currently being stored in nested lists, 
this could be a lot faster.
Pelease excuse the mess, It's decided to upload it in all it's testing glory.


 
