# Sabziwala - the vegetable vendor problem

### Problem statement: 
Harilal is a local vegetable vendor. Sometimes he sells fruits too depending on his profits and available stock in the wholesale. Early morning around 4 am he visits the Rythubazar - the local wholesale farm and buys objects that he can sell.
Here is your data, you will be the given the items that he can carry such as Cauliflower, Brinjal, or even fruits like apple, oranges etc.
You will be given the weight of each item.
You will be given the maximum weight of his basket that he can carry and the profit in Rs that he makes per item.
Device a strategy to maximize his profit in one trip.

### Example:
On a particular day he can buy the following items in the Rythubazar - Potatoes, Bell pepper, Banana and Watermelon
Their weights respectively are 2Kg, 3Kg, 1Kg and 4kg
Respective profit on each item respectively is Rs4, Rs5, Rs3 and Rs7
But the maximum weight that he can carry is only 5Kg.
The answer for the above example is 5 banana’s that will fetch him the profit of Rs.15
Your logic should work by changing the above data (for example change the number of items or their weights or their profits or the maximum weight that he can carry when his son joins him).

### My Solution:
This program tries out the different combination of items whose weight is not exceeded by given max weight.
Profits of every iteartion is compared to previous profits. If the current profit is greater than previous profit then we change profit value to current profit and log the combination of items in a dictionary.
