## Nex
The Nex programming language. High-level, compiled and weird. Written in Python

### Example
Here's a simple example of Nex
```
! Heres a simple example
! This is a comment

Num a = 5.
Num b = 10.

met add [x @Num, y @Num] @Num ( x + y... )

Num result = add [a, b].
print? [result].

met HelloWorld [] @Null ( print? ["Hello, World!"]. )
HelloWorld [].
```
