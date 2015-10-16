from ctypes import *
from const import *
import errorcodes
import IPython
import time

# XXX make this refer to somewhere more sane
mdll = WinDLL("C:\control\drivers\MNuserDriver10.dll")

homepos = None


# function for converting python bools to meridian bools
def mnBool(val):
    if val == False:
        return c_ushort(0)
    if val == True:
        return c_ushort(-1)


def checkerror(err):
    code = errorcodes.lookup(err)
    if code[0] == "MN_OK":
        return True
    raise Exception(' '.join(code))

    #
    # print "Motor files:"
    # for node in self.nodes:
    #     print "Node %d: " % (node),
    #     print '"%s"' % (self.iscGetMotorFileName(node))
    #


class MeridianMaster(object):
    def __init__(self, port, baud=115200):
        self.port = port
        self.baud = baud
        self.dllsetup()
        return

    def init(self):
        self.mnInitializeNets()
        self.nodecnt = self.mnSysNodeCount()
        print "Node count: %d" % self.nodecnt

        self.nodes = self.mnSysInventoryRecord(NODEID_MD, maxdev=self.nodecnt)
        print "nodeids: ",
        print self.nodes

        print "Restarting net:"
        self.mnRestartNet(0, True)
        return

    def dllsetup(self):
        mdll.mnSysNodeCount.restype = c_ulong
        mdll.mnShutdown.restype = c_ulong
        mdll.mnSysInventoryRecord.restype = c_ulong
        mdll.mnRestartNode.restype = c_ulong
        mdll.mnRestartNet.restype = c_ulong
        mdll.iscGetAppConfigReg.restype = c_ulong
        mdll.iscSetAppConfigReg.restype = c_ulong
        mdll.iscGetStatusRTReg.restype = c_ulong
        mdll.iscGetMotorFileName.restype = c_ulong
        mdll.iscGetParameter.restype = c_ulong
        mdll.netAlertClear.restype = c_ulong
        mdll.iscSetParameter.restype = c_ulong
        mdll.iscGetUserOutputReg.restype = c_ulong
        mdll.iscSetUserOutputReg.restype = c_ulong
        mdll.iscForkMoveEx.restype = c_ulong
        mdll.mnInitializeNets.restype = c_ulong
        mdll.netNodeStop.restype = c_ulong
        mdll.iscForkVelMove.restype = c_ulong
        mdll.iscGetHwConfigReg.restype = c_ulong
        mdll.iscAddToPosition.restype = c_ulong
        mdll.iscGetHwConfigReg.restype = c_ulong
        mdll.iscGetWarningReg.restype = c_ulong
        mdll.iscGetParameterEx.restype = c_ulong
        return

    def mnInitializeNets(self):
        class CTRLSPEC(Structure):
            _fields_ = [("baud", c_ulong),
                        ("port", c_ushort)]

        cs = CTRLSPEC()
        cs.port = self.port
        cs.baud = self.baud

        err = mdll.mnInitializeNets(mnBool(False), c_ulong(1), pointer(cs))
        checkerror(err)
        return

    def mnSysNodeCount(self):
        res = c_ulong()
        err = mdll.mnSysNodeCount(byref(res))
        checkerror(err)
        return res.value

    def mnShutdown(self):
        err = mdll.mnShutdown()
        checkerror(err)
        return

    def mnSysInventoryRecord(self, devtype, maxdev):
        res = (c_uint16 * maxdev)()
        err = mdll.mnSysInventoryRecord(c_uint16(devtype), c_ulong(maxdev), byref(res))
        checkerror(err)

        ret = []
        for node in res:
            ret.append(node)

        return ret

    def mnRestartNode(self):
        err = mdll.mnRestartNode(c_uint16(self.addr))
        checkerror(err)
        return

    def mnRestartNet(self, channel, restart):
        restart = mnBool(restart)
        err = mdll.mnRestartNet(c_uint32(channel), restart)
        checkerror(err)
        return


