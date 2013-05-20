#!/usr/bin/env python
# -*- coding: utf-8 -*-

# classes for events


import sys
import types

sys.path = sys.path + ['..']

from libframes import mac_api
#from libframes.mac_frcl import dc_type2str, dc_stype2str
#from libframes.mac_frcl import dc_type2num, dc_type2str, dc_stype2num, dc_stype2str

'''A module to handle events.

Events type and subtype are reserved for standard compliant denominations, such as Type and Subtype in frames. Field ev_nickname is a descriptive nomination to handle events in Finite State Machines or other; ev_nickname is a convention of this project.
Nickname: 1. A descriptive name added to or replacing the actual name of a person, place, or thing (American Heritage Dictionary).

To create an event use function mkevent().

@var dc_nicknames: a dictionary {nickname: (type, subtype, eventclass) } of valid nicknames, their corresponding type and subtype, and the class object used for construction.
'''



class Event:
    '''A general class for all types of event.
    '''

    def __str__(self):
        ss = 'Event class name: ' + self.__class__.__name__
        ss += "\n  Nickname: '%s'; Type: '%s'; SubType: '%s'"  % \
            ( self.ev_nickname, self.ev_type, self.ev_subtype)
        return ss

class EventFrame(Event):
    '''An event associated with a frame.
    
    @ivar ev_nickname: a descriptive name for this event.
    @ivar ev_type: frame event type.
    @ivar ev_subtype: frame event subtype.
    @ivar src_addr: source address.
    @ivar dst_addr: destination address.
    @ivar frmpkt: a packed frame in bin format, as for transmission.
    '''

    def __init__(self, pnickname, ptype, psubtype, pfrmpkt=''):
        '''Constructor.
        
        Frame event type and subtype must be valid frame type and subtype.
        @param pnickname: a descriptive name for this event.
        @param ptype: frame event type.
        @param psubtype: frame event subtype.
        @param pfrmpkt: a packed frame in bin format, as for transmission.
        '''
        self.ev_nickname = pnickname
        self.ev_type = ptype
        self.ev_subtype = psubtype
        self.src_addr = None
        self.dst_addr = None
        frmpkt = pfrmpkt
        return



class EventTimer(Event):
    '''An event associated with a timer.
    
    @ivar pnickname: a descriptive name for this event.
    @ivar ptype: timer event type.
    @ivar psubtype: timer event subtype.
    @ivar add_info: additional info.
    '''
    
    def __init__(self, pnickname, ptype, psubtype, add_info=None):
        '''Constructor.

        @param pnickname: a descriptive name for this event.
        @param ptype: timer event type.
        @param psubtype: timer event subtype.
        @param add_info: additional info.
        '''
        self.ev_nickname = pnickname
        self.ev_type = ptype
        self.ev_subtype = psubtype
        if add_info:
            self.add_info = add_info
        return


class EventNameException(Exception):
    '''An exception to rise on non valid parameters for event construction.
    '''
    pass        



# a dictionary of nicknames, types and subtypes
#   nickname          :  (type,     subtype )
dc_nicknames = { \
    'CtrlRTS'         : ('Ctrl',   'RTS',     EventFrame ), \
    'CtrlCTS'         : ('Ctrl',   'CTS',     EventFrame ), \
    'CtrlACK'         : ('Ctrl',   'ACK',     EventFrame ), \
    'DataData'        : ('Data',   'Data',    EventFrame ), \
    'ActionOpen'      : ('Mgmt',   'Action',  EventFrame ), \
    'ActionClose'     : ('Mgmt',   'Action',  EventFrame ), \
    'ActionConfirm'   : ('Mgmt',   'Action',  EventFrame ), \
    'MgmtBeacon'      : ('Mgmt',   'Beacon',  EventFrame ), \
    'TimerTOH'        : ('Timer',  'TOH',     EventTimer ), \
    'TimerTOC'        : ('Timer',  'TOC',     EventTimer ), \
    'TimerTOR1'       : ('Timer',  'TOR1',    EventTimer ), \
    'TimerTOR2'       : ('Timer',  'TOR2',    EventTimer ) \
    }

    
def mkevent(pnickname):
    '''Returns an event of the given event nickname.

    >>> ev_ob_tmr = mkevent('TimerTOH')
    >>> print ev_ob_tmr
    Event class name: EventTimer
      Nickname: 'TimerTOH'; Type: 'Timer'; SubType: 'TOH'
    >>> ev_ob_frm = mkevent('CtrlCTS')
    >>> print ev_ob_frm
    Event class name: EventFrame
      Nickname: 'CtrlCTS'; Type: 'Ctrl'; SubType: 'CTS'
    
    @param pnickname: a valid event nickname, i.e. one that is a key in dictionary of valid nicknames.
    '''
    #if not type(eventclass) == types.ClassType:
    #    raise EventNameException('eventclass must be a class object.')
    if dc_nicknames.has_key(pnickname):
        ptype, psubtype, eventclass = dc_nicknames[pnickname]
        return eventclass(pnickname, ptype, psubtype)
    else:
        raise EventNameException(pnickname + ' is not a valid nickname.')



if __name__ == '__main__':
    import doctest
    doctest.testmod()

