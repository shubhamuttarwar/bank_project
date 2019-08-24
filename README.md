
**POCKETS**

**PROBLEM I AIM TO SOLVE:**

Often we find that we spend more money on things that are unncessary and miss out buying things that will actually provide some value to our life. One of the reasons is , we think we would save up for the thing we think would add value to our value, but we cannot lock its funds easily at the snap of the fingers. We have to go through a long and tiring process of going physically to the bank and add the funds in some sort of fixed deposit or savings account.

**WHAT I THINK:**

I find this process tiring and not efficient.Thus, I decided to develop Bank Pockets. 

**MY EFFORT TO SOLVE IT:**

Bank Pockets aims to seamlessly integrate in the banking system and allow you to lock funds for particular things and would not allow you to spend the money upfront. This would allow us to control our sudden urge to buy something, knowing you have locked your funds for something of value.

The code as of now is in development and the main idea is to create a account and add multiple pockets associated with that account like a one to many relationship. The function names are self explanatory as what they intend to do.

The flow of the program is as follows.

1. We first create an account object with params such as firstname, lastname of the customer.

2. Class Pocket then inherits the params of its Parent Class Accounts and associates the created pocket objects to its associated bank account.

3. Class Pocket has setters and getters such as getting the pocket balance, the account balance, adding money to the pocket through card and adding money to pocket from bank to name a few.

4. Once you create a pocket object and associate with an account, the function lock_pocket() would lock the pocket from your usage and would discourage the customer from accidentally spending the locked amount.

5. Each Pocket object can be locked down with a pin and you need to verify the pin if you need to do any changes or withdraw the funds.

**This project is an onging project of mine and I would add additional functionalities as and when they are ready to be pushed to this repository.**

This is in general the working of the Project as of now.


**FUTURE WORK:**

1.I plan to use scientific libraries like numpy to better integrate the calculations that will be required to be done.

2. Adding security is also one of the key parts of this project.

3. The beta testing and analysis of the beta/ dummy accounts would be done using pandas and other data science libraries.


**WHAT VALUE IT WOULD PROVIDE:**

This would help us manage our money better, as we have a complete understanding of how much exactly funds are available for leisure activities and how much is present for specific purpose, all at the avaiability of your fingertips.
It would discourage reckless spending and allow us to have a better control of our money that in turn controls our assets and decides our liabilities.


