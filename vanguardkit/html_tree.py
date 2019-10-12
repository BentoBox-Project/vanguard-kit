from bs4 import BeautifulSoup
from vanguardkit import VanguardNode


def create_html_tree(html_file, specific_tag=None, **attrs):
    """
    Generates a tree/graph recursively based on html file

    Parameters
    ----------
    html_file: str | file like object
        The html file to be used to genrete the graph
    specific_tag: str
        A tag used to looking for a specific html element by name

    Returns
    ------
    VanaguardNode
        The parent node with the underlying graph based on a given html file
    """
    soup = BeautifulSoup(html_file, 'html5lib')
    body_tag = _build_body_tag(soup, specific_tag, **attrs)
    body_node = VanguardNode(body_tag.name, attrs=body_tag.attrs)
    body_node = _build_tree(body_node, body_tag)
    return body_node


def _build_body_tag(soup, specific_tag=None, **attrs):
    if specific_tag is not None:
        body_tag = soup.find(specific_tag, **attrs)
        if body_tag is None:
            return
    else:
        body_tag = soup.html.body
    return body_tag


def _build_tree(parent_node, parent_tag):
    if parent_tag.children:
        for child_tag in parent_tag.children:
            if child_tag.name is not None:
                parent_node = _add_kids_to_parent(parent_node, child_tag)
    return parent_node


def _add_kids_to_parent(parent_node, child_tag):
    child_node = VanguardNode(child_tag.name, attrs=child_tag.attrs)
    child_node = _build_tree(child_node, child_tag)
    parent_node.addkid(child_node)
    return parent_node
