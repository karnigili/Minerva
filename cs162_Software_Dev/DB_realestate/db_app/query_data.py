from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query
import datetime
import pprint
import numpy as np
from create_db import *
from tabulate import tabulate



engine = create_engine('sqlite:///estate.db')

meta = MetaData()
meta.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

## Queries 

def top_five_ofices (session):
    ##1 Find the top 5 offices with the most sales for that month.

    top_five_offices_q = session.query(Offices.id, Offices.zip_code, Offices.Email, Offices.PhoneNum, func.count(Deals.PropertyID).label('sales') ).\
    join(Offices_Agents, Offices_Agents.OfficeID == Offices.id).\
    join(Deals, Offices_Agents.id == Deals.DealOffice_AgentID).\
    group_by(Offices_Agents.OfficeID).\
    filter(Deals.DealDate > datetime.datetime.now().date().replace(day=1)).\
    order_by(func.sum(Deals.PropertyID)).limit(5).all()
    
    return top_five_offices_q

def top_five_agents(session):
    # 2 Find the top 5 estate agents who have sold the most 
    # (include their contact details and their sales details

    top_five_agents_q = session.query(Agents.id, Agents.FirstName, Agents.SurName, Agents.Email, Agents.PhoneNum, func.count(Deals.PropertyID)).\
    join(Deals, Offices_Agents.AgentID == Agents.id).\
    join(Offices_Agents, Offices_Agents.id == Deals.DealOffice_AgentID).\
    group_by(Offices_Agents.OfficeID).\
    filter(Deals.DealDate > datetime.datetime.now().date().replace(day=1)).\
    order_by(func.sum(Deals.PropertyID)).\
    limit(5).all()

    return top_five_agents_q

def commision_per_agent(session):
    #3 Calculate the commission that each estate agent must receive and store the results in a separate table.
    agent_commission = session.query(Agents.FirstName, Agents.SurName, func.sum(SumSales.CommissionSum)).\
    join(Offices_Agents, Offices_Agents.AgentID == Agents.id).\
    join(SumSales, SumSales.ListingOffice_AgentID == Offices_Agents.id).\
    join(Deals, Deals.DealOffice_AgentID == Offices_Agents.id).\
    filter(Deals.DealDate > datetime.datetime.now().date().replace(day=1)).\
    group_by(Offices_Agents.AgentID).\
    all()

    return agent_commission

def avg_market_days(session):
    # 4 For all houses that were sold that month, calculate the average number of days that the house was on the market.

    avg_selling_days = session.query( func.avg(func.julianday(Deals.DealDate)-func.julianday(Property.ListingDate))).\
    join(Property, Deals.PropertyID == Property.id).\
    filter(Deals.DealDate > datetime.datetime.now().date().replace(day=1)).\
    all()

    return avg_selling_days

def avg_price(session):
    # 5 For all houses that were sold that month, calculate the average selling price

    avg_selling_price = session.query(func.avg(Deals.DealPrice)).\
    filter(Deals.DealDate > datetime.datetime.now().date().replace(day=1)).\
    all()

    return avg_selling_price

def top_zips(session):
    # 6 Find the zip codes with the top 5 average sales prices
    top_zip = session.query(Property.zip_code, func.avg(Deals.DealPrice)).\
    join(Deals, Deals.PropertyID == Property.id).\
    filter(Deals.DealDate > datetime.datetime.now().date().replace(day=1)).\
    group_by(Property.zip_code).\
    order_by(func.avg(Deals.DealPrice)).\
    limit(5).all()

    return top_zip

def time_it (query):
    begining = datetime.datetime.now()
    query(session=session)
    end = datetime.datetime.now()

    return (end-begining)



if __name__ == "__main__":



    print ('Query sample results')
    print ('------------------------')
    print ('\nTop five offices and their sales \n')
    re_five_o = ( top_five_ofices(session=session))

    
    headers = ['id', 'zip_code', 'Email', 'PhoneNum','sales']
    t = {col:[] for col in headers}
    
    for r in re_five_o:
        for col,i in zip(headers, range(len(headers))):
            t[col].append(r[i])

    print (tabulate(t, headers='keys'))

    print ('\nTop agents and their sales \n')
    re_five_a = ( top_five_agents(session=session))

    
    headers = ['id', 'First name', 'Last name','Email', 'PhoneNum','sales']
    t = {col:[] for col in headers}
    
    for r in re_five_a:
        for col,i in zip(headers, range(len(headers))):
            t[col].append(r[i])
    
    print (tabulate(t, headers='keys'))

    print ('\nCommission per agents')
    com = ( commision_per_agent(session=session))

    
    headers = ['First name', 'Surname', 'commission']
    t = {col:[] for col in headers}
    
    for r in com:
        for col,i in zip(headers, range(3)):
            t[col].append(r[i])

    print (tabulate(t, headers=[i for i in t.keys()]))

    print ('\nAVG market days')
    avg_market =  ( avg_market_days(session=session))

    print (tabulate(avg_market, headers=['days']))

    print ('\nAVG sell price')
    avg_price = avg_price(session=session)

    print (tabulate(avg_price, headers=['price']))

    print ('\nTop sell zips')
    zips = top_zips(session=session)

    print (tabulate(zips, headers=['zip','sum']))
    
    session.close()

