

## App description
This app serves as a database for a hypothetical real estate company. The DB holds information about the offices, agents, sellers, buyer, properties, and deals. The app contains dummy data to provide demo results. 


## DB structure and relations

1. Offices: This contains information about the agency offices
2. Agents: This includes information on the agency agents
3. Offices_Agents: reflects the many-to-many relations between the agents to the offices. Handels two foreign keys, one for each table which it joins.
4. Property: Contains all the listed properties the agency handles. For simplicity reasons, I have not 
    Implemented time bounded contracts and assumed lifetime commitment between a property and an agent. Evry entry entails information about the seller and the agent, allows many-to-one relationship; such that sellers and agents can handle more than one property (but not vise verse).
5. Sellers: This contains information about the homeowners selling through the agency.
6. Buyers: This includes information on the home seekers looking to buy through the agency.
7. Commissions: This table holds the rates of commissions agents receive for a given sale price.
8. Deals: This table holds all deals ever made within the agency, linked to a property id
9. SumSales: A summary table that contains information regarding the sales per office_agent.
10. Locations: connects zip code to a general address


## Running instruction

python3.6 -m venv .venv\
source .venv/bin/activate\
pip3 install -r requirements.txt\
python3 init_db.\
python3 query_data.py

## demo results

Query sample results
------------------------

Top five offices and their sales 

Email    PhoneNum    id    sales    zip_code
-------  ----------  ----  -------  ----------

Top agents and their sales 

Last name    PhoneNum    sales    Email    First name    id
-----------  ----------  -------  -------  ------------  ----

Commission per agents
First name    Surname    commission
------------  ---------  ------------

AVG market days
   days
-------
7868.46

AVG sell price
  price
-------
 305277

Top sell zips
  zip     sum
-----  ------
10002  174262
10005  197046
10008  266534
10009  267907
10000  317166


