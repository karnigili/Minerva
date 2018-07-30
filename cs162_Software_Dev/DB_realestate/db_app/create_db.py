from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query
import os

engine = create_engine('sqlite:///estate.db', echo=True)
Base = declarative_base()

INDEX_FLAG = True

## create tables

class Offices(Base):
    __tablename__ = 'Offices'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    zip_code = Column(Integer, ForeignKey('Locations.zip_code'))
    PhoneNum = Column(String)
    Email = Column(String)

    def __repr__(self):
       return "<Offices(id ={}, zip_code={}, PhoneNum={}, Email={})>".format(
                            self.id, self.zip_code, self.PhoneNum, self.Email)

    if INDEX_FLAG:
        __table_args__ = (Index('Offices_id_index', "id"),  )


    '''
    This table lists all offices operating in the agency.
    '''

class Agents(Base):
    __tablename__ = 'Agents'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    FirstName = Column(Integer)
    SurName = Column(String)
    PhoneNum = Column(String)
    LicenseNumber = Column(String)
    Email = Column(String)

    def __repr__(self):
       return "<Agents(id={}, FirstName={}, SurName={}, PhoneNum={}, LicenseNumber={}, Email={})>".format(
                            self.id, self.FirstName, self.SurName, self.PhoneNum, self.LicenseNumber, self.Email)

    if INDEX_FLAG:
        __table_args__ = (Index('Agents_id_index', "id"), Index('Agents_n_index', "FirstName", "SurName"),   )

    '''
    This table lists all agents operating in the agency.

    Two types of indexes;
    1. index on the id column - ease join queries in the many to many combinations
    2. A composite index including first name and last name - ease queries looking for agent information 
    '''

class Offices_Agents(Base):
    __tablename__ = 'Offices_Agents'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    AgentID = Column(Integer, ForeignKey('Agents.id'))
    OfficeID = Column(Integer, ForeignKey('Offices.id'))

    def __repr__(self):
       return "<Offices_Agents(id={}, AgentID={}, OfficeID={})>".format(
                        self.id, self.AgentID, self.OfficeID )
    if INDEX_FLAG:
        __table_args__ = (Index('Offices_Agents_id_index', "id"), 
            Index('Offices_Agents_aid_index', "AgentID"),
            Index('Offices_Agents_oid_index', "OfficeID"),)
    
    '''
    This is a join table, listing the relations between agents to offices.

    To set a many to many relations, I chose to use a join table. This a form of normalization.
    The decision whether to normalize or denormalize is in the balance between insertions to queries. 
    This is since; normalization is lighter on insertion and heavier on queries, whereas denormalization
    is heavier on insertions and lighter on queries.

    I believe the case in a real-estate agent is probably balanced; that is, there are as many insertions as queries. 
    Operating under this assumption, I decided to use a normalization here.

    To improve queries performance, I add indexes to this table on each column. The rationale is
    that these columns are used in joined queries independently further.
    '''

class Property(Base):
    __tablename__ = 'Property'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    zip_code = Column(Integer, ForeignKey('Locations.zip_code'))
    sellerID = Column(Integer, ForeignKey('Sellers.id'))
    BedRooms = Column(Integer)
    BathRooms = Column(Integer)
    ListingPrice = Column(Integer)
    ListingDate = Column(Date)
    ListingOffice_AgentID = Column(Integer, ForeignKey('Offices_Agents.id'))
    StatusID = Column(Boolean) # 0 is open 1 is sold

    def __repr__(self):
       return "<Property(id={}, zip_code={}, sellerID={}, BedRooms={}, BathRooms={}, ListingPrice={}, ListingDate={}, ListingOffice_AgentID={}, StatusID={})>".format(
                        self.id, self.zip_code, self.sellerID, self.BedRooms, self.BathRooms, self.ListingPrice, self.ListingDate, self.ListingOffice_AgentID, self.StatusID)
    if INDEX_FLAG:
        __table_args__ = (Index('ppi_index', "id"),Index('ppz_index', "zip_code"),)

    '''
    This table lists all properties handled by the agency. For simplicity reasons, I have not implemented time bounded 
    contracts and assumed lifetime commitment between a property and an agent.

    I indexed the id column of property to increase performance when querying property 
    considering the columns that are used mostly to interact with this table.
    In this case, id and zip code.
    '''

class Sellers(Base):
    __tablename__ = 'Sellers'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    zip_code = Column(Integer, ForeignKey('Locations.zip_code'))
    FirstName = Column(Integer)
    SurName = Column(String)
    Email = Column(String)
    PhoneNum = Column(String)

    def __repr__(self):
       return "<Sellers(id={}, FirstName={}, SurName={}, PhoneNum={}, zip_code={}, Email={})>".format(
                            self.id, self.FirstName, self.SurName, self.PhoneNum, self.zip_code, self.Email)

    '''
    This table lists all sellers working in the agency.
    '''

