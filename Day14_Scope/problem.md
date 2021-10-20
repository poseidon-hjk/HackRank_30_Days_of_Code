## Objective
Today we're discussing scope. Check out the <a href="https://www.hackerrank.com/challenges/30-scope/tutorial">Tutorial</a> tab for learning materials and an instructional video!
<hr>

The absolute difference between two integers, **_a_** and **_b_**, is written as **_|a - b|_**. The maximum absolute difference between two integers in a set of positive integers, **_elements_**, is the largest absolute difference between any two integers in **___elements_**.

The Difference class is started for you in the editor. It has a private integer array (**_elements_**) for storing **_N_** non-negative integers, and a public integer (**_maximumDifference_**) for storing the maximum absolute difference.

##Task
Complete the Difference class by writing the following:

- A class constructor that takes an array of integers as a parameter and saves it to the **___elements_** instance variable.
- A computeDifference method that finds the maximum absolute difference between any **_2_** numbers in **___elements_** and stores it in the **_maximumDifference_** instance variable.

## Input Format

You are not responsible for reading any input from stdin. The locked Solution class in the editor reads in **_2_** lines of input. The first line contains **_N_**, the size of the elements array. The second line has **_N_** space-separated integers that describe the **___elements_** array.

## Constraints
- 1 <= **_N_** <= 10
- 1 <= **___elements[i]_** <= **_100_**, where **_0_** <= **_i_** <= **_N - 1_**

## Output Format

You are not responsible for printing any output; the Solution class will print the value of the **_maximumDifference_** instance variable.

## Sample Input

    STDIN   Function
    -----   --------
    3       __elements[] size N = 3
    1 2 5   __elements = [1, 2, 5]

## Sample Output

    4

## Explanation

The scope of the **___elements_** array and **_maximumDifference_** integer is the entire class instance. The class constructor saves the argument passed to the constructor as the **___elements_** instance variable (where the computeDifference method can access it).

To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference between any **_2_** elements: **|1 - 2| = 1** 
**|1 - 5| = 4**
**|2 - 5| = 3**

The maximum of these differences is **4**, so it saves the value **4** as the **_maximumDifference_** instance variable. 
The locked stub code in the editor then prints the value stored as **_maximumDifference_**, which is **4**.