# Design requirements

### Core 
1) Assign each individual a target with a set of restrictions. 
2) Send an email to each individual telling them the identity of their target. 
3) Output a file which saves the decisions. 

### Pairing Restrictions
1) Each individual is picked once. 
2) Each individual is assigned a target. 
3) Each individual isn't assigned the same target as last year. 
4) Each group (family) has a target outside their group. 
5) Some individuals (partners) are targeted within their group. 


## Hill climber style Method
* Assign points for each rule. 
* Total up the points for picking each combinatino. 
* Pick a starting permuation randomly. 
* For each member in the list, see if a swap exists which will increase points. If so swap them. 
* Repeat for a number of cycles. 