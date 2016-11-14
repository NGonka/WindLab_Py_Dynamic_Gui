import serial,json,time,csv,sys
from serial.tools import list_ports

import time
import pylab
import numpy as np
import threading
import scipy
import scipy.fftpack
import Queue




class DataHandling(object):
    """
    
    """
    
    def __init__(self,port=None,baudrate=250000, timeout=5):
        """ """
        self.port=port
        self.baudrate=baudrate
        self.timeput=timeout
        ports_available=list(list_ports.comports())
        if not self.port:
            portlist=[]
            for port in ports_available:
                portlist.append(port[0])
            portlist= sorted(portlist)
            # print(self.portlist)
        # self.portlist = serial.tools.list_ports.comports()
        # print
        # print (serial.tools.list_ports.comports())
        # for p in self.portlist: print p
        # try:
            # self.portlist = serial.tools.list_ports.comports()
            # print(self.portlist)
        # except:
            # print("No active com ports found")
            # exit()
    
    #===========================================================================
    # ### SERIAL COMUNICATION SETUP
    #===========================================================================
    
    def portList(self):
        print("portList port: %s" %self.port)
        ports_available=list(list_ports.comports())
        if not self.port:
            portlist=[]
            for port in ports_available:
                portlist.append(port[0])
            portlist= sorted(portlist)
            # print(self.portlist)
        return portlist
        
    def setPort(self,port):
        self.port=port
        print("setPort to: %s"%self.port)
        
    def openCom(self):
        try:
            self.ser = serial.Serial(self.port,self.baudrate, dsrdtr=True)
#             self.ser = serial.Serial(self.port,self.baudrate, dsrdtr=False)
            return True
        except Exception,e: 
            print str(e)
            return False
    
    def closeCom(self):
        try:
            
            self.ser.flushOutput()
            self.ser.close()
            print("closeCom:  close com port")
            return True
        except:
            print("closeCom: cannot close com port")
            return False
            
    #===========================================================================
    # DATA HANDLING
    #===========================================================================
      
    
    def start_serial_data_stream(self):
        try:
            self.ser.flushOutput()
            self.ser.write("AC")
            time.sleep(1.0)
            self.ser.write("AA")
            return
        except Exception,e: print e
    
    def stop_data_stream(self):
        self.close()
        self.ser.write("A0")
        time.sleep(1.0)
        
        
    def start_data_stream(self):
        self.start_serial_data_stream()
        self.keepRecording=True
        self.data=None
        self.fft=None
        self.dataFiltered=None
        self.stream_thread_new()
#         if self.ser.isOpen():
#             self.stream_readchunk()
#             self.stream=self.readlineSD()
#             print("start_data_stream:." + self.stream+".")
            
    
    def readlineSD(self):
        serialData=""
        start = False
        
        while True:
#            print("start")
            ch = self.ser.read()
            # print(len(ch))
            # print(type(ch))
            # print(ch)
            try: 
                if ch.decode('utf-8')=='{':
                    start=True
            except:
                pass
            if start:
                try:
                    serialData+=ch.decode('utf-8')
                    
                except:
                    print('Fail to decode')
                    pass
    #             print('serialData: {0}', str(serialData))
                try:
                    if serialData.find('}\r\n',0)!=-1:
                        print('readlineSD serialData: %s' %str(serialData))
                        return serialData[1:-3]
                except:
                    print('Fail to find Endchar')
                    pass
    
    def string_to_array(self, datastring):
        datastring = np.asarray(datastring.split(',')).astype(long)
        
        if len(datastring) == 13:
            return datastring
        else:
            raise ValueError('Wrong String length %d'% len(datastring))
            
                
    #===========================================================================
    # Stream Handling
    #===========================================================================
    
    
    
    def stream_readchunk(self):
        try:
            print("stream_readchunk: %s"%self.readlineSD())
            print("stream_readchunk: %d"%self.string_to_array(self.readlineSD()))
#             self.data = np.fromstring(self.readlineSD(), dtype=np.int16)
#             print "stream_readchunk"+ self.data
            
        except Exception, e:
            print ("## Eception! Terminating Stream")
            print (e)
            self.keepRecording=False
        
        if self.keepRecording:
            self.stream_thread_new()
        else:
            self.close()
            print("Stream stopped")
    
    def stream_thread_new(self):
        self.t = threading.Thread(target=self.stream_readchunk)
        self.t.start()
        
    def close(self):
        self.keepRecording=False
        print("Wait for Thread to close")
        while (self.t.isAlive() ):
            time.sleep(0.01)
        print("Thread is closed")        
#         self.stream.stop_data_stream()
        
    
if __name__=="__main__":
    data= DataHandling()
    print("in if")