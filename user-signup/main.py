import webapp2
import re


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)


PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASS_RE.match(password)


EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return EMAIL_RE.match(email)


def build_page(textarea_content):
    user_label = "<label>Username:</label>"
    username = "<input type='text' name='username'/>"

    pass_label = "<label>Password:</label>"
    password = "<input type="password" name="password">"

    verify_label = "<label>Verify Password:</label>"
    verify = "<input type="password" name="verify">"

    email_label = "<label>Email(Optional)</label>"
    email = "<input type="text" name="email">"

    submit = "<input type='submit'/>"
    form = ("<form method='post'>"
            + user_label + username + "<br>"
            + pass_label + password + "<br>"
            + verify_label + verify + "<br>"
            + email_label + email + "<br>"
            + submit + "</form>")

    header = "<h1>User Signup</h1>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        params = dict(username = username, email = email)


        if not valid_username(username):
            params['error_username'] = "That's not a valid username."
            have_error = True

        if not valid_password(password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif password != verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True

        if not valid_email(email):
            params['error_email'] = "That's not a valid email."
            have_error = True

        if have_error:
            self.post(form)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)