from but_in_python.sources.BinaryTreeTraversalInOrder import BinaryNode

def get_test_tree_1():
    root = BinaryNode(20)
    l1_r = BinaryNode(50, root)
    l1_l = BinaryNode(10, root)
    root.left = l1_l
    root.right = l1_r

    l2_r = BinaryNode(100, l1_r)
    l2_l = BinaryNode(30, l1_r)
    l1_r.left = l2_l
    l1_r.right = l2_r

    l3_r = BinaryNode(45, l2_l)
    l3_l = BinaryNode(29, l2_l)
    l2_l.left = l3_l
    l2_l.right = l3_r

    l1_l.right = BinaryNode(15, l1_l)

    l2_r2 = BinaryNode(5, l1_l)
    l3_r2 = BinaryNode(7, l2_r2)

    l2_r2.right = l3_r2
    l1_l.left = l2_r2

    return root

def get_test_tree_2():
    root = BinaryNode(20)
    l1_r = BinaryNode(50, root)
    l1_l = BinaryNode(10, root)
    root.left = l1_l
    root.right = l1_r

    l2_l = BinaryNode(30, l1_r)
    l1_r.left = l2_l

    l3_r = BinaryNode(45, l2_l)
    l3_l = BinaryNode(29, l2_l)
    l2_l.left = l3_l
    l2_l.right = l3_r

    l3_r3 = BinaryNode(49, l3_r)
    l3_r.right = l3_r3

    l3_l3 = BinaryNode(21, l3_r)
    l3_r.left = l3_l3

    l1_l.right = BinaryNode(15, l1_l)

    l2_r2 = BinaryNode(5, l1_l)
    l3_r2 = BinaryNode(7, l2_r2)

    l2_r2.right = l3_r2
    l1_l.left = l2_r2

    return root