"""Multiple Choice Quizzes for Lab 5.
   Creates the actual quiz with specific questions and answers.
   Uses variables to match the questions for easy location, eg Q1.1 is q1_1.
   quiz.py defines question types, must be in same dir, parent dir or path.
   Modified: July 2021
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


def section_seven() -> None:
    """calls all questions in section seven"""
    q7_0 = quiz.quiz_dropdown(
        'What does "w" mean in open()?', ["Open in write mode", "Open in read mode", "Open and wait", "Open with warning"], "Open in write mode",
        rand=True,
    )
    q7_1 = quiz.quiz_dropdown(
        "In which directory has outfile.txt been created?", ["In the same directory as lab04.ipynb", r"In C:\temp", "In lab04.ipynb's parent directory", "In Downloads"], "In the same directory as lab04.ipynb",
        rand=True,
    )
    q7_2 = quiz.quiz_dropdown(
        "What is the size of outfile.txt just now?", ["0 bytes", "1 byte", "1kb", "5kb"], "0 bytes",
        rand=False,
    )
    q7_3 = quiz.quiz_dropdown(
        r"Which code would create outfile.txt in C:\temp, for writing to?",
        [r'open(r"C:\temp\outfile.txt", "w")',
         r'open("C:\temp\outfile.txt", "w")',
         r'open(r"..\..\outfile.txt", "w")'],
        r'open(r"C:\temp\outfile.txt", "w")',
        rand=True,
    )
    quiz.display(q7_0)
    quiz.display(q7_1)
    quiz.display(q7_2)
    quiz.display(q7_3)


def section_eight() -> None:
    """calls all questions in section eight"""
    q8_1 = quiz.quiz_dropdown(
        'getcwd is a', ["function", "class", "instance (variable)", "sub-module"],
        "function",
        rand=True,
    )
    q8_2 = quiz.quiz_dropdown(
        'path is a', ["function", "class", "instance (variable)", "sub-module"],
        "sub-module",
        rand=True,
    )
    q8_3 = quiz.quiz_dropdown(
        'linesep is a', ["function", "class", "instance (variable)", "sub-module"],
        "instance (variable)",
        rand=True,
    )
    q8_4 = quiz.quiz_dropdown(
        'error is a', ["function", "class", "instance (variable)", "sub-module"],
        "class",
        rand=True,
    )
    quiz.display(q8_1)
    quiz.display(q8_2)
    quiz.display(q8_3)
    quiz.display(q8_4)


def section_nine() -> None:
    """calls all questions in section one part one"""
    q9_1 = quiz.quiz_dropdown(
        "Which function in the os module changes directory in the underlying file system?",
        ["os.chdir()", "os.chmod()", "os.getcwd()", "os.listdir()", "os.mkdir()"],
        "os.chdir()",
        rand=True,
    )
    q9_2 = quiz.quiz_dropdown(
        "Which function in the os module shows the current directory in the underlying file system?",
        ["os.chdir()", "os.chmod()", "os.getcwd()", "os.listdir()", "os.mkdir()"],
        "os.getcwd()",
        rand=True,
    )
    q9_3 = quiz.quiz_dropdown(
        "Which function in the os module creates a new directory?",
        ["os.chdir()", "os.chmod()", "os.getcwd()", "os.listdir()", "os.mkdir()"],
        "os.mkdir()",
        rand=True,
    )
    q9_4 = quiz.quiz_dropdown(
        "Which type of object is returned by os.listdir()?",
        ["list", "string", "tuple", "dict"],
        "list",
        rand=True,
    )
    q9_5 = quiz.quiz_dropdown(
        "What are the Windows line separation characters?",
        [r"\r\n", r"\t", r". (a dot)", r"\\"],
        r"\r\n",
        rand=True
    )
    q9_6 = quiz.quiz_dropdown(
        "What is the Windows separation character used in file paths?",
        [r"\r\n", r"\t", r". (a dot)", r"\\"],
        r"\\",
        rand=True
    )
    q9_7 = quiz.quiz_dropdown(
        "What does os.name represent?",
        ["an abbreviated description of the file system", "the user name", "the file name", "something else"],
        "an abbreviated description of the file system",
        rand=True
    )
    quiz.display(q9_1)
    quiz.display(q9_2)
    quiz.display(q9_3)
    quiz.display(q9_4)
    quiz.display(q9_5)
    quiz.display(q9_6)
    quiz.display(q9_7)


def section_eleven() -> None:
    q11_1 = quiz.quiz_dropdown(
        "What does the os.path.dirname() method do?",
        ["It shows the directory part of the path", "It shows the filename part of the path", "It splits the file extension from the rest of the path", "It separates the path and the filename"],
        "It shows the directory part of the path",
        rand=True
    )
    q11_2 = quiz.quiz_dropdown(
        "What does the os.path.basename() method do?",
        ["It shows the directory part of the path", "It shows the filename part of the path", "It splits the file extension from the rest of the path", "It separates the path and the filename"],
        "It shows the filename part of the path",
        rand=True
    )
    q11_3 = quiz.quiz_dropdown(
        "What does the os.path.splitext() method do?",
        ["It shows the directory part of the path", "It shows the filename part of the path", "It splits the file extension from the rest of the path", "It separates the path and the filename"],
        "It splits the file extension from the rest of the path",
        rand=True
    )
    quiz.display(q11_1)
    quiz.display(q11_2)
    quiz.display(q11_3)


def section_twelve() -> None:
    """calls all questions in section four"""
    q12_1 = quiz.quiz_dropdown(
        "What type of object is sys.modules?",
        ["list", "string", "tuple", "dict"],
        "dict",
        rand=True,
    )
    q12_2 = quiz.quiz_checkbox(
        'What are the effects of using "w" as the second argument in open()?',
        ["It opens the file for writing",
         "It opens the file for appending",
         "Previous file contents are kept and added to",
         "Previous file contents are overwritten",
         "It creates the file if it doesn't already exist"],
        ["It opens the file for writing",
         "Previous file contents are overwritten",
         "It creates the file if it doesn't already exist"],
        rand=True,
        arrange="vertical"
    )
    q12_3 = quiz.quiz_dropdown(
        "Why do we use str() in line 4?",
        ["No reason, this could be removed",
         "Trying to write a dict would give an error"
         ],
        "Trying to write a dict would give an error",
        rand=True,
    )
    quiz.display(q12_1)
    quiz.display(q12_2)
    quiz.display(q12_3)


def section_fifteen() -> None:
    """calls all questions in section 15"""
    common_ans = ["1", "14", "19", "26"]
    q15_0 = quiz.quiz_dropdown(
        """How many common passwords are in common3.txt?\n(Or how many common passwords were in the original list called common?)""",
        common_ans,
        "26",
        rand=True,
    )
    q15_1 = quiz.quiz_dropdown(
        "How many common passwords need to be hashed to crack the password '123'?",
        common_ans,
        "1",
        rand=True,
    )
    q15_2 = quiz.quiz_dropdown(
        "How many common passwords need to be hashed to crack the password 'arsenal'?",
        common_ans,
        "14",
        rand=True,
        )
    q15_3 = quiz.quiz_dropdown(
        "If the password you are trying to crack is not in the list of common passwords at all, how many hashes do you need to calculate until you know that it cannot be cracked?",
        common_ans,
        "26",
        rand=True,
    )
    q15_4 = quiz.quiz_checkbox(
        "After the first function call, all the hashes you calculated during the call...?",
        ["...are stored",
         "...can be reused by the next function call",
         "...are discarded",
         "...have to be calculated again for the next function call"],
        ["...are discarded",
         "...have to be calculated again for the next function call"],
        rand=True,
        arrange="vertical"
    )
    q15_5 = quiz.quiz_checkbox(
        'What would happen if you had a much bigger list of common passwords, that contains 10,000 words?',
        ["More hashes could be cracked successfully",
         "Cracking a hash would usually take longer",
         'We "lose even more" when trying to crack more than one hash'
         ],
        ["More hashes could be cracked successfully",
         "Cracking a hash would usually take longer",
         'We "lose even more" when trying to crack more than one hash'
         ],
        rand=True,
        arrange="vertical"
    )
    quiz.display(q15_0)
    quiz.display(q15_1)
    quiz.display(q15_2)
    quiz.display(q15_3)
    print("Our solution from lab 3 or after challenge A above has several function calls as the test cases in main().")
    quiz.display(q15_4)
    quiz.display(q15_5)


def main() -> None:
    """Calls all sections, could be used for a recap quiz at end"""
    section_one()
    section_two()
    # add other section functions here as you make them


# Standard boilerplate code to call the main() function
if __name__ == "__main__":
    main()
