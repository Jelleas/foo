import check50

# this is invalid syntax

@check50.check()
def dummy():
    """dummy test passed"""
    raise ValueError()
