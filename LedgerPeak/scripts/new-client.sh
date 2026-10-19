#!/usr/bin/env bash
# Usage: scripts/new-client.sh "Client Name"
# Copies clients/_TEMPLATE into clients/<client-slug>/ and fills in name and date.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NAME="${1:-}"
[ -z "$NAME" ] && { echo "Usage: $0 \"Client Name\""; exit 1; }
ASCII="$(printf '%s' "$NAME" | sed -E 's/(à|á|â|ä|ã|å)/a/g; s/(À|Á|Â|Ä|Ã|Å)/A/g; s/(è|é|ê|ë)/e/g; s/(È|É|Ê|Ë)/E/g; s/(ì|í|î|ï)/i/g; s/(ò|ó|ô|ö|õ|ø)/o/g; s/(Ò|Ó|Ô|Ö|Õ|Ø)/O/g; s/(ù|ú|û|ü)/u/g; s/(Ù|Ú|Û|Ü)/U/g; s/(ç)/c/g; s/(Ç)/C/g; s/(ñ)/n/g')"
SLUG="$(echo "$ASCII" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')"
DEST="$ROOT/clients/$SLUG"
[ -e "$DEST" ] && { echo "Already exists: $DEST"; exit 1; }
TODAY="$(date +%d/%m/%Y)"
cp -R "$ROOT/clients/_TEMPLATE" "$DEST"
for f in "$DEST"/*.md; do
  ESC_NAME="$(printf '%s' "$NAME" | sed 's/[&|\\]/\\&/g')"
  sed -i.bak -e "s|{{CLIENT_NAME}}|$ESC_NAME|g" -e "s|{{DATE}}|$TODAY|g" "$f" && rm -f "$f.bak"
done
# Fill the Word engagement letter if Python + python-docx are available
if command -v python3 >/dev/null 2>&1; then
python3 - "$DEST/03-engagement-letter.docx" "$NAME" "$TODAY" <<'PY' || echo "Note: fill name/date in the engagement letter by hand."
import sys
from docx import Document
p,n,d=sys.argv[1:]
doc=Document(p)
for para in doc.paragraphs:
    for r in para.runs:
        r.text=r.text.replace("{{CLIENT_NAME}}",n).replace("{{DATE}}",d)
doc.save(p)
PY
fi
echo "$TODAY | New client folder created: $NAME | new-client.sh" >> "$ROOT/office/work-log.md"
echo "Created $DEST"
