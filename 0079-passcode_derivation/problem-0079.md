# [Passcode derivation](https://projecteuler.net/problem=79) 

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was `531278`, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: `317`.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

## Answers 


1. `73126890` &larr; Incorrect; likely due to incomplete analysis of printed network
1. `73162890` &larr; Correct; misjudged the interaction between 6 &harr; 2.

## Notes

1. This problem had to be solved by generating a network of interacting members.
