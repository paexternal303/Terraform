def test_summarize():
    from blog.utils import summarize
    assert summarize("a" * 120) == "a" * 100 + "..."
