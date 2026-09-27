import urllib.request
import re

with open('tracolab_raw.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Update Title
html = re.sub(r'<title>.*?</title>', '<title>CoverseERP — All-in-One Cloud ERP, HRMS & Operations Platform</title>', html)

# 2. JSON-LD schema
html = html.replace('Traco Lab', 'CoverseERP')
html = html.replace('http://www.tracolab.com/', 'https://coverseerp.in/')
html = html.replace('http://tracolab.com/', 'https://coverseerp.in/')

# 3. Header Logo replacement
old_logo_pattern = r'<a\s+href="[^"]*"\s+class="logo\s+d-flex\s+align-items-center\s+me-auto">\s*<img\s+src="[^"]*tracolab4\.png"[^>]*>.*?</a>'
new_logo = '''<a href="./" class="logo d-flex align-items-center me-auto text-decoration-none">
          <div style="width: 38px; height: 38px; border-radius: 8px; background: linear-gradient(135deg, #00a1ff 0%, #0b366b 100%); color: #ffffff; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; margin-right: 10px; box-shadow: 0 4px 10px rgba(0, 161, 255, 0.3);">
            <i class="fa-solid fa-cube"></i>
          </div>
          <span style="font-family: 'Raleway', sans-serif; font-size: 24px; font-weight: 800; color: #0b366b; letter-spacing: -0.5px;">CoverseERP</span>
        </a>'''

html = re.sub(old_logo_pattern, new_logo, html, flags=re.DOTALL)

# 4. Contact Address replacement
html = re.sub(
    r'Plot No -1032, 2nd Floor, Sarahah Tower, Old Railway Road,.*?Gurugram, Haryana - 122001, INDIA',
    'C-535 block c urbtech trade center , sector 132 noida',
    html,
    flags=re.DOTALL
)

# 5. Footer Address replacement
html = re.sub(
    r'H No-511, Sarahah Tower, Subhash Nagar,.*?(?:Gurugram, India, Pin-122001, INDIA|Gurugram|INDIA)',
    'C-535 block c urbtech trade center , sector 132 noida',
    html,
    flags=re.DOTALL,
    count=1
)

# 6. Phone Number replacement
html = html.replace('+91-742-860-0608', '+91 9958089836')

# 7. Email replacement
html = html.replace('info@tracolab.com', 'info@coverseerp.com')

# 8. Sentences & brand text
html = html.replace("Tracolab's business solutions", "CoverseERP's business solutions")
html = html.replace("Tracolab's", "CoverseERP's")
html = html.replace("Tracolab", "CoverseERP")

# 9. Internal page anchor links
html = html.replace('href="https://tracolab.com/web/overview"', 'href="#about"')
html = html.replace('href="https://tracolab.com/web/about"', 'href="#about"')
html = html.replace('href="https://tracolab.com/web/services"', 'href="#services"')
html = html.replace('href="https://tracolab.com/web/contact"', 'href="#contact"')
html = html.replace('href="https://tracolab.com/web/helpCenter"', 'href="#faq"')
html = html.replace('href="https://tracolab.com/web/faq"', 'href="#faq"')
html = html.replace('href="https://tracolab.com/web/crm"', 'href="#services"')
html = html.replace('href="https://tracolab.com/web/hrms"', 'href="#services"')
html = html.replace('href="https://tracolab.com/web/employeeMonitoring"', 'href="#services"')
html = html.replace('href="https://tracolab.com/web/orderManagement"', 'href="#services"')
html = html.replace('href="https://tracolab.com/web/stockInventory"', 'href="#services"')
html = html.replace('href="https://tracolab.com/web/documentation"', 'href="#about"')
html = html.replace('href="https://tracolab.com/web/terms"', 'href="#about"')
html = html.replace('href="https://tracolab.com/web/privacy_policy"', 'href="#about"')
html = html.replace('href="https://tracolab.com/"', 'href="./"')

# 10. CTAs and Signup links to open the trial modal
html = html.replace('href="https://tracolab.com/web/signup"', 'href="#trialModal" data-bs-toggle="modal" data-bs-target="#trialModal"')
html = html.replace('href="https://tracolab.com/login"', 'href="#trialModal" data-bs-toggle="modal" data-bs-target="#trialModal"')

# 11. Modal form action to client-side handler
html = html.replace(
    'action="https://tracolab.com/web/tryitfree" method="POST"',
    'onsubmit="handleTrialSubmit(event)"'
)

# 12. Add a toast notification and client-side handler before </body>
script_insert = '''
<div id="toastBox" style="display:none; position:fixed; bottom:24px; right:24px; background:#0b366b; color:#fff; padding:14px 24px; border-radius:6px; box-shadow:0 10px 30px rgba(0,0,0,0.25); z-index:99999; border-left:4px solid #00a1ff;">
  <i class="bi bi-check-circle-fill text-info me-2"></i>
  <span id="toastText">Thank you! Your request has been received.</span>
</div>

<script>
function handleTrialSubmit(e) {
  e.preventDefault();
  var modalEl = document.getElementById('trialModal');
  var modal = bootstrap.Modal.getInstance(modalEl);
  if (modal) modal.hide();
  
  var toast = document.getElementById('toastBox');
  var toastText = document.getElementById('toastText');
  toastText.textContent = "Thank you! Your CoverseERP 14-day free trial is being setup. We will contact you at +91 9958089836 shortly.";
  toast.style.display = 'block';
  setTimeout(function() { toast.style.display = 'none'; }, 5000);
}

// Make contact form also give instant feedback
document.addEventListener('DOMContentLoaded', function() {
  var contactForm = document.querySelector('.php-email-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      var toast = document.getElementById('toastBox');
      var toastText = document.getElementById('toastText');
      toastText.textContent = "Thank you for reaching out to CoverseERP! Our team will contact you shortly.";
      toast.style.display = 'block';
      contactForm.reset();
      setTimeout(function() { toast.style.display = 'none'; }, 5000);
    });
  }
});
</script>
'''

html = html.replace('</body>', script_insert + '\n</body>')

# Write output to index.html and coverseerp.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('coverseerp.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Transformation successfully written to index.html and coverseerp.html')
print('Length of transformed HTML:', len(html))
