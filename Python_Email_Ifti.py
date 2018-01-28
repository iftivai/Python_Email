import smtplib
>>> conn = smtplib.SMTP('smtp.gmail.com', 587)
>>> type(conn)
<class 'smtplib.SMTP'>
>>> conn
<smtplib.SMTP object at 0x000000000354DEB8>
>>> conn.ehlo()
(250, b'smtp.gmail.com at your service, [211.112.84.6]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
>>> conn.starttls()
(220, b'2.0.0 Ready to start TLS')
>>>conn.login ('email id', 'password')
>>>conn.sendmail('From email", 'to email', 'body of the email')
>>>conn.quit()
