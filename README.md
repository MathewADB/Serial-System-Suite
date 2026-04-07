# Serial System Suite

Serial System Suite (SSS) is an application created as a test project for testing serial ports

Serial System Suite — V1.1.3



#### Overview

Version 1 of Serial System Suite is a lightweight desktop application for basic serial communication.

It allows users to detect and connect to a serial (COM). This version establishes the foundation for a larger industrial monitoring platform.



#### Features

Connect to available COM ports

Select baud rate

Manual connect / disconnect

Status indication (connected / disconnected)

User Interface

The interface is minimal and focused on functionality:

This version follows a simple but scalable structure:

The separation ensures future extensibility.



#### How It Works

Select a COM port

Choose a baud rate

Connect to the device



#### Installation

git clone https://github.com/MathewADB/serial-system-suite

cd serial-system-suite

pip install -r requirements.txt

python main.py



#### Usage

Launch the application

Select the desired COM port

Click connect

