from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query
import datetime
import pprint
import numpy as np

from faker import Faker
from create_db import *

engine = create_engine('sqlite:///estate.db')
Session = sessionmaker(bind=engine)
session = Session()
faker = Faker()


class DealException(Exception):
    # expection for deal validation failure
    def __init__(self, *args, **kwargs):
        super(Exception, self).__init__(*args, **kwargs)

def close_a_deal (buyer_id, property_id, deal_price, session):
    
    today_date = datetime.datetime.now().date()

    try:
        # check auth
        credit_auth = session.query(Buyers.creditAuth).filter_by(id = buyer_id).first()[0]  # enough credit
        status_of_property = session.query(Property.StatusID).filter_by(id = property_id).first()[0]  # open to be sold

        if not (credit_auth >= deal_price and status_of_property == 0):
            print ('credit auth {}/ deal price {}, property ava {}'.format(credit_auth, deal_price,status_of_property))
            session.rollback()
            raise DealException(credit_auth, status_of_property)

        # insert to deals
        comm = session.query(Commissions.Commission).filter(and_(Commissions.MaxPrice > deal_price , Commissions.MinPrice < deal_price)).all()[0][0]
        deal_oa = session.query(Property.ListingOffice_AgentID).filter(Property.id == property_id).all()[0][0]


        insert_deal = Deals(PropertyID=property_id, DealDate=today_date, DealPrice= deal_price, BuyerID=buyer_id, Commission=comm*deal_price)
        session.add(insert_deal) 

        # change prop status
        session.query(Property).filter(Property.id == property_id).update({Property.StatusID: 1})

        #update summary table
        session.query(SumSales).filter(SumSales.ListingOffice_AgentID == deal_oa).update({
            SumSales.SalesCount: SumSales.SalesCount+1,
            SumSales.SalesSum: SumSales.SalesSum+deal_price, 
            SumSales.CommissionSum: SumSales.CommissionSum+comm*deal_price })

        summary_ag = session.query(SumSales).filter(SumSales.ListingOffice_AgentID == deal_oa).all()
        summary_all = session.query(SumSales).filter(SumSales.ListingOffice_AgentID == deal_oa).all()

        session.query(func.sum(SumSales.SalesCount).label('deals'),
            func.sum(SumSales.SalesSum).label('sum'),
            func.sum(SumSales.CommissionSum).label('com')
            ).group_by(SumSales.ListingOffice_AgentID).all()

    except:
        session.rollback()
        raise

    deal_details = {
        'buyer_id' :buyer_id,
        'date':today_date,
        'credit status':credit_auth,
        'propert_status':status_of_property,
        'agent':deal_oa,
        'Commission':comm,
        'summay':summary_ag,
        'all':summary_all
    }

    return deal_details

def add_agent(agent_details, session):
    # name,lastname, phone, license, mail, zip
    try:
        ag = Agents(FirstName=agent_details['name'], SurName=agent_details['surname'], PhoneNum=agent_details['phone'], LicenseNumber=agent_details['License'], Email=agent_details['mail'])
        session.add(ag)
        session.flush()

        office_id = session.query(Offices.id).filter(Offices.zip_code == agent_details['zip']).first()
        office_id = office_id[0]

        # update agent ofice
        ao = Offices_Agents(AgentID=ag.id, OfficeID = office_id)
        session.add(ao)
        session.flush()

        ss = SumSales(ListingOffice_AgentID= ao.id, SalesSum = 0, SalesCount= 0, CommissionSum = 0)
        session.add(ss)

    except:
        session.rollback()
        raise

def insert_data (n=2):


    scaling_array = {'offices':n, 'agents':10*n, 'properties':20*n, 'buyers':5*n, 'deals':4*n}

    insert_commissions = [ 
        Commissions( id = 9001 , MinPrice = 0, MaxPrice = 100000, Commission = .1),
        Commissions( id = 9002, MinPrice = 100000, MaxPrice = 200000, Commission = .075),
        Commissions( id = 9003, MinPrice = 200000, MaxPrice = 500000, Commission = .06),
        Commissions( id = 9004, MinPrice = 500000, MaxPrice = 1000000, Commission = .05),
        Commissions( id = 9005, MinPrice = 1000000, MaxPrice = float('inf'), Commission = .04)]

    session.add_all(insert_commissions)
    session.commit()

    # add fake data

    # Locations
    zips = [i for i in range(10000,99999)][0:scaling_array['offices']]

    faker_locations = [Locations(zip_code = i , Neighborhood = faker.city(), City = faker.city(), State = faker.state()) for i in zips]
    session.add_all(faker_locations)
    session.commit()

    # Offices
    faker_offices = [Offices(zip_code = i, PhoneNum=faker.phone_number(),Email=faker.email()) for i in zips]
    session.add_all(faker_offices)
    session.commit()

    # Agents

    faker_agents = [Agents(id=i, FirstName=faker.name().split()[0], SurName=faker.name().split()[1], PhoneNum=faker.phone_number(), LicenseNumber=faker.ssn(), Email=faker.email()) for i in range (scaling_array['agents'])]

    for agent in faker_agents:
        data = {'id':agent.id, 'name':agent.FirstName,'surname':agent.SurName, 'phone':agent.PhoneNum, 'License':agent.LicenseNumber, 'mail':agent.Email, 'zip': np.random.choice(zips)}
        add_agent(data, session=session)
    session.commit()

    # Sellers
    n_sellers = 8
    faker_sellers = [Sellers(zip_code = np.random.choice(zips), FirstName=faker.name().split()[0], SurName=faker.name().split()[1], Email = faker.email(), PhoneNum = faker.phone_number()) for i in range(n_sellers)]
    session.add_all(faker_sellers)
    session.commit()

    sellers_id =  [f_seller.id for f_seller in faker_sellers]
    oa_id = session.query(Offices_Agents.id).all()
    oa_id = [i[0] for i in oa_id]

    # Properties

    faker_property = [Property(zip_code = np.random.choice(zips), sellerID = np.random.choice(sellers_id), BedRooms = np.random.choice(range(1,8)), BathRooms = np.random.choice(range(1,5)), ListingPrice = np.random.choice(range(700000,4500000)), ListingDate = datetime.datetime.strptime(faker.date(), "%Y-%m-%d").date(), ListingOffice_AgentID = np.random.choice(oa_id), StatusID = 0) for i in range(scaling_array['properties'])]
    session.add_all(faker_property)
    session.commit()

    # Sumsales
    sumsales = [SumSales(ListingOffice_AgentID= i, SalesSum = 0, SalesCount= 0, CommissionSum = 0) for i in oa_id]
    session.add_all(sumsales)
    session.commit()

    # Buyers

    faker_buyer = [ Buyers(FirstName=faker.name().split()[0], SurName=faker.name().split()[1], Email = faker.email(), zip_code = np.random.choice(zips), PhoneNum = faker.phone_number(), creditAuth = np.random.choice(range(550000,6500000))) for i in range(scaling_array['buyers'])]
    session.add_all(faker_buyer)
    session.commit()

    # Deals
    n_buyers = scaling_array['deals']
    for i in range(1, n_buyers):
        close_a_deal(buyer_id=np.random.choice(range(1,n_buyers)), property_id=i, deal_price = np.random.choice(range(150000,500000)), session=session)
    session.commit()


    session.close()

if __name__ == "__main__":
    insert_data()

