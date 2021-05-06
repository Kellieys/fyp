# COMP3025 Final Year Project
## Understanding the folder
#### The folder name listed below is the process of each step:
##### *Please note that each of these folder contains its own README file to explains its purpose and what has been done to achieve the outcome.
<ol>
<li>dataset</li>
<li>cnn_training</li>
<li>trained_model</li>
</ol>

#### The final implementation file is real-time-detection.py

#
## How to run this project on Raspberry Pi?
#### Run the following command in the terminal to install dependencies: 
<ol>
<li>git clone "link of this repository"</li>
<li>pip3 install -r raspirequirements.txt</li>
<li>sudo apt install -y libatlas-base-dev liblapacke-dev gfortran</li>
<li>sudo apt install -y libhdf5-dev libhdf5-103</li>
<li>pip3 install -r requirements.txt</li>
<li>wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh"</li>
<li>chmod +x ./tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh</li>
<li>pip3 install tensorflow-2.4.0-cp37-none-linux_armv7l.whl</li>
</ol>

#### Execute the project
#### *Make you your terminal is in the cloned folder directory, then execute:
<ol>
<li>python3 real-time-detection.py</li>
<li>press "q" on keyboard to quit the program</li>
</ol>

#### Hardware Setup:
<li> Raspberry Pi 4 Computer Model B 8GB RAM </li>
<li> Raspberry Pi Camera Module </li>
<li> Monitor </li>

#
## How to run this project on personal computer?
#### Run the following command in the terminal to install dependencies: 
<ol>
<li>pip install requirements.txt</li>
</ol>

#### Execute the project
#### *Make you your terminal is in the cloned folder directory, then execute:
<ol>
<li>python3 real-time-detection.py</li>
<li>press "q" on keyboard to quit the program</li>
</ol>