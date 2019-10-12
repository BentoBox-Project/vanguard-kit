from vanguard_kit import create_html_tree, calcuate_html_tree_distance


def test_calculate_the_realistic_difference_between_a_b():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_b.html") as example_b:
            a_tree = create_html_tree(example_a)
            b_tree = create_html_tree(example_b)
            assert calcuate_html_tree_distance(a_tree, b_tree) > 0
            assert calcuate_html_tree_distance(a_tree, b_tree) > 5
            assert calcuate_html_tree_distance(a_tree, b_tree) < 10


def test_calculate_distance_between_navbars_a_and_b():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_b.html") as example_b:
            a_tree = create_html_tree(
                example_a,
                specific_tag="nav",
                class_="navbar navbar-default"
            )
            b_tree = create_html_tree(
                example_b,
                specific_tag="nav",
                class_="navbar navbar-default"
            )
            assert calcuate_html_tree_distance(a_tree, b_tree) > 5
            assert calcuate_html_tree_distance(a_tree, b_tree) == 9


def test_calculate_distance_between_main_div_a_and_b():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_b.html") as example_b:
            a_tree = create_html_tree(
                example_a,
                specific_tag="div",
                class_="main-div"
            )
            b_tree = create_html_tree(
                example_b,
                specific_tag="div",
                class_="main-div"
            )
            assert calcuate_html_tree_distance(a_tree, b_tree) == 0


def test_calculate_distance_between_footers_a_and_b():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_b.html") as example_b:
            a_tree = create_html_tree(example_a, specific_tag="footer")
            b_tree = create_html_tree(example_b, specific_tag="footer")
            assert calcuate_html_tree_distance(a_tree, b_tree) == 0
