#!/bin/bash
#This is a shell script for lab 6 Homework Assignment
# Script for saying the current local time

#variable that includes the date and the string literal
NOW=$(date + " The current time is %M past %I %p ")

echo $NOW

#commmand for generating a TTS file and incorporating the variable. This must show some variation from the one in class. 
pico2wave -w TTSdate.wav "$NOW"

#command for playing back the TTS audio file. This must show some variation from the one in class. 

aplay TTSdate.wav
