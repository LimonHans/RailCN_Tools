# encoding: utf-8
#############################
#   Project: RailCN_Tools   #
#  Developed by HansLimon.  #
#                           #
#    Created: 2024/05/15    #
# Last modified: 2024/05/15 #
#############################
import requests

class Crawler:
    cookie: str
    def __init__(self):
        with open("cookie.txt", "r") as f:
            self.cookie = f.read()
        if len(self.cookie) < 10:
            raise Exception("Cookie is empty!")
    def enquiry(self, start_code: str, end_code: str, date: str):
        url = f"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={start_code}&leftTicketDTO.to_station={end_code}&purpose_codes=ADULT"
        headers = {
            'cookie': self.cookie
        }
        response = requests.get(url = url, headers = headers).json()
        all_trains = {}
        for now_response in response['data']['result']:
            split_resp = now_response.split('|')
            info = {
                '发时': split_resp[8],
                '历时': split_resp[10],
                '终时': split_resp[9],
                '商务/特等座': split_resp[32],
                '一等座': split_resp[31],
                '二等座': split_resp[30],
                '高级软卧': split_resp[21],
                '软卧/一等卧': split_resp[23],
                '硬卧/二等卧': split_resp[28],
                '软座': split_resp[24],
                '硬座': split_resp[29],
                '无座': split_resp[26]
            }
            # info['动卧'] = 0
            all_trains[split_resp[3]] = info
        return all_trains