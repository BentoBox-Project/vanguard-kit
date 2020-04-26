from vanguardkit import calcuate_html_tree_distance, create_html_tree


def test_calculate_the_realistic_difference_between_a_c():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_c.html") as example_c:
            a_tree = create_html_tree(example_a)
            c_tree = create_html_tree(example_c)
            assert calcuate_html_tree_distance(a_tree, c_tree) > 0
            assert calcuate_html_tree_distance(a_tree, c_tree) > 15


def test_calculate_distance_between_navbars_a_and_c():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_c.html") as example_c:
            a_tree = create_html_tree(
                example_a, specific_tag="nav", class_="navbar navbar-default"
            )
            c_tree = create_html_tree(
                example_c, specific_tag="nav", class_="navbar navbar-default"
            )
            assert calcuate_html_tree_distance(a_tree, c_tree) > 0
            assert calcuate_html_tree_distance(a_tree, c_tree) > 5


def test_calculate_distance_between_main_div_a_and_c():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_c.html") as example_c:
            a_tree = create_html_tree(example_a, specific_tag="div", class_="main-div")
            c_tree = create_html_tree(example_c, specific_tag="div", class_="main-div")
            assert calcuate_html_tree_distance(a_tree, c_tree) > 0
            assert calcuate_html_tree_distance(a_tree, c_tree) > 5


def test_calculate_distance_between_footers_a_and_c():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_c.html") as example_c:
            a_tree = create_html_tree(example_a, specific_tag="footer")
            c_tree = create_html_tree(example_c, specific_tag="footer")
            assert calcuate_html_tree_distance(a_tree, c_tree) == 0
