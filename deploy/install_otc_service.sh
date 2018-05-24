#!/bin/bash
sudo yum update
sudo yum install python-pip python-devel openssl openssl-devel gcc install unzip  
sudo pip install --upgrade pip
sudo pip install "Flask==0.12.1" "cryptography<2.2" Flask-Ask Flask-Babel shade oslo-log python-magic

GREEN='\033[0;32m'
NC='\033[0m'

mkdir -p ${HOME}/.config/openstack

OTCCERT_FILENAME="${HOME}/.config/openstack/otc_certs.pem"
SHADE_CONFIG_FILENAME="${HOME}/.config/openstack/clouds.yml"
if [ ! -f ${SHADE_CONFIG_FILENAME} ]; then
echo "clouds:  
  otc-alexa:  
    region_name: eu-de  
    identity_api_version: 3  
    verify: True
    cacert: ${OTCCERT_FILENAME} 
    auth:  
      username: '<your alexa username here; a dedicated IAM recommended>'  
      password: '<your authentication token here>'  
      project_domain_name: '<tenant-id OTC00xxxxxxxx1xxxxx>'  
      project_name: 'eu-de'  
      tenant_name: eu-de  
      user_domain_name: '<tenant-id OTC00xxxxxxxx1xxxxx>'  
      auth_url: 'https://iam.eu-de.otc.t-systems.com/v3'" > ${SHADE_CONFIG_FILENAME}
fi

if [ ! -f ${OTCCERT_FILENAME} ]; then
   cp ./otc_certs.pem ${OTCCERT_FILENAME}
fi

echo
echo
echo -e "${GREEN}Adapt your openstack configuration in ${SHADE_CONFIG_FILENAME}"
echo -e "${GREEN}Check configuration with 'python -m os_client_config.config'${NC}"
