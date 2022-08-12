# Leveraging Machine Learning to Reduce Cold Start Latency of Containers in Serverless Computing

`git clone https://github.com/ryanbannon/openwhisk.git`

`sudo bash ~/openwhisk/install.sh > ~/installation.log`

### Server 1:
#### Experiment 1:
`sudo nohup /tmp/jmeter/bin/jmeter.sh -n -t "/home/ubuntu/openwhisk/jmeter/Experiment_1/Experiment_1.jmx" -l "/home/ubuntu/experiment_1_logs.csv" > /home/ubuntu/experiment_1.log &`

#### Experiment 1_2:
`sudo nohup python /home/ubuntu/openwhisk/controller.py 1 experiment_serverless_1 & /tmp/jmeter/bin/jmeter.sh -n -t "/home/ubuntu/openwhisk/predictions/Experiment_1/Experiment_1_2.jmx" -l "/home/ubuntu/experiment_1_2_logs.csv" > /home/ubuntu/experiment_1_2.log &`

### Server 2:
#### Experiment 2:
`sudo nohup /tmp/jmeter/bin/jmeter.sh -n -t "/home/ubuntu/openwhisk/jmeter/Experiment_2/Experiment_2.jmx" -l "/home/ubuntu/experiment_2_logs.csv" > /home/ubuntu/experiment_2.log &`

#### Experiment 2_2:
`sudo nohup python /home/ubuntu/openwhisk/controller.py 2 experiment_serverless_2 & /tmp/jmeter/bin/jmeter.sh -n -t "/home/ubuntu/openwhisk/predictions/Experiment_2/Experiment_2_2.jmx" -l "/home/ubuntu/experiment_2_2_logs.csv" > /home/ubuntu/experiment_2_2.log &`
