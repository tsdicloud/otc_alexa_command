# Steps to Install the demo #

## Service to receive Alexa commands ##

Use script `install otc_service.sh` on a small machine with EIP on the internet.

## Quickly create a self-signed certificate for testing ##
```
> openssl req -x509 -sha256 -nodes-days 730  -newkey rsa:4096 -keyout alexa_otc_ss.key -out alexa_otc_cert.pem 
```


## OPen up internal firewall on centos 
```
> sudo firewall-cmd --permanent --zone=public --add-port=5443/tcp --add-service=https
```

## Multi language support ##
```
pybabel extract -F babel.cfg -o messages.pot .
```
creates a language label file.

```
pybabel init -i messages.pot -d translations -l de
pybabel update -i messages.pot -d translations 
```
create the required files for language de.

```
pybabel compile -d translations
```

