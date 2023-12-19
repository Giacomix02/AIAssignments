**Features:**

- ```Lr_dusty``` is true when the living room is dusty

- ```Gar_dusty``` is true when the garage is dusty

- ```Lr_dirty_floor``` is true when the living room floor is dirty

- ```Gar_dirty_floor``` is true when the garage floor is dirty

- ```Dustcloth_clean``` is true when the dust cloth is clean

- ```Rob_loc``` is the location of the robot, with values **{Luogo}**

**Rooms:**

- ```garage``` se è polveroso è extra-polveroso

- ```livingRoom``` non è extra-polveroso

**Actions:**

- ```move``` > si muove da una stanza all'altra

- ```dust``` > spolvera la stanza in cui si trova il robot, solo se la stanza sia polverosa e il panno sia pulito

- ```sweep``` > il robot spazza il pavimento della stanza in cui si trova

# Esercizio 1

**Give the STRIPS representation for dust. [Hint: because STRIPS cannot represent 
conditional effects, you may need to use two separate actions that depend on the robot’s location.]**


>***dust garage***:
>- preconditions: ```Dustcloth_clean``` ∧ ```Gar_dusty``` ∧ ```Rob_loc``` = ```Garage```
>- effects: ¬```Dustcloth_clean```, ¬```Gar_dusty```

>***dust living room***:
>- preconditions: ```Dustcloth_clean``` ∧ ```Lr_dusty```∧ ```Rob_loc``` = ```lr```
>- effects: ¬ ```Lr_dusty```

# Esercizio 2
**Give the feature-based representation for lr_dusty**

Rules for “living room is dusty”


>```lr_dusty``` ← ¬```lr_dusty``` ∧ ```Lr_dirty_floor``` ∧ Act = ```sweep``` ∧ ```Rob_loc``` = ```livingRoom```

>```lr_dusty``` ← ```lr_dusty``` ∧ ```Rob_loc``` ≠ ```livingRoom``` ∧ Act ≠ ```dust``` 


# Esercizio 3
**Suppose that the initial state is that the robot is in the garage, both rooms are dusty but have 
clean floors and the goal is to have both rooms not dusty. Draw the first two levels (with two
actions, so the root has children and grandchildren) of a forward planner with multiple-path 
pruning, showing the actions (but you do not have to show the states). Show explicitly what 
nodes are pruned through multiple-path pruning.**

Initial state: 

< ```garage```, ```lr_dusty```, ```Gar_dusty```, ¬```Lr_dirty_floor```, ¬```Gar_dirty_floor```, ```Dustcloth_clean``` >

![](/Quinta%20Consegna/img/AI.svg)


# Esercizio 4
**Pick two of the states at the second level (after two actions) and show what is true in those states.**

let's pick the only 2 states that are possible after 2 actions: "robot in lr", and "lr pulita"

>**robot in lr:**
>
>< ```lr```, ```lr_dusty```, ¬```Gar_dusty```, ¬```Lr_dirty_floor```, ¬```Gar_dirty_floor```, ¬```Dustcloth_clean``` >

>**lr pulita:**
>
>< ```lr```, ¬```lr_dusty```, ```Gar_dusty```, ¬```Lr_dirty_floor```, ¬```Gar_dirty_floor```, ¬```Dustcloth_clean``` >

# Esercizio 5
**Suppose that the initial state is that the robot is in the garage, both rooms are dusty but have clean floors and the goal is to have both rooms not dusty. Draw the first two levels (with two actions, so the root has children and grandchildren) of a regression planner showing the actions but you do not have to show what the nodes represent.**
![](/Quinta%20Consegna/img/AI2.svg)

# Esercizio 6
**Pick two of the nodes at the second level (after two actions) and show what the subgoal is at those nodes.**

Subgoal "garage pulito - panno pulito":

>< ```garage```, ```lr_dusty```, ¬```Gar_dusty```, ¬```Lr_dirty_floor```, ¬```Gar_dirty_floor```, ```Dustcloth_clean``` >

Subgoal "lr pulita":
>< ```lr```, ¬```lr_dusty```, ```Gar_dusty```, ¬```Lr_dirty_floor```, ¬```Gar_dirty_floor```, ```Dustcloth_clean``` >

# Esercizio 7
**Draw the CSP for a planning horizon of two. Describe each constraint by 
specifying which values are (in)consistent**
