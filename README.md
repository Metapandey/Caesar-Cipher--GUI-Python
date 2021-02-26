# Caesar-Cipher--GUI-Python
## Only Works with Alphabets, No Numbers or Special Charaters are Allowed
### Encrypt and Decrypt text


**In cryptography, a Caesar-Cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in 
his private correspondence.
The Caesar cipher is named after Julius Caesar, who, according to Suetonius, used it with a shift of three (A becoming D when encrypting, and D becoming A when decrypting) to protect messages of military significance. While Caesar's was the first recorded use of this scheme, other substitution ciphers are known to have been used earlier.**
*"If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out. If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth letter of the alphabet, namely D, for A, and so with the others."*
> -Suetonius, Life of Julius Caesar 56


It is likely to have been reasonably secure, not least because most of Caesar's enemies would have been illiterate and others would have assumed that the messages were written in an unknown foreign language.

Kahn (1967) describes instances of lovers engaging in secret communications enciphered using the Caesar cipher in The Times. Even as late as 1915, the Caesar cipher was in use: the Russian army employed it as a replacement for more complicated ciphers which had proved to be too difficult for their troops to master; German and Austrian cryptanalysts had little difficulty in decrypting their messages.

# About the Logic


The Caesar Cipher encryption rule can be expressed mathematically as:
c = (x + n) % 26



Each of these characters is represented in computer memory using a number called Unicode of the character, which is an 8-bit number and encodes almost all the English language’s characters, digits, and punctuations.
For instance, the uppercase ‘A’ is represented by the number 65, ‘B’ by 66, and so on. Similarly, lowercase characters’ representation begins with the number 97.


# Python ord() function

In Python, the ord() function accepts a string of unit length as an argument and returns the Unicode equivalence of the passed argument. In other words, given string of length 1, the ord() function returns an integer representing the Unicode code point of the character when the argument is a Unicode object, or the value of the byte when the argument is an 8-bit string


# Python chr() function
The chr() method returns a character (a string) from an integer (represents unicode code point of the character).
Syntax:

chr(num)

num : integer value

# About the GUI
## Tkinter Python
The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, as well as on Windows systems. (Tk itself is not part of Python; it is maintained at ActiveState.)
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

Here is the  image
[<img align="left" src="https://user-images.githubusercontent.com/49518917/109299274-dc19cc00-785a-11eb-9174-7222d62f1996.PNG"/>]