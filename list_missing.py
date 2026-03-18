import re

with open('caparks.html', 'r') as f:
    content = f.read()

# Extract PARK_DETAILS block roughly
match = re.search(r'const PARK_DETAILS\s*=\s*\{([\s\S]*?)\n};\n\nfunction', content)
if not match:
    print("Could not find PARK_DETAILS")
    exit(1)

details_str = match.group(0)

# We can find park keys by looking for lines like: 'park-id':{
# or "park-id":{
# Actually it's something like:
#   'castle-rock':{
#     highlight: "...",
park_keys = re.findall(r"\n\s*'([^']+)':\s*\{", details_str)

parks_to_update = []
for pk in park_keys:
    # Extract the block for this park
    # We can match from 'pk':{ to the next park key or end
    pk_escape = re.escape(pk)
    # this regex is a bit fragile but let's try
    start_idx = details_str.find(f"'{pk}':{{")
    if start_idx == -1:
        start_idx = details_str.find(f"'{pk}': {{")
    
    # Just a simple check if string 'biking' is missing, etc. inside the whole file for this park is hard.
    # Let's write a small node script instead since it's valid JS!
