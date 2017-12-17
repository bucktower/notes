# Final Exam Review
SDS 321: Intro to Probability and Statistics

## Basics
**Sample space**: set of all possible outcomes of an experiment

**Event**: subset of sample space

**Discrete**: countable and finite

**Continuous**: uncountable and infinite

### Sets
**Union**: <img src="https://rawgit.com/bucktower/notes/master/svgs/37aa8ac310dfac2ef92c0ed02ab82d37.svg?invert_in_darkmode" align=middle width=176.255805pt height=24.6576pt/>

**Intersection**: <img src="https://rawgit.com/bucktower/notes/master/svgs/ec278796f6951f9369023fbb9a029a77.svg?invert_in_darkmode" align=middle width=145.205445pt height=24.6576pt/>

<img src="https://rawgit.com/bucktower/notes/master/svgs/a3212891807793f0174e26c5cac6fba0.svg?invert_in_darkmode" align=middle width=136.073355pt height=24.6576pt/> is a **partition** of <img src="https://rawgit.com/bucktower/notes/master/svgs/85750e887deda5a81004be11ec8d52ed.svg?invert_in_darkmode" align=middle width=86.75799pt height=24.6576pt/> and is **mutually exclusive**.

### Komolgrov's Axioms
1. <img src="https://rawgit.com/bucktower/notes/master/svgs/829d0bde04766f2eb5732d4cf65d6d4a.svg?invert_in_darkmode" align=middle width=98.978055pt height=24.6576pt/>
2. <img src="https://rawgit.com/bucktower/notes/master/svgs/4198b3c1813c78d69d3e3b71fb9230ff.svg?invert_in_darkmode" align=middle width=66.786555pt height=24.6576pt/>
3. <img src="https://rawgit.com/bucktower/notes/master/svgs/7e45d72cff21422d73ce0b09813d2f23.svg?invert_in_darkmode" align=middle width=139.42731pt height=24.65793pt/> for events that are mutually exclusive

As a result:

- <img src="https://rawgit.com/bucktower/notes/master/svgs/ffa0d4277f1d5d803d7ec7b0de95fd0f.svg?invert_in_darkmode" align=middle width=134.33343pt height=24.6576pt/> where <img src="https://rawgit.com/bucktower/notes/master/svgs/2a30304a6636d7cc643fa26698225af0.svg?invert_in_darkmode" align=middle width=18.95685pt height=22.46574pt/> is the complement of <img src="https://rawgit.com/bucktower/notes/master/svgs/fe2c4a079225e6b6d0ad09af8a22ef4b.svg?invert_in_darkmode" align=middle width=13.08219pt height=22.46574pt/>
- <img src="https://rawgit.com/bucktower/notes/master/svgs/2542e33cb956f87c9cac9f2571cc4841.svg?invert_in_darkmode" align=middle width=318.173955pt height=24.6576pt/>
- <img src="https://rawgit.com/bucktower/notes/master/svgs/0ac3b9491a04c965ed0ebb38dab4cca4.svg?invert_in_darkmode" align=middle width=83.676945pt height=30.64842pt/>

### Important Sums
- <img src="https://rawgit.com/bucktower/notes/master/svgs/f2cbb87ed5b223b49fd3f275076dec71.svg?invert_in_darkmode" align=middle width=114.931575pt height=33.20559pt/>
- <img src="https://rawgit.com/bucktower/notes/master/svgs/71029bce4cf9ede13951dc037e35aa0c.svg?invert_in_darkmode" align=middle width=163.902255pt height=33.20559pt/>
- <img src="https://rawgit.com/bucktower/notes/master/svgs/28ee994097820a7196ce60b0bae1d849.svg?invert_in_darkmode" align=middle width=126.319875pt height=33.825pt/>
- <img src="https://rawgit.com/bucktower/notes/master/svgs/7b6716cfa52b6c6e66d6941f7d673ca4.svg?invert_in_darkmode" align=middle width=104.217135pt height=27.77577pt/> if <img src="https://rawgit.com/bucktower/notes/master/svgs/4f6a8cc8507e0b1400a2f97556d02543.svg?invert_in_darkmode" align=middle width=47.95857pt height=24.6576pt/>

#### Binomial Theorem
<img src="https://rawgit.com/bucktower/notes/master/svgs/cb43bf86527070448a1d9071e0a59d44.svg?invert_in_darkmode" align=middle width=189.157155pt height=27.94572pt/>

Tip: <img src="https://rawgit.com/bucktower/notes/master/svgs/c00a79f2e6c6a06de2ade2dc8cb3810f.svg?invert_in_darkmode" align=middle width=23.19471pt height=27.94572pt/> is the same as C(n,i)

## Basic Counting Principles
**Product rule**: if there are two tasks, with n<sub>1</sub> ways to do the first **and** n<sub>2</sub> ways to do the second, then there are n<sub>1</sub>n<sub>2</sub> ways to do the procedure.

**Sum rule**: if a task can be done either in n<sub>1</sub> ways **or** n<sub>2</sub> ways, then there are n<sub>1</sub>n<sub>2</sub> ways to do the task.

## Conditional and Total Probability
**Conditional Probability**:
<p align="center"><img src="https://rawgit.com/bucktower/notes/master/svgs/14e349e5854e73aeadbbda75be2be693.svg?invert_in_darkmode" align=middle width=268.8345pt height=38.834895pt/></p>
Rearrange the terms to get other equations, such as <img src="https://rawgit.com/bucktower/notes/master/svgs/4db28fcf6132387c43ee24422a1bc5db.svg?invert_in_darkmode" align=middle width=69.50922pt height=24.6576pt/>.

