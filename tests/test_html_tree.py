from vanguard_kit import create_html_tree
from vanguard_kit import VanguardNode


def test_create_html_tree():
    with open("tests/html_examples/example_a.html") as example_a:
        tree = create_html_tree(example_a)
        assert type(tree) is VanguardNode


def test_create_html_with_specifig_tag():
    with open("tests/html_examples/example_a.html") as example_a:
        tree = create_html_tree(example_a, specific_tag="div")
        assert tree is not None
        assert tree.label == "div"
        assert tree.children


def test_create_html_with_specifig_class_attr():
    with open("tests/html_examples/example_a.html") as example_a:
        tree = create_html_tree(
            html_file=example_a,
            specific_tag="div",
            class_="main-div"
        )
        assert tree is not None
        assert "class" in tree.attrs
        assert tree.children


def test_create_html_with_specifig_id_attr():
    with open("tests/html_examples/example_a.html") as example_a:
        tree = create_html_tree(
            html_file=example_a,
            specific_tag="div",
            id="super-div"
        )
        assert tree is not None
        assert "id" in tree.attrs
        assert tree.children
