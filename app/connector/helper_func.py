import string, random
import pickledb
from flask import current_app

def store_to_db(original_url):
    print(f"Storing URL: {original_url}")
    try:
        db = pickledb.load('url_db.db', auto_dump=True)
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        print(f"Generated short URL: {short_url}")
        
        # Store the original URL with the generated short URL
        db.set(short_url, original_url)
        db.dump()
        
        print(f"Short URL generated: {short_url} for {original_url}")
        return True
    
    except Exception as e:
        print(f"Error storing URL: {e}")
        return False

def get_all_urls():
    try:
        db = pickledb.load('url_db.db', auto_dump=True)
        urls = db.getall()
        print(f"Retrieved URLs: {urls}")
        return urls
    except Exception as e:
        print(f"Error retrieving URLs: {e}")
        return None