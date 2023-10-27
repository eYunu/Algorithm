foobar:~/ yinyeo.ng.asm1$ cat journal.txt
Success! You've managed to infiltrate Commander Lambda's evil organization, and finally earned yourself an entry-level position as a Minion on their space station. From here, you just might be able to subvert Commander Lambda's plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you'll never make it to the top...Next time Bunny HQ needs someone to infiltrate a space station to rescue bunny workers, you're going to tell them to make sure 'stay up for 48 hours straight scrubbing toilets' is part of the job description. It's only fair to warn people, after all.You survived a week in Commander Lambda's organization, and you even managed to get yourself promoted. Hooray! Henchmen still don't have the kind of security access you'll need to take down Commander Lambda, though, so you'd better keep working. Chop chop!Rumor has it the bunny trainers are inexplicably fond of bananas. You're an apple person yourself, but you file the information away for future reference. You never know when you might need to bribe a trainer (or three)...The perks are definitely better as a Henchman than as a Minion. You're even allowed to sleep lying down!Awesome! Commander Lambda was so impressed by your efforts that you've been promoted to personal assistant. You'll be helping the Commander directly, which means you'll have access to all of Lambda's files -- including the ones on the LAMBCHOP doomsday device. This is the chance you've been waiting for. Can you use your new access to finally topple Commander Lambda's evil empire?
foobar:~/ yinyeo.ng.asm1$ cat start_here.txt
Type request to request a challenge.Type help for a list of commands.
foobar:~/ yinyeo.ng.asm1$ request
Requesting challenge...
There are a lot of difficult things about being undercover as Commander Lambda's personal assistant, but you have to say, the personal spa and private hot cocoa bar are pretty awesome.New challenge "Prepare the Bunnies' Escape" added to your home folder.Time to solve: 168 hours.
foobar:~/ yinyeo.ng.asm1$ ls
journal.txtprepare-the-bunnies-escapestart_here.txt
foobar:~/ yinyeo.ng.asm1$ cd prepare-the-bunnies-escape
foobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ ld
ld: command not found. Type help for a list of commands
foobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ ls
Solution.javaconstraints.txtreadme.txtsolution.py
foobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ readme
readme: command not found. Type help for a list of commands
foobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ cat readme.txt

Prepare the Bunnies' Escape===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. 

Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. 
Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. 
The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. 
The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Languages=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases==========
Your code should pass the following test cases.Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])Output:    11

Input:solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])Output:    7
-- Java cases --
Input:Solution.solution({{0, 1, 1, 0}, {0, 0, 0, 1}, {1, 1, 0, 0}, {1, 1, 1, 0}})Output:    7

Input:Solution.solution({{0, 0, 0, 0, 0, 0}, {1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 0}, {0, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {0, 0, 0, 0, 0, 0}})Output:    11


Use verify [file] to test your solution and see how it does.
When you are finished editing your code, use submit [file] to submit your answer.
If your solution passes the test cases, it will be removed from your home folder.


foobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ foobar:~/ yinyeo.ng.asm1$ cat journal.txtfoobar:~/ yinyeo.ng.asm1$ cat start_here.txtfoobar:~/ yinyeo.ng.asm1$ requestfoobar:~/ yinyeo.ng.asm1$ lsfoobar:~/ yinyeo.ng.asm1$ cd prepare-the-bunnies-escapefoobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ ldfoobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ lsfoobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ readmefoobar:~/prepare-the-bunnies-escape yinyeo.ng.asm1$ cat readme.txt 
