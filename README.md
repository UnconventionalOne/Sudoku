# Sudoku

Originally I tried figuring out on my own how to solve and generate Sudokus. The scripts here 
are the best things that have come out of that so far.  

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
it't pretty slow. Pelease excuse the mess. I decided to upload it in all it's messy, testing glory.


 
