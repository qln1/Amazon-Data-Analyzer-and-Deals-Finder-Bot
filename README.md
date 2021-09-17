# Amazon-Data-Analyzer-and-Deals-Finder-Bot
Web scrapes Amazon for the most competitive prices by searching for the highest discounts. Then it will list the collected product information into an Excel spreadsheet for easy sorting and viewing.

<h2>About</h2>
This program web scrapes the product view page on Amazon and analyzes each product for and looks to see if there is a sale going on. The user can modify the Amazon link as needed to search for different products and categories. The user can specify the maximum and minimum discounts they are looking for and the program will only list products within that price range. For example, if the user sets the lowest_discount to 60 and the highest discount to 100, then the program will look for products that have 60% off or higher. After the program has searched the entire page, then it will list the results in an Excel spreadsheet for easy viewing and record-keeping.

<h2>Goal and Requirements</h2>
The goal of this project is provide users with a way to more accurately search and find deals on Amazon. Through this program, the user can search for the best possible deals available and have all of the products listed in a convinient and easy to review way through an Excel spreadsheet. This program analyzes the current product and sees if a discount is available. If there isn't a discount or the discount doesn't meet the user's criteria, the program moves on. If the proper discount is listed, then the program will store the prduct's name, original price, new price, discount and the current customer ratings, which include the number of stars and the number of customer reviews.

<h2>Installation</h2>
1. Microsoft Excel, Beautiful Soup, and the XLWT library should be pre-installed.
2. Download this project as zip and extract it <br />
3. Open in any IDE that supports Python (such as Pycharm) <br />
4. Compile and run

<h2>Authors</h2>
Quintin Nguyen
