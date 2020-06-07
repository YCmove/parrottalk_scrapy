import json
import csv
import pprint
import requests
import http.client as http_client

from setting import headers, cookies
from tools import cookieChangeToDict



def main():
    pp = pprint.PrettyPrinter(indent=4)
    # http_client.HTTPConnection.debuglevel = 1



    # search_url = 'https://www.vocabulary.com/dictionary/definition.ajax?search={}&lang=en'.format()



    r = requests.get(url='https://www.parrottalks.com/api/catalogs?__rnd=1562310364589&note_only=1', headers=headers, cookies=cookieChangeToDict(cookies))
    restext = json.loads(r.text)
    # print("r.status_code: ", r.status_code)
    print("len of restext: ", len(restext))

    for cate in restext:
        print("cate name: ", cate["name"])
        print("cate id: ", cate["id"])

        questions_api = "https://www.parrottalks.com/api/catalog/{}/questions?__rnd=1562313870160".format(cate["id"])

        res = requests.get(url=questions_api, headers=headers, cookies=cookieChangeToDict(cookies))
        res_text = json.loads(res.text)

        print("res_text: ", res_text)

        continue

        with open('./books/parrot_{}.csv'.format(cate["name"]), 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', doublequote=True)
            for vocab in res_text:
                # pp.pprint(vocab)
                if 'sentence' in vocab.keys():
                    spamwriter.writerow([vocab['id'], vocab['question'], vocab['answer'], vocab['sentence']['text']])
                else:
                    spamwriter.writerow([vocab['id'], vocab['question'], vocab['answer']])




if __name__ == "__main__":
    main()