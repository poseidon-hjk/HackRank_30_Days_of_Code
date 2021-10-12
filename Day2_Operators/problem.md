## Objective
In this challenge, you will work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video.

## Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost. Round the result to the nearest integer.

## Example
<i><b>
meal_cost = 100  <br>
tip_percent = 15 <br>
tax_percent = 8
</i></b>

A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. Print the value <i>123</i> and return from the function.

## Function Description
Complete the solve function in the editor below.

solve has the following parameters:

- int meal_cost: the cost of food before tip and tax
- int tip_percent: the tip percentage
- int tax_percent: the tax percentage

Returns The function returns nothing. Print the calculated value, rounded to the nearest integer.

<b>Note:</b> Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result.

## Input Format

There are <b>3</b> lines of numeric input:  <br>
The first line has a double, <i><b>meal_cost</i></b> (the cost of the meal before tax and tip). <br>
The second line has an integer, <i><b>tip_percent</b></i> (the percentage of <i><b>meal_cost</b></i> being added as tip).   <br>
The third line has an integer, <i><b>tax_percent</b></i> (the percentage of <i><b>meal_cost</b></i> being added as tax).

##Sample Input
<p>
12.00 <br>
20 <br>
8 
</p>

## Sample Output

15 

## Explanation

<code>Given: </code><br>
<i>
meal_cost = 12, tip_percent = 20, tax_percent = 8
</i>

<code>Calculations: </code> <br>
<i>
tip = 12 and 12/100 * 20 = 2.4 <br>
tax = 8 and 8/100 * 20 = 0.96 <br>
total_cost = meal_cost + tip + tax = 12 + 2.4 + 0.96 = 15.36 <br>
round(total_cost) = 15
</i>

We round  to the nearest integer and print the result, <b>15</b> .