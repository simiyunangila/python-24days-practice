#                                                              Day1
# 1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included)
# .The numbers obtained should be printed in a comma-separated sequence on a single line.

                                                # for loop conditional statement
def make_calculations():
    new_num=[]
    for i in range(2000,3200):
        if (i % 7 == 0) and (i % 5 != 0):
            new_num.append(i)
    return new_num
    
    
    
print (make_calculations())        

# 2.Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line
# .Suppose the following input is supplied to the program: 8 Then, the output should be:40320

                                       # while loop
def factorial(n):
    fact=1
    i=1
    while i<= n:
        fact=fact*i
        i=i+1
    return fact

print(factorial(8))  



# 3.With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1
#  and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
# Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

                                        # for loop

def generate_dictionary(n):
    ans={}
    for i in range(1,n+1):
        ans[i]=i*i
    return ans   

print(generate_dictionary(8))  



                                                 # question4

# Write a program which accepts a sequence of comma-separated numbers from console and generate a
#  list and a tuple which contains every number.Suppose the following input is supplied to the program:


                                                # Question5
# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use init method to construct some parameters

                                                # Question:6
# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:Question:
# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

# Then, the output of the program should be:

                                                    # Question:7
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
                                                     # Question:8
# Suppose the following input is supplied to the program:
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.


                                                            
#                                                             DAY 3
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing allduplicate words and sorting them
#  alphanumerically.


def remove_duplicate_sort(inputss):
    input_string=inputss.split()
    new = []
    for word in input_string:
        if word not in new:
            new.append(word )
    return (" ".join(sorted(new)))



print(remove_duplicate_sort("hello world and practice makes perfect and hello world again"))  


#                                            Question6
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers 
# that are divisible by 5 are to be printed in a comma separated sequence.

def not_divisible_by_5(numbers):
        new_numbers = []
        for num in numbers:
            if num % 5 != 0:
                new_numbers.append(num)
        return new_numbers


print(not_divisible_by_5([1234,5000,3450,1000,3452]))
                        
#                                              Question7
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should 
# be printed in a comma-separated sequence on a single line.    
def even_num():
    new_list=[]
    for num in range(1000-1,3000+1):
        if num % 2 ==0:
            new_list.append(num)
    return new_list

print(even_num())            


#                                          Question8
# Write a program that accepts a sentence and calculate the number of letters and digits.

def calculate_digits_letters(sentence):
    result = {"Letters":0,"Digits":0}
    for i in sentence:
        if i.isdigit():
            result["Digits"] +=1
        elif i.isalpha():
            result["Letters"] +=1
        else:
            pass
    return result        
print(calculate_digits_letters("The fox jumped over the lazy fox")) 


# QUESTION9
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:Hello world!

def case_letters_count(sentence):
    counted={"uppercase":0,"lowercase":0}
    for letter in sentence:
        if letter.isupper():
            counted ["uppercase"] +=1
        elif letter.islower():
            counted["lowercase"] +=1   
        else:
            pass
    return counted
print(case_letters_count("Hello world !!"))            

# question10
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:9

def get_value(a):
    sum= a+a**2+a**3+a**4
    return sum

print( get_value(9) )  

# question11,
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
#  >Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9

def square_odd_number(nums):
    squared = []
    for i in nums:
        if i % 2 != 0:
            squared.append(i*i)
    return squared
print(square_odd_number([ 1,2,3,4,5,6,7,8,9]))    

# Question12
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log 
# format is shown as following:D 300,D 300,W 200,D 100

def net_bank_account(transaction):
    account_balance = 0
    for i  in range(0,len(transaction),2):
        transaction_type,amount = transaction[i],transaction[i+1]
        
        if transaction_type == 'D':
            account_balance += int(amount)
        elif transaction_type =='W':
            account_balance -= int(amount)
        else:
            pass
    return account_balance


print(net_bank_account(['D', 300 ,'D', 300,'W' ,200, 'D ',100]))    

# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345

def check(x):
    cnt = (6 <= len(x) and len(x) <= 12)
    uppercase_found = False
    lowercase_found = False
    numeric_found = False
    special_char_found = False
    
    for i in x:
        if i.isupper():
            uppercase_found = True
        if i.islower():
            lowercase_found = True
        if i.isnumeric():
            numeric_found = True
        if i == '@' or i == '#' or i == '$':
            special_char_found = True
    
    return cnt and uppercase_found and lowercase_found and numeric_found and special_char_found

s = input("Enter a comma-separated list of strings: ").split(',')
lst = filter(check, s)
print(",".join(lst))

# Question:19
# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.

# If the following tuples are given as input to the program:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85



tuples = [
    ('Tom', 19, 80),
    ('John', 20, 90),
    ('Jony', 17, 91),
    ('Jony', 17, 93)
]

# Sort the tuples based on name, age, and score
sorted_tuples = sorted(tuples, key=lambda x: (x[0], x[1], x[2]))

# Print the sorted tuples
for tuple in sorted_tuples:
    print(tuple)