import argparse
import datetime
import re
from slacker import Slacker

class GenerateData(object):
  'Class to generate report for the given time period'

  def __init__(self, group_name, access_token, oldest, latest):
    self.group_name = group_name
    self.access_token = access_token
    self.oldest = oldest
    self.latest = latest
  
  def get_connection(self):
    slack = Slacker(self.access_token)
    return slack

  def get_group_history(self):
    conn = self.get_connection()
    history = conn.groups.history(self.group_name, latest=self.latest, oldest=self.oldest).body
    return history
  
  def generate_data(self):
    history_data = self.get_group_history()
    for text in history_data["messages"]:
      test = re.search('.*:.*:Service .* check is .*', text['text'])
      if test != None:
        print "%s at  %s" %(test.group(0),datetime.datetime.fromtimestamp(float(text["ts"])))
    
    

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    subparsers = argparser.add_subparsers(dest='action', help='Action to perform')

    getdata_parser  = subparsers.add_parser('generate_data', help='Generate data ')
    getdata_parser.add_argument('access_token', help='Access Token')
    getdata_parser.add_argument('group_name', help='Name of the group')
    getdata_parser.add_argument('--oldest', help='Starting point timestamp')
    getdata_parser.add_argument('--latest', help='End point timestamp')

    args = argparser.parse_args()
    if args.action == 'generate_data':
        generatedata = GenerateData(args.group_name, args.access_token, args.oldest, args.latest)
        print generatedata.generate_data()     
