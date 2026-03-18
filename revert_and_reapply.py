import re
import os
import subprocess

with open("caparks.html", "r", encoding="utf-8") as f:
    orig_content = f.read()

# 1. Extract the CSS for is-exporting
css_match = re.search(r"(\.is-exporting \.pm-footer-btns.*?\}\n  </style>\n  <script src=\"https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js\"></script>\n)", orig_content, re.DOTALL)
if css_match:
    export_css = css_match.group(1)
else:
    print("Could not find CSS snippet")

# 2. Extract captureModalAsImage function
func_match = re.search(r"(async function captureModalAsImage\(parkId\) \{.*?\}\n\n)function normalizeParkDetail\(d\)", orig_content, re.DOTALL)
if func_match:
    capture_func = func_match.group(1)
else:
    print("Could not find function snippet")

# 3. Extract the footer btn change
footer_match = re.search(r'(      <div class="pm-footer-btns".*?</div>\n      <div class="pm-watermark">.*?</div>\n    </div>`;)', orig_content, re.DOTALL)
if footer_match:
    footer_code = footer_match.group(1)
else:
    print("Could not find footer snippet")

# Run git checkout
subprocess.run(["git", "checkout", "caparks.html"], check=True)

with open("caparks.html", "r", encoding="utf-8") as f:
    clean_content = f.read()

# Re-apply CSS
clean_content = clean_content.replace("  </style>\n</head>", export_css.replace("  </style>\n  <script", "  </style>\n</head>\n<head>\n  <script").replace("</head>\n<head>\n  <script", "  <script") if "  <script" not in export_css else export_css)

# Wait, simple replace:
if "html2canvas.min.js" not in clean_content:
    clean_content = clean_content.replace("  </style>\n</head>", "    .is-exporting .pm-footer-btns,\n    .is-exporting .pm-close {\n      display: none !important;\n    }\n    .pm-watermark {\n      display: none;\n      text-align: center;\n      padding-top: 20px;\n      font-size: 11px;\n      color: var(--text-muted);\n      font-weight: 500;\n      letter-spacing: 0.5px;\n    }\n    .is-exporting .pm-watermark {\n      display: block;\n    }\n  </style>\n  <script src=\"https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js\"></script>\n</head>")

# Re-apply JS Function
if "captureModalAsImage(" not in clean_content:
    clean_content = clean_content.replace("function normalizeParkDetail(d){", capture_func + "function normalizeParkDetail(d){")

# Re-apply Footer HTML
# The previous footer was:
old_footer = r"""      <div class="pm-footer-btns" style="flex-wrap: wrap;">
        <a class="pm-btn" href="${p.website}" target="_blank" rel="noopener">🌐 Official Website</a>
        <a class="pm-btn" href="https://www.google.com/maps/dir/?api=1&destination=${p.lat},${p.lon}" target="_blank" rel="noopener"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" style="vertical-align:middle;transform:rotate(-45deg)"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg> Navigate</a>
        <button class="pm-btn pm-primary" onclick="closeParkModal();flyTo('${p.id}')">📍 Show on Map</button>
        <button class="pm-btn" style="flex: 1 1 100%; font-weight: 700; color: #146c43; border-color: #b7e2ca; background: #edf9f1;" title="Copies the full park brief, opens ChatGPT, then you paste it there" onclick="openChatGPTPrompt('${p.id}', this)">Ask ChatGPT to Plan This Trip</button>
      </div>
    </div>`;"""
if "captureModalAsImage" in footer_code:
    # Handle the typo in the clean file where it might be `openopenChatGPTPrompt` or missing `openChatGPTPrompt`? Wait, I fixed that earlier today. Let's just do a regex sub to replace the footer.
    clean_content = re.sub(r'      <div class="pm-footer-btns".*?</div>\n    </div>`;', footer_code, clean_content, flags=re.DOTALL)

with open("caparks.html", "w", encoding="utf-8") as f:
    f.write(clean_content)

print("Revert and re-apply complete.")
