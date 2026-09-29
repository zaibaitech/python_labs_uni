"""Multiple Choice Quizzes for Lab 3.
   Creates the actual quiz with specific questions and answers.
   Uses variables to match the questions for easy location, eg Q1.1 is q1_1.
   quiz.py defines question types, must be in same dir, parent dir or path.
   Modified: July 2021, Sept 2023
"""
# hack to allow import from parent directory
# from https://codeolives.com/2020/01/10/python-reference-module-in-parent-directory/
# next line disables pylint comment about import order, noqa is for pycodestyle
# pylint: disable=C0413
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import quiz  # noqa: E402


def section_one_one() -> None:
    """calls all questions in section one part one"""
    q1_6 = quiz.quiz_dropdown(
        "Which method outputs only the values of a dictionary?",
        [".values()", ".items()", ".descriptions()", ".strings()", ".keys()"],
        ".values()",
        rand=True,
    )
    q1_7 = quiz.quiz_dropdown(
        "with .keys(), what type of data structure is the result? (Use the type() function)",
        ["dict_keys", "dict_values", "dict_string", "dict_items"],
        "dict_keys",
        rand=True,
    )
    q1_8 = quiz.quiz_dropdown(
        "With .items(), what type of data structure is output for each key: value pair?",
        ["dict_items", "dict_string", "dict_object", "dict_lists"],
        "dict_items",
        rand=True
    )
    quiz.display(q1_6)
    quiz.display(q1_7)
    quiz.display(q1_8)

    

def section_one_three() -> None:
    """calls all questions in section one three"""
    q1_9 = quiz.quiz_dropdown(
        "How many items in dic?", ["3", "6", "4", "8"], "3",
        rand=True,
    )
    q1_10 = quiz.quiz_dropdown(
    "Why not six?", ["Only keys are counted.", "Only the values are counted.", "The keys and the values are counted.", "None of the above."],
    "Only keys are counted.",
    rand=False,
    )
    quiz.display(q1_9)
    quiz.display(q1_10)

    
    
def section_three() -> None:
    """calls all questions in section three"""
    q3_1 = quiz.quiz_dropdown(
        "Which list is used for the keys in dic1? Which list is for the values? (english or french)", ["When using the zip function, the first argument is the key (english) and the second is the value (french).", "When using the zip function, the first argument is the key (french) and the second is the value (english).", "When using the zip function, the second argument is the key (english) and the first is the value (french).", "When using the zip function, the first argument is the value (english) and the second is the key (french)."], "When using the zip function, the first argument is the key (english) and the second is the value (french).",
        rand=True,
    )
    q3_2 = quiz.quiz_dropdown(
        "What is a dictionary?",
        ["A dictionary is a collection which is mutable and indexed.",
         "A dictionary is a collection which is immutable and indexed.",
         "A dictionary is a collection which is immutable and not indexed.",
         "A dictionary is a collection which is mutable but not indexed."],
        "A dictionary is a collection which is mutable and indexed.",
        rand=True,
    )
    q3_3 = quiz.quiz_dropdown(
        "What does the dict() function do?", ["The dict() function turns something into a dictionary.", "The dict() function turns something into a list.", "The dict() function turns something into a tuple.", "The dict() function turns something into a string."], "The dict() function turns something into a dictionary.",
        rand=True,
    )
    q3_4 = quiz.quiz_dropdown(
        "What happens if you omit dict from the command?", ["If zip() is used without dict(), it creates tuples based on the lists.", "If zip() is used without dict(), it creates a zip object.", "If zip() is used without dict(), it creates strings based on the lists.", "If zip() is used without dict(), it creates tuples based on the strings."], "If zip() is used without dict(), it creates a zip object.",
        rand=True,
    )
    quiz.display(q3_1)
    quiz.display(q3_2)
    quiz.display(q3_3)
    quiz.display(q3_4)


