from vanguardkit import create_html_tree


def test_simple_distance_through_the_sub_dunder_method():
    with open("tests/html_examples/example_a.html") as example_a:
        with open("tests/html_examples/example_b.html") as example_b:
            a_tree = create_html_tree(example_a)
            b_tree = create_html_tree(example_b)
            assert a_tree - b_tree == 1


def test_simple_distance_through_the_sub_dunder_method_with_realistic_case():
    with open("tests/html_examples/realistic_example_a.html") as example_a:
        with open("tests/html_examples/realistic_example_d.html") as example_d:
            a_tree = create_html_tree(example_a)
            d_tree = create_html_tree(example_d)
            assert a_tree - d_tree > 15
