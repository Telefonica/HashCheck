import sys
import os
import random
import string
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from pass_lib import passme_password

YES = "It is possible that your password has been filtered.\n"
NO = "Your password has not been filtered yet.\n"
SRT = "Invalid Hash, please use a prefix of at least 5 characters.\n"


def test_myoutput(capsys):
    for _ in range(150):
        passme_password(''.join(random.choices(string.ascii_uppercase
                        + string.digits, k=100)))
        captured = capsys.readouterr()
        assert captured.out == YES or captured.out == NO

    for _ in range(150):
        n = random.randint(0, 100)
        passme_password(''.join(random.choices(string.ascii_uppercase
                        + string.digits, k=n)))
        captured = capsys.readouterr()
        assert captured.out == YES or captured.out == NO or captured.out == SRT
