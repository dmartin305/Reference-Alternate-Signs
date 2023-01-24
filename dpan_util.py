import os
import markdown
import itertools
signer_dir = "/Users/davidmartin/Desktop/DPAN_QA/4a.8006/4a.8006"
sign_savvy_prefix = "https://www.signingsavvy.com/search/"
sign_names = []
sign_links = []

for filename in os.listdir(signer_dir):
    sign_names.append(filename.lower())


sign_names.remove('.ds_store')
sign_names.sort()

for sign in sign_names:
    sign_links.append(sign_savvy_prefix + sign)

with open("signs.md", 'a') as w:
    for i, sign_link in enumerate(sign_links):
        text = "[" + str(sign_names[i]) + "]" + "(" + sign_link + ")\n"
        w.write(text)
