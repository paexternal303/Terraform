from blog.models import BlogPost

def render_post(post: BlogPost):
    return f"<h1>{post.title}</h1><p>{post.content}</p>"
