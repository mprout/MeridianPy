import meridian as mn

Master = mn.MeridianMaster(4)

Master.init()

Node0 = mn.MeridianNode(Master, 4)

ST = mn.MeridianStepper(Node0, 0)

ST.init()




