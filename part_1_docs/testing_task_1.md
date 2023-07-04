### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #should be == instead of =
      return True
    else #missing colon after else
      return False
   

  dif highest_card(self, card1 card2): #dif instead of def, missing a comma between card1 
  if card1.value > card2.value:        #and card2
    return card
  else:
    return card2
  


def cards_total(self, cards):
  total    #should say total = 0
  for card in cards:
    total += card.value #this line should be after for loop
    return "You have a total of" + total
  
```
