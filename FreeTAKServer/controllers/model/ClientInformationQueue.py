#######################################################
# 
# ClientInformationQueue.py
# Python implementation of the Class ClientInformationQueue
# Generated by Enterprise Architect
# Created on:      21-May-2020 9:47:34 AM
# Original author: Natha Paquette
# 
#######################################################
from multiprocessing import Queue

class ClientInformationQueue:
    def __init__(self):  

        self.clientQueue = Queue()