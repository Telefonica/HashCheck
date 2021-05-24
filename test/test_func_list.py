import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from pass_lib import passme_file

YES = "It is possible that your password has been filtered.\n"
NO = "Your password has not been filtered yet.\n"


def test_myoutput(capsys):
    passme_file("lines.txt")
    captured = capsys.readouterr()
    assert YES in captured.out or NO in captured.out
