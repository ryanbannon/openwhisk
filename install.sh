sudo apt-get update

# Set up the repository
sudo apt-get install --assume-yes ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install --assume-yes docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo docker --version
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
sudo docker-compose --version

# Install OpenWhisk
sudo git clone https://github.com/apache/openwhisk-devtools.git
sudo apt --assume-yes install make npm zip unzip python-pip
#sudo git clone https://github.com/ryanbannon/openwhisk.git
sudo unlink /etc/resolv.conf
sudo cp ~/openwhisk/resolv.conf /etc/resolv.conf
sudo chmod 444 /etc/resolv.conf
sudo cp ~/openwhisk/Makefile ~/openwhisk-devtools/docker-compose/Makefile
sudo make -C openwhisk-devtools/docker-compose/ quick-start

# Install Java & JMeter
#sudo apt update
#sudo apt install openjdk-11-jdk --assume-yes
#sudo wget https://downloads.apache.org/jmeter/binaries/apache-jmeter-5.4.3.zip
#sudo unzip apache-jmeter-5.4.3.zip
#sudo mv apache-jmeter-5.4.3 jmeter
#sudo mv jmeter /tmp
#echo 'export PATH="$PATH:/tmp/jmeter/bin"' >> ~/.bashrc
#source ~/.bashrc

# Install OpenWhisk CLI
sudo cp openwhisk/wsk /usr/bin
sudo chmod +x /usr/bin/wsk
sudo wsk property set --apihost 'localhost' --auth '23bc46b1-71f6-4ed5-8c54-816aa4f8c502:123zO3xZCLrMN6v2BKK1dXYFpXlPkccOFqm12CdAsMgRU4VrNZ9lyGVCGuMDGIwP'
