# ? == 0 or 1 instance
# + == 1 or more instances
# () == grouping or including
# {1,5} == 1 to 5 times of instances
# {5} == 5 instances

# [a-z] == a letter from a to z, a range
# [a-z][a-z] == two letters next to each other
# \d or [0-9] == a digit
# \w == a number or a character [a-zA-Z0-9]

# . == any thing
# ^ == except
import re


def reg_exp(str1):
    for x in str1:
        flag = 0
        text = " matches the pattern: "
        if re.match(r'[0-9]+$', x):
            print(x + text + "An integer")
            flag = 1
        if re.match(r'[0-9]+\.[0-9]+', x):
            print(x + text + "A float consists of 1 or more digits before and after decimal point")
            flag = 1
        if re.match(r'[0-9]+\.[0-9]{2}', x):
            print(x + text + "A float with exactly 2 digits after the decimal point")
            flag = 1
        if re.match(r'[0-9]+\.[0-9]+(f)', x):
            print(x + text + "A float end with letter f (4.321f)")
            flag = 1
        if re.match(r'[A-Z]+[a-z]+[0-9]', x):
            print(x + text + "Capital letters, followed by small case letters, followed by digits")
            flag = 1
        if re.match(r'[0-9]{3}[a-zA-z]{2,}', x):
            print(x + text + "Exactly 3 digits, followed by at least 2 letters")
            flag = 1
        if flag == 0:
            print(x + " Does not match any pattern")

def remove_str(str1):
    pattern = r'\d+'
    pos = re.match(r'\d+', str1)
    result = re.sub(pattern,'',str1)
    print(pos)
    print("Found integer",pos.group(),"at the beginning of this string, starting at index",pos.start(),"ending in index",pos.end(),"The rest of the string is "+result)

        # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reg_exp(["22.11", "23", "66.7f", "123abcde", "Case44", "Happy", "78", "66.7", "yes123", "Book111"])
    remove_str("22 street")
    remove_str("90years")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
