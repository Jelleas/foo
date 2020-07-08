import check50
import lib50

raise lib50.InvalidSlugError("foo")

#this is invalid syntax

@check50.check()
def dummy():
    """dummy test passed"""
    raise ValueError()
