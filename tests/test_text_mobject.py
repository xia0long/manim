import pytest

from manim import RED, Text


def get_color(mobject):

    return mobject.get_color().get_hex()


def test_set_color_by_t2c():
    """Test Text.set_color_by_t2c()."""
    text = Text(
        "Cherry Blossoms in Spring", disable_ligatures=False, t2c={"Spring": RED}
    )
    assert all(get_color(c) == RED.lower() for c in text.submobjects[-6:])

    text.disable_ligatures = True
    assert all(get_color(c) == RED.lower() for c in text.submobjects[-6:])

    text2 = Text(
        "Cherry Blossoms in Spring", disable_ligatures=False, t2c={"Blossoms in": RED}
    )
    assert all(get_color(c) == RED.lower() for c in text2.submobjects[7:16])

    text2.disable_ligatures = True
    assert all(get_color(c) == RED.lower() for c in text2.submobjects[7:16])

    text3 = Text(
        "Cherry Blossoms in Spring Cherry Blossoms in Spring",
        disable_ligatures=False,
        t2c={"in Spring": RED},
    )
    assert all(get_color(c) == RED.lower() for c in text3.submobjects[-8:])
    assert all(get_color(c) == RED.lower() for c in text3.submobjects[14:22])

    text3.disable_ligatures = True
    assert all(get_color(c) == RED.lower() for c in text3.submobjects[-8:])
    assert all(get_color(c) == RED.lower() for c in text3.submobjects[14:22])
