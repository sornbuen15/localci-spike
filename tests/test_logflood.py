def test_prints_30mb_then_fails():
    # pytest shows captured output only for failing tests, so this one fails on purpose
    line = "x" * 1023
    for _ in range(30 * 1024):
        print(line)
    assert False, "log flood"
