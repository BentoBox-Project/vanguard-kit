from vanguardkit import calcuate_html_tree_distance, create_html_tree


def test_calculate_the_realistic_difference_between_a_c():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_d.html") as example_d:
            a_tree = create_html_tree(example_a)
            d_tree = create_html_tree(example_d)
            assert calcuate_html_tree_distance(a_tree, d_tree) > 0
            assert calcuate_html_tree_distance(a_tree, d_tree) > 15


def test_calculate_distance_between_navbars_a_and_c():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_d.html") as example_d:
            a_tree = create_html_tree(
                example_a, specific_tag="nav", class_="navbar navbar-default"
            )
            d_tree = create_html_tree(
                example_d, specific_tag="nav", class_="navbar navbar-default"
            )
            assert calcuate_html_tree_distance(a_tree, d_tree) > 0
            assert calcuate_html_tree_distance(a_tree, d_tree) > 5


def test_calculate_distance_between_main_div_a_and_c():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_d.html") as example_d:
            a_tree = create_html_tree(example_a, specific_tag="div", class_="main-div")
            d_tree = create_html_tree(example_d, specific_tag="div", class_="main-div")
            assert calcuate_html_tree_distance(a_tree, d_tree) > 0
            assert calcuate_html_tree_distance(a_tree, d_tree) > 5


def test_calculate_distance_between_footers_a_and_c():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_d.html") as example_d:
            a_tree = create_html_tree(example_a, specific_tag="footer")
            d_tree = create_html_tree(example_d, specific_tag="footer")
            assert calcuate_html_tree_distance(a_tree, d_tree) > 0
