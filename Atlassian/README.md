# Atlassian_Intern_Process

## Round 1 - Test
Solved 2.5 out of 3 questions and got WL. I know people who solved 3 questions and didnt get SL or WL.

## Round 2 - Technical Interview
Approx 1 hour long. They had asked me to keep a code editor ready before hand and share my screen.

### Question:
Given an array of pairs of integers, wherein each pair denotes the start and end time of a meeting, return a boolean array with the ith element of the array being true when the ith meeting can be scheduled.
The ith meeting can be scheduled if it doesn not overlap in time with any of the previously scheduled meetings.

### Solution:
Initialise an empty array, which will contain all the meetings scheduled so far. For every new meeting, binary search through the array of scheduled meetings, for the earliest scheduled meeting that starts after the start time of the new meeting. If the start time of this scheduled meeting is before the end time of the new meeting, the meeting can't be scheduled.

### Tips:
Atlassian doesn't care about just solving the question, they are more concenred about how you write and develop software. Here are a few things I did, which I felt helped.
1. Before coding the solution I wrote a tester function, which takes the input array and the ideal output, calls my solution and cross checks the output. Towards the end of the interview, it made running my code and verifying it across multiple test cases very easy.
2. Ask insightful questions before starting to code and make an example problem, and solve it verbally with the interviewer once to confirm that you have understood the question properly.
3. Write well formatted code, with comments and proper variable names.
4. I made the code modular by describing functions for every small functionality I was implementing, made the code very readable.

### Follow-up
Lets say we are hosting meetings on zoom, which has the breakout room feature, which will allow us to run multiple meetings in parallel. Now, given an input array of meetings, return the minimum number of breakout room we will ever need to make to ensure all meetings happen. 

### Solution
I wasn't asked to code this, due to time constraints, just explain my logic. The logic was to maintain an array of arrays(matrix). Each array in this matrix, is a breakout room and has the start and end times of the meetings scheduled in it. We try to fit every meeting into the first breakout room. If that isnt possible, we try to fit it into the second, and if that is again not possible, it tries the third and so on.
The number of breakout rooms created is the answer.

## Round 3 - Leadership something something (Basically HR round)
Was taken by a senior engineer at Atlassian. Asked me about my experience working in a team. Questions like "Give an example of when you finished a project solely based on your motivation." and "Give an example of a time you took up a leadership position in a project.", etc. 
