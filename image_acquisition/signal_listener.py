import serial.tools.list_ports

ports = serial.tools.list_ports.comports(0)
portList = []
serialInst = serial.Serial()


for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("select port: /dev/cu.")

for i in range(len(portList)):
    if portList[i] .startswith('/dev/cu.' + str(val)):
        portVar = "/dev/cu." + str(val)
        print(portList[i])

serialInst.port = portVar
serialInst.baudrate = 9600
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf'))