**Total Probability** (just apply Conditional Probability with the A<sup>C</sup>):
<p align="center"><img src="https://rawgit.com/bucktower/notes/master/svgs/010991871aa09827d1933735aaf52bfd.svg?invert_in_darkmode" align=middle width=482.64315pt height=18.75984pt/></p>

## Independence
**Independent**: A and B are independent if <img src="https://rawgit.com/bucktower/notes/master/svgs/285f1f0c6f91af5dee382f1b983347fe.svg?invert_in_darkmode" align=middle width=116.643945pt height=24.6576pt/>; occurence of A provides no information about B's occurence

**IID**: Independent, indentically distributed (probability of success on many trials always stays the same)

- <img src="https://rawgit.com/bucktower/notes/master/svgs/b3d8dcc6bbea5382941875d9728be2e9.svg?invert_in_darkmode" align=middle width=183.817755pt height=24.6576pt/>
- Applies even if <img src="https://rawgit.com/bucktower/notes/master/svgs/00193095fdb87a6f23be973290db3444.svg?invert_in_darkmode" align=middle width=68.08791pt height=24.6576pt/>

Conditioning can effect independence:

![Independence Conditioning Example](https://github.com/bucktower/notes/raw/master/utcs/SDS%20321:%20Intro%20to%20Probability%20and%20Statistics/IndependenceConditioning.png)

If A and B are independent by themselves, yet we are told that C occurred, then A and B are *no longer independent*.

**Pairwise independence**: a set of random variables from which any two are independent -- *does not imply independence*

**Conditional independence**: <img src="https://rawgit.com/bucktower/notes/master/svgs/08da9bfd631b4c2ce16790c568589897.svg?invert_in_darkmode" align=middle width=236.291055pt height=24.6576pt/>

## Permutations and Combinations
|                | Ordered      | Not Ordered |
|----------------|--------------|-------------|
| Replacement    | Product Rule |             |
| No Replacement | Permutation  | Combination |

### Permutation
Order matters, no replacement

<p align="center"><img src="https://rawgit.com/bucktower/notes/master/svgs/fd90fc12b213d73cec1f4dd0b4f1daaf.svg?invert_in_darkmode" align=middle width=132.145695pt height=37.92162pt/></p>

"How many ways are there of arranging...?"

You can always use the slots as a visual aid (useful for strings)

### Combination
Order *doesn't* matter, no replacement

<p align="center"><img src="https://rawgit.com/bucktower/notes/master/svgs/6ef5b62b7ad939374db1f012fa581fa9.svg?invert_in_darkmode" align=middle width=145.875015pt height=37.92162pt/></p>

"How many ways are there of selecting at once...?"

#### Stars and Bars/Bagels
Explains the Combination equation. Say you're buying 6 bagels of 4 types.

Stars = bagels, Bars = separator between types

Example assortment: * * | * | * | * *

6 stars (**n**) + 3 bars (**k**) = 9 symbols

How many possible assortments? C(n,k) = C(6,3) = 20 possible assortments

[![Stars and Bars Tutorial](http://img.youtube.com/vi/UTCScjoPymA/0.jpg)](http://www.youtube.com/watch?v= UTCScjoPymA)

## Special Random Variables
**Probability mass function** (PMF): describes the growth in probability from one to the next (cumulative)

**NOTE**: Put table with equations here

### Discrete Uniform
Same probability for all cases

| X = x            | 1   | 2   | 3   |
|------------------|-----|-----|-----|
| P<sub>x</sub>(x) | 1/3 | 1/3 | 1/3 |

### Bernoulli
Either a success or a failure

| X = x            | S | F     |
|------------------|---|-------|
| P<sub>x</sub>(x) | P | 1 - P |

### Binomial
Counts successes in **n** IID Bernoulli trials

Distribution usually ends up being normal

### Poisson
Sample space is infinite (x = 0, 1, 2, ...)

<img src="https://rawgit.com/bucktower/notes/master/svgs/0ae3f8e52e8833a55be05df21031a4fc.svg?invert_in_darkmode" align=middle width=9.58914pt height=22.83138pt/> = average over time and space

## Expectation
Expected value of a discrete random variable = sum of probabilities weighted by their probabilities

<p align="center"><img src="https://rawgit.com/bucktower/notes/master/svgs/aa1a52e5ef0aef73176aac2ed3ee1fc7.svg?invert_in_darkmode" align=middle width=166.76385pt height=36.164535pt/></p>

### Variance
If <img src="https://rawgit.com/bucktower/notes/master/svgs/2d1362669b0aef70cf2e306e40254e24.svg?invert_in_darkmode" align=middle width=73.474005pt height=24.6576pt/>, the **variance** of X is:

<p align="center"><img src="https://rawgit.com/bucktower/notes/master/svgs/3105651074a6157d35986d91b381828c.svg?invert_in_darkmode" align=middle width=278.71635pt height=18.31236pt/></p>

### Properties of Expectation and Variance
If **a** and **b** are constants, then:

<p align="center"><img src="https://rawgit.com/bucktower/notes/master/svgs/ee781e6d5140c3b85f0de77c299edafc.svg?invert_in_darkmode" align=middle width=167.8347pt height=16.438356pt/></p>

<p align="center"><img src="https://rawgit.com/bucktower/notes/master/svgs/2388378d0f1752ddb5894442d1c15fec.svg?invert_in_darkmode" align=middle width=181.5066pt height=18.31236pt/></p>

## Random Vectors

