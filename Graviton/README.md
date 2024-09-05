# Role : Quant Researcher

# Test
3 challenging Probability puzzles. We had to give a descriptive answer.
I think they shortlisted people who solved 2 or more.

## Q1:
200 people in a firm, who trade in various markets. What is minimum number of markets that need to exist, such that for any 2 people A and B in the firm, there exists at least 1 market that A trades in and B does not, and vice versa.

<details hide>
  <summary>Answer</summary>
  10 markets.
  <details hide>
  <summary>Solution</summary>
 Logic: If there are N markets, we can give everyone a combination of N/2 markets to every person in the firm. Each combination will be unique, hence must satisfy the criteria mentioned above.
</details>
</details>

## Q2:
You are playing a game wherein you have 100 turns and 2 chests. Each turn you can choose to wait or stash. When you wait, one coin is randomly added to one of the chests with equal probability. When you stash, you collect the coins inside one of the 2 chests, with equal probability. 

Part A:
If you must stash exactly N times, derive a formula for the maximum expected returns from this game. 
<details hide>
  <summary>Solution</summary>
  Wait 100-N turns, stash the last N turns. Maximum expected returns is calculated using 2 cases. Case 1, where returns from only 1 chest is stashed in all N stashes. Case 2, where all coins are stashed. 
</details>
<br />
Part B:
What is the value of N, for which the expected returns from this game will be maximised.
<br />
<details hide>
  <summary>Answer</summary>
  6
</details>


# Interview
2 Rounds of Interview, first round was just probability puzzles.
One question I remember is given a coin and a fraction p/q, how would I make a game wherein player A has a p/q chance of winning and player B has a 1-p/q chance of winning.

Follow up to this was what should I do if I replace p/q with an irrational number.
