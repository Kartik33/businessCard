from django.test import Client,TestCase,override_settings


#class LoginTestCase(TestCase):
#    def test_login(self):
#        c = Client()
#        response = c.post("/login/",
#                {"username":'kk19011','password':'word123Won'}
#                )
#        self.assertRedirects(response,'/users/30/')


class SignupTestCase(TestCase):
    def test_signup(self):
        c = Client()
        response = c.post("/signup/",
                {"username":"kartik",
                    "password1":"word123Won",
                    "password2":"word123Won"})
        print(response)
        self.assertRedirects(response,'/users/1/')
