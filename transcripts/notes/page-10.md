# PDF page 10: Understanding in Large Language Models — Paul Boghossian

Source: `CCF11082026.pdf`, PDF page 10.
Status: OCR-assisted transcription checked against the scan; layout and emphasis simplified. Original wording and errors retained. Refer to scan for quotation.

This answer is incorrect.

I asked whether it was using a dedicated calculator or generating answers using the model itself?
– No.

It added:

    I can use external computational tools. In this environment, I have access to Python, which can perform exact integer arithmetic. Had I used Python to multiply 5,647 by 8,911, that would have involved an actual arithmetic computation executed outside the language model.

    Without such a tool, accuracy is not guaranteed. Language models can make arithmetic mistakes, especially with large numbers, because their learned computational procedures aren't necessarily as systematic or reliable as conventional algorithms.

Interestingly, in the course of answering this question about method, it discovered that it had given the wrong answer.

    There's also a revealing detail: my previous answer was incorrect.

    The correct result is:
    5647 × 8911 = 50,319,417

    I had given 50,322,417.

Interestingly, this answer, too, is incorrect. It continued:

    This raises precisely the philosophical question you've been exploring: whether a neural network that develops an internal procedure for multiplication should count as grasping the rule of multiplication, even if its implementation is less reliable than that of a classical computer.

I said: actually, the correct answer is 50,320,417. ChatGPT6 responded:

    You're quite right.

    5647 × 8911 = 50,320,417

    My first answer was wrong, and so was my attempted correction. Your answer is correct.
    This is a particularly striking illustration of the difference between generating plausible arithmetic answers and reliably executing an arithmetic algorithm.

It’s very plausible that if these models really had an understanding of what they’re being asked, there would be no mistakes of this type.

Saying 9.11 is greater than 9.9 on the grounds that 11 is bigger than 9, if said by a child, would show that grasp of the concept of decimal notation had not yet snapped into place.

And the same goes for the multiplication case.

