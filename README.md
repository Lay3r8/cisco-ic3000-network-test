# Network test
This repository contains two very simple webservers used to test the networking between containers deployed on the Cisco IC3000

## container_a (frontend)
This container listens on port 80. When browsing it, it will do a ```GET http://1.1.1.1``` to query container_b and display its response in a <p> element.

## container_b (backend)
Exposes a single endpoint on path / (port 80) that responds with ```{'test': 'hello world'}```

## Installation
```bash
git clone git@github.com:Lay3r8/cisco-ic3000-network-test.git
cd cisco-ic3000-network-test.git
```

## Usage
```bash
# build container A
cd container_a
./package_from_yaml.sh

# now you can deploy package.tar on the IC3000

# after deploying package.tar
cd container_a
ioxclient application activate container_a container_a/activation.json

# build container B
cd container_b
./package_from_yaml.sh

# now you can deploy package.tar on the IC3000

# after deploying package.tar
cd container_b
ioxclient application activate container_b container_b/activation.json
```
