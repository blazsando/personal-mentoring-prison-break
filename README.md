# Prison Break

## Problem to solve

In a prison the prison warden gathers all the prisoners into a big gathering hub. He sais, from this day on each and
every day they take a randomly selected prisoner into the same room that is separate from the cells and has only a light
switch in it.

The prisoners cannot talk after that day, cannot see the room from the outside and the only thing they can do in it is
either switch the light or not touch it at all. If in the future anyone sais to the warden, that **"I know for a fact
that everyone was in the room at least once"** and he is telling the truth, than everyone can go home.

## Milestones to the solution:

1. They can count how many they are the first day
2. They can only communicate with the switch
3. Someone must have all the information, partly information is useless
4. They most likely visit the room multiple times before it is guaranteed
5. The assigned counter has different task than everyone else

## Solution:

Counter only switch off the light version (opposed to always switch on)

The first person to visit the room after the puzzle gets to be the counter. His task is to switch off the light each
time it is switched on. It is applied the first visit as well. In case it is off, he doesnt touch it.

Everyone else has to switch on the light only once. You can only switch it on if it is off when you enter the room and
you haven't switched it on before.

As soon as the counter switches the light off as many times as there are prisoners minus one after the first visit he is
guaranteed to tell the warden that everyone visited the room

