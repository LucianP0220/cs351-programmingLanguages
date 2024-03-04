#Python lab 1
#Learn from the online interactive tutorial and finish below tasks
#You can edit in this file by filling blanks after each question.
#Submit the .py file for your own reference
#This practice is graded only on submission. 
#It will help you to get started on Python for the homework

#####
#Example function
#####
def example(): #def is function definition
    print("I am the example code")
#Now, go to the end of this file and you will find the main function & how to run your code there
#Around line #94


#####
#1. function in python
####

def printHello(): #Remove the # at the begining of this line.
    print("Hello World")
    #tab is IMPORTANT in python. tab in python replaces {} in C++
    #print string hello world. One line of code here. Make sure it is indented to show it belongs to this function


#####
#2. variable definition in python
#####

def someVars():
    #define a few integer and float numbers, add them together and print result out
    my_int = 2
    my_float = 2.0
    total_sum = my_int + my_float
    print(total_sum)
#call the function to run it in the main function at the end of the file

#####
#3. define a list in python
#####

def mylis():
    #define a list with 5 numbers, print it out
    mylis = [2, 4, 6, 8, 9]
    for x in mylis:
        print(x)
    #define an empty list and append a few numbers into it, then print it out
    mylist = []
    mylist.append(1)
    mylist.append(3)
    mylist.append(5)
    mylist.append(7)
    mylist.append(9)
    for x in mylist:
        print(x)
#call your mylis func to execute in the main function at the end of the file

#####
#4. string output
#####

def printstr(input_str1, input_int1):
    #convert int into string and append the int with the string to form a long string
    #(technical googling practice -- google what func to use)
    #print the long str out
    print(input_str1 + str(input_int1))

#In the main function, define an input string and an input int.
#Pass them in as parameters to the function. Call and run the function to see results.

####
#5. passing var to func and return
####

def funcvars(inputvar1, inputvar2):
    #add the input numbers together
    #returen the result
    return inputvar1 + inputvar2
#Define the input variables in main, pass them into the function.
#In main, use a result variable to receive the result from funcvars and print the result out

####
#6. for loop
####

def go_over_list(mylis):
    #use for loop to go over the input list and print out items one by one
    for x in mylis:
        print(x)

def go_over_list1():
    #use for loop to directly print out numbers from 10 to 17
    for x in range(10, 18):
        print(x)

def go_over_list2(mylis):
    #use for loop & go over your list
    for x in mylis:
    #multiply 2 to every item in your list, print results out
        print(2 * x)
def go_over_list3(mylis):
    #create an empty list resLis
    reLis = []
    #go over items in the input list, multiply 2 to every item
    for x in mylis:
        reLis.append(2 * x)
    return reLis
    #add result one by one to resLis
    #return resLis

#Call all the functions in main. Provide necessary inputs to the functions.
#For those with return values, print the return values out in main.

####
#7. while loop
####
def while_list(mylis):
    count = 0
    while count < 1:
        for x in mylis:
            print(x)
        count += 1

def while_list1():
    count = 10
    while count < 18:
        print(count)
        count += 1

def while_list2(mylis):
    count = 0
    while count < 1:
        for x in mylis:
            print(2 * x)
        count += 1

def while_list3(mylis):
    reLis = []
    count = 0
    while count < 1:
        for x in mylis:
            reLis.append(2 * x)
        count+= 1
        return reLis
#do all the problems in 6 using while loop instead


#####
#Here is the main function
#You can have only 1 main function in 1 script
#Left click on the green arrow next to the line number of the line of the main function definition
#Your code would run.
if __name__ == '__main__': #a quick way to type this line is: type "main" and then tab
    print("****Question 1****")
    printHello()
    print("****Question 2****")
    someVars()
    print("****Question 3****")
    mylis()
    print("****Question 4****")
    printstr("The number ", 2)
    print("****Question 5****")
    result = funcvars(1, 2)
    print(result)
    print("****Question 6****")
    mylis = [1, 2, 3, 4, 5]
    go_over_list(mylis)
    print("------")
    go_over_list1()
    print("-----")
    go_over_list2(mylis)
    print("-----")
    reLis = go_over_list3(mylis)
    for x in reLis:
        print(x)
    print("****Question 7****")
    while_list(mylis)
    print("-----")
    while_list1()
    print("-----")
    while_list2(mylis)
    print("-----")
    reLis = while_list3(mylis)
    for x in reLis:
        print(x)
    #you can start call and run your functions here


######
#Python is an easier PL to learn than C++ and looks like C++
#From this lab experience, reflect and summary what it feels like
#when you are learning a new PL that is similar to a PL that you already know?
#Your answer here:

#In this case, when you want to learn a new PL that looks like a PL that you already know,
#how can you learn the new PL quickly? Any steps?
#Your answer here:
