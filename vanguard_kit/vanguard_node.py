from zss import Node, simple_distance


class VanguardNode(Node):
    """
    A class that extends the functionality of the zss.Node class

    simple node object that can be used to construct trees to be used with
    :py:func:`zss.distance`.

    Attributes
    ----------
    label: str
        The name of the node
    children: list
        The children of the current node
    attrs: dict
        The html attributes of the node
    """

    def __init__(self, label, children=None, attrs=None):
        """
        Parameters
        ----------
        label: str
            The name of the node
        children: list
            The children of the current node
        attrs: dict
            The html attributes of the node
        """
        super().__init__(label, children=None)
        self.attrs = attrs

    def __sub__(self, other):
        return simple_distance(self, other)
