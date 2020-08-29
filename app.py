import requests
import json
import schedule
import datetime
import time
import pandas as pd
from parse import parse_json

URL = 'https://parkingkzn.ru/api/2.12/objects'

def get_structure (URL):
    response = requests.request("GET", URL, timeout=100)
    try:
        response_json = json.loads(response.text)
        return response_json.get('objects')
    except Exception as exp:
        print(str(exp))
        return None




def create_file ():
    now = datetime.datetime.now()
    date_string = now.strftime('%Y-%m-%d')
    file_name = date_string + ".csv"
    df = pd.DataFrame (columns = ['date-time', \
                                  '_id', \
                                  'spaces-total', \
                                  'spaces-forDisabled', \
                                  'spaces-free', \
                                  'spaces-ratio', \
                                  'address-street', \
                                  'address-house', \
                                  'category', \
                                  'contacts', \
                                  'description', \
                                  'center', \
                                  'location'])
    df.to_csv(file_name, \
              encoding='utf-8', \
              header=True, \
              mode='a', \
              index=False, \
              sep=";", \
              na_rep='?', \
              quotechar='"', \
              doublequote=True)



    return file_name
# create_file ()


def dataset_p (json_structure):
    now = datetime.datetime.now()
    date_string = now.strftime('%Y-%m-%d %H %M %S')
    file_dataset = date_string + '.json'

    with open(file_dataset, 'w', encoding='utf-8') as f:
        json.dump(json_structure, f, ensure_ascii=False, indent=4)
# dataset_p (get_structure (URL))

def run_task():
    now = datetime.datetime.now()
    date_string = now.strftime('%Y-%m-%d')
    file_name = date_string + ".csv"
    parse_json(get_structure (URL),file_name)
#
#------------------------------------------------------
# Create schedule
#------------------------------------------------------
schedule.every(15).minutes.do(run_task)
schedule.every().day.at('00:00').do(create_file)
# schedule.every().day.at('14:00').do(report_run)
# schedule.every().day.at('15:00').do(report_run)

print('Service starting.....')
while True:
    print(datetime.datetime.now())
    schedule.run_pending()
    time.sleep(60)
#






