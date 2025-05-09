
def clean_history(raw: str) -> str:
    lines = raw.strip().split('\n')
    return '\n'.join(line for line in lines if line.startswith('User:') or line.startswith('Bot:'))
