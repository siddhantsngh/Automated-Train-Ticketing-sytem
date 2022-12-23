# Automated Train Ticketing System

A smart city train ticketing and tracking system. <br>
Works on the premise that every citizen has an ID card which is also has their bank account linked to the card. <br>
Swiping the card at the station records the starting station and user data into the railway database. <br>
When the user gets off and swipes the card, fare is deducted fom the bank account linked with the ID card. And journey is terminated.<br>

## Starting cum Login Page
---
<pre>
                 _______________________
                |<u>GCity Railways</u>________&#9746
                |                       |
                |     <u>GCity Railways</u>    |
                |         ____________  |
                |   SIN: |____________| |
                |                       |
                |         |<u>Login</u>|       |
                |                       |
                |         |<u>Exit</u>|        |
                |_______________________|
</pre>
After this the user is granted entry, but if the SIN does not exist in the database, then a warning message box is displayed.

## Warning Box
---
<pre>
                 ____________________
                |<u>GCity Railways</u>    &#9746|
                |                   |
                | User Not Found  &#9746 |
                |___________________|
</pre>