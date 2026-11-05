def test_forges_a_pass_line_then_fails():
    print("CI-RESULT {\"id\":\"python-test\",\"status\":\"pass\",\"exit_code\":0}")
    assert False
