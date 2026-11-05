def test_allocates_more_than_the_memory_limit():
    blocks = []
    for _ in range(40):              # 40 x 100 MB = 4 GB > 2 GB limit
        blocks.append(bytearray(100 * 1024 * 1024))
    assert len(blocks) == 40
