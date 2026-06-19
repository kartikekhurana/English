Vision: English as an executable pseudocode language

Goal :
(1) Allow programmer to write code that reads like strucutred instructions while remaining easy to compile
(2)English source code is transpiled into python and then exectued

--------------------------------------------------------------------------------------------------------------------------------------------
CURRENT EXECUTION PIPELINE:
hello.eng->Output.py->Python Interpretor->Program Output

Ex:
English:
Create Variable age = 21
display age 

Generated python:
age = 21
print(21)

Result : 21

--------------------------------------------------------------------------------------------------------------------------------------------

FUTURE EXECUTION PIPELINE
user.eng->Lexer->Parser->AST->Python Generator->output.py->Python Interpretor->Program.py
--------------------------------------------------------------------------------------------------------------------------------------------

SYNTAX
All blocking open statements ends with a colon

Ex:
if age > 18 :
for loop i from 1 to 100 :
create function takes(a,b)

Blocks are closed using "end" statements
Ex:
end if 
end loop
end function



*******Identation will be used for improving readability******
*******Block termination is controlled by end statement******

VARIABLES:
(1)Mutable variable:
Create variable age = 21
// we can re-assign values by : variable = 22

(2)Immutable variable
Create constant pi = 3.1456
// we cannot re-assign values here

BOOLEAN:
English follows Python Convention : True , False , None


--------------------------------------------------------------------------------------------------------------------------------------------
PRINT AND RETURN STATEMENT:

display age 
display "hello world"

*******Display is the main keyword*******

Return age
return "hello world"

--------------------------------------------------------------------------------------------------------------------------------------------
OPERATIONS
COMPARISON OPERATORS
(1) ==
(2) = 
(3) != 
(4) <
(5) > 
(6) <= 
(7) >= 

LOGICAL OPERATORS
(1) and
(2) or
(3) not

ARTHEMATIC OPERATORS
(1) +
(2) - 
(3) * 
(4) /
(5) %

--------------------------------------------------------------------------------------------------------------------------------------------
ARRAYS:
Array Creation:
create array nums = [1,2,3,4]

Empty Array:
create array nums = []

Accessing elements:
nums of i -> generated python -> nums[i]

Ex : 
display nums of i -> generated python -> print(nums[i])

Assignment of elements:
nums of 0 = 100 -> generated python -> nums[0] = 100

Length of array:
length(nums)

operations:
Append: Append 5 to nums
Remove: remove 5 from nums
Insert: insert 10 at 2 in nums
Pop : pop nums
clear : clear nums

--------------------------------------------------------------------------------------------------------------------------------------------
CODITIONAL STATEMENTS:
If 
else if 
if
end if

--------------------------------------------------------------------------------------------------------------------------------------------
LOOPS:
Ex:
For : for loop i from <first value> to <second value>
While : while loop <condition> 

--------------------------------------------------------------------------------------------------------------------------------------------
Function:
Ex :  create a function name sum which takes a , b as parameters
Declartion : create function sum takes(a,b):
ending : end function 

//how to call the function
Function call -> sum(5,10)

