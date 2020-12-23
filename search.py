import pprint
import settings as my_settings
from googleapiclient.discovery import build


def search_main(query):
    service = build("customsearch", "v1",
                    developerKey=my_settings.GOOGLE_API_KEY)

    result = service.cse().list(
        q=query,
        cx=my_settings.GOOGLE_CSE_KEY,
    ).execute()
    # print("response", result)
    try:
        items = result["items"]
        top_five_links = []
        for i,item in enumerate(items):
            if(len(top_five_links) < 5):
                top_five_links.append(str(i+1)+". "+item["link"])
        pprint.pprint(result["items"])
        # print(top_five_links)
        return top_five_links
    except Exception as e:
        print('Exception raised in search :', str(e))
        return
