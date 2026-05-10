from __future__ import annotations

import html
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "docs" / "source"
OUTPUT_DIR = ROOT / "docs" / "extracted"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def clean_text(value: str) -> str:
    value = html.unescape(value)
    if any(marker in value for marker in ("â", "Ã", "ð")):
        try:
            value = value.encode("latin1").decode("utf-8")
        except UnicodeError:
            pass
    value = value.replace("\xa0", " ")
    return re.sub(r"[ \t]+", " ", value).strip()


def paragraph_text(paragraph: ET.Element) -> str:
    parts: list[str] = []
    for node in paragraph.iter():
        tag = node.tag.rsplit("}", 1)[-1]
        if tag == "t" and node.text:
            parts.append(node.text)
        elif tag == "tab":
            parts.append("\t")
        elif tag in {"br", "cr"}:
            parts.append("\n")
    return clean_text("".join(parts))


def extract_docx(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as docx:
        document_xml = docx.read("word/document.xml")
    root = ET.fromstring(document_xml)
    body = root.find("w:body", NS)
    if body is None:
        return []

    blocks: list[str] = []
    for child in body:
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "p":
            text = paragraph_text(child)
            if text:
                blocks.append(text)
        elif tag == "tbl":
            rows: list[list[str]] = []
            for row in child.findall("w:tr", NS):
                cells: list[str] = []
                for cell in row.findall("w:tc", NS):
                    cell_parts = [
                        paragraph_text(p)
                        for p in cell.findall(".//w:p", NS)
                    ]
                    cells.append(clean_text(" ".join(x for x in cell_parts if x)))
                if any(cells):
                    rows.append(cells)
            if rows:
                widths = max(len(row) for row in rows)
                normalized = [row + [""] * (widths - len(row)) for row in rows]
                blocks.append("\n".join("| " + " | ".join(row) + " |" for row in normalized))
    return blocks


def title_from_stem(stem: str) -> str:
    return re.sub(r"^\d+_", "", stem).replace("_", " ")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for source in sorted(SOURCE_DIR.glob("*.docx")):
        blocks = extract_docx(source)
        output = OUTPUT_DIR / f"{source.stem}.md"
        lines = [
            "---",
            f"title: {title_from_stem(source.stem)}",
            f"source_file: docs/source/{source.name}",
            "extraction_method: docx_xml",
            "extraction_status: faithful_text_extraction",
            "---",
            f"# {title_from_stem(source.stem)}",
            "",
            f"Source: `docs/source/{source.name}`",
            "",
            "## Extracted Text",
            "",
        ]
        for block in blocks:
            lines.extend([block, ""])
        output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        print(f"{source.name}: {len(blocks)} blocks -> {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
