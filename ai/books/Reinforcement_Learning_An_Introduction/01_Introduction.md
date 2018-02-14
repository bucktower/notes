# Introduction

Most important characteristics:

- **Trial and error search**: we don't know what exactly the right answer is, but we can infer it based on results
- **Delayed reward**: desired results may not be immediate, and may require certain steps that lead to more steps, that then lead to the reward

## Markov Decision Process
1. Sensation
2. Aspect
3. Goal

## Main Subelements of a Reinforcement Learning System
1. Policy
    - Defines agent behavior
2. Reward signal
    - Single number that the agent tries to maximize over the long term; has an immediate value
3. Value function
    - Long term expectations of how much reward you can expect accumulating
4. Model of the environment
    - Mimics behavior of the environment, allowing for inferences as to how the environment will behave

Reinforcement learning takes use of "learning" over "evolution":

- Ideal policy is a function from states to actions
- Pay attention to states an individual passes thru throughout its lifetime/which it selects

## Tic-Tac-Toe
- Dynamic programming strategy would be to play the opponent a number of times and try to model its behavior
- Evolutionary method directly searches the space of possible policies for one with a high probability of winning against the opponent. Then we'd try to direct the next policy to consider next based off of which has the best shot at achieving a win
    - A policy that results in a win receives a bump, one that loses loses a bit. But changes are only made once (at the end of games)
- Value function (assume we're Xs):
    - Give different states different values
        - State with 3 Os >> `0`
        - State with 3 Xs >> `1`
        - All other states >> `0.5` (50% chance of winning)
    - Then, move greedily, considering the value of the state that would result in the highest reward
    - Sometimes, there would be a tie and you would pick a move randomly -- *exploration*
    - Once that move is made and a new state comes about, we let the other player play, and when the state comes back, we change the previous move's state using a *step-size parameter* to bring it closer to that of the current state (maybe linear +/-, an average of both, etc)
    - This update rule is one instance of a *temporal difference* learning method because its changes are based on a difference of `STATE1 - STATE2` at two different times

### Exercises
1.1: It would learn just the same (given exploratory moves are still picked randomly), although its progression towards being more competitive would probably be much slower since the rounds would be played against a randomly-playing opponent, not one who already has some sense of strategy to learn from.

1.2: Taking advantage of symmetries by putting all symmetric sets into the same value "group" that gets incremented and decremented altogether would likely help our algorithm in becoming more competitive. Unless, of course, the opponent never takes into account symmetry. While symmetric states would seem the same to our program, the psychology and perception that goes into a human might result in completely different moves or gaffs made by the human that doesn't recognize equivalency in symmetrical states.

In that case, we might want to leave symmetrical state grouping off the table to give us the advantage for a player who plays different when he sees different iterations of the symmetrical group.

1.3: A greedy algorithm looks pretty good for tic-tac-toe. However, there might be some underlying strategy that seems worse at first but ends up really well that a short-term-capitalizing greedy algorithm would overlook

1.4: If learning updates occurred after all moves, then the set might converge to {0, 1}. This would likely be better for more wins, since propogation from winning states moves quicker back to early-game type moves

If learning updates only occurred after non-exploratory moves, then the set that would be converged upon would probably look something like {0, 0.5, 1}. This strategy would be better for learning/long term because its less quick to judge new/exploratory moves for quick wins/losses. This slower propogation back would likely result in more state score-ties happenning in making decisions for the next state to go for (ie "explorations") would allow more trials on each exploration before coming to a conclusion about it.

1.5: For a non-empty ending board (meaning that the algorith won/lost early on), you'd give values < 0 if the algorithm lost quickly, and values > 1 if the algorithm won quickly to incentivize the program to want to win as quick as it can and become even more competitive.