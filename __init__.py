import check50

@check50.check()
def dummy():
    """dummy test passed"""
    print("hello")
    raise ValueError()
