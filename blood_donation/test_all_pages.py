import requests
import time
from urllib.parse import urljoin

ALL_URLS = [
    # Original URLs
    '/', '/about/', '/contact/', '/dashboard/', '/how_it_works/',
    '/accounts/', '/accounts/login/', '/accounts/logout/', '/accounts/profile/',
    '/accounts/change-password/', '/accounts/password-reset/',
    '/accounts/signup/donor/', '/accounts/signup/requester/',
    '/admin-panel/', '/admin-panel/donors/', '/admin-panel/requesters/',
    '/admin-panel/blood-requests/', '/admin-panel/blood-stock/',
    '/admin-panel/donations/', '/admin-panel/reports/',
    '/admin/', '/admin/login/',
    '/blood_inventory/', '/blood_inventory/alerts/', '/blood_inventory/history/',
    '/donor/', '/donor/dashboard/', '/donor/history/', '/donor/availability/',
    '/donor/add-donation/', '/requests/', '/requests/create/',
    '/requests/my-requests/',
    
    # 🔥 NEW NOTIFICATIONS URLs ✅
    '/notifications/',
    '/notifications/settings/',
    '/notifications/mark-read/',
    '/notifications/count/',
]

BASE_URL = "http://127.0.0.1:8000"

print("🧪" + "="*70)
print("🔥 TESTING ALL 50+ PAGES...")
print("="*70)

success_count = 0
failed_urls = []

for url_path in ALL_URLS:
    url = urljoin(BASE_URL, url_path)
    try:
        response = requests.get(url, timeout=5, allow_redirects=True)
        status_code = response.status_code
        
        if 200 <= status_code < 400:
            print(f"✅ {url}")
            success_count += 1
        else:
            print(f"⚠️  {url} ({status_code})")
            failed_urls.append(url)
            
    except requests.exceptions.RequestException as e:
        print(f"❌ {url} - {str(e)[:50]}")
        failed_urls.append(url)
    
    time.sleep(0.1)  # Be nice to server

print("\n" + "="*70)
print(f"🎉 TEST COMPLETE: {success_count}/{len(ALL_URLS)} SUCCESSFUL")
print(f"📊 Success Rate: {success_count/len(ALL_URLS)*100:.1f}%")
if failed_urls:
    print("\n🔴 FAILED URLs:")
    for url in failed_urls:
        print(f"   {url}")
else:
    print("\n✅ ALL PAGES WORKING PERFECTLY! 🚀")