from zss import simple_distance


def calcuate_html_tree_distance(a, b):
    """
    Calculates the distance between two trees, based on html graphs.

    Parameters
    ----------
    a : VanguardNode | zss.Node
        It's a html graph recursively generated
    b : VanguardNode | zss.Node
        It's a html graph recursively generated

    Returns
    -------
    int
        The distance calculated based on the Zhang-Shasha algorithm
    """
    return simple_distance(a, b)
