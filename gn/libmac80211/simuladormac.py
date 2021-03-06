# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:55:46 2013

@author: belza, ggomez
"""

import sys
sys.path +=['..']

import Queue,time
import libmanagement.NetworkConfiguration as NetworkConfiguration
import libmanagement.DiscoveryPeeringController as DiscoveryPeeringController
import libmanagement.Beacon as Beacon
import libadaptationlayer.schedEvToFr as schedEvToFr
import libadaptationlayer.schedFrToEv as schedFrToEv
import ieee80211mac as Mac
import libvirtualchannel.virtualchannel as virtualchannel
import libvirtualchannel.EventSimulator as eventsimulator
import libvirtualchannel.EventConsumer as eventconsumer

def simulates():

    "-------------------NODE 1: MAC Addr 100-------------------------------------------------------"    
    " Layer 3 packet queues"
    pkt_rx_q1 = Queue.Queue(10)
    pkt_tx_q1 = Queue.Queue(10)

    " Configuration of the Scheduler of Node 1 that recieves frames and generates management events."
    frame_rx_q1 = Queue.Queue(10)
    ctrl_q1, mgmt_q1, data_q1 = Queue.Queue(10), Queue.Queue(10), Queue.Queue(10)
    out_queues1 = { \
        'Ctrl': (ctrl_q1), \
        'Mgmt': (mgmt_q1), \
        'Data': (data_q1)  \
        }
    sch1 = schedFrToEv.SchedFrToEv(frame_rx_q1, out_queues1)
    sch1.start()
    
    "Configuration of the scheduler of Node 1 that recieves events and generates frame events."
    frame_tx_q1 = Queue.Queue(10)
    tx_ev_q1 = Queue.Queue(10)
    out_queues_tx1 = { \
        'frames':    (frame_tx_q1) \
    }
    tx1 = schedEvToFr.SchedEvToFr(tx_ev_q1, out_queues_tx1)
    tx1.start()

    " Network configuration: the MAC Addr, the name of the network and the broadcast Addr"    
    net_conf1 = NetworkConfiguration.NetworkConfiguration("100",'my network',"256",1)
    net_conf1.retry_timeout = 5    

    " Starts the Controller of The FSM for Peering Discovering"
    #dpcontrol1 =  DiscoveryPeeringController.DiscoveryPeeringController(net_conf1,None,mgmt_q1,tx_ev_q1)
    #dpcontrol1.start()

    " Start the MAC controller"
    macctrl1 = Mac.ControllerMAC( net_conf1, ctrl_q1, mgmt_q1, data_q1, tx_ev_q1, pkt_rx_q1, pkt_tx_q1 )
    macctrl1.start()

    "Starts the beacon generator of this node"
    #myBeacon1 = Beacon.Beacon(net_conf1 ,tx_ev_q1)
    #myBeacon1 = Beacon.Beacon(net_conf1 ,pkt_rx_q1 )
    #myBeacon1.start()    

    "---------------------END NODE 1 -----------------------------------------------"
    
    "-------------------NODE 2: MAC Addr 101-------------------------------------------------------"    
    " Layer 3 packet queues"
    pkt_rx_q2 = Queue.Queue(10)
    pkt_tx_q2 = Queue.Queue(10)

    " Configuration of the Scheduler of Node 2 that recieves frames and generates management events."
    frame_rx_q2 = Queue.Queue(10)
    ctrl_q2, mgmt_q2, data_q2 = Queue.Queue(10), Queue.Queue(10), Queue.Queue(10)
    out_queues2 = { \
        'Ctrl': (ctrl_q2), \
        'Mgmt': (mgmt_q2), \
        'Data': (data_q2)  \
        }
    sch2 = schedFrToEv.SchedFrToEv(frame_rx_q2, out_queues2)
    sch2.start()
    
    "Configuration of the scheduler of Node 2 that recieves events and generates frame events."
    " The frames tx queue is the same for all nodes ( = frame_tx_q1) to simulates a shared medium"
    frame_tx_q2 = frame_tx_q1
    tx_ev_q2 = Queue.Queue(10)
    out_queues_tx2 = { \
        'frames':    (frame_tx_q2) \
    }
    tx2 = schedEvToFr.SchedEvToFr(tx_ev_q2, out_queues_tx2)
    tx2.start()

    " Network configuration: the MAC Addr, the name of the network and the broadcast Addr"    
    net_conf2 = NetworkConfiguration.NetworkConfiguration("101",'my network',"256",1)
    net_conf2.retry_timeout = 5    

    " Starts the Controller of The FSM for Peering Discovering"
    #dpcontrol2 =  DiscoveryPeeringController.DiscoveryPeeringController(net_conf2,None,mgmt_q2,tx_ev_q2)
    #dpcontrol2.start()

    " Start the MAC controller"
    macctrl2 = Mac.ControllerMAC( net_conf2, ctrl_q2, mgmt_q2, data_q2, tx_ev_q2, pkt_rx_q2, pkt_tx_q2 )
    macctrl2.start()

    "Starts the beacon generator of this node"
    #myBeacon2 = Beacon.Beacon(net_conf2 ,tx_ev_q2)
    #myBeacon2 = Beacon.Beacon(net_conf2 ,pkt_rx_q2 )
    #myBeacon2.start()  

    
    "-------------------END NODE 101-------------------------------------------------------"    
  

 
    "-------------------NODE 3: MAC Addr 102-------------------------------------------------------"    
    " Layer 3 packet queues"
    pkt_rx_q3 = Queue.Queue(10)
    pkt_tx_q3 = Queue.Queue(10)

    " Configuration of the Scheduler of Node 3 that recieves frames and generates management events."
    frame_rx_q3 = Queue.Queue(10)
    ctrl_q3, mgmt_q3, data_q3 = Queue.Queue(10), Queue.Queue(10), Queue.Queue(10)
    out_queues3 = { \
        'Ctrl': (ctrl_q3), \
        'Mgmt': (mgmt_q3), \
        'Data': (data_q3)  \
        }
    sch3 = schedFrToEv.SchedFrToEv(frame_rx_q3, out_queues3)
    sch3.start()
    
    "Configuration of the scheduler of Node 3 that recieves events and generates frame events."
    " The frames tx queue is the same for all nodes ( = frame_tx_q1) to simulates a shared medium"
    frame_tx_q3 = frame_tx_q1
    tx_ev_q3 = Queue.Queue(10)
    out_queues_tx3 = { \
        'frames':    (frame_tx_q3) \
    }
    tx3 = schedEvToFr.SchedEvToFr(tx_ev_q3, out_queues_tx3)
    tx3.start()

    " Network configuration: the MAC Addr, the name of the network and the broadcast Addr"    
    net_conf3 = NetworkConfiguration.NetworkConfiguration("102",'my network',"256",1)
    net_conf3.retry_timeout = 5    

    " Starts the Controller of The FSM for Peering Discovering"
    #dpcontrol3 =  DiscoveryPeeringController.DiscoveryPeeringController(net_conf3,None,mgmt_q3,tx_ev_q3)
    #dpcontrol3.start()

    " Start the MAC controller"
    macctrl3 = Mac.ControllerMAC( net_conf3, ctrl_q3, mgmt_q3, data_q3, tx_ev_q3, pkt_rx_q3, pkt_tx_q3 )
    macctrl3.start()

    "Starts the beacon generator of this node"
    #myBeacon3 = Beacon.Beacon(net_conf3 ,tx_ev_q3)
    #myBeacon3 = Beacon.Beacon(net_conf3 ,pkt_rx_q3 )
    #myBeacon3.start()  
    "---------------------END NODO 102 -----------------------------------------------"

    vc= virtualchannel.VirtualChannel(frame_tx_q1)
    vc.add(frame_rx_q1) 
    vc.add(frame_rx_q2)
    vc.add(frame_rx_q3)
    vc.start()
	
    # rx_event = frame_tx_q1.get()
    print "Start Simulator"
    mySimulator = eventsimulator.EventSimulator( 100,"DataData", pkt_rx_q1,"100","101")
    mySimulator.start()

    print "Start Consumers"
    myConsumer1 = eventconsumer.EventConsumer( "Node1-L3", pkt_tx_q1 )
    myConsumer1.start()

    myConsumer2 = eventconsumer.EventConsumer( "Node2-L3", pkt_tx_q2 )
    myConsumer2.start()

    myConsumer3 = eventconsumer.EventConsumer( "Node3-L3", pkt_tx_q3 )
    myConsumer3.start()

if __name__ == '__main__':
    try:
        simulates()
    except KeyboardInterrupt:
        pass


