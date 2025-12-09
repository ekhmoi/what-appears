#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    script_path = Path(__file__).resolve()
    # repo_root/.github/workflows/generate_book_order.py
    # parents[0] -> .github/workflows
    # parents[1] -> .github
    # parents[2] -> repo root
    repo_root = script_path.parents[2]

    chapters_dir = repo_root / "_chapters"
    output_file = repo_root / "book-order.txt"

    if not chapters_dir.is_dir():
        raise SystemExit(f"No _chapters directory found at: {chapters_dir}")

    parts = sorted(
        [p for p in chapters_dir.iterdir() if p.is_dir()],
        key=lambda p: p.name,
    )

    lines: list[str] = []

    for idx, part_dir in enumerate(parts, start=1):
        # Header for the part
        lines.append(f"# === Part {idx} ===")

        # All .md files directly inside the part directory, sorted by filename
        md_files = sorted(
            [f for f in part_dir.glob("*.md") if f.is_file()],
            key=lambda f: f.name,
        )

        for f in md_files:
            rel_path = f.relative_to(repo_root)
            # Use POSIX-style paths
            lines.append(rel_path.as_posix())

        # Blank line between parts
        lines.append("")

    # Remove trailing blank lines
    while lines and lines[-1] == "":
        lines.pop()

    output_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated {output_file}")


if __name__ == "__main__":
    main()
