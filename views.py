from blog.models import BlogPost

def render_post(post: BlogPost):
    tag_html = " ".join(f"<span>{t}</span>" for t in post.tags)
    return f"<h1>{post.title}</h1><h4>By {post.author}</h4><p>{post.content}</p><div>{tags}</div>"
