from pycs.data_structures.avl_tree.avl_tree import AVLTree


def incorrect_avl_sort(nums: list[int]) -> list[int]:
    """This implementation is not correct since the AVLTree class does
    not record repeated identical values! """
    tree: AVLTree = AVLTree()
    for x in nums:
        tree.insert(key=x)
    return tree.inorder()
