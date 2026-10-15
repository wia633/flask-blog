from flask import Flask, render_template, abort

app = Flask(__name__)

# 範例文章資料
posts = [
    {
        "title": "我的第一篇文章",
        "author": "王小明",
        "content": "這是我的第一篇部落格文章，歡迎大家閱讀！"
    },
    {
        "title": "學習 Python Flask",
        "author": "李小華",
        "content": "Flask 是一個輕量級的 Python Web 框架，適合用來開發網站。"
    },
    {
        "title": "Template 的使用方式",
        "author": "陳大文",
        "content": "Flask 可以透過 Jinja2 Template，將 Python 資料呈現在 HTML 頁面中。"
    }
]


# 首頁：顯示所有文章
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


# 文章內頁：根據文章編號顯示單篇文章
@app.route("/post/<int:post_id>")
def show_post(post_id):
    if post_id < 0 or post_id >= len(posts):
        abort(404)

    post = posts[post_id]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
