# Cursor Marketing Automation Template (PoC)

このリポジトリは、AIエディタ「Cursor」とPythonスクリプトを活用して、
マーケティング業務におけるキャンペーンの進行・管理・レポート作成をテンプレート化・自動化するPoC（概念実証）テンプレートです。

## 🔧 機能概要
- Markdownベースのドキュメントテンプレート（Jinja2）を使用
- YAMLによるキャンペーン情報の入力データ管理
- Pythonでテンプレートをレンダリングし、Cursorで編集可能な構造を生成
- Cursorの`.workflow.yml`でテンプレート実行手順を記述
- マーケティング担当者向けのコピー案、報告書、メール下書きの自動生成に活用

## 📁 ディレクトリ構成

```
cursor-marketing-automation-template/
├── README.md
├── templates/
│   ├── copy_generation.md.j2
│   ├── mail_draft.md.j2
│   └── report_outline.md.j2
├── data/
│   └── sample_campaign.yml
├── scripts/
│   └── render_templates.py
├── output/
│   ├── copy_generation.md
│   ├── mail_draft.md
│   └── report_outline.md
├── .cursor/
│   └── workflow.yml
├── docs/
│   ├── flowchart.png
│   └── user_guide.pdf
└── .gitignore
```

## 🚀 セットアップ手順

```bash
# 1. リポジトリをクローン
$ git clone https://github.com/kagehero/marketing_automation_template.git
$ cd cursor-marketing-automation-template

# 2. 必要なパッケージをインストール
$ pip install jinja2 pyyaml
```

## 📝 使用方法

```bash
# YAMLファイルとテンプレートからMarkdownを出力
$ python scripts/render_templates.py
```

1. `data/sample_campaign.yml` にキャンペーン情報を記入
2. `output/` フォルダにMarkdownファイルが生成される
3. `.cursor/workflow.yml` をCursorで開くと、各プロンプトに応じて編集が可能

## 📄 使用例

### 🔹 sample_campaign.yml
```yaml
campaign_name: 春の新生活応援キャンペーン
start_date: 2025-04-01
end_date: 2025-04-30
lead_copy: "新しい季節、新しいあなたへ。"
email_subject: "春の特別セール開催中！"
```

### 🔹 copy_generation.md.j2
```markdown
# キャンペーンコピー案生成

キャンペーン名：{{ campaign_name }}
期間：{{ start_date }}〜{{ end_date }}

## コピー案候補
- {{ lead_copy }}
- {{ campaign_name }}を通じて、○○を届けよう。
- 季節に合わせた特別企画 — {{ campaign_name }}
```

### 🔹 render_templates.py
```python
import os
import yaml
from jinja2 import Environment, FileSystemLoader

# テンプレートとデータのパス
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "output"
DATA_FILE = "data/sample_campaign.yml"

# 出力対象テンプレート
TEMPLATES = [
    "copy_generation.md.j2",
    "mail_draft.md.j2",
    "report_outline.md.j2"
]

# 出力処理
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    context = yaml.safe_load(f)

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
for tmpl_name in TEMPLATES:
    template = env.get_template(tmpl_name)
    rendered = template.render(context)

    output_path = os.path.join(OUTPUT_DIR, tmpl_name.replace('.j2', ''))
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered)
```

### 🔹 .cursor/workflow.yml
```yaml
version: 1.0
steps:
  - name: Generate Campaign Copy
    run: python scripts/render_templates.py
    output: output/copy_generation.md

  - name: Review Generated Copy in Cursor
    open: output/copy_generation.md
```

## 🧠 技術構成
- Python 3.x
- Jinja2（テンプレートレンダリング）
- PyYAML（データ定義）
- Cursor（AI支援エディタ）

## 🧭 想定ユースケース
- マーケティング業務における「定型文作成」の自動化
- コピー案、キャンペーン進行フロー、完了報告などの文書テンプレート整備
- 社内の非エンジニア向けに「Cursorを使って自然文から一括生成できる仕組み」を提供

## 📌 ライセンス
MIT

## 🙋‍♂️ お問い合わせ
このリポジトリに関するご質問・導入サポートは [nightfurry2345@gmail.com] までご連絡ください。
