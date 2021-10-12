## Objective
Today, we are building on our knowledge of arrays by adding another dimension. Check out the <a href="https://www.hackerrank.com/challenges/30-2d-arrays/tutorial">Tutorial</a> tab for learning materials and an instructional video.

## Context
Given a <i><b>6 * 6</i></b> 2D Array, <i><b>A</i></b>:

    1 1 1 0 0 0 
    0 1 0 0 0 0 
    1 1 1 0 0 0 
    0 0 0 0 0 0 
    0 0 0 0 0 0 
    0 0 0 0 0 0

We define an hourglass in <i><b>A</i></b> to be a subset of values with indices falling in this pattern in <i><b>A</i></b>'s graphical representation:

    a b c 
      d   
    e f g

There are <i><b>16</i></b> hourglasses in <i><b>A</i></b>, and an hourglass sum is the sum of an hourglass' values.

## Task
Calculate the hourglass sum for every hourglass in <i><b>A</i></b>, then print the maximum hourglass sum.

## Example

In the array shown above, the maximum hourglass sum is <i><b>7</i></b> for the hourglass in the top left corner.

## Input Format

There are <i><b>6</i></b> lines of input, where each line contains <i><b>6</i></b> space-separated integers that describe the 2D Array <i><b>A</i></b>.

## Constraints
-     -9 <= A[i][j] <= 9
-     0 <= i,j <= 5

## Output Format

Print the maximum hourglass sum in <i><b>A</i></b>.

## Sample Input

    1 1 1 0 0 0 
    0 1 0 0 0 0 
    1 1 1 0 0 0 
    0 0 2 4 4 0   
    0 0 0 2 0 0 
    0 0 1 2 4 0

## Sample Output

    19

## Explanation

<i><b>A</i></b> contains the following hourglasses:

  
    1 1 1   1 1 0   1 0 0   0 0 0  
      1       0       0       0  
    1 1 1   1 1 0   1 0 0   0 0 0

    0 1 0   1 0 0   0 0 0   0 0 0
      1       1       0       0
    0 0 2   0 2 4   2 4 4   4 4 0

    1 1 1   1 1 0   1 0 0   0 0 0
      0       2       4       4
    0 0 0   0 0 2   0 2 0   2 0 0

    0 0 2   0 2 4   2 4 4   4 4 0
      0       0       2       0
    0 0 1   0 1 2   1 2 4   2 4 0
  
The hourglass with the maximum sum () is:

    2 4 4
      2
    1 2 4