class MeridianNode(object):
    def __init__(self, master, addr):
        self.master = master
        self.addr = addr
        return

    def init(self):
        self.enable()

    def enable(self):
        self.netNodeStop(self.addr, STOP_TYPE_CLR_ALL)
        self.netAlertClear()
        if hasattr(self, 'safespeed'):
            self.safespeed()

        reg = self.iscGetUserOutputReg()
        reg['Enable'] = True
        self.iscSetUserOutputReg(reg)
        return

    def disable(self):
        reg = self.iscGetUserOutputReg()
        reg['Enable'] = False
        self.iscSetUserOutputReg(reg)
        return

    def iscGetAppConfigReg(self):
        regs = c_uint32()
        err = mdll.iscGetAppConfigReg(c_uint16(self.addr), byref(regs))
        checkerror(err)
        return AppConfigReg(regs.value)

    def iscSetAppConfigReg(self, reg):
        err = mdll.iscSetAppConfigReg(c_uint16(self.addr), c_uint32(reg.data))
        checkerror(err)
        return

    def iscGetStatusRTReg(self):
        regs = (c_uint16 * 3)()
        err = mdll.iscGetStatusRTReg(c_uint16(self.addr), byref(regs))
        checkerror(err)

        # pack into bitstruct
        return StatusReg(regs[2] | (regs[1] << 16) | (regs[2] << 32))

    def iscGetMotorFileName(self):
        buflen = 1024
        buf = c_char_p(' ' * buflen)
        err = mdll.iscGetMotorFileName(c_uint16(self.addr), buf, c_uint16(buflen))
        checkerror(err)
        return buf.value

    def iscGetParameter(self, param):
        res = c_double()
        p = c_uint32(param)
        err = mdll.iscGetParameter(c_uint16(self.addr), p, byref(res))
        checkerror(err)
        return res.value

    def netNodeStop(self, stoptype, all=False):
        err = mdll.netNodeStop(c_uint16(self.addr), c_uint16(stoptype), mnBool(all))
        checkerror(err)
        return

    def netAlertClear(self):
        err = mdll.netAlertClear(c_int16(self.addr))
        checkerror(err)
        return

    def iscSetParameter(self, param, val):
        p = c_uint32(param)
        err = mdll.iscSetParameter(c_int16(self.addr), p, c_double(val))
        checkerror(err)
        return

    def iscGetUserOutputReg(self):
        reg = c_uint16()
        err = mdll.iscGetUserOutputReg(c_uint16(self.addr), byref(reg))
        checkerror(err)
        return UserOutputReg(reg.value)

    def iscSetUserOutputReg(self, reg):
        err = mdll.iscSetUserOutputReg(c_uint16(self.addr), c_uint16(reg.data))
        checkerror(err)
        return

    def iscForkMoveEx(self, pos, movetype):
        mt = c_uint16(movetype)
        err = mdll.iscForkMoveEx(c_uint16(self.addr), c_long(pos), mt)
        checkerror(err)
        return

    def iscForkVelMove(self, vel, triggered=False):
        err = mdll.iscForkVelMove(c_uint16(self.addr), c_double(vel), mnBool(triggered))
        checkerror(err)
        return

    def iscGetHwConfigReg(self):
        res = c_uint32()
        err = mdll.iscGetHwConfigReg(c_uint16(self.addr), byref(res))
        checkerror(err)
        return res

    def iscSetHwConfigReg(self, reg):
        err = mdll.iscSetHwConfigReg(c_uint16(self.addr), c_uint32(reg))
        checkerror(err)
        return

    def iscAddToPosition(self, value):
        err = mdll.iscAddToPosition(c_uint16(self.addr), c_double(value))
        checkerror(err)
        return

    def iscGetWarningReg(self):
        regs = (c_uint32 * 3)()
        err = mdll.iscGetWarningReg(c_uint16(self.addr), byref(regs))
        checkerror(err)
        return regs

    def iscGetParameterEx(self, param):
        res = c_double()

        class paramInfo(Structure):
            _fields_ = [("reciprical", c_uint16),
                        ("signextend", c_uint16),
                        ("paramtype", c_uint8),
                        ("unittype", c_uint8),
                        ("paramsize", c_int),
                        ("scalefrombase", c_double),
                        ("descID", c_uint16),
                        ("unitID", c_uint16)]

            def show(self):
                print "reciprical:    %s" % (self.reciprical)
                print "signextend:    %s" % (self.signextend)
                print "paramtype:     %s" % (self.paramtype)
                print "unittype:      %s" % (self.unittype)
                print "paramsize:     %s" % (self.paramsize)
                print "scalefrombase: %s" % (self.scalefrombase)
                print "descID:        %s" % (self.descID)
                print "unitID:        %s" % (self.unitID)

                return

        pi = paramInfo()

        p = c_uint32(param)
        err = mdll.iscGetParameterEx(c_uint16(self.addr), p, byref(res), byref(pi))
        checkerror(err)
        return (res.value, pi)

    def wait(self, polltime=.1):
        """ Wait for a move to complete
        :param polltime: Polling time
        :return:
        """
        while 1:
            self.iscGetStatusRTReg()
            if self.iscGetStatusRTReg()['Move Done'] == True:
                return
            else:
                time.sleep(polltime)
        return

    def getposition(self):
        return long(self.iscGetParameter(ISC_P_POSN_MEAS))


