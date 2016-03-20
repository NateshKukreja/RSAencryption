# RSAencryption
Code to try and encrypt messages into RSA form

This code is not finished. I ran into a bug that does not find the correct relative prime number needed to ecrypt the message. I will be trying to fix the bug and update the code. Each update will say "Update" along with a date.

Update 1 (March 2th/2016): I changed the code slightly. I realized that all the numbers that can be set as 'e' are all prime numbers. Instead of searching for the first prime number, I found all the prime numbers from the range 1<i<n, added them to a list and selected one at random; also made sure that n%e != 0. My next task is to find d.