def section_six() -> None:
    """calls all questions in section six"""
    q6_1 = quiz.quiz_dropdown(
        "When does the while loop end?", ["Never", "When the user enters 0", "When the user doesn't enter anything for a while", "When the user enters -1"], "When the user enters 0",
        rand=True,
    )
    q6_2 = quiz.quiz_checkbox(
        "Why do we set reply=True before the start of the loop?\nChoose all correct options.", ["reply must be True for the loop to start", "this line is not necessary, could be removed", "an exception is raised if reply is not defined"], ["reply must be True for the loop to start", "an exception is raised if reply is not defined"],
        rand=True,
        arrange="vertical"
    )
    q6_3 = quiz.quiz_dropdown(
        "Why do we write while reply: and not while reply == True:?", ["No reason - both work equally", "The conditions are the same, but while reply: is shorter", "while reply == True: would not work"], "The conditions are the same, but while reply: is shorter",
        rand=True,
    )
    quiz.display(q6_1)
    quiz.display(q6_2)
    quiz.display(q6_3)


def section_seven_one() -> None:
    """calls all questions in section eight one"""
    q7_1 = quiz.quiz_dropdown(
        "Which type of object is passwords?", ["_io.TextIOWrapper", "str", "bool", "_sitebuiltins._Helper"], "_io.TextIOWrapper",
        rand=True,
    )
    q7_2 = quiz.quiz_dropdown(
        'What does "r" mean in open()?', ["Open in read mode", "Open for regex", "Open to run", "Open to re-edit"], "Open in read mode",
        rand=True,
    )
    quiz.display(q7_1)
    quiz.display(q7_2)
    
    
    
def section_seven_two() -> None:
    """calls all questions in section eight two"""
    q7_3 = quiz.quiz_dropdown(
        "Which of these methods reads content from the file object?", [".read()", ".open()", ".remove()", ".append()"], ".read()",
        rand=True,
    )
    q7_4 = quiz.quiz_dropdown(
        "Which of these methods reads a single line from the file object and returns a string?", [".readline()", ".read()", ".parse()", ".open()", ".readlines()"], ".readline()",
        rand=True,
    )
    quiz.display(q7_3)
    quiz.display(q7_4)


def section_ten_one() -> None:
    """calls all questions in section five"""
    q10_1_1 = quiz.quiz_dropdown(
        "What type of brackets do we use for tuples?", ["()","{}","[]","<>"], "()",
        rand=True,
    )
    q10_1_2 = quiz.quiz_dropdown(
        "What type of brackets do we use for lists?", ["[]","{}","()","<>"], "[]",
        rand=True,
    )
    q10_1_3 = quiz.quiz_dropdown(
        "What type of brackets fo we use for dictionaries?", ["{}","()","[]","<>"], "{}",
        rand=True,
    )
    quiz.display(q10_1_1)
    quiz.display(q10_1_2)
    quiz.display(q10_1_3)
    
    
    
def section_ten_two() -> None:
    """calls all questions in section five"""
    q10_2 = quiz.quiz_dropdown(
        "What happens if you run the code above?", ["An error is displayed for the last line of code.","4 lines of code are printed.","An error stops the code running.", "An error is displayed after one line of code is run."], "An error is displayed for the last line of code.",
        rand=True
    )
    q10_3 = quiz.quiz_dropdown(
        "Why has an exception been raised?", ["Expecting 2 variables, received 3.","Expecting 3 variables, received 2.","Expecting 4 variables, received 3.","Expecting 4 variables, received 2."], "Expecting 2 variables, received 3.",
        rand=True
    )
    quiz.display(q10_2)
    quiz.display(q10_3)
    
    
def section_ten_three() -> None:
    """calls all questions in section five"""
    q10_5 = quiz.quiz_dropdown(
        "Did this work?", ["Value error expected 2 to unpack","Value error expected 4 to unpack","Value error expected 1 to unpack","Value error expected 6 to unpack"], "Value error expected 2 to unpack",
        rand=True
    )
    q10_6 = quiz.quiz_dropdown(
        "What is the problem?", ["The tuple were trying to assign results to has a length of 2. It can only handle one variable on top of the password.","The tuple we are trying to assign results to has a length of 3. It can only handle one variable on top of the password.","The tuple we are trying to assign results to has a length of 1. It can only handle one variable on top of the password."], "The tuple were trying to assign results to has a length of 2. It can only handle one variable on top of the password.",
        rand=True
    )
    quiz.display(q10_5)
    quiz.display(q10_6)
    
    
