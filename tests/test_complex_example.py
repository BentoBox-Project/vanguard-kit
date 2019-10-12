from vanguardkit import create_html_tree, calcuate_html_tree_distance


def test_calculate_impact_when_a_branch_changes():
    with open("tests/html_examples/complex_example_a.html") as example_a:
        with open("tests/html_examples/complex_example_b.html") as example_b:
            a_tree = create_html_tree(example_a)
            b_tree = create_html_tree(example_b)
            assert calcuate_html_tree_distance(a_tree, b_tree) > 1


def test_calculate_difference_between_div_class_branch_a():
    with open("tests/html_examples/complex_example_a.html") as example_a:
        with open("tests/html_examples/complex_example_b.html") as example_b:
            a_tree = create_html_tree(example_a,
                                      specific_tag="div",
                                      class_="branch-a")
            b_tree = create_html_tree(example_b,
                                      specific_tag="div",
                                      class_="branch-a")
            assert calcuate_html_tree_distance(a_tree, b_tree) == 4


def test_calculate_difference_between_div_class_branch_b():
    with open("tests/html_examples/complex_example_a.html") as example_a:
        with open("tests/html_examples/complex_example_b.html") as example_b:
            a_tree = create_html_tree(example_a,
                                      specific_tag="div",
                                      class_="branch-b")
            b_tree = create_html_tree(example_b,
                                      specific_tag="div",
                                      class_="branch-b")
            assert calcuate_html_tree_distance(a_tree, b_tree) == 0
