# Steps to Install the demo #

## Service to receive Alexa commands ##

Use script `install otc_service.sh` on a small machine with EIP on the internet.

## Quickly create a self-signed certificate for testing ##
```
> openssl req -x509 -sha256 -nodes-days 730  -newkey rsa:4096 -keyout alexa_otc_ss.key -out alexa_otc_cert.pem 
```


## Open up internal firewall on centos ##
```
> sudo firewall-cmd --permanent --zone=public --add-port=5443/tcp --add-service=https
```

## Multi language support ##

Create a language label file (once):
```
cd src
pybabel extract -F babel.cfg -o messages.pot .
```

Start a new language (e.g. for language de):
```
cd src
pybabel init -i messages.pot -d translations -l de
```

Update the language label translation file with new/chaged labels:
```
cd src
pybabel update -i messages.pot -d src/translations 
```

Finally, compile the messages:
```
cd src
pybabel compile -d translations
```

