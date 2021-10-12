## Objective
Today, we're discussing data types. Check out the <a href="https://www.hackerrank.com/challenges/30-data-types/tutorial">Tutorial</a> tab for learning materials and an instructional video!

## Task
Complete the code in the editor below. The variables <i><b>i</b></i>, <i><b>d</b></i>, and <i><b>s</b></i> are already declared and initialized for you. You must:

1. Declare <b><i>3</i></b> variables: one of type <i>int</i>, one of type <i>double</i>, and one of type <i>String</i>.
2. Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
3. Use the + operator to perform the following operations:
   1. Print the sum of  plus your int variable on a new line.
   2. Print the sum of  plus your double variable to a scale of one decimal place on a new line.
   3. Concatenate  with the string you read as input and print the result on a new line.
<b>Note</b>: If you are using a language that doesn't support using  for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.

## Input Format

The first line contains an integer that you must sum with <i><b>i</b></i>.
The second line contains a double that you must sum with <i><b>d</b></i>.
The third line contains a string that you must concatenate with <i><b>s</b></i>.

## Output Format

Print the sum of both integers on the first line, the sum of both doubles (scaled to <i><b>1</b></i> decimal place) on the second line, and then the two concatenated strings on the third line.

## Sample Input

12  <br>
4.0 <br>
is the best place to learn and practice coding!

## Sample Output

16  <br>
8.0 <br>
HackerRank is the best place to learn and practice coding!

## Explanation

When we sum the integers <b>4</b> and <b>12</b>, we get the integer <b>16</b>.
When we sum the floating-point numbers <b>4.0</b> and <b>4.0</b>, we get <b>8.0</b>.
When we concatenate <code>HackerRank</code> with <code>is the best place to learn and practice coding!</code>, we get <code>HackerRank is the best place to learn and practice coding!</code>.

<b>You will not pass this challenge if you attempt to assign the Sample Case values to your variables instead of following the instructions above and reading input from stdin.</b>