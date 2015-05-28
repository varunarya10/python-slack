# python-slack
The module will use slacker and provide command to generate data for given time period 
The module provides generate_data utility which expects slack token, time range and private group id

positional arguments:

  access_token     Access Token

  group_name       Name of the group

  start_date

  end_date


python -m slackmon.get_history  generate_data xoxp-3000911101-3529492522 G046CBWFV "22-05-2015" "28-05-2015"



python -m slackdata.get_history  generate_excel xoxp-3000911101-3529492522 G046CBWFV "22-05-2015" "28-05-2015"
