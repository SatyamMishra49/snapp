import string
import random
from pickledb import PickleDB


def p_db(original_url):
    print(f"Storing URL: {original_url}")
    try:
        db = PickleDB('d.db')
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        print(f"Generated short URL: {short_url}")
        
        # Store the original URL with the generated short URL
        db.set(short_url, original_url)
        db.save()

        print(f"Short URL generated: {short_url} for {original_url}")
        return True
    
    except Exception as e:
        print(f"Error storing URL: {e}")
        return False
    

def get_url():
    try:
        db = PickleDB('d.db')
        urls = db.all()
        print(f"Retrieved URLs: {urls}")
        return urls
    except Exception as e:
        print(f"Error retrieving URLs: {e}")
        return None