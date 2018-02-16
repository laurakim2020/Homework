import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
      """
    print("")

    print("tests for Problem 7")
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")

    print("tests for Problem 8")
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")


#Problem2
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    print(letter + suffix)

#Problem 3
def count_letters(fruit,letter):
    count = 0
    for char in fruit:
        if char == letter:
            count += 1
    print(count)
count_letters("banana","a")

#Problem 4
def find(strng, ch, start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

#Problem 6
layout = "{0:>10}{1:>2}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>4}{13:>5}"

print (layout.format("", "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
print(layout.format("", ":", "------", "-----", "------", "------", "------", "------", "------","------",
                    "------", "-----", "----", ""))
for i in range(1,13) :
    print(layout.format(i, ":", i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))

#Problem 7
def reverse(word):
    backwards = word[::-1]
    return backwards

#Problem 8
def mirror(word):
    reverse = word[::-1]
    return word + reverse

test_suite()