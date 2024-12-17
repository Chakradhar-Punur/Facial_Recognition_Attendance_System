# Facial Recognition Attendance System

This repository contains a Facial Recognition Attendance System implemented in Python. It leverages modern image processing and face recognition libraries to automate the process of attendance marking.

## Features

	1.	Face Encoding: The system encodes faces from images stored in the attendance_dataset directory.
	2.	Real-Time Recognition: Recognizes faces using a webcam feed and matches them against the encoded dataset.
	3.	Attendance Logging: Automatically logs attendance in a CSV file with a timestamp when a recognized face is detected.

## How It Works

The project consists of two main components:

### 1.	Data Preparation and Encoding:

	1.	Encodes all the images in the attendance_dataset folder into face embeddings using face_recognition.
	2.	Saves the encodings into a serialized file (encodePickle) for future use.
 
### 2.	Real-Time Face Recognition:

	1.	Captures a live video feed using a webcam.
	2.	Identifies faces in real-time and compares them with the pre-encoded dataset.
	3.	Marks attendance in the attendance.csv file when a match is found.

## Project Workflow

	1.	Data Gathering: Store face images in the dataset folder.
	2.	Encoding: Generate face embeddings using face_recognition.
	3.	Real-Time Detection: Compare webcam-detected faces with the dataset.
	4.	Attendance Logging: Automatically mark attendance for recognized individuals.

## Results

The system identifies individuals accurately in real-time, marking their attendance efficiently. It’s robust, scalable, and ideal for environments requiring automated attendance management.

## Authors

	•	Chakradhar Punur
	•	Bhargava M
	•	Aditya Anand

M.S. Ramaiah Institute of Technology, 2022.
