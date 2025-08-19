import re
BLOCK_PATTERNS = [re.compile(r'\b(credit card|ssn|aadhar|pan number)\b', re.I)]
def is_blocked(text: str) -> bool:
    res = any(p.search(text or "")for p in BLOCK_PATTERNS)
    return res