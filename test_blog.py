def test_tags():
    from blog.models import BlogPost
    post = BlogPost("Test", "Content", tags=["ai", "dev"])
    assert "ai" in post.tags


def test_summarize():
    from blog.utils import summarize
    assert summarize("AI is awesome. " * 10) == ("AI is awesome. " * 5).strip() + "..."
