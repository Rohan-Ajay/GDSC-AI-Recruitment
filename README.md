# GDSC-AI-Recruitment
Solutions to challenges given in the first phase of recruitment for AI department in GDSC.

## Question 1 :
 Implement a function StringManipulation(str), that accepts a string as the str parameter and performs the following operations on it:
 
 Every letter in the string should be changed to its succeeding alphabet (ie., c becomes d, z becomes a). Numbers are left unchanged. (Hint: lists can be used)
 
 The string is inverted after removing all vowels. (Reminder: Don’t alter the alphabets’ case)
 The string has every alternate character from the original string (e.g. for an input “abcdefg”, the output string would be “aceg”)
 Print every output separately and label them appropriately. You must use python to solve this question.
 
## Solution 1 :

![image](https://user-images.githubusercontent.com/113159416/189270953-884318d9-7949-4b11-9445-ffaa903bbb7e.png)

## Question 2 :
 Use the linked Titanic dataset to answer the following questions using python code:
 
 Display only the numeric columns.
 Remove the null values from column ‘Age’, ‘Fare’.
 Replace the null values of ‘Age’ and ‘Fare’ with the column mean.
 
## Solution 2 :
 
 ### The Dataset :
  
  ![image](https://user-images.githubusercontent.com/113159416/189271472-bb665a7e-7166-40c3-a3ea-ef7a97273623.png)

 ### Task-1 : Display only the numeric columns
  
  ![image](https://user-images.githubusercontent.com/113159416/189271632-6403d85e-8faf-416f-8e6b-5c6780ce5e2f.png)
  
  **(NOTE : Observe Row-88. Here, the column 'Age' bears a Null value)**
 
 ### Task-2 : Remove the null values from column ‘Age’, ‘Fare’
  
  ![image](https://user-images.githubusercontent.com/113159416/189271931-c29b4d9f-b1b4-43a1-93ca-8a693fe283e3.png)
  
  **(NOTE : The Row-88 is deleted as 'Age' bears a Null value)**
  
 ### Task-3 : Replace the null values of ‘Age’ and ‘Fare’ with the column mean
  
  ![image](https://user-images.githubusercontent.com/113159416/189271965-5e2ee7e4-f18f-4207-b8a0-2c4b17edf829.png)

  **(NOTE : Observe Row-88. Previously, the column 'Age' held Null value. Now, it holds the mean value.)**

