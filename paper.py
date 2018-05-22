#! /usr/bin/env python3.6

"""
When I first started working on this kata, I started with a paper class.
However, I quickly scrapped it because it seemed odd to have a class that
was, in essence, a variable. But, as you pointed out, you're then stuck
with a pencil that can "read" which sounds really silly.
But there's a larger, more interesting, discussion to have here that
probably only applies to the domain of katas. Should the code model the
real world? I was particularly struck by this a few months ago while
auditioning a candidate on the vending machine kata and I came to the
conclusion that you should do your best to ignore the real world and
focus instead on readability.
But then you can lose out on proving some of what
a kata is looking to test. I say this not to challenge your feedback, but
because, I'm hoping, you might be the only other person in the world
who finds this to be an interesting discussion.
"""
class Paper:

    def __init__(self):
        self.text = ''

    """
    I'm torn between having a write/read function and
    just using a more traditional getter 
    and setter (since that's what it is). Somehow this seems a tad more semantic
    though it also seems strange in a different light.
    Or perhaps, I should go with the more pythonic approach of not using getters
    and setters at all but, I don't know, that's still hard for me.
    Thoughts!?
    """
    def write(self, text):
        self.text = text

    def read(self):
        return self.text
