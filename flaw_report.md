# Flaw report

## FLAW 1

### A02 Cryptographic failures: Use of hard-coded cryptographic key and password

Description: The cryptographic key used as a salt for encrypting and decryption is stored hard-coded in the program code. Knowing the salt may give unauthorized access if the hacker knows the salt and has access to some encrypted credentials. In Django projects, this key comes hard-coded as default, which may be an unpleasant surprise if the initial code is not examined thoroughly.

In addition the passwords are stored hard-coded in the program code. If a user gets access to the program code, the whole authentication system is compromised.

How to fix: Many programming languages come with a library for using environment variables. In Python, there is Python-dotenv. With dotenv, environment variables can be stored in an .env file and referenced in the code with the name of the variable. When the code is published, e.g. pushed to Github, it’s important to gitignore the .env file, so that it will not become public. There are usually places in web-services as well, where one can store the secret keys as the local .env file will not be transfered to the service.

Concerning passwords: They should be stored and encrypted so, that they cannot be recovered even by the system admin.

## FLAW 2

### A01 Broken access control: Cross-site request forgery

Description: If a user is authenticated to an application (target) and e.g. the session cookie is stored in the browser data, an another application may take advantage of this an send a request to the target application which seems to be authenticaticated. The request may be sent via various ways, e.g. by hidden forms or image tags.

How to fix: Many frameworks, e.g. Django, offer protection for cross-site request forgery by default. At least exempting the csrf protection should not be used in production build. Also generating nonces for one-time use in forms may be used. In critical requests, e.g. in online banking, additional confirmations can also be sent to the user's mobile phone.

## FLAW 3

### A03 Injection

Description: There can be many kinds of injections. This example concerns JavaScript injection. A JavaScript injection means that a user can post code to the website which is then executed on the browser. The injection can be made for example a form the content of which is then rendered to the website. If the content is then interpreted as html code with a JavaScript app, a hacker can embed a malicious app as a part of the website.

How to fix: The most important fix is a thoroughful validation of forms and converting the critical characters to such form that HTML is not executed in the content posted by the user. For example, the "<" charater can be converted to expression "&lt" which means lesser than. Some frameworks, e.g. Django has this protection as default so it is enough to not disable the protection as in this app.

## FLAW 4

### A04 Insecure design

Description: Insecure design means that you are exposing information to the end user that should be retained in secrecy. In this Django app the vulnerability is caused by leaving the debug setting as true. While this helps in the development phase, the user should not have access to local variables in production version as the variables can contain sensitive data. In debug state, the user will also have access to the source code (which is the case for open source projects in general, though).

Insecure design can occur in many forms, not just by leaving the debug state as true. Printing to console is useful in development, but exposes information if console logs or equivalent are not removed from the production version. Insecure design can also mean that the backend endpoints return all possible data as http response. Even without logs, the response can be seen from the developer console.

How to fix: In Django, the first step is to change the debug state as false. Also the console logs or such should be removed from the production version. The backend should work that way that the database is queried only to the necessary extent and only the data that is necessary for the functionality of the app is returned as http response.

## FLAW 5

### A05 Security misconfiguration: Missing custom error page

Description: The app has no customized error page or error view for failed login. Instead, the app controls the password by assertion. When the assertion fails, the page shows an error page containing Traceback with local variables and a lot of useful information for potential misuse.

How to fix: In this case a simple error message would be appropriate. No assertion or other errors should be raised. To improve safety, the message should not contain information whether the user exists in the database or not. If the existence of the username is known, hacking the password becomes easier, especially if the password is weak. Also concerning personal data privacy, a failed login should not give information if a person uses some app or not.