class Commissions(Base):
    __tablename__ = 'Commissions'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    MinPrice = Column(Integer)
    MaxPrice = Column(Integer)
    Commission = Column(Float, CheckConstraint('1>Commission>0')) #in 0 to 1 range

    def __repr__(self):
       return "<Commissions(id={}, MinPrice={}, MaxPrice={}, Commission={})>".format(
                            self.id, self.MinPrice, self.MaxPrice, self.Commission)
    '''
    This table holds the commission rates in the agency.

    This table is a form of normalization, instead of re-writing the commission in each case-
This table centralizes this information. It helps maintain ACID since it ensures consistency 
    and enables changes to be performed globally.

    This table will no be inserted to. Hence its small size will not change (about five entries).
    Thus I believe indexes are irrelevant in this case.
    '''

class Buyers(Base):
    __tablename__ = 'Buyers'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    FirstName = Column(Integer)
    SurName = Column(String)
    Email = Column(String)
    zip_code = Column(Integer, ForeignKey('Locations.zip_code'))
    PhoneNum = Column(String)
    creditAuth = Column(Integer)

    def __repr__(self):
       return "<Buyers(id={}, FirstName={}, SurName={}, PhoneNum={}, zip_code={}, Email={}, creditAuth={})>".format(
                            self.id, self.FirstName, self.SurName, self.PhoneNum, self.zip_code, self.Email, self.creditAuth)

    '''
    This table lists all buyers working in the agency.
    '''

class Deals(Base):
    __tablename__ = 'Deals'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    PropertyID = Column(Integer, ForeignKey('Property.id'))
    DealOffice_AgentID = Column(String, ForeignKey('Offices_Agents.id'))  
    DealDate = Column(Date)
    DealPrice = Column(Integer)
    BuyerID = Column(Integer, ForeignKey('Buyers.id'))
    Commission = Column(Integer)

    def __repr__(self):
       return "<Deals(id={}, PropertyID={}, DealOffice_AgentID={}, DealDate={}, DealPrice={}, BuyerID={}, Commission={})>".format(
                            self.id, self.PropertyID, self.DealOffice_AgentID, self.DealDate, self.DealPrice, self.BuyerID, self.Commission)
    if INDEX_FLAG:
        __table_args__ = (Index('Deals_ao_index', "DealOffice_AgentID"), 
            Index('Deals_p_index', "PropertyID"), )


    '''
    This table is listing all done deals. The relation between deals to properties is one to one.
    Hence, each deal considers only one property, and each property can be closed only in one deal.

    The field DealOffice_AgentID is technically redundant since this information can be retrieved from the property table.
    Yet, it represents a form of denormalization which I believe is in place since the use-cases for querying from the deals 
    table and the property table are distinctive; I preferred not to condition the search for deals by looking over the 
    property tables.
    '''

class SumSales(Base):
    __tablename__ = 'SumSales'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ListingOffice_AgentID = Column(Integer, ForeignKey('Offices_Agents.id'))
    SalesSum = Column(Integer)
    SalesCount = Column(Integer)
    CommissionSum = Column(Integer)

    def __repr__(self):
       return "<SumSales(id={}, ListingOffice_AgentID={}, SalesSum={}, SalesCount={}, CommissionSum={})>".format(
                            self.id, self.ListingOffice_AgentID, self.SalesSum, self.SalesCount, self.CommissionSum)

    if INDEX_FLAG:
        __table_args__ = (Index('sumsale_index', "ListingOffice_AgentID"), )

    '''
    This table is a summary table mentions all revenue done by each office_agent. 
    It is being updated with every deal to capture to the current state of the agency.
    Joining with the Office_agent table, it can draw information about each agent and each office.

    The index on the ListingOffice_AgentID represents that there is a tight relation 
    between these tables, thus a performance improvement is in need.
    '''

class Locations(Base):
    __tablename__ = 'Locations'

    zip_code = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Neighborhood = Column (String)
    City = Column (String)
    State = Column (String)

    def __repr__(self):
       return "<Locations(zip_code={}, Neighborhood={}, City={}, State={})>".format(
                            self.zip_code, self.Neighborhood, self.City, self.State)
    if INDEX_FLAG:
        __table_args__ = (Index('zip_index', "zip_code"), )


        '''
        This table lists all zip codes with their associated addresses.
        This is a form of normalization. Since addresses are being written in the DB many times,
        this table makes this operation faster. Moreover, it enables ACID since it helps with the consistency of the information regarding addresses.

        The index ensures better queries since information is most likely to be retrieved using
        the zip code itself.
        '''

def create_schema ():
    try:
        os.remove('estate.db')
    except OSError:
        pass

    Base.metadata.create_all(engine)

if __name__ == "__main__":
    
    create_schema()
    



