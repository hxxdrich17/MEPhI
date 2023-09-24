def send_email(message, description):
    import smtplib
    user = "moskalenkoivan228@gmail.com"
    pwd = "qzamslowevukndls"
    to = "add-to-things-mjxs3oi5cu1ls8ifd61@things.email"
    
    message = f"subject:{message}\n\n{description}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user, pwd)
        print([message])
        server.sendmail(user, to, message)
        server.close()
        return True
    except:
        return False
    
print(send_email("hello", "let's\ngooooo"))