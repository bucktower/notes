# Final Exam Review
SDS 321: Intro to Probability and Statistics

## Basics
**Sample space**: set of all possible outcomes of an experiment
**Event**: subset of sample space

### Sets
**Union**: <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/37aa8ac310dfac2ef92c0ed02ab82d37.svg?invert_in_darkmode" align=middle width=176.25580499999998pt height=24.65759999999998pt/>

**Intersection**: <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/ec278796f6951f9369023fbb9a029a77.svg?invert_in_darkmode" align=middle width=145.205445pt height=24.65759999999998pt/>

<img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/a3212891807793f0174e26c5cac6fba0.svg?invert_in_darkmode" align=middle width=136.07335500000002pt height=24.65759999999998pt/> is a **partition** of <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/85750e887deda5a81004be11ec8d52ed.svg?invert_in_darkmode" align=middle width=86.75799pt height=24.65759999999998pt/> and is **mutually exclusive**.

### Komolgrov's Axioms
1. <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/829d0bde04766f2eb5732d4cf65d6d4a.svg?invert_in_darkmode" align=middle width=98.97805500000001pt height=24.65759999999998pt/>
2. <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/4198b3c1813c78d69d3e3b71fb9230ff.svg?invert_in_darkmode" align=middle width=66.78655499999999pt height=24.65759999999998pt/>
3. <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/7e45d72cff21422d73ce0b09813d2f23.svg?invert_in_darkmode" align=middle width=139.42730999999998pt height=24.65792999999999pt/> for events that are mutually exclusive

As a result:

- <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/ffa0d4277f1d5d803d7ec7b0de95fd0f.svg?invert_in_darkmode" align=middle width=134.33343pt height=24.65759999999998pt/> where <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/2a30304a6636d7cc643fa26698225af0.svg?invert_in_darkmode" align=middle width=18.956850000000006pt height=22.46574pt/> is the complement of <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/fe2c4a079225e6b6d0ad09af8a22ef4b.svg?invert_in_darkmode" align=middle width=13.082190000000004pt height=22.46574pt/>
- <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/2542e33cb956f87c9cac9f2571cc4841.svg?invert_in_darkmode" align=middle width=318.173955pt height=24.65759999999998pt/>
- <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/0ac3b9491a04c965ed0ebb38dab4cca4.svg?invert_in_darkmode" align=middle width=83.676945pt height=30.648420000000016pt/>

### Important Sums
- <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/f2cbb87ed5b223b49fd3f275076dec71.svg?invert_in_darkmode" align=middle width=114.93157499999998pt height=33.20559pt/>
- <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/71029bce4cf9ede13951dc037e35aa0c.svg?invert_in_darkmode" align=middle width=163.902255pt height=33.20559pt/>
- <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/28ee994097820a7196ce60b0bae1d849.svg?invert_in_darkmode" align=middle width=126.319875pt height=33.824999999999996pt/>
- <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/7b6716cfa52b6c6e66d6941f7d673ca4.svg?invert_in_darkmode" align=middle width=104.21713499999998pt height=27.775769999999994pt/> if <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/4f6a8cc8507e0b1400a2f97556d02543.svg?invert_in_darkmode" align=middle width=47.95857pt height=24.65759999999998pt/>

#### Binomial Theorem
<img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/cb43bf86527070448a1d9071e0a59d44.svg?invert_in_darkmode" align=middle width=189.15715500000002pt height=27.94572000000001pt/>

Tip: <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/c00a79f2e6c6a06de2ade2dc8cb3810f.svg?invert_in_darkmode" align=middle width=23.19471pt height=27.94572000000001pt/> is the same as C(n,i)

## Basic Counting Principles
**Product rule**: if there are two tasks, with n<sub>1</sub> ways to do the first **and** n<sub>2</sub> ways to do the second, then there are n<sub>1</sub>n<sub>2</sub> ways to do the procedure.

**Sum rule**: if a task can be done either in n<sub>1</sub> ways **or** n<sub>2</sub> ways, then there are n<sub>1</sub>n<sub>2</sub> ways to do the task.

## Conditional and Total Probability
**Conditional Probability**:
<p align="center"><img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/14e349e5854e73aeadbbda75be2be693.svg?invert_in_darkmode" align=middle width=268.8345pt height=38.834894999999996pt/></p>
Rearrange the terms to get other equations, such as <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/4db28fcf6132387c43ee24422a1bc5db.svg?invert_in_darkmode" align=middle width=69.50922pt height=24.65759999999998pt/>.

**Total Probability** (just apply Conditional Probability with the A<sup>C</sup>):
<p align="center"><img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/010991871aa09827d1933735aaf52bfd.svg?invert_in_darkmode" align=middle width=482.64315pt height=18.75984pt/></p>

## Independence
**Independent**: A and B are independent if <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/285f1f0c6f91af5dee382f1b983347fe.svg?invert_in_darkmode" align=middle width=116.64394499999999pt height=24.65759999999998pt/>; occurence of A provides no information about B's occurence

- <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/b3d8dcc6bbea5382941875d9728be2e9.svg?invert_in_darkmode" align=middle width=183.81775499999998pt height=24.65759999999998pt/>
- Applies even if <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/00193095fdb87a6f23be973290db3444.svg?invert_in_darkmode" align=middle width=68.08791pt height=24.65759999999998pt/>

Conditioning can effect independence:

![Independence Conditioning Example]()

If A and B are independent by themselves, yet we are told that C occurred, then A and B are *no longer independent*.

**Pairwise independence**: a set of random variables from which any two are independent -- *does not imply independence*

**Conditional independence**: <img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/08da9bfd631b4c2ce16790c568589897.svg?invert_in_darkmode" align=middle width=236.29105499999997pt height=24.65759999999998pt/>

## Permutations and Combinations
|                | Ordered      | Not Ordered |
|----------------|--------------|-------------|
| Replacement    | Product Rule |             |
| No Replacement | Permutation  | Combination |

### Permutation
Order matters, no replacement

<p align="center"><img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/fd90fc12b213d73cec1f4dd0b4f1daaf.svg?invert_in_darkmode" align=middle width=132.145695pt height=37.92162pt/></p>

"How many ways are there of arranging...?"

### Combination
Order *doesn't* matter, no replacement

<p align="center"><img src="https://rawgit.com/in	git@github.com:bucktower/notes/master/svgs/6ef5b62b7ad939374db1f012fa581fa9.svg?invert_in_darkmode" align=middle width=145.875015pt height=37.92162pt/></p>

"How many ways are there of selecting at once...?"

#### Stars and Bars/Bagels
Explains the Combination equation. Say you're buying 6 bagels of 4 types.

Stars = bagels, Bars = separator between types

Example assortment: * * | * | * | * *

6 stars (**n**) + 3 bars (**k**) = 9 symbols

How many possible assortments? C(n,k) = C(6,3) = 20 possible assortments

## Special Continuous Distributions