class MeridianAxis(MeridianNode):
    def __init__(self, master, addr):
        super(MeridianAxis, self).__init__(master, addr)
        self.limit_pos = None
        self.limit_neg = None
        return

    def safespeed(self):
        self.iscSetParameter(ISC_P_ACC_LIM, 50000)
        self.iscSetParameter(ISC_P_VEL_LIM, 20000)
        return

    def hardstop_on(self):
        self.iscSetParameter(ISC_P_DRV_HARDSTOP_ENTRY_SPD, 10000)
        self.iscSetParameter(ISC_P_DRV_HARDSTOP_ENTRY_TRQ, 14)
        self.iscSetParameter(ISC_P_DRV_HARDSTOP_FLDBK_TRQ_TC, 100)
        appreg = self.iscGetAppConfigReg()
        appreg['Enable HardStop Foldback'] = True
        self.iscSetAppConfigReg(appreg)
        return

    def hardstop_off(self):
        appreg = self.iscGetAppConfigReg()
        appreg['Enable HardStop Foldback'] = False
        self.iscSetAppConfigReg(appreg)
        return

    def findlimits(self, timeout=60):
        self.hardstop_on()
        self.safespeed()

        # find pos limit
        self.iscForkVelMove(5000)
        t1 = time.time()
        while 1:
            if t1 - time.time() > timeout:
                self.disable()
                raise Exception("Positive limit hard stop home timeout")
            reg = self.iscGetStatusRTReg()
            if reg['Hard Stopped'] == True:
                break
            else:
                time.sleep(.25)

        self.iscForkVelMove(0)
        self.limit_pos = self.getposition()

        # find neg limit
        self.iscForkVelMove(-5000)
        t1 = time.time()
        while 1:
            if t1 - time.time() > timeout:
                self.disable()
                raise Exception("Negative limit hard stop home timeout")
            reg = self.iscGetStatusRTReg()
            if reg['Hard Stopped'] == True:
                break
            else:
                time.sleep(.25)

        self.iscForkVelMove(0)
        self.limit_neg = self.getposition()

        # move over to be out of safe limit
        self.iscForkMoveEx(20000, MG_MOVE_STYLE_NORM)
        self.hardstop_off()
        return


class MeridianServo(MeridianNode):
    def __init__(self, master, addr):
        super(MeridianServo, self).__init__(master, addr)
        self.indexpos = None
        return

    def safespeed(self):
        self.iscSetParameter(ISC_P_ACC_LIM, 120000)
        self.iscSetParameter(ISC_P_VEL_LIM, 20000)
        return

    def getindex(self):
        """ Get the current index pulse location
        :return: Current index pulse location
        """
        self.indexpos = self.iscGetParameterEx(ISC_P_POSN_CAP_INDEX)
        return self.indexpos

    def home(self):
        self.safespeed()
        self.iscForkMoveEx(10000, MG_MOVE_STYLE_NORM)
        return self.getindex()


