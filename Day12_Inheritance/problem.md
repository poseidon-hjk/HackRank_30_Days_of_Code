## Objective
Today, we're delving into Inheritance. Check out the attached <a href="https://www.hackerrank.com/challenges/30-inheritance/tutorial">tutorial</a> for learning materials and an instructional video.

## Task
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

- A Student class constructor, which has <b>4</b> parameters:
  1. A string, <i><b>firstName</b></i>.
  2. A string, <i><b>lastName</b></i>.
  3. An integer, <i><b>idNumber</b></i>.
  4. An integer array (or vector) of test scores, .
- A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
<br><br>
  ![](https://s3.amazonaws.com/hr-challenge-images/17165/1458142706-3073bc9143-Grading.png "Grading.png")

## Input Format

The locked stub code in the editor reads the input and calls the Student class constructor with the necessary arguments. It also calls the calculate method which takes no arguments.

The first line contains <i><b>firstName</b></i>, <i><b>lastName</b></i>, and <i><b>idNumber</b></i>, separated by a space. The second line contains the number of test scores. The third line of space-separated integers describes <i><b>scores</b></i>.

## Constraints
<i><b>
- 1 <= length of firstName, length of lastName <= 10
- length of idNumber == 7
- 0 <= score <= 100
</b></i>.

## Output Format

Output is handled by the locked stub code. Your output will be correct if your Student class constructor and calculate() method are properly implemented.

### Sample Input

    Heraldo Memelli 8135627
    2
    100 80

### Sample Output

    Name: Memelli, Heraldo
    ID: 8135627
    Grade: O

## Explanation

This student had  scores to average: _**2**_. _**100**_ and _**80**_. The student's average grade is **_(100+80) / 2 = 90_**. An average grade of _**90**_ corresponds to the letter grade _**O**_, so the calculate() method should return the character'O'.