**Features:**

- ```Lr_dusty``` is true when the living room is dusty

- ```Gar_dusty``` is true when the garage is dusty

- ```Lr_dirty_floor``` is true when the living room floor is dirty

- ```Gar_dirty_floor``` is true when the garage floor is dirty

- ```Dustcloth_clean``` is true when the dust cloth is clean

- ```Rob_loc``` is the location of the robot, with values **{Luogo,Polverosità}**

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

>```move```:
>- preconditions:
>- effects:


>```dust```:
>- preconditions:
>- effects:

>```sweep```:
>- preconditions:
>- effects:
