from tm_trees import TMTree, FileSystemTree


def test_delete_self() -> None:
    """Tests functionality of delete_self()
    """
    sstree = TMTree('s', [])
    subtree = TMTree('f', [sstree])
    leaf2 = TMTree('ld', [])
    tree3 = TMTree('trs', [subtree, leaf2])
    assert leaf2.delete_self()
    assert leaf2 not in tree3._subtrees
    assert sstree.delete_self()
    assert not subtree._subtrees
    # test trying to remove root
    assert not tree3.delete_self()
