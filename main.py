from asnake.client import ASnakeClient
from aspipe2 import *
def main():
    from secrets import baseurl, username, password
    
    # Initialize client
    client = ASnakeClient(baseurl=baseurl, username=username, password=password)
    client.authorize()
    
    # Fetch archival objects details
    objects = fetch_archival_objects_details(client)
    
    # Save to JSON
    save_archival_objects_to_json(objects)
    
    print(f"Processed {len(objects)} archival objects")

if __name__ == "__main__":
    main()