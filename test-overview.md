## Switch Pokemon	
### Test case 1
#### Process
- Create a player instance
- Generate three pokemon objects, and add it to the player's pokemon collection object
- In the pokemon collection object, record the values for: active_pokemon, collection and available properties
- Trigger switch pokemon method inside pokemon battle method by selecting the switch pokemon option as input, select a different pokemon to switch to, check selected pokemon is now the active pokemon in the battle, exit battle
- In the pokemon collection object, again record the values for the same properties

#### Expected
- Active pokemon should be the other pokemon which was selected via user input
- Collection should have same objects, same order but with selected pokemon now at index 0
- Available should have same objects, but with selected pokemon now at index 0

## Switch Pokemon	
### Test Case 2	
#### Process
- Create a player instance
- Generate one pokemon object, and add it to the player’s pokemon collection object.
- Trigger switch pokemon method by selecting switch pokemon as input, a prompt should appear saying I can’t switch, because there’s only one pokemon, and the pokemon battle function should return to the top of it’s loop

#### Expected
- The prompt saying you can't switch should appear.
- Should be taken to the start of the pokemon battle method's loop


## Health Potion	
### Test Case 1
#### Process
- Create a player instance
- Generate a health potion, and add it to player's items
- Record player's health potion count and pokemon's hp
- In pokemon battle, give it to the pokemon with full health

#### Expected
- Health potion count should have decreased by 1
- Pokemon remaining hp, should not have changed, and should be the same as it's total hp
- Afterwards, Health potion shouldn't be an option that appears when selecting 'use item' in pokemon battle, as it's on 0

## Health Potion	
### Test Case 2
#### Process
- Create a player instance
- Generate a health potion, and add it to player's items
- Record player's health potion count and pokemon's hp
- In pokemon battle, give it to the pokemon with very low health

#### Expected
- Health potion count should have decreased by 1
- Pokemon remaining hp should have improved by health potions amount attribute
- Afterwards, Health potion shouldn't be an option that appears when selecting 'use item' in pokemon battle, as it's on 0
  