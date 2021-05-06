------------------------------
 COMP3025 Final Year Project
------------------------------

---Understanding the folder---
The folder name listed below is the process of each step:
*Please note that each of these folder contains its own README file to explains its purpose.
1. dataset
2. cnn_training
3. trained_model

The final implementation file is real-time-detection.py

-----------------------------------------------------------------------------------------------
---How to run this project on Raspberry Pi?---

Run the following command in the terminal to install dependencies:

1. git clone "link of this repository"
2. pip3 install -r raspirequirements.txt
3. sudo apt install -y libatlas-base-dev liblapacke-dev gfortran
4. sudo apt install -y libhdf5-dev libhdf5-103
5. pip3 install -r requirements.txt
6. wget "https://raw.githubusercontent.com/PINTO0309/Tensorflow-bin/master/tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh"
7. chmod +x ./tensorflow-2.4.0-cp37-none-linux_armv7l_download.sh
8. pip3 install tensorflow-2.4.0-cp37-none-linux_armv7l.whl

---Execute the project---
*Make you your terminal is in the cloned folder directory, then execute:

1. python3 real-time-detection.py
2. press "q" on keyboard to quit the program

---Hardware Setup---
Raspberry Pi 4 Computer Model B 8GB RAM
Raspberry Pi Camera Module
Monitor

---How to run this project on personal computer?---
Run the following command in the terminal to install dependencies:

1. pip install requirements.txt

---Execute the project---
*Make you your terminal is in the cloned folder directory, then execute:
1. python3 real-time-detection.py
2. press "q" on keyboard to quit the program


