# RSAencryption
Code to try and encrypt messages into RSA form

This code is not finished. I ran into a bug that does not find the correct relative prime number needed to ecrypt the message. I will be trying to fix the bug and update the code. Each update will say "Update" along with a date.

Update 1 (March 20th/2016): I changed the code slightly. I realized that all the numbers that can be set as 'e' are all prime numbers. Instead of searching for the first prime number, I found all the prime numbers from the range 1<i<n, added them to a list and selected one at random; also made sure that n%e != 0. My next task is to find d.

Update 2 (March 21st/2016): I found the value for d, which is used for the private key encryption. I have created the encryption code, however I have not created the decrytion code yet. I am thinking of trying to implement my own version of the Square and Multiply alogrithm to decrpyt the messages.
