#!/usr/bin/env python

import re
import sys

twiki = sys.stdin.read()

twiki = re.sub('``` screen', '``` console', twiki)
twiki = re.sub('``` rootscreen', '``` console', twiki)
twiki = re.sub('<span class="twiki-macro TOC".*></span>\n', '', twiki)
twiki = re.sub('<span class="twiki-macro UCL\_PROMPT\_ROOT"></span>', '[root@client ~] $', twiki)
twiki = re.sub('<span class="twiki-macro UCL\_PROMPT"></span>', '[user@client ~] $', twiki)
twiki = re.sub('%UCL_PROMPT_ROOT%', '[root@client ~] $', twiki)
twiki = re.sub('%UCL_PROMPT%', '[user@client ~] $', twiki)
twiki = re.sub('&lt;', '<', twiki)
twiki = re.sub('&gt;', '>', twiki)
twiki = re.sub('<span class="twiki-macro RED"></span> \*\*NOTE:\*\* <span class="twiki-macro ENDCOLOR"></span>',
               '!!! note\n   ', twiki)

print twiki