class MeridianStepper(MeridianNode):
    def __init__(self, master, addr):
        super(MeridianStepper, self).__init__(master, addr)
        return

    def safespeed(self):
        self.iscSetParameter(ISC_P_ACC_LIM, 100000)
        self.iscSetParameter(ISC_P_DEC_LIM, 100000)
        self.iscSetParameter(ISC_P_VEL_LIM, 1000)
        return

    # XXX enumify limit switch modes

    def limit_on(self):
        appreg = self.iscGetAppConfigReg()
        appreg['Limit Switch Mode'] = 1
        self.iscSetAppConfigReg(appreg)
        return

    def limit_off(self):
        appreg = self.iscGetAppConfigReg()
        appreg['Limit Switch Mode'] = 0
        self.iscSetAppConfigReg(appreg)
        return

    def home(self):
        # check if limit is on, if so move down a fixed number of steps
        limits = self.iscGetStatusRTReg()
        if limits['GPI-2/+Limit'] or limits['GPI-2/+Limit']:
            self.limit_off()
            self.iscForkMoveEx(-5000, MG_MOVE_STYLE_NORM)
            self.wait()

        self.limit_on()
        self.iscForkMoveEx(100000, MG_MOVE_STYLE_NORM)
        self.wait()
        self.iscAddToPosition(-self.getposition())
        return

        #
        #
        # def goto_index(addr, idx):
        #     getindex(self.addr)
        #     iscForkMoveEx(addr, homepos + (idx*1000), MG_MOVE_STYLE_NORM_ABS)
        #     waitfordone(self.addr)
        #     return



        return

        # def centrifuge(addr, vel=100000, acc=200000, runtime=60):
        #     iscSetParameter(addr, ISC_P_ACC_LIM, acc)
        #     iscSetParameter(addr, ISC_P_DEC_LIM, acc)
        #     iscSetParameter(addr, ISC_P_VEL_LIM, vel)
        #     iscForkVelMove(addr, vel, False)
        #     waitfordone(self.addr)
        #     time.sleep(runtime)
        #     iscForkVelMove(addr, 0, False)
        #     waitfordone(self.addr)
        #     safespeed(self.addr)
        #     return
        #
        # def testmove(nodes=(0,), cnt=1):
        #
        #     for node in nodes:
        #         netNodeStop(node, STOP_TYPE_CLR_ALL)
        #         netAlertClear(node)
        #         iscSetParameter(node, ISC_P_ACC_LIM, 100000)
        #         iscSetParameter(node, ISC_P_VEL_LIM, 20000)
        #
        #         # get output reg
        #         reg = iscGetUserOutputReg(node)
        #         # enable
        #         reg |= PLAOUT_ENABLE
        #         # write it back
        #         iscSetUserOutputReg(node, reg)
        #
        #     time.sleep(1)
        #
        #     # move forward
        #     for x in range(cnt):
        #         for node in nodes:
        #             iscForkMoveEx(node, 100000,  MG_MOVE_STYLE_NORM)
        #
        #         for node in nodes:
        #             waitfordone(node)
        #
        #         for node in nodes:
        #             iscForkMoveEx(node, -100000,  MG_MOVE_STYLE_NORM)
        #
        #         for node in nodes:
        #             waitfordone(node)
        #
        #     return
        #


if __name__ == "__main__":
    master = MeridianMaster(4)
    master.init()

    print "Init Servo"
    cf = MeridianServo(master, 4)
    cf.init()

    print "Init Stepper"
    st = MeridianStepper(master, 8)
    st.init()

    print "Init Axis"
    ax = MeridianAxis(master, 0)
    ax.init()

    IPython.embed()

    print "Shutting Down"
    master.mnShutdown()




    # print "Status regs:"
    # for node in nodes:
    #     print "Node %d:" % (node)
    #     status = iscGetStatusRTReg(node)
    #     print "State: (%.4x %.4x %.4x)" % (status[0], status[1], status[2])
    #     pprint.pprint(const.parse_all_regs(status))


    # enable(4)
    # time.sleep(1)
    #   # home(4)
    #   # goto_index(4,0)
    #
    #
    #   enable(8)
    #
    #   # print "Restarting nodes:"
    #   # for node in nodes:
    #   #     print "Node %d: ... " % (node),
    #   #     mnRestartNode(node)
    #   #     print "Done"
    #
    # #  testmove((1,))
    #   IPython.embed()
    #
    #   # while 1:
    #   #     print "ctrl %d" % (1)
    #   #     res = iscGetParameter(1, ISC_P_POSN_CAP_INDEX)
    #   #     print "Idx pos: %s" % (res)
    #   #     res = iscGetParameter(1, ISC_P_POSN_MEAS_MTR)
    #   #     print "Cur pos: %s" % (res)
    #   #     time.sleep(1)
    #
    #
    #
    #   print "shutdown"
    #   mnShutdown()
    #
    #
    #
    #
    #
