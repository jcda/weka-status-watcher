#!/usr/bin/env python3
import configparser
import subprocess
import json
import os
import smtplib, ssl
import xmpp

def setconfigfile():  #set a dummy file for the config if the file couldnt be found
    #
    #   TBC
    #
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45',
                         'Compression': 'yes',
                         'CompressionLevel': '9'}
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'     # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here
    config['DEFAULT']['ForwardX11'] = 'yes'
    with open('example.ini', 'w') as configfile:
        config.write(configfile)
def readconfigfile():
    #
    #    TBC
    #
    config = configparser.ConfigParser()
       config.sections()
    
       config.read('example.ini')
    
       config.sections()
    #['bitbucket.org', 'topsecret.server.com']
    #>>> 'bitbucket.org' in config
    #True
    #>>> 'bytebong.com' in config
    # False
    #>>> config['bitbucket.org']['User']
    #'hg'
    #>>> config['DEFAULT']['Compression']
    #'yes'
    #>>> topsecret = config['topsecret.server.com']
    #>>> topsecret['ForwardX11']
    #'no'
    #>>> topsecret['Port']
    #'50022'
    #>>> for key in config['bitbucket.org']:  
    #    ...     print(key)
    #    user
    #    compressionlevel
    #    serveraliveinterval
    #    compression
    #    forwardx11
    #    >>> config['bitbucket.org']['ForwardX11']
    #    'yes'
    return(config)

def sendmail():
    #
    #   TBC
    #
    port = 465  # For SSL
    password = input("Type your password and press enter: ")

    # Create a secure SSL context
    context = ssl.create_default_context()
    
    # Try to log in to server and send email
    try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
            # Print any error messages to stdout
                print(e)
    finally:
            server.quit() 

def sendxmpp():
    username = 'username'
    passwd = 'password'
    to='name@example.com'
    msg='hello :)'


    client = xmpp.Client('gmail.com')
    client.connect(server=('talk.google.com',5223))
    client.auth(username, passwd, 'botty')
    client.sendInitPresence()
    message = xmpp.Message(to, msg)
    message.setAttr('type', 'chat')
    client.send(message)


# creation of a json model for an example
alert_dict =  {
                "action": "Change the admin user password to using 'weka user passwd' to ensure only authorized users can access the cluster",
                "description": "The admin password is still set to factory default, it should to be changed to ensure only authorized users can access the cluster",
                "muted": False,
                "title": "Default Password In Use",
                "type": "AdminDefaultPassword"
                }
print(type(alert_dict))
#the formatting of this one was just plain awful
#alerts_dict = os.system('weka alerts -f json')
alerts_dict = subprocess.check_output(["weka","alerts","-f","json"])
print(type(alerts_dict))
print(alerts_dict)
foo = str(alerts_dict)
bar = json.load(foo)
print(bar)
        
#def getstatus():

    #os.system('weka alerts -f json >> current-alerts.json')
    #alertFile = open('current-alerts.json')

    #current_status = json.load(alertFile)
    
    #foo = os.system('weka alerts -f json')
    #bar = json.dumps(foo)
    #print(type(bar))
    #print(foo)
    #print(bar)
   # current_status = json.load(alertFile)
    #for i in current_status:
    #     print(i)

    #print('------------------')

    #cmd = subprocess.Popen(["weka", "alerts","-f", "json"], bufsize=1)
    #output = cmd.communicate()

    #print('------------------')

    #foo=str(cmd)
    #print(foo)
    #alerts = json.load(str(cmd))




#if __name__ == "__main__":
##    getstatus()
#def main():
#    print(type(foo)) # <- this gives a type int)
#    print(foo)A

#with open('alerts.txt', 'w') as json_file:
#    json.dump(alert_dict, json_file)

