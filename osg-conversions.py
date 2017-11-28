#!/usr/bin/env python

import re
import sys

twiki = sys.stdin.read()

replacements = [(r'``` screen', '``` console'),
                (r'``` rootscreen', '``` console'),
                (r'<span class="twiki-macro TOC".*></span>\n', ''),
                (r'<span class="twiki-macro UCL\_PROMPT\_ROOT"></span>', '[root@client ~] $'),
                (r'\[root@client ~\]\s*\$', 'root@host #'),
                (r'<span class="twiki-macro UCL\_PROMPT"></span>', '[user@client ~] $'),
                (r'\[user@client ~\]\s*\$', 'user@host $'),
                (r'%UCL_PROMPT_ROOT%', 'root@host #'),
                (r'%UCL_PROMPT%', 'user@host $'),
                (r'&lt;', '<'),
                (r'&gt;', '>'),
                (r'<span class="twiki-macro NOTE"></span>', '!!! note\n   '),
                (r'<span class="twiki-macro DOC_STATUS_TABLE"></span>\s*', ''),
                (r'<span class="twiki-macro STARTSECTION">.*', ''),
                (r'<span class="twiki-macro ENDSECTION">.*', ''),
                (r'<span class="twiki-macro COMMENT" type="tableappend"></span>\s*', ''),
                (r'-- Main\..*\n', ''),
                (r'\\#[\w\s]+\n', ''),
                (r'\*\*Comments\*\*\s*\n[-=\s]*', ''),
                (r'^-*\\[#\s]*Comments\s*\n', ''),
                (r'<span class="twiki-macro TWISTY">%TWISTY\\_OPTS\\_OUTPUT%</span>\s*', '<details>'),
                (r'<span style="background-color: #\w+;">([^<]+)</span>', r'%RED%\1%ENDCOLOR%'),
                (r'<span class="twiki-macro TWISTY.*showlink="([\w\s]*).*</span>', r'<details>\n  <summary>\1</summary>'),
                (r'<span class="twiki-macro ENDTWISTY"></span>', '</details>'),
                (r'<span class="twiki-macro RED"></span> \*\*NOTE:\*\* <span class="twiki-macro ENDCOLOR"></span>', '!!! note\n   ')]

for args in replacements:
    orig, sub = args
    twiki = re.sub(orig, sub, twiki)


# optionally take link mapping argument
try:
    with open(sys.argv[1], 'r') as f:
        links = [x.split() for x in f.readlines()]

    for link in links:
        twiki = re.sub(r'\(%s\)' % link[0].split('/')[-1], r'(%s)' % link[1], twiki)
except (IOError, IndexError):
    pass

print twiki
