def test_tags():
    from blog.models import BlogPost
    post = BlogPost("Test", "Content", tags=["ai", "dev"])
    assert "ai" in post.tags
