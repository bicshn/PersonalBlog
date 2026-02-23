"""
new_post.py
-----------
Generates a new blog post HTML file from a template.

Usage:
    python tools/new_post.py "My Post Title" --tag travel

This creates:
    site/posts/my-post-title.html   ← ready to edit
And prints the <li> block to paste into site/index.html.
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

SITE_DIR = Path(__file__).parent.parent / "site"
POSTS_DIR = SITE_DIR / "posts"


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def generate_post(title: str, tag: str) -> Path:
    today = date.today().isoformat()
    slug = slugify(title)
    filename = POSTS_DIR / f"{slug}.html"

    if filename.exists():
        sys.exit(f"ERROR: {filename} already exists. Choose a different title.")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — My Blog</title>
  <meta name="description" content="TODO: add a one-sentence description." />
  <link rel="stylesheet" href="../css/style.css" />
</head>
<body>

  <header>
    <div class="container">
      <a href="/" class="site-title">My Blog</a>
      <nav>
        <a href="/">Posts</a>
        <a href="/about.html">About</a>
      </nav>
    </div>
  </header>

  <main class="container">

    <a href="/" class="back-link">&larr; All posts</a>

    <article>
      <div class="post-header">
        <div class="post-meta">{today} &nbsp;&middot;&nbsp; TODO min read</div>
        <h1>{title}</h1>
      </div>

      <div class="post-content">

        <p>
          TODO: Write your post here. Delete this paragraph and start writing.
        </p>

      </div>
    </article>

  </main>

  <footer>
    <div class="container">
      &copy; {date.today().year} My Blog
    </div>
  </footer>

</body>
</html>
"""

    filename.write_text(html, encoding="utf-8")
    return filename, today, slug, tag


def index_snippet(title: str, slug: str, today: str, tag: str) -> str:
    return f"""      <li class="post-item">
        <div class="post-meta">{today} &nbsp;·&nbsp; X min read</div>
        <h2><a href="posts/{slug}.html">{title}</a></h2>
        <p class="post-excerpt">TODO: add a short excerpt.</p>
        <span class="tag">{tag}</span>
      </li>"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new blog post")
    parser.add_argument("title", help="Post title (in quotes)")
    parser.add_argument("--tag", default="misc", help="Tag label (default: misc)")
    args = parser.parse_args()

    filepath, today, slug, tag = generate_post(args.title, args.tag)

    print(f"\n✓ Post created: {filepath}")
    print(f"\nAdd this block to the top of the <ul class=\"post-list\"> in site/index.html:\n")
    print(index_snippet(args.title, slug, today, tag))
    print()
