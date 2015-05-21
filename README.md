# python-slack
The module will use slacker and provide command to generate data for given time period 
The module provides generate_data utility which expects slack token, time range and private group id

positional arguments:

  access_token     Access Token

  group_name       Name of the group


optional arguments:

  --oldest OLDEST  Starting point timestamp

  --latest LATEST  End point timestamp


python -m slackdata.get_history  generate_data xoxp-3000911101-3529492522 G046CBWFV --oldest="1431946770" --latest="1432033170"

Following is the sample output:

cp1-testjenkins-puppet-rjil-gate-1197:nova-compute:Service 'nova-compute' check is warning. at  2015-05-18 17:42:42.000053

gcp1-testjenkins-puppet-rjil-gate-1197:nova-compute:Service 'nova-compute' check is passing. at  2015-05-18 17:37:58.000051

gcp1-testjenkins-puppet-rjil-gate-1197:nova-compute:Service 'nova-compute' check is warning. at  2015-05-18 17:35:22.000050

gcp1-testjenkins-puppet-rjil-gate-1197:nova-compute:Service 'nova-compute' check is passing. at  2015-05-18 17:24:37.000049

gcp1-testjenkins-puppet-rjil-gate-1197:nova-compute:Service 'nova-compute' check is passing. at  2015-05-18 17:22:06.000048

gcp1-testjenkins-puppet-rjil-gate-1197:nova-compute:Service 'nova-compute' check is passing. at  2015-05-18 17:17:07.000046

