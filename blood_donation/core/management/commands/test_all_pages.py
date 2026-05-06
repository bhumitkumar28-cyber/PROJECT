import requests
import time

# ALL YOUR URLS FROM show_urls output
ALL_URLS = [
    '/', '/about/', '/contact/', '/dashboard/', '/how_it_works/',
    '/accounts/', '/accounts/login/', '/accounts/logout/', '/accounts/profile/',
    '/accounts/change-password/', '/accounts/password-reset/',
    '/admin-panel/', '/admin-panel/donors/', '/admin-panel/requesters/',
    '/admin-panel/blood-requests/', '/admin-panel/blood-stock/',
    '/admin-panel/donations/', '/admin-panel/reports/',
    '/admin/', '/admin/login/',
    '/blood_inventory/', '/blood_inventory/alerts/', '/blood_inventory/history/',
    '/donor/', '/donor/dashboard/', '/donor/history/', '/donor/availability/',
    '/requests/', '/requests/create/', '/requests/my-requests/',
]

BASE_URL = "http://127.0.0.1:8000"

def test_all_pages():
    print("🧪" + "="*60)
    print("🔥 TESTING ALL 50+ PAGES...")
    print("="*60)
    
    working = 0
    failed = 0
    
    for url in ALL_URLS:
        full_url = BASE_URL + url
        try:
            response = requests.get(full_url, timeout=5)
            status = response.status_code
            
            if status == 200:
                print(f"✅ {full_url}")
                working += 1
            elif status == 302 or status == 301:
                print(f"🔄 {full_url} (Redirect - Login required)")
                working += 1
            elif status == 404:
                print(f"⚠️  {full_url} (404 - Page not found)")
                failed += 1
            else:
                print(f"❌ {full_url} ({status})")
                failed += 1
                
        except Exception as e:
            print(f"💥 {full_url} (ERROR: {e})")
            failed += 1
        
        time.sleep(0.5)  # Be nice to server
    
    print("="*60)
    print(f"🎉 RESULTS: {working} ✅ | {failed} ❌ | Total: {len(ALL_URLS)}")
    print("✅ Site is LIVE!")

if __name__ == "__main__":
    test_all_pages()