## What is this?

This is supposed to be a simple implementation in Python of a Diffie-Hellman key exchange and an encryption algorithm for the sender and a decryption algorithm for the receiver.

## How does it work?

Initially both peers have picked a secret number and have agreed on a base number. They perform the DH key exchange, and then the sender encrypts some data that the user inputs and sends it to the receiver, where it is decrypted and printed. All traffic passes through the middlebox socket, which acts as a router operating between the two peers, where someone might want to read the data being sent through.

## What is it for?

Nothing much, just wanted to see if I have sufficient understanding of the underlying principles to implement it without leeching off of other people's code.

## How do I run it?

I wrote this on Windows, so there's only a 'run_ssp.bat' batch file to make running easier. That being said, if you're on Linux you can probably figure out how to run the main.py file.

Requires Python 3.8. I am not responsible if your computer catches on fire if you try running it with 3.7 or anything else.