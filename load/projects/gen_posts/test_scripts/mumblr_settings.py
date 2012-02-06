###############################################################################
# Settings file for mumblr load tests
###############################################################################

# base URL of installation
BASE_URL = 'http://ec2-50-17-153-135.compute-1.amazonaws.com'
LOGIN_URL = BASE_URL + '/admin/login'

# the maximum number of threads you plan to run for each test
# (specifies user pool size for each test script)
MAX_THREADS = 5

ADMIN_USERNAME = 'user_'
ADMIN_PASS = 'asdfjk'
