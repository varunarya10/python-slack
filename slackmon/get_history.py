import argparse
import time
import datetime
import re
from pandas import DataFrame
from slacker import Slacker

class GenerateData(object):
  'Class to generate report for the given time period'

  def __init__(self, group_name, access_token, oldest, latest):
    self.group_name = group_name
    self.access_token = access_token
    self.oldest = int(time.mktime(datetime.datetime.strptime(oldest, "%d-%m-%Y").timetuple()))
    self.latest = int(time.mktime(datetime.datetime.strptime(latest, "%d-%m-%Y").timetuple()))
  
  def get_connection(self):
    slack = Slacker(self.access_token)
    return slack

  def get_group_history(self):
    conn = self.get_connection()
    history = conn.groups.history(self.group_name, latest=self.latest, oldest=self.oldest).body
    return history
  
  def generate_data(self):
    capture_data = []
    history_data = self.get_group_history()
    for text in history_data["messages"]:
      test = re.search('.*:.*:Service .* check is .*', text['text'])
      if test != None:
        stgdata = test.group(0).split(":")
        status = stgdata[2].split(" ")
        capture_data.append( {"host":stgdata[0] ,"service": stgdata[1],"status": status[4], "time_of": datetime.datetime.fromtimestamp(float(text["ts"]))} )
    return capture_data
  
  def generate_excel(self):
    data = self.generate_data()
    if data:
      dataframe = DataFrame(data)
      dataframe.to_excel('data.xlsx', sheet_name='sheet1', index=False)
      print "Generated Excel Sheet with name data.xlsx"
    else:
      print "No data found"
  
    

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers(dest='action', help='Action to perform')

    getdata_parser  = subparsers.add_parser('generate_data', help='Generate data ')
    getdata_parser.add_argument('access_token', help='Access Token')
    getdata_parser.add_argument('group_name', help='Name of the group')
    getdata_parser.add_argument('start_date', help='Starting point timestamp')
    getdata_parser.add_argument('end_date', help='End point timestamp')

    getexl_parser  = subparsers.add_parser('generate_excel', help='Generate Excel ')
    getexl_parser.add_argument('access_token', help='Access Token')
    getexl_parser.add_argument('group_name', help='Name of the group')
    getexl_parser.add_argument('start_date', help='Log start date in format of dd-mm-yyyy')
    getexl_parser.add_argument('end_date', help='Log end date in format of  dd-mm-yyyy')


    args = argparser.parse_args()
    if args.action == 'generate_data':
        generatedata = GenerateData(args.group_name, args.access_token, args.start_date, args.end_date)
        print generatedata.generate_data()    
    if args.action == 'generate_excel':
        generatedata = GenerateData(args.group_name, args.access_token, args.start_date, args.end_date)
        print generatedata.generate_excel() 
