# B551 Assignment 0: Searching and Python
##### Submission by Sri Harsha Manjunath - srmanj@iu.edu
###### Fall 2019

## Part 1: Finding your way
It’s your first day at IU and you are looking for Luddy Hall. The CS Department has provided a map, but,
in typical CS style, it is encoded with esoteric symbols in an ASCII text file. The map file consists of N
lines, each with M columns, representing a campus of size N × M units. Each cell of campus is marked with
one of three symbols: # represents your current location, @ is Luddy Hall, sidewalks are marked by ., and
other buildings, which you are not allowed to enter, are marked by &. Here is an example:
```
....&&&
.&&&...
....&..
.&.&...
.&.&.&.
#&...&@
```
#### Search Abstraction
##### 1. Set of States S
The set of states S, can be defined as all states reachable from initial state by any legal sequence of actions

##### 2. Successor Function
The successor function used in this problem returns the immediate neighbour in all 4 cardinal directions that comply with the following rules
* Only goes on the side walk or to Luddy Hall represented by '.' and '&' respectivly
* Stays within the given n x n board

##### 3. Initial State
Initial state is represented by '#' to denote the starting point and @ denoting the destination (Luddy Hall)
'.' representing sidewalk and '&' represent building that cannot be entered

##### 4. Goal State:
To reach Luddy hall(@) from the initial state(#) in the most optimal way.(with the least amount of steps)

##### 4. Cost:
The number of steps taken from the initial state to goal state

#### Why does the program often fail to find a solution? Implement a fix to make the code work better, and explain what you did.
The program fails because it does not have any mechanism to store the nodes it has visited. It hence goes in a loop visiting the same nodes over and over

##### Fix:
* Create a list, called 'visited' that appends every node that was visited. 
* Use this to navigate away from nodes visited in future iterations

####  The existing code is missing a number of the specifications given above. (For example, it doesn’t display the path as a string of compass directions.) Complete the implementation, and explain what you did in your report
Specifications implemented - 
* Path taken - Modified the fringe to include a field to hold the path it has taken. Also modified the moves() function to return the cardinal direction along with the row and column values. Also changed the search1() function to append the direction in which a move is made with every append to the fringe.

* Search Algorithm used - Breadth First Search (BFS) 
Replacing the stack from the default implementation to a queue will ensure the algorithm explores the breadth of the problem space first. This approach ensures the shortest path is explored and returned with number of nodes visited being the cost. DFS also succeeds in converging to a solution in most cases but is not always optimal.

* Return 'Inf' when no solution exists
The function search1() returns 'None' when there exists no solution. Implemented an if statement to check for the same and print 'Inf' accordingly.

## Part 2: Hide-and-seek
You’ve made k new friends so far at IU, but none of them like each another. Your goal is to arrange your
friends on the IU campus such that no two of your friends can see one another. Write a program called
hide.py that takes the filename of a map in the same format as Part 1 as well as a single parameter specifying
the number k of friends you have. Assume two friends can see each other if they are on either the same row
or column of the map, and there are no buildings between them. Your friends can only be positioned on
sidewalks. (It’s okay if friends see you. Any building including Luddy Hall obscures the view, but you do
not.) Your program should output to the screen (in the last lines of its output) a new version of the map,
but with your friends’ locations marked with letters F. If there is no solution, your program should just
display None. Here’s an example:
```
[<>djcran@tank ~] ./hide.py map.txt 9
...F&&&
.&&&F..
.F..&F.
.&F&...
F&.&F&F
#&.F.&@
```
#### Search Abstraction
##### 1. Set of States S
The set of states S, can be defined as all states in which a friend 'F' can be placed such that
* S(he) is placed on a sidewalk 
* There are no other friends in the same row/column without a building in between them

##### 2. Successor Function
The successor function used in this problem returns every alternate possibility of the given board where 
* there exist '.' representing sidewalks
* have no friends directly visible in the same row or column

##### 3. Initial State
A set of '.' denoting sidewalk on which friends can be placed. Buildings represented by '@ or &'

##### 4. Goal State:
To place the number of friends specified by the user on the board, while complying with the given restrictions. If no solution existsm, then to return None.

##### 4. Cost:
Since there is no explicit cost associated with the problem, the cost here would refer to the amount of time the program takes to come up with a soution to a given board and number of friends to be placed

* Search Algorithm used - Depth First Search (DFS)

###### Assumptions
* This program assumes the friends cannot see diagonally
