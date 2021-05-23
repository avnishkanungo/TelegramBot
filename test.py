import requests
import time
import datetime

date = datetime.datetime.now()
date_formatted = date.strftime('%d-%m-%Y')

# print(date_formatted)

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

params = dict(
    district_id='770',
    date= date_formatted,
)

resp = requests.get(url=url,params=params,headers=headers)
data = resp.json() # Check the JSON Response Content documentation below
# print(data['centers'][0]['sessions'][0]['available_capacity_dose1'])

n=0

for i in data['centers']:
    for k in i['sessions']:
        if ( k['available_capacity_dose1'] > 0):
            print(i['address'])
            params1 = dict(
                    chat_id= 976114231,
                    text = i['address'],
                    )
            
            tele_url= 'https://api.telegram.org/bot1839665801:AAFNxc7cPaYv3-TLkV7T-guCUUZeb4eEnfM/sendMessage'
            requests.post(tele_url, params = params1)
else:
    tele_url= 'https://api.telegram.org/bot1839665801:AAFNxc7cPaYv3-TLkV7T-guCUUZeb4eEnfM/sendMessage?chat_id=976114231&text= No Centers Available'
    requests.post(tele_url)

        


            

