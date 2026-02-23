# Workflow: Write and Publish a Blog Post

## Objective
Create a new post, write the content, and publish it to the live site.

## Tools
- `tools/new_post.py` — generates the post HTML file and index snippet

---

## Step 1 — Generate the post file

```bash
python tools/new_post.py "Your Post Title" --tag yourtag
```

This creates `site/posts/your-post-title.html` and prints an `<li>` block to copy.

**Common tags:** `travel`, `tech`, `life`, `food`, `ideas`, `misc`

---

## Step 2 — Write the post

Open `site/posts/your-post-title.html` and:
- Replace `TODO: Write your post here.` with your actual content
- Update `TODO min read` in the meta line (rough guide: ~200 words per minute)
- Update the `<meta name="description">` tag with a one-sentence summary

Use these HTML elements inside `.post-content`:
- `<p>` — paragraph
- `<h2>` / `<h3>` — section headings
- `<blockquote>` — pull quotes
- `<ul>` / `<ol>` / `<li>` — lists
- `<code>` — inline code, `<pre><code>` — code blocks

---

## Step 3 — Add to the index

Open `site/index.html` and paste the `<li>` block printed in Step 1 at the **top** of the `<ul class="post-list">` (newest posts first). Update the excerpt text.

---

## Step 4 — Preview locally

Open `site/index.html` in your browser (double-click the file, or drag it in). Click through to the post to check formatting.

---

## Step 5 — Deploy to server

*(Fill in `.env` with your server details first.)*

**Option A — SFTP/SCP (simple)**
```bash
scp -r site/ $SERVER_USER@$SERVER_HOST:$SERVER_PATH
```

**Option B — rsync (faster, only uploads changes)**
```bash
rsync -avz --delete site/ $SERVER_USER@$SERVER_HOST:$SERVER_PATH
```

**Option C — FTP client**
Use Transmit, Cyberduck, or FileZilla. Upload the `site/` folder to your web root.

---

## Customisation Checklist (do once)

- [ ] Replace `My Blog` in `site/index.html` and all post files with your actual site name
- [ ] Update the intro text on `site/index.html`
- [ ] Create `site/about.html` (copy a post page, remove article content, write your bio)
- [ ] Update `&copy; 2026 My Blog` in the footer of each page
- [ ] Add your domain to `.env`

---

## Edge Cases

**Slug collision** — if a post with that title already exists, the script will error. Rename it slightly.

**Special characters in title** — the slugifier strips punctuation automatically. `"It's great!"` → `its-great`.

**Updating a published post** — edit the HTML file directly, then re-upload just that file.
