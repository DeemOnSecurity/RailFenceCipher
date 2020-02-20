# Week 1 Code Challenge Guide

This week the code challenge provided is the Rail Fence Cipher. 

This is a relatively simple cipher and is a good introduction to cryptography.
it works like this:

> If given a string: "Hello World!"
> and given a key: 4

The rail fence cipher will create the amount of rows as there are keys:

| Row 1 |
|-------|
| Row 2 |
| Row 3 |
| Row 4 |

The cipher will then fill in the text, up and down the rows, until there is no
more text:

| H |   |   |   |   |   | W |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | E |   |   |   |   |   | O |   |   |   | ! |
|   |   | L |   | O |   |   |   | R |   | D |   |
|   |   |   | L |   |   |   |   |   | L |   |   |

The rows are then taken and read individually like so:


> Row 1

HW

> Row 2

E O!

> Row 3

LORD

> Row 4

LL

The text is then combined: HWE O!LORDLL

Your task this week is to make a method to encrypt and decrypt a rail fence
cipher, good luck!
