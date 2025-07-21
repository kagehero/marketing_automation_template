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
