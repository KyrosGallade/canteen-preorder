This web app was made to allow students to pre-order their meals to reduce queues in canteens. Although, it didn't turn out like I had hoped due to limitations in my knowledge (not knowing how to use cookies for logins and limited JavaScript knowledge), the functions I wanted could be implemented.

# Ordering
Students using the web app will first be brought to the home page, where they are presented with a menu that allows them to choose which stall they wish to order from, what item they wish to purchase from the stall, the quantity and any additional requests. The item selection changes depending on which stall they choose through the use of JavaScript to change the options.

Once they have submitted their order, they will be brought to a page that shows their order number, which they will have to display to the store owner to confirm they are the ones who submitted the order. The payment will then be made through cash.

# Owners
For owners, there will be a hyperlink at the bottom of the home page that brings them to the login page for stall vendors. Each store owner can enter their username and password, which will bring them to the page for the stall vendors. 

The page for vendors allows them to view the order details sent by the students, as well as a button that will allow them to mark the order as complete once the customer has paid. They can also check the history of all the orders sent previously in the database.

# Challenges
1: At first, I did not know cookies existed until after I had made my videos. This would have helped with issues with displaying all_orders from each stall owner.
2: I had trouble troubleshooting many parts of my html due to not being experienced with Flask
