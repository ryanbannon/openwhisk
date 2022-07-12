sudo apt-get update

# Set up the repository
sudo apt-get install --assume-yes ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install --assume-yes docker-ce docker-ce-cli containerd.io docker-compose-plugin
#sudo docker --version
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
#sudo docker-compose --version

# Install OpenWhisk
sudo git clone https://github.com/apache/openwhisk-devtools.git
sudo apt --assume-yes install make npm zip unzip python-pip 
sudo unlink /etc/resolv.conf
sudo cp ~/openwhisk/resolv.conf /etc/resolv.conf
sudo chmod 444 /etc/resolv.conf
sudo cp ~/openwhisk/Makefile ~/openwhisk-devtools/docker-compose/Makefile
sudo make -C ~/openwhisk-devtools/docker-compose/ quick-start

# Install Java & JMeter
sudo apt update
sudo apt install openjdk-11-jdk --assume-yes
sudo wget https://downloads.apache.org/jmeter/binaries/apache-jmeter-5.4.3.zip
sudo unzip apache-jmeter-5.4.3.zip
sudo mv apache-jmeter-5.4.3 jmeter
sudo mv jmeter /tmp
echo 'export PATH="$PATH:/tmp/jmeter/bin"' >> ~/.bashrc
source ~/.bashrc

# Install OpenWhisk CLI
sudo cp ~/openwhisk/wsk /usr/bin
sudo chmod +x /usr/bin/wsk
sudo wsk property set --apihost 'localhost' --auth '23bc46b1-71f6-4ed5-8c54-816aa4f8c502:123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP'

# Create OpenWhisk actions for Azure Dataset load execution
sudo wsk -i action create 313c03f53a0d31f70aec25f62efb33e7dd779725ca4af579018452d1204beaad --kind python:3 python_function.py
sudo wsk -i action create 155e47f8e7f751d0c845049456d01832013c61336a8cd85901330ac821a71534 --kind python:3 python_function.py
sudo wsk -i action create c9f8e30e36d1aef62c10b3cfca6e289a93848a148d876dd514753040314f4817 --kind python:3 python_function.py
sudo wsk -i action create bd5be891d0d10fbc3c59215d5f8159ea496433bc41adba7d8d10ea21d35c3e3a --kind python:3 python_function.py
sudo wsk -i action create 905e6674359f6487df567fa2c8ca1c8641e7740f2e32d9fd26e9fe1ff7a4670d --kind python:3 python_function.py
sudo wsk -i action create 30aa434528bc68ee07745ee7be3a0bdb33d58961fdc8460ce5b5b46b4def96e8 --kind python:3 python_function.py
sudo wsk -i action create 9b61fd55aa093a2d172db1a68a60af5cf6cbfa7f5ea1fbc71846027a5954616d --kind python:3 python_function.py
sudo wsk -i action create 619caebdeff262e3b78a18e5c54a48f33f871f4210d57657e7fe4ce847e5a22c --kind python:3 python_function.py
sudo wsk -i action create cc5bb2108cc7daf53f9728ad21f661a8ef9c8b36284bacfcb712e2be87eef842 --kind python:3 python_function.py
sudo wsk -i action create 762835950e81a11cd04cedcb05275dc111c651625d575077fce49f82170e0986 --kind python:3 python_function.py
sudo wsk -i action create 8e5f533dbf1092f56ac6c7542ef3bdec4661bd442c9b5e7537fabc7b8c03f5a8 --kind python:3 python_function.py
sudo wsk -i action create 090691f051acb420d7663cd61db5ade89ca57b3516a14600758c5003015f4d42 --kind python:3 python_function.py
sudo wsk -i action create 41630cdded05ac1d73e45a72ff07c22e90fe6b1d537c5825377a983998c05ad0 --kind python:3 python_function.py
sudo wsk -i action create 4ce7573ec82ce8a37bc9e2a3f45343b2fccf86faa0a8d1507b59424ca1948aa9 --kind python:3 python_function.py
sudo wsk -i action create 58b5ab07aba3f2312b7c99f7d4561e7195fa81744cad27b6e989fbdbb5c6eac7 --kind python:3 python_function.py
sudo wsk -i action create 0b1826008749cba0443c854732e217364d96c3f6d124b510f1e6b2dd847cffca --kind python:3 python_function.py
sudo wsk -i action create 52543d2fdbdfb711086dbf73725c9b5866f6e6d08cbf9afa054272689043c6cf --kind python:3 python_function.py
sudo wsk -i action create 88261f9085de9ebc40ecb55d4fa39d839a00ba792a1b741a26ca926114aab474 --kind python:3 python_function.py
