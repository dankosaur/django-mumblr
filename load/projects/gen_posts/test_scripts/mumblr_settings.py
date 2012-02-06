###############################################################################
# Settings file for mumblr load tests
###############################################################################

# base URL of installation
BASE_URL = 'http://dev.tracelytics.com:8080'
LOGIN_URL = BASE_URL + '/admin/login'

# the maximum number of threads you plan to run for each test
# (specifies user pool size for each test script)
MAX_THREADS = 5

ADMIN_USERNAME = 'testuser'
ADMIN_PASS = 'asdfjk'
