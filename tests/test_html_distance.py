from vanguard_kit import create_html_tree, calcuate_html_tree_distance


def test_calculate_distance_between_trees():
    with open("tests/html_examples/example_a.html") as example_a:
        with open("tests/html_examples/example_b.html") as example_b:
            a_tree = create_html_tree(example_a)
            b_tree = create_html_tree(example_b)
            assert calcuate_html_tree_distance(a_tree, b_tree) == 1
