# pip install xlrd
# pip install pandas

import json
import pandas as pd
import datetime

def file_read (file_name):
    with open(file_name, "r") as handle:
        dictdump = json.loads(handle.read())
    # return dictdump.get('objects')
    return dictdump

def parse_json(response_dic,file_name):
    now = datetime.datetime.now()
    date_time = now.strftime('%Y-%m-%d %H:%M')
    index = 0
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

    for element in response_dic:
        if element.get('objectType') == 'parkings':
            df.loc[index] = {
                'date-time': date_time,
                '_id':element.get('_id'),
                'spaces-total':element.get('spaces').get('total'),
                'spaces-forDisabled':element.get('spaces').get('forDisabled'),
                'spaces-free':element.get('spaces').get('free'),
                'spaces-ratio':element.get('spaces').get('ratio'),
                'address-street':element.get('address').get('street').get('ru'),
                'address-house':element.get('address').get('house').get('ru'),
                'category': str(element.get('category')),
                'contacts': element.get('contacts').get('ru'),
                'description': element.get('description').get('ru'),
                'center': str(element.get('center')).replace("'",'"'),
                'location': str(element.get('location')).replace("'",'"')
            }
            index = index + 1

    df.to_csv(file_name, \
              encoding='utf-8', \
              header=False, \
              mode='a', \
              index=False, \
              sep=";", \
              na_rep='?', \
              quotechar='"', \
              doublequote=True)
    return True
# s.replace("'", r"\'")
# parse_json(file_read('2020-08-29 19 35 06.json'),'test.csv')
