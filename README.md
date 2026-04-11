# Serial System Suite

Serial System Suite (SSS) is an application created as a test project for testing and communicating with serial ports

Serial System Suite — V1.3.3



#### Overview

Version 3 of Serial System Suite is a lightweight desktop application for basic serial communication.

It allows users to detect, connect, send data and read data from a serial (COM). This version establishes the foundation for a larger industrial monitoring platform.



#### Features

Connect to available COM ports

Select baud rate

Manual connect / disconnect

Status indication (connected / disconnected)

See the incoming data as decimal

Send data as decimal

User Interface

The interface is minimal and focused on functionality:

This version follows a simple but scalable structure:

The separation ensures future extensibility.



#### How It Works

Open port settings

Select a COM port

Choose a baud rate

Apply the settings

Connect to the device

Write data in TX

Click send to send the data



#### Installation

git clone https://github.com/MathewADB/serial-system-suite

cd serial-system-suite

pip install -r requirements.txt

python main.py



#### Usage

Launch the application

Select the desired COM port from available ports

Connect and communicate with the port

