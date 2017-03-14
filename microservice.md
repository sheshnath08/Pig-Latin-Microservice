Welcome to the Vicarious Pig Latin MicroService Project.

## Background

You've elected to take this challenge rather than supply an existing code sample. The purpose of this challenge is to demonstrate how you architect, implement, test and organize your software projects- as such there will be less of an emphasis on algorithms and more on the project as a whole.

You are allowed to use external libraries but must document their usage.


## Project Description

You've been tasked with writing a Pig Latin Translation Microservice. The rules of Pig Latin are described below.

This project should-

* Listen on port 80 and accept a string that contains at least one word, but potentially entire paragraphs.

* Convert the words in the string to Pig Latin and return the results in the HTTP message body.

* Preserve all of the punctuation in the original string.


## Pig Latin

For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, "ay" is added.

* "pig" → "igpay"
* "banana" → "ananabay"
* "trash" → "ashtray"
* "happy" → "appyhay"
* "duck" → "uckday"
* "glove" → "oveglay"


For words that begin with vowel sounds or a silent letter, one just adds "yay" to the end.

* "eat" → "eatyay"
* "omelet" → "omeletyay"
* "are" → "areyay"


## Deliverables

* A git repository containing all the code needed to run the microservice.

* Instructions for installing and running the microservice and test suite.
