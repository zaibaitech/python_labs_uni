"""Multiple Choice Quizzes.
   This "Master" script defines the available question types.
   Use a separate file to create an actual quiz with specific questions
   and answers. In that file, import quiz and use variables to match the
   questions for easy location, eg Q1.1 should be q1_1.
   Modified: July 2021
"""
# Modified from:
# https://github.com/jupyter-widgets/ipywidgets/issues/2487#issuecomment-510721436
# Checkbox help from: https://stackoverflow.com/a/64290695
# other help and ideas from
# https://github.com/jupyter-widgets/ipywidgets/issues/2396
# https://stackoverflow.com/questions/50605029/how-to-reduce-the-space-occupied-by-an-ipywidget-checkbox-below-100px
# https://minrk-ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html

import random
from typing import List, Any
import ipywidgets as widgets
import IPython.display as dis


display = dis.display


def quiz_radio(description: str,
               options: List[str],
               correct_answer: str,
               rand: bool = True) -> str:
    """Creates radio buttons for multiple choice questions.
       The optional parameter rand controls whether to randomize the answers,
       rand=True is default; use rand=False to stop randomisation.
    """
    if correct_answer not in options:
        # adds correct answer to end if it isnt in the options
        options.append(correct_answer)
    correct_answer_index = options.index(correct_answer)

    # count of how many buttons needed
    radio_options = [(words, i) for i, words in enumerate(options)]

    # shuffle if "random"
    if rand:
        random.shuffle(radio_options)

    # creates the radio buttons
    alternativ = widgets.RadioButtons(
        options=radio_options, description="", disabled=False, value=None
    )

    description_out = widgets.Output()
    with description_out:
        print(description)
    feedback_out = widgets.Output()

    def check_radio(_selection: Any) -> None:
        """Checks if an answer is correct"""
        # selection prefixed with underscore to disable pylint warning
        # apparently unused but code breaks if removed
        ans = int(alternativ.value)
        if ans == correct_answer_index:
            response = "Correct! :-)"
        else:
            response = "Try Again :-("
        with feedback_out:
            dis.clear_output()
            print(response)

    check = widgets.Button(description="submit")
    check.on_click(check_radio)

    return widgets.VBox([description_out, alternativ, check, feedback_out])


def quiz_checkbox(description: str,
                  options: List[str],
                  correct_answer: List[str],
                  rand: bool = True,
                  arrange: str = "horizontal") -> str:
    """Creates checkboxes for multiple answer questions.
       The optional parameter random controls whether to randomize the answers,
       rand=True is default; use rand=False to stop randomisation.
       The optional parameter arrange controls whether display direction.
       arrange="horizontal" is default, use arrange="vertical" to override.
    """
    # setting the correct answer(s)
    correct_answer_index = []
    for ans in correct_answer:
        if ans not in options:
            options.append(ans)
    if rand:
        # shuffle the answers
        random.shuffle(options)
    for ans in correct_answer:
        correct_answer_index.append(options.index(ans))
    correct_answer_index.sort()

    # create the checkboxes
    checkboxes = [widgets.Checkbox(value=False, description=label,
                                   indent=False)
                  for label in options]
    if arrange == "vertical":
        output = widgets.VBox(children=checkboxes)
    elif arrange == "horizontal":
        output = widgets.HBox(children=checkboxes,
                              layout=widgets.Layout(width="850px",
                                                    height="50px"))

    description_out = widgets.Output()
    with description_out:
        print(description)
    feedback_out = widgets.Output()

    def check_checkbox(_selection) -> None:
        """Checks if a checkbox answer is correct"""
        child_val = -1
        child_index = []
        # finds the checkbox index
        for child in output.children:
            child_val += 1
            if child.value:
                child_index.append(child_val)
        # checks the index of selected answer and correct answer match
        if child_index == correct_answer_index:
            response = "Correct! :-)"
        else:
            response = "Try Again :-("
        with feedback_out:
            dis.clear_output()
            print(response)

    check = widgets.Button(description="submit")
    check.on_click(check_checkbox)

    return widgets.VBox([description_out, output, check, feedback_out])


def quiz_dropdown(description: str,
                  options: List[str],
                  correct_answer: str,
                  rand: bool = True) -> str:
    """Creates a drop-down box for multiple choice questions.
       The optional rand parameter controls whether to randomize the answers,
       use rand=True (default) or rand=False to stop randomisation.
    """
    if correct_answer not in options:
        # adds correct answer to end if it isnt in the options
        options.append(correct_answer)
    correct_answer_index = options.index(correct_answer)

    # count of how many buttons needed
    radio_options = [(words, i) for i, words in enumerate(options)]

    if rand:
        random.shuffle(radio_options)

    # creates the radio buttons
    alternativ = widgets.Dropdown(options=radio_options,
                                  description="",
                                  disabled=False,
                                  value=None)

    description_out = widgets.Output()
    with description_out:
        print(description)
    feedback_out = widgets.Output()

    def check_radio(_selection: Any) -> None:
        """Checks if an answer is correct"""
        ans = int(alternativ.value)
        if ans == correct_answer_index:
            response = "Correct! :-)"
        else:
            response = "Try Again :-("
        with feedback_out:
            dis.clear_output()
            print(response)

    check = widgets.Button(description="submit")
    check.on_click(check_radio)

    return widgets.VBox([description_out, alternativ, check, feedback_out])
