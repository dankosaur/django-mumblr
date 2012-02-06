import cookielib
import mechanize
import weakref
from mumblr_settings import *

class UserPool(object):
    def __init__(self, size=MAX_THREADS, username=ADMIN_USERNAME):
        self.in_users = []
        self.out_users = {}
        for i in xrange(size):
            print "Filling pool with", username
            (cj, br) = _init_browser()
            u = User(username, cj, br, self)
            self.in_users.append(u)

    def checkout(self):
        u = self.in_users.pop()
        self.out_users[u] = True
        return u

    def checkin(self, u):
        del self.out_users[u]
        self.in_users.append(u)

class User(object):
    def __init__(self, user, cj, br, pool):
        self.user = user
        self.cj = cj
        self.br = br
        self.logged_in = False
        self.pool = weakref.proxy(pool)

    def ensure_logged_in(self):
        if not self.logged_in:
            _login(self.br, self.user, ADMIN_PASS)
            self.logged_in = True
        return

    def checkin(self):
        self.pool.checkin(self)

    def __str__(self):
        return "User<user=%s,logged_in=%s>" % (self.user, self.logged_in)

# utility functions
def _init_browser():
    """Returns an initialized browser and associated cookie jar."""
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    return cj,br

def _login(br, u, p):
    _ = br.open(LOGIN_URL)

    print LOGIN_URL

    br.select_form(nr=0)
    print br.form
    br.form['username'] = u
    br.form['password'] = p
    r = br.submit()
    assert (r.code == 200), 'Bad HTTP Response'
