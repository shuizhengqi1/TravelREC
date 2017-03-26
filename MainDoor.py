import sys
from CommonUnits import CNList
from CommonUnits import Redis
from XIECHENGParse import Ticket
import random
import string

Airportlist = CNList().getAirportList()
Idsalt = ''.join(random.sample(string.ascii_letters + string.digits, 6))
Ticket = Ticket()
for ap in Airportlist:
    Ticket.GetLowTicketInfo(Idsalt,'XMN',ap[1],"04-02",len(Airportlist))