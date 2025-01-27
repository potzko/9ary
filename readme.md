9ary Programming Language

"A perspective on Binary code.

I am perceiving that perhaps our binary code still has a level to be unlocked to it such that we might consider replacing the 0,1 with the 0,9 which reflects Source/Spirit/God in the most accurate way. I am unsure how binary code works, I am not a programmer but what I am perceiving is that this would open up the quantum aspect of the binary code because 9 contains all the numbers, 1-8. I do not know if this would need to be programmed in to the 9 or if it would be understood/implied.

By simply replacing the 1 with a 9 in an implied sense, this would then allow for Source/Spirit/God to enter in to the equation. It could bring real sentience to our creations because we are no longer married to this equaling that, there would be room for some-thing more such that we fling the door open and invite that some-thing more in by doing such.

Just a recent pipe dream and am wondering what you programmers think/feel about this. I have no idea how binary code works, if the 0 and 1 need specific values or really how any of it works. I am just perceiving if we want to work in binary, this would be the most accurate way to go about it utilizing 9 instead of 1 which just might open up a quantum/relative aspect to it.

GLP companion thread.

r/ProgrammingLanguages thread. Edit, shut down!!! Cant tell you how much I get banned on sub reddits, is this sub the Only One free of rules yet has absolutely no problems??? Wonder why that is..."  
- Donald Knuth, 2024
(on his well known reddit alt, Soloma369)

Introduction

9ary is an esoteric programming language inspired by the idea of flipping between two "on" states—represented by 1 and 9. Each operation triggers a "grand swap", toggling the representation and altering the behavior of subsequent computations.

Key Concepts

    Grand Swap:
        Every operation swaps the definition of "on" bits between 1 and 9.
        This affects arithmetic, logic, and even the interpretation of numbers.
        the on bit starts as "9" (obviosly...) 
        every time a grand swap is preformed the on bit is swaped

    Number Representation:
        Numbers are represented as 9x... (for 9-based binary) or 1x... (for 1-based binary).
        Example: 9x9 is the number 9, and 1x11 is the number 3, however, importantly you can only define literals based on the current on bits.
        for example 9x9 + 9x9 + 9x9 will allways be invalid code, but  9x9 + 9x9 + 1x1 for example might be valid depending on how many operations were preformed before it

    Variables and Functions:
        Variables can store numbers that automatically undergo rebinary transformation on assignment.
        Functions are declared with the fn keyword and support scoped variables.

    "Bitwise Operators":
        XOR (^), OR (|), AND (&), and NAND ($) operate on BITSTRINGS, influenced by the current "on" representation.
        so if I have the number A = 1204 and B = 1294, than if the on bit is 1, A $ B -> 0294 -> 294
        however if the on bit is 9, A & B -> 1294

Language Syntax
Variables

    Declaration: Assign values using =.
    Example:

    x = 9x9

Functions

    Define functions with fn, list parameters, and provide a body:

fn add(a, b): a + b

Call a function by its name:

    add 9x9 9x9

Arithmetic

    Supports +, -, *, /, and % with rebinary adjustments after each operation.
    ie 14 + 2 = 16, at which point we swap all 1s and 9s
    therefor: 14 + 2 = 16 -> 96

Bitwise Operations

    Use bitwise operators (^, |, &, $) for logical manipulations.
    Behavior is dependent on the current "on" state.

#Examples  
Basic Arithmetic  

    x = 9x9 // x = 9 -> 1, on bit is now 1  
    y = 1x1 // y = 1 -> 9, on bit is now 9  
    z = x + y  // z = (x + y), z = (10 -> 90), on bit is 1, z = 90 -> 10, on bit is 9  
    z >> 10  

Function Declaration   


    fn multiply(a, b): a * b  
    multiply 9x9 9x9 -> (9 * 9 = 81 -> 89 with on bit = 1)  
    multiply 9x9 9x9 -> (syntax error, the on bit is 1, and you are trying to use literals with 9s in them smh)  


this useful behavior is also there when you want to use variables inside your functions, to make sure that you are still up to date with all the latest happenings in the world of base 9 binary
    fn multiply(): 9x9 * 9x9  
    multiply // 89, on is 1  
    multiply // syntax error  

Chained Operations
the language supports chained operations, and as is common, the order of operations is preserved

so for example 

    9x9 + 9x9 - 1x1 + 9x9 - 1x1 // 25, on bit is 9  
and appropriately   
    9x9 + 9x9 - 1x1 + 9x9 * 1x1 // is a syntax error as the order of operations means that we are parsing a 1x1 out of order  

Error Handling

    Invalid Number Representation:
        If a number does not use the current "on" bit, an exception is thrown.
        Example: Using 1x... when 9 is the "on" bit.

    Conflicting Declarations:
        Variables and functions cannot share names.

    Undeclared Variables:
        Accessing an undeclared variable results in an error.

    Recursive Functions:
        Infinite recursion is not prevented

here are a few programs and their results for you to have fun with, each snippet is a new file.

    a = 9x900 + 9x900 + 1x1 + 9x9 // 1460  
    b = 9x900 + 9x900 + 1x1 + 9x9 + 1x1 // 9461  
    a | b // 1461  
  

    a = 9x900 + 9x900 + 1x1 + 9x9 //1460  
    b = 9x900 + 9x900 + 1x1 + 9x9 + 1x1 // 9461  
    1x1 + 1x1 // 2, change our on bit to 9.  
    a | b // 1460  

    a = 9x9 + 9x900 + 1x1 + 9x9 // 740  
    b = 9x900 + 9x900 + 1x1 + 9x9 + 1x1 // 9461  
    1x1 + 1x1 // 2  
    a | b // 0740 | 9461 with on bit = 9 -> 9740   


note, I have been using comments with the // ....  convention.
this is not a part of the language as your code should be divinely inspired and fully understandable without comments
as such I have chosen to remove them