def section_twelve_one() -> None:
    """calls all questions in section five"""
    q12_5 = quiz.quiz_dropdown(
        "What is the length of the hash signature generated?", ["8 characters","16 characters","32 characters","64 characters"], "32 characters",
        rand=False
    )
    q12_6 = quiz.quiz_dropdown(
        "Compare this with the length of the hash of your name. What do you find?", ["The hashes are the same length","They differ in size hugely","They differ in size slightly"],"The hashes are the same length",
        rand=True
    )
    q12_7 = quiz.quiz_dropdown(
        "What would be the length of the MD5 hash signature generated for this entire lab sheet?", ["8 characters","16 characters","32 characters","64 characters"], "32 characters",
        rand=False
    )
    q12_8 = quiz.quiz_dropdown(
        "What dictates the length of a hash signature?", ["The hashing algorithm used","The length of the input","The type of input (password, document, ...)","The tool used to calculate the hash (Python, Linux, ...)"], "The hashing algorithm used",
        rand=True
    )
    quiz.display(q12_5)
    quiz.display(q12_6)
    quiz.display(q12_7)
    quiz.display(q12_8)
    
    
    
def section_thirteen_one() -> None:
    """calls all questions in section thirteen - regular hashes without further implementation"""
    hash_ans = ["(Password not recovered)", "letmein", "123123", "starwars"]
    q13_1 = quiz.quiz_dropdown(
        "What is the password for '4297f44b13955235245b2497399d7a93'?",
        hash_ans,
        "123123",
        rand=True,
    )
    q13_2 = quiz.quiz_dropdown(
        "What is the password for '4297f44b13955235245b2497399d7a92'?",
        hash_ans,
        "(Password not recovered)",
        rand=True,
    )
    q13_3 = quiz.quiz_dropdown(
        "What is the password for '5badcaf789d3d1d09794d8f021f40f0e'?",
        hash_ans,
        "starwars",
        rand=True,
    )
    q13_4 = quiz.quiz_dropdown(
        "What is the password for '0d107d09f5bbe40cade3de5c71e9e9b7'?",
        hash_ans,
        "letmein",
        rand=True,
    )
    q13_5 = quiz.quiz_dropdown(
        "What is the password for '5c916794deca0f7c3eeaee426b88f8bd'?",
        hash_ans,
        "(Password not recovered)",
        rand=True,
    )   
    quiz.display(q13_1)
    quiz.display(q13_2)
    quiz.display(q13_3)
    quiz.display(q13_4)
    quiz.display(q13_5)


def section_thirteen_two() -> None:
    """calls all questions for cracking upper case passwords"""
    upper_ans = ["(Password not recovered)", "BATMAN", "MONTYPYTHON", "ARSENAL"]
    q13_6 = quiz.quiz_dropdown(
        "What is the password for '5c916794deca0f7c3eeaee426b88f8bd'?",
        upper_ans,
        "MONTYPYTHON",
        rand=True,
    )   
    q13_7 = quiz.quiz_dropdown(
        "What is the password for 'ab5d903c26acf41bdcd246e212a59fad'?",
        upper_ans,
        "ARSENAL",
        rand=True,
    )
    quiz.display(q13_6)
    quiz.display(q13_7)


def section_thirteen_three() -> None:
    """calls all questions for cracking capitalised passwords"""
    cap_ans = ["(Password not recovered)", "Cheese", "Montypython", "Starwars"]
    q13_8 = quiz.quiz_dropdown(
        "What is the password for 'a67778b3dcc82bfaace0f8bc0061f20e'?",
        cap_ans,
        "Cheese",
        rand=True,
    )   
    q13_9 = quiz.quiz_dropdown(
        "What is the password for '1e2c72aded7b120573ec8d5e40e44b0d'?",
        cap_ans,
        "Starwars",
        rand=True,
    )
    q13_10 = quiz.quiz_dropdown(
        "What is the password for '4297f44b13955235245b2497399d7a92'?",
        cap_ans,
        "(Password not recovered)",
        rand=True,
    )
    quiz.display(q13_8)
    quiz.display(q13_9)
    quiz.display(q13_10)

    
    
def main() -> None:
    """Calls all sections, could be used for a recap quiz at end"""
    section_one_one()
    section_three()
    # add other section functions here as you make them


# Standard boilerplate code to call the main() function
if __name__ == "__main__":
    main()
