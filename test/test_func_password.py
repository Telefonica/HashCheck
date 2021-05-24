import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from pass_lib import passme_password

YES = "It is possible that your password has been filtered.\n"
NO = "Your password has not been filtered yet.\n"


def test_myoutput(capsys):
    passme_password("password")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("123456")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("123456789")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("987654321")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("qwerty")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("qwertyuiop")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("password1")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("iloveyou")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("admin")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("1q2w3e4r")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_password("·$%$·%&$%/TERT%TFG·$")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_password("%$&EYSERIAERIA%=Psfiiosen")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_password("dj983hn3·$F·$$)F·$)FSEFBUESYF$))$%)()")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_password("MSADDSAOIDSAD)ADUE$(RHSDFKNASDJAS")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_password("!!ª!ª!=$·)FHWEUFH·$WR((EHUFefnesfiyeuebrf")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_password("??¿R¿RSEÑ¨:_;F;SELFOSEJFD")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_password("_:;EMFIESNFKIESHDFOPERO·)$·NKL")
    captured = capsys.readouterr()
    assert captured.out == NO
