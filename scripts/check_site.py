"""Check generated HTML for broken local links, missing image alt text and page landmarks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote, urljoin
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
errors = []
pages = list(root.rglob('*.html'))
if not pages:
    raise SystemExit('No generated HTML found; build the site first.')

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.main_count = 0
        self.h1_count = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'): self.ids.add(attrs['id'])
        if tag == 'main': self.main_count += 1
        if tag == 'h1': self.h1_count += 1
        if tag == 'img' and 'alt' not in attrs: errors.append(f'{page}: image missing alt')
        for attr in ('href', 'src'):
            if attrs.get(attr): self.links.append(attrs[attr])

for page in pages:
    parsed = Page()
    parsed.feed(page.read_text())
    if parsed.main_count != 1: errors.append(f'{page}: expected one main landmark')
    if parsed.h1_count != 1: errors.append(f'{page}: expected one h1')
    base = '/' + page.relative_to(root).as_posix()
    for link in parsed.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        path = unquote(urlsplit(urljoin(base, link)).path).lstrip('/')
        target = root / path
        if not target.is_file() and not (target / 'index.html').is_file():
            errors.append(f'{page.relative_to(root)}: missing local target {link}')
        elif url.fragment:
            target_page = target if target.is_file() else target / 'index.html'
            if target_page.suffix == '.html':
                destination = Page()
                destination.feed(target_page.read_text())
                if unquote(url.fragment) not in destination.ids:
                    errors.append(f'{page.relative_to(root)}: missing fragment {link}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} HTML pages; local links/fragments, image alt attributes, and page landmarks.')
