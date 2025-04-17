# ManimGL

## Structrue

```text
Manim/
├── assets/
│   ├── raster_images/
│   ├── vector_images/
│   ├── sounds/
│   ├── data/
│   └──downloads/ 
├── cache/
├── outputs/  
├── src/
└── custom_config.yml
```
## A little changes for Chinese

- /manimlib/utils/tex_file_writing.py
    For the `full_tex_to_svg` method, modify the line: change `tex_path.write_text(full_tex)` to `tex_path.write_text(full_tex, encoding='utf-8')`
- /manimlib/tex_template.yml
    Remove `\usepackage[english]{babel}` from the ctex section.