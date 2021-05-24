import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from pass_lib import passme_hash

YES = "It is possible that your password has been filtered.\n"
NO = "Your password has not been filtered yet.\n"
SHORT = "Invalid Hash, please use a prefix of at least 5 characters.\n"


def test_myoutput(capsys):
    passme_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("7c4a8d09ca3762af61e59520943dc26494f8941b")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("b1b3773a05c0ed0176787a4f1574ff0075f7521e")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("6367c48dd193d56ea7b0baad25b19455e529f5ee")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("ee8d8728f435fd550f83852aabab5234ce1da528")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("e38ad214943daad1d64c102faec29de4afe9da3d")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("b0399d2029f64d445bd131ffaa399a42d2f8e7dc")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("bfe54caa6d483cc3887dce9d1b8eb91408f1ea7a")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("50d8b4a941c26b89482c94ab324b5a274f9ced66")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("e0cd4a54a95218a910e28ee40b68999bed9ce743")
    captured = capsys.readouterr()
    assert captured.out == YES

    passme_hash("e2354f034d5e7cf261e9e26b80208e2651600628")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("25989ae31363a2d961716bd817a619ebd92d555d")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("f4dbf94265df9d8a9dc4e80ff79538799fbc4c3e")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("52e280bbd03f31cc30f0063ec708990af7c7240b")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("3bfd4fdbb75e5060dcd994f079e6d6386779f022")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("8b04ab3f6779b94d0a396168719b132e0bd2d67a")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("fa713e56c2acf537e82f18aacb75a0df8eb96a13")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("47d2a592472eac013f7a16b6573f8da5e0aa71c5")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("5583a616f691c18ae14c69f9c6914bc031b2c34c")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("f7c3bc1d808e04367adf679965ccc34ca7ae3441")
    captured = capsys.readouterr()
    assert captured.out == NO

    passme_hash("213")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("wqe2")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("312e")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("21wd")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("32t")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("grxc")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("zsdc")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("56hr")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("&$Gt")
    captured = capsys.readouterr()
    assert captured.out == SHORT

    passme_hash("23WE")
    captured = capsys.readouterr()
    assert captured.out == SHORT
