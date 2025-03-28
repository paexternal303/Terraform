def test_summarize():
    from blog.utils import summarize
    assert summarize("AI is awesome. " * 10) == ("AI is awesome. " * 5).strip() + "..."
