MN_ERR_BASE = 0x80040000
MN_ERR_CMD_ERR_BASE = 0x80040100
MN_ERR_NET_ERR_BASE = 0x80040120
MN_ERR_EXTEND_ERR_BASE = 0x80040140
MN_ERR_NETBREAK_ERR_BASE = 0x80040300
MN_ERR_NETBREAK_ERR_END = MN_ERR_NETBREAK_ERR_BASE + 0xff

errcodes = {
    0x0: ("MN_OK", "function succeeded"),
    0x80040001: ("MN_ERR_FAIL=MN_ERR_BASE+1", "function generically failed"),
    0x80040002: ("MN_ERR_TIMEOUT", "failed due to time-out"),
    0x80040003: ("MN_ERR_CHECKSUM", "failed due to checksum failure"),
    0x80040004: ("MN_ERR_DEV_ADDR", "device addressing problems"),
    0x80040005: ("MN_ERR_TOO_MANY", "there are too many nodes on the net"),
    0x80040006: ("MN_ERR_RESP_FMT", "response is garbled"),
    0x80040007: ("MN_ERR_RESP_ADDR", "response is from wrong address"),
    0x80040008: ("MN_ERR_OFFLINE", "the node is offline"),
    0x80040009: ("MN_ERR_PARAM_RANGE", "parameter is out of range"),
    0x8004000a: ("MN_ERR_MEM_LOW", "memory is low"),
    0x8004000b: ("MN_ERR_OS", "operating system error"),
    0x8004000c: ("MN_ERR_CLOSED", "attempting to use a closed device"),
    0x8004000d: ("MN_ERR_VALUE", "the value requested is invalid"),
    0x8004000e: ("MN_ERR_FRAME", "command frame error"),
    0x8004000f: ("MN_ERR_UNKN_DEVICE", "attempting to use unknown device"),
    0x80040010: ("MN_ERR_DEV_WAIT_TO", "time-out waiting for command access"),
    0x80040011: ("MN_ERR_PKT_ERR", "Packet length != buffer length err"),
    0x80040012: ("MN_ERR_BUF_OVERFLOW", "RX buffer overflow"),
    0x80040013: ("MN_ERR_RX_ACCESS", "RX buffer access/sync problem"),
    0x80040014: ("MN_ERR_NOT_IMPL", "feature not implemented"),
    0x80040015: ("MN_ERR_PORT_PROBLEM", "Serial port driver open failure"),
    0x80040016: ("MN_ERR_TX_BUSY", "TX Buffer full"),
    0x80040017: ("MN_ERR_IN_SERIAL_PORT", "In serial port mode"),
    0x80040018: ("MN_ERR_PARAM_NOT_INIT", "Parameter Database not initialized"),
    0x80040019: ("MN_ERR_TEST_INCOMPLETE", "Initialization tests incomplete due to old firmware"),
    0x8004001a: ("MN_ERR_IRQ_FAILED", "Interrupt interface appears broken"),
    0x8004001b: ("MN_ERR_CMD_OFFLINE", "Command attempt while net offline"),
    0x8004001c: ("MN_ERR_ADDR_LOCK", "Address is locked"),
    0x8004001d: ("MN_ERR_RESOURCE_BUSY", "A resource is busy", "request canceled"),
    0x8004001e: ("MN_ERR_ATTN_OVERRUN", "ATTN FIFO over-run"),
    0x8004001f: ("MN_ERR_NO_TEST_INIT_ERR", "Old firmware/initialization failure"),
    0x80040020: ("MN_ERR_P2P_MOVE_TIMEOUT", "Move segment time-out"),
    0x80040021: ("MN_ERR_P2P_DELAY_TIMEOUT", "Delay segment time-out"),
    0x80040022: ("MN_ERR_DEPRECATED", "Deprecated API element attempt"),
    0x80040023: ("MN_ERR_NET_ERRS_DETECT", "Network errors detected"),
    0x80040024: ("MN_ERR_NO_NODES_DETECTED", "No nodes are detected on both the diag and app net"),
    0x80040025: ("MN_ERR_DATAACQ_INVALID", "There is an invalid dataAcq point detected; Reasons: Dropped packet",
                 "data overflow"),
    0x80040026: ("MN_ERR_DATAACQ_EMPTY", "There is no data acq data point available"),
    0x80040027: ("MN_ERR_BADARG", "API function passed bad argument"),
    0x80040028: ("MN_ERR_WRONG_NODE_TYPE", "Interaction with wrong node type"),
    0x80040029: ("MN_ERR_BAUD_NOT_SUPPORTED", "Port does not support request rate"),
    0x8004002a: ("MN_ERR_SEND_FAILED", "Send failed"),
    0x8004002b: ("MN_ERR_SEND_LOCKED", "Could not acquire NC command interface "),
    0x8004002c: ("MN_ERR_SEND_UNLOCK", "Could not release NC command interface"),
    0x8004002d: ("MN_ERR_RESP_FAILED", "Response failed to transfer"),
    0x8004002e: ("MN_ERR_RESP_TIMEOUT", "Response not found in time"),
    0x8004002f: ("MN_ERR_CMD_TIMEOUT", "Command timeout"),
    0x80040030: ("MN_ERR_CANCELED", "Command canceled"),
    0x80040031: ("MN_ERR_THREAD_CREATE", "Thread create error"),
    0x80040032: ("MN_ERR_UNSOLICITED", "Unsolicted response detected"),
    0x80040033: ("MN_ERR_DEF_RESP_TO", "Deferred response time-out"),
    0x80040034: ("MN_ERR_ADDR_RANGE", "Response from out of range address"),
    0x80040035: ("MN_ERR_WRONG_SRC", "Response from wrong source"),
    0x80040036: ("MN_ERR_FLUSH_MANY", "Flush finding many characters"),
    0x80040037: ("MN_ERR_PRIO_FAILED", "Failed to set thread priority"),
    0x80040038: ("MN_ERR_NET_DIAG_FAILED", "Network diagnostic problems detected"),
    0x80040039: ("MN_ERR_RD_COMM_IRQ", "Could not start the read COMM IRQs"),
    0x8004003a: ("MN_ERR_NULL_RETURN", "Read returned NULL buffer"),
    0x8004003b: ("MN_ERR_RESET_FAILED", "Reset command failed"),
    0x8004003c: ("MN_ERR_LOG_CHANGED", "Error log changed during read"),
    0x8004003d: ("MN_ERR_DATAACQ_OVERRUN", "Data acquisition over-run"),
    0x8004003e: ("MN_ERR_HOST_APP_OVERRUN", "Host's application port over-run"),
    0x8004003f: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040040: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040041: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040042: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040043: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040044: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040045: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040046: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040047: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040048: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040049: ("MN_ERR_HOST_DIAG_OVERRUN1", "Host's diagnostic port over-run"),
    0x80040100: ("MN_ERR_CMD_INTERNAL", "Generic internal error"),
    0x80040101: ("MN_ERR_CMD_CMD_UNK", "Command unknown on this node"),
    0x80040102: ("MN_ERR_CMD_ARGS", "Illegal or missing command args"),
    0x80040103: ("MN_ERR_CMD_WR_FAIL", "Attempt to write read-only info"),
    0x80040104: ("MN_ERR_CMD_EEHW", "Non-Volatile memory failure"),
    0x80040105: ("MN_ERR_CMD_ACCESS_LVL", "Access level violation"),
    0x80040106: ("MN_ERR_CMD_MV_FULL", "Move Buffers full"),
    0x80040107: ("MN_ERR_CMD_MV_SPEC", "Move specification error"),
    0x80040108: ("MN_ERR_CMD_MV_ESTOPPED", "Motion attempt in E-Stopped state"),
    0x80040109: ("MN_ERR_CMD_MV_RANGE", "Motion attempt is out of range"),
    0x8004010a: ("MN_ERR_CMD_MV_SHUTDOWN", "Motion attempt / drive in shutdown"),
    0x8004010b: ("MN_ERR_CMD_IEX_ERROR", "IEX interaction while stopped"),
    0x8004010c: ("MN_ERR_CMD_MV_BLOCKED", "Motion blocked / non-disabling shutdown present"),
    0x8004010d: ("MN_ERR_CMD_MV_RES1", "Reserved for move errors"),
    0x8004010e: ("MN_ERR_CMD_MV_RES1", "Reserved for move errors"),
    0x8004010f: ("MN_ERR_CMD_MV_RES1", "Reserved for move errors"),
    0x80040110: ("MN_ERR_NODE_IN_MOTION", "Drive is in motion"),
    0x80040120: ("MN_ERR_NET_FRAG", "Packet fragment detected"),
    0x80040121: ("MN_ERR_NET_CHKSUM", "Bad checksum detected"),
    0x80040122: ("MN_ERR_NET_STRAY", "Stray Data Found"),
    0x80040123: ("MN_ERR_NET_PORT_OVERRUN", "Serial Port overran receive"),
    0x80040300: ("MN_ERR_BRK_OTHER_00_01", "Net Break OTHER: node 00-01	"),
    0x80040301: ("MN_ERR_BRK_OTHER_01_02", "Net Break OTHER: node 01-02 "),
    0x80040302: ("MN_ERR_BRK_OTHER_02_03", "Net Break OTHER: node 02-03 "),
    0x80040303: ("MN_ERR_BRK_OTHER_03_04", "Net Break OTHER: node 03-04 "),
    0x80040304: ("MN_ERR_BRK_OTHER_04_05", "Net Break OTHER: node 04-05 "),
    0x80040305: ("MN_ERR_BRK_OTHER_05_06", "Net Break OTHER: node 05-06 "),
    0x80040306: ("MN_ERR_BRK_OTHER_06_07", "Net Break OTHER: node 06-07 "),
    0x80040307: ("MN_ERR_BRK_OTHER_07_08", "Net Break OTHER: node 07-08 "),
    0x80040308: ("MN_ERR_BRK_OTHER_08_09", "Net Break OTHER: node 08-09 "),
    0x80040309: ("MN_ERR_BRK_OTHER_09_10", "Net Break OTHER: node 09-10 "),
    0x8004030a: ("MN_ERR_BRK_OTHER_10_11", "Net Break OTHER: node 10-11 "),
    0x8004030b: ("MN_ERR_BRK_OTHER_11_12", "Net Break OTHER: node 11-12 "),
    0x8004030c: ("MN_ERR_BRK_OTHER_12_13", "Net Break OTHER: node 12-13 "),
    0x8004030d: ("MN_ERR_BRK_OTHER_13_14", "Net Break OTHER: node 13-14 "),
    0x8004030e: ("MN_ERR_BRK_OTHER_14_15", "Net Break OTHER: node 14-15 "),
    0x8004030f: ("MN_ERR_BRK_OTHER_15_HOST", "Net Break OTHER: node 15-host"),
    0x80040310: ("MN_ERR_BRK_APP_00_01", "Net Break APP: node 00-01"),
    0x80040311: ("MN_ERR_BRK_APP_01_02", "Net Break APP: node 01-02 "),
    0x80040312: ("MN_ERR_BRK_APP_02_03", "Net Break APP: node 02-03 "),
    0x80040313: ("MN_ERR_BRK_APP_03_04", "Net Break APP: node 03-04 "),
    0x80040314: ("MN_ERR_BRK_APP_04_05", "Net Break APP: node 04-05 "),
    0x80040315: ("MN_ERR_BRK_APP_05_06", "Net Break APP: node 05-06 "),
    0x80040316: ("MN_ERR_BRK_APP_06_07", "Net Break APP: node 06-07 "),
    0x80040317: ("MN_ERR_BRK_APP_07_08", "Net Break APP: node 07-08 "),
    0x80040318: ("MN_ERR_BRK_APP_08_09", "Net Break APP: node 08-09 "),
    0x80040319: ("MN_ERR_BRK_APP_09_10", "Net Break APP: node 09-10 "),
    0x8004031a: ("MN_ERR_BRK_APP_10_11", "Net Break APP: node 10-11 "),
    0x8004031b: ("MN_ERR_BRK_APP_11_12", "Net Break APP: node 11-12 "),
    0x8004031c: ("MN_ERR_BRK_APP_12_13", "Net Break APP: node 12-13 "),
    0x8004031d: ("MN_ERR_BRK_APP_13_14", "Net Break APP: node 13-14 "),
    0x8004031e: ("MN_ERR_BRK_APP_14_15", "Net Break APP: node 14-15 "),
    0x8004031f: ("MN_ERR_BRK_APP_15_TO_HOST", "Net Break APP: node 15-host"),

    0x80040700: ("MN_ERR_PORT_FAILED_PORTS_0", "Problems detected at port index 0"),
    0x80040701: ("MN_ERR_PORT_FAILED_PORTS_1", "Problems detected at port index 1"),
    0x80040702: ("MN_ERR_PORT_FAILED_PORTS_2", "Problems detected at port index 2"),
    0x80040703: ("MN_ERR_PORT_FAILED_PORTS_3", "Problems detected at port index 3"),
    0x80040704: ("MN_ERR_PORT_FAILED_PORTS_4", "Problems detected at port index 4"),
    0x80040705: ("MN_ERR_PORT_FAILED_PORTS_5", "Problems detected at port index 5"),
    0x80040706: ("MN_ERR_PORT_FAILED_PORTS_6", "Problems detected at port index 6"),
    0x80040707: ("MN_ERR_PORT_FAILED_PORTS_7", "Problems detected at port index 7")

}


def lookup(code):
    if errcodes.has_key(code) == False:
        return ("%.8x" % code, "UNKNOWN")
    return errcodes[code]

    # /** 0x80040320: Network Break detected on the diagnostic channel between
    #     node \e 0 and the node \e 1.
    # **/
    # MN_ERR_BRK_DIAG_00_01=MN_ERR_NETBREAK_ERR_BASE+0x20,
    # /** 0x80040321: Network Break detected on the diagnostic channel between
    #     node \e 1 and the node \e 2.
    # **/
    # MN_ERR_BRK_DIAG_01_02,		// 0x80040321: Net Break DIAG: node 01-02
    # /** 0x80040322: Network Break detected on the diagnostic channel between
    #     node \e 2 and the node \e 3.
    # **/
    # MN_ERR_BRK_DIAG_02_03,		// 0x80040322: Net Break DIAG: node 02-03
    # /** 0x80040323: Network Break detected on the diagnostic channel between
    #     node \e 3 and the node \e 4.
    # **/
    # MN_ERR_BRK_DIAG_03_04,		// 0x80040323: Net Break DIAG: node 03-04
    # /** 0x80040324: Network Break detected on the diagnostic channel between
    #     node \e 4 and the node \e 5.
    # **/
    # MN_ERR_BRK_DIAG_04_05,		// 0x80040324: Net Break DIAG: node 04-05
    # /** 0x80040325: Network Break detected on the diagnostic channel between
    #     node \e 5 and the node \e 6.
    # **/
    # MN_ERR_BRK_DIAG_05_06,		// 0x80040325: Net Break DIAG: node 05-06
    # /** 0x80040326: Network Break detected on the diagnostic channel between
    #     node \e 6 and the node \e 7.
    # **/
    # MN_ERR_BRK_DIAG_06_07,		// 0x80040326: Net Break DIAG: node 06-07
    # /** 0x80040327: Network Break detected on the diagnostic channel between
    #     node \e 7 and the node \e 8.
    # **/
    # MN_ERR_BRK_DIAG_07_08,		// 0x80040327: Net Break DIAG: node 07-08
    # /** 0x80040328: Network Break detected on the diagnostic channel between
    #     node \e 8 and the node \e 9.
    # **/
    # MN_ERR_BRK_DIAG_08_09,		// 0x80040328: Net Break DIAG: node 08-09
    # /** 0x80040329: Network Break detected on the diagnostic channel between
    #     node \e 9 and the node \e 10.
    # **/
    # MN_ERR_BRK_DIAG_09_10,		// 0x80040329: Net Break DIAG: node 09-10
    # /** 0x8004032a: Network Break detected on the diagnostic channel between
    #     node \e 10 and the node \e 11.
    # **/
    # MN_ERR_BRK_DIAG_10_11,		// 0x8004032a: Net Break DIAG: node 10-11
    # /** 0x8004032b: Network Break detected on the diagnostic channel between
    #     node \e 11 and the node \e 12.
    # **/
    # MN_ERR_BRK_DIAG_11_12,		// 0x8004032b: Net Break DIAG: node 11-12
    # /** 0x8004032c: Network Break detected on the diagnostic channel between
    #     node \e 12 and the node \e 13.
    # **/
    # MN_ERR_BRK_DIAG_12_13,		// 0x8004032c: Net Break DIAG: node 12-13
    # /** 0x8004032d: Network Break detected on the diagnostic channel between
    #     node \e 13 and the node \e 14.
    # **/
    # MN_ERR_BRK_DIAG_13_14,		// 0x8004032d: Net Break DIAG: node 13-14
    # /** 0x8004032e: Network Break detected on the diagnostic channel between
    #     node \e 14 and the node \e 15.
    # **/
    # MN_ERR_BRK_DIAG_14_15,		// 0x8004032e: Net Break DIAG: node 14-15
    # /** 0x8004032f: Network Break detected on the diagnostic channel between
    #     node \e 15 and the host.
    # **/
    # MN_ERR_BRK_DIAG_15_TO_HOST,	// 0x8004032f: Net Break DIAG: node 15-host
    #
    #  Network Break detected on the application channel between node \e xx
    #  and the host.
    # MN_ERR_BRK_APP_00_HOST=MN_ERR_NETBREAK_ERR_BASE+0x30,
    # MN_ERR_BRK_APP_01_HOST,		// 0x330-0x33f Between node xx and host
    # MN_ERR_BRK_APP_02_HOST,
    # MN_ERR_BRK_APP_03_HOST,
    # MN_ERR_BRK_APP_04_HOST,
    # MN_ERR_BRK_APP_05_HOST,
    # MN_ERR_BRK_APP_06_HOST,
    # MN_ERR_BRK_APP_07_HOST,
    # MN_ERR_BRK_APP_08_HOST,
    # MN_ERR_BRK_APP_09_HOST,
    # MN_ERR_BRK_APP_10_HOST,
    # MN_ERR_BRK_APP_11_HOST,
    # MN_ERR_BRK_APP_12_HOST,
    # MN_ERR_BRK_APP_13_HOST,
    # MN_ERR_BRK_APP_14_HOST,
    # MN_ERR_BRK_APP_15_HOST,
    #
    # /**
    # 0x80040340 Network Break detected on the diagnostic channel between node
    # \e 0 and the host.
    # **/
    # MN_ERR_BRK_DIAG_00_HOST=MN_ERR_NETBREAK_ERR_BASE+0x40,
    # /**
    # 0x80040341 Network Break detected on the diagnostic channel between node
    # \e 1 and the host.
    # **/
    # MN_ERR_BRK_DIAG_01_HOST,
    # /**
    # 0x80040342 Network Break detected on the diagnostic channel between node
    # \e 2 and the host.
    # **/
    # MN_ERR_BRK_DIAG_02_HOST,
    # /**
    # 0x80040343 Network Break detected on the diagnostic channel between node
    # \e 3 and the host.
    # **/
    # MN_ERR_BRK_DIAG_03_HOST,
    # /**
    # 0x80040344 Network Break detected on the diagnostic channel between node
    # \e 4 and the host.
    # **/
    # MN_ERR_BRK_DIAG_04_HOST,
    # /**
    # 0x80040345 Network Break detected on the diagnostic channel between node
    # \e 5 and the host.
    # **/
    # MN_ERR_BRK_DIAG_05_HOST,
    # /**
    # 0x80040346 Network Break detected on the diagnostic channel between node
    # \e 6 and the host.
    # **/
    # MN_ERR_BRK_DIAG_06_HOST,
    # /**
    # 0x80040347 Network Break detected on the diagnostic channel between node
    # \e 7 and the host.
    # **/
    # MN_ERR_BRK_DIAG_07_HOST,
    # /**
    # 0x80040348 Network Break detected on the diagnostic channel between node
    # \e 8 and the host.
    # **/
    # MN_ERR_BRK_DIAG_08_HOST,
    # /**
    # 0x80040349 Network Break detected on the diagnostic channel between node
    # \e 9 and the host.
    # **/
    # MN_ERR_BRK_DIAG_09_HOST,
    # /**
    # 0x8004034a Network Break detected on the diagnostic channel between node
    # \e 10 and the host.
    # **/
    # MN_ERR_BRK_DIAG_10_HOST,
    # /**
    # 0x80040341 Network Break detected on the diagnostic channel between node
    # \e 11 and the host.
    # **/
    # MN_ERR_BRK_DIAG_11_HOST,
    # /**
    # 0x8004034c Network Break detected on the diagnostic channel between node
    # \e 12 and the host.
    # **/
    # MN_ERR_BRK_DIAG_12_HOST,
    # /**
    # 0x8004034d Network Break detected on the diagnostic channel between node
    # \e 13 and the host.
    # **/
    # MN_ERR_BRK_DIAG_13_HOST,
    # /**
    # 0x8004034e Network Break detected on the diagnostic channel between node
    # \e 14 and the host.
    # **/
    # MN_ERR_BRK_DIAG_14_HOST,
    # /**
    # 0x8004034f Network Break detected on the diagnostic channel between node
    # \e 15 and the host.
    # **/
    # MN_ERR_BRK_DIAG_15_HOST,
    #
    #  Network Break detected between node \e xx and the host.
    # MN_ERR_BRK_00_HOST=MN_ERR_NETBREAK_ERR_BASE+0x50,
    # MN_ERR_BRK_01_HOST,			// 0x340-0x34f Between node xx and host
    # MN_ERR_BRK_02_HOST,
    # MN_ERR_BRK_03_HOST,
    # MN_ERR_BRK_04_HOST,
    # MN_ERR_BRK_05_HOST,
    # MN_ERR_BRK_06_HOST,
    # MN_ERR_BRK_07_HOST,
    # MN_ERR_BRK_08_HOST,
    # MN_ERR_BRK_09_HOST,
    # MN_ERR_BRK_10_HOST,
    # MN_ERR_BRK_11_HOST,
    # MN_ERR_BRK_12_HOST,
    # MN_ERR_BRK_13_HOST,
    # MN_ERR_BRK_14_HOST,
    # MN_ERR_BRK_15_HOST,
    #
    # // Detected offline nodes are reported with this group. These are
    # // usually caused by a node restarting via power or firmware error.
    # MN_ERR_OFFLINE_00=MN_ERR_NETBREAK_ERR_BASE+0xa0,
    # 						    // 0x800403a0: Node 0  detected offline
    # MN_ERR_OFFLINE_01,	    	// 0x800403a1: Node 1  detected offline
    # MN_ERR_OFFLINE_02,	    	// 0x800403a2: Node 2  detected offline
    # MN_ERR_OFFLINE_03,	    	// 0x800403a3: Node 3  detected offline
    # MN_ERR_OFFLINE_04,	    	// 0x800403a4: Node 4  detected offline
    # MN_ERR_OFFLINE_05,	    	// 0x800403a5: Node 5  detected offline
    # MN_ERR_OFFLINE_06,	    	// 0x800403a6: Node 6  detected offline
    # MN_ERR_OFFLINE_07,	    	// 0x800403a7: Node 7  detected offline
    # MN_ERR_OFFLINE_08,	    	// 0x800403a8: Node 8  detected offline
    # MN_ERR_OFFLINE_09,	    	// 0x800403a9: Node 9  detected offline
    # MN_ERR_OFFLINE_10,	    	// 0x800403aa: Node 10 detected offline
    # MN_ERR_OFFLINE_11,	    	// 0x800403ab: Node 11 detected offline
    # MN_ERR_OFFLINE_12,	    	// 0x800403ac: Node 12 detected offline
    # MN_ERR_OFFLINE_13,	    	// 0x800403ad: Node 13 detected offline
    # MN_ERR_OFFLINE_14,	    	// 0x800403ae: Node 14 detected offline
    # MN_ERR_OFFLINE_15,	    	// 0x800403af: Node 15 detected offline
    #
    # // Special Diagnostic Errors
    # MN_ERR_BRK_DIAG_LOC_UNKNOWN=MN_ERR_NETBREAK_ERR_BASE+0xFC,
    # 							< 0x800403fc: Net Break Diag: unknown location
    # MN_ERR_BRK_APP_LOC_UNKNOWN,	< 0x800403fd: Net Break App: unknown location
    #    MN_ERR_BRK_LOC_UNKNOWN,    	< 0x800403fe: Net Break unknown
    # MN_ERR_NO_NET_CONNECTIVITY,	< 0x800403ff: Cannot detect net connectivity
    #
    # // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # // Initialization bit oriented error codes
    # // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #
    # /**
    # 	\brief Initialization Error(s)
    #
    # 	The following codes describe the failing port initialization issue.
    # 	The 8 LSBs represent the problem ports with LSB = port 0.
    #
    # 	0x80040600-0x80040607
    # **/
    # MN_ERR_INIT_FAILED_BASE=0x80040600,
    # /**
    # 0x80040601: Port opened OK but no nodes were found attached to the link.
    # Problems detected at port index: 0.
    # **/
    # MN_ERR_INIT_FAILED_PORTS_0,			// 0x80040601 Port 0 problem
    # /**
    # 0x80040602: Port opened OK but no nodes were found attached to the link.
    # Problems detected at port index: 1.
    # **/
    # MN_ERR_INIT_FAILED_PORTS_1,			// 0x80040602: Port 1 problem
    # /**
    # 0x80040603: Port opened OK but no nodes were found attached to the link.
    # Problems detected at port index: 0 & 1.
    # **/
    # MN_ERR_INIT_FAILED_PORTS_1_0,		// 0x80040603: Port 0&1 problem
    # /**
    # 0x80040604: Port opened OK but no nodes were found attached to the link.
    # Problems detected at port index: 2.
    # **/
    # MN_ERR_INIT_FAILED_PORTS_2,			// 0x80040604: Port 2 problem
    # /**
    # 0x80040605: Port opened OK but no nodes were found attached to the link.
    # Problems detected at port index: 2 & 0.
    # **/
    # MN_ERR_INIT_FAILED_PORTS_2_0,		// 0x80040605: Port 2&0 problem
    # /**
    # 0x80040606: Port opened OK but no nodes were found attached to the link.
    # Problems detected at port index: 2 & 1.
    # **/
    # MN_ERR_INIT_FAILED_PORTS_2_1,		// 0x80040606: Port 2&1 problem
    # /**
    # 0x80040607: Port opened OK but no nodes were found attached to the link.
    # Problems detected at port index: 2 & 1 & 0.
    # **/
    # MN_ERR_INIT_FAILED_PORTS_2_1_0,		// 0x80040607: Port 2&1&0 problem
    #
    # /**
    # 	\brief Port Open Error(s)
    #
    # 	The following codes describe the failing port failed to open issue.
    # 	The 8 LSBs represent the problem ports with LSB = port 0.
    #
    # 	0x80040700-0x80040707
    # **/
    # MN_ERR_PORT_FAILED_BASE = 0x80040700,
    # /**
    # 0x80040701: Port failed to open. Make sure you specify a working port or check
    # that the USB cable is properly inserted.
    # Problems detected at port index: 0.
    # **/
    # MN_ERR_PORT_FAILED_PORTS_0,			// 0x80040701: Port 0 problem
    # /**
    # 0x80040702: Port failed to open. Make sure you specify a working port or check
    # that the USB cable is properly inserted.
    # Problems detected at port index: 1.
    # **/
    # MN_ERR_PORT_FAILED_PORTS_1,			// 0x80040702: Port 1 problem
    # /**
    # 0x80040703: Port failed to open. Make sure you specify a working port or check
    # that the USB cable is properly inserted.
    # Problems detected at port index: 0 & 1.
    # **/
    # MN_ERR_PORT_FAILED_PORTS_1_0,		// 0x80040703: Port 0&1 problem
    # /**
    # 0x80040704: Port failed to open. Make sure you specify a working port or check
    # that the USB cable is properly inserted.
    # Problems detected at port index: 2.
    # **/
    # MN_ERR_PORT_FAILED_PORTS_2,			// 0x80040704: Port 2 problem
    # /**
    # 0x80040705: Port failed to open. Make sure you specify a working port or check
    # that the USB cable is properly inserted.
    # Problems detected at port index: 2 & 0.
    # **/
    # MN_ERR_PORT_FAILED_PORTS_2_0,		// 0x80040705: Port 2&0 problem
    # /**
    # 0x80040706: Port failed to open. Make sure you specify a working port or check
    # that the USB cable is properly inserted.
    # Problems detected at port index: 2 & 1.
    # **/
    # MN_ERR_PORT_FAILED_PORTS_2_1,		// 0x80040706: Port 2&1 problem
    # /**
    # 0x80040707: Port failed to open. Make sure you specify a working port or check
    # that the USB cable is properly inserted.
    # Problems detected at port index: 2 & 1 & 0.
    # **/
    # MN_ERR_PORT_FAILED_PORTS_2_1_0,		// 0x80040707: Port 2&1&0 problem
    # /**
    # 	\brief Initialization Error	Due to Unsupported Port Rate
    #
    # 	The following codes describe the failing port initialization issue.
    # 	The 8 LSBs represent the problem ports with LSB = port 0
    #
    # 	0x80040800-0x80040807
    # **/
    # MN_ERR_BAUD_FAILED_BASE = 0x80040800,
    # /**
    # 0x80040801: Port opened OK but doesn't support the requested baud rate.
    # Problems detected at port index: 0.
    # **/
    # MN_ERR_BAUD_FAILED_PORTS_0,			// 0x80040801: Port 0 problem
    # /**
    # 0x80040802: Port opened OK but doesn't support the requested baud rate.
    # Problems detected at port index: 1.
    # **/
    # MN_ERR_BAUD_FAILED_PORTS_1,			// 0x80040802: Port 1 problem
    # /**
    # 0x80040803: Port opened OK but doesn't support the requested baud rate.
    # Problems detected at port index: 0 & 1.
    # **/
    # MN_ERR_BAUD_FAILED_PORTS_1_0,		// 0x80040803: Port 0&1 problem
    # /**
    # 0x80040804: Port opened OK but doesn't support the requested baud rate.
    # Problems detected at port index: 2.
    # **/
    # MN_ERR_BAUD_FAILED_PORTS_2,			// 0x80040804: Port 2 problem
    # /**
    # 0x80040805: Port opened OK but doesn't support the requested baud rate.
    # Problems detected at port index: 2 & 0.
    # **/
    # MN_ERR_BAUD_FAILED_PORTS_2_0,		// 0x80040805: Port 2&0 problem
    # /**
    # 0x80040806: Port opened OK but doesn't support the requested baud rate.
    # Problems detected at port index: 2 & 1.
    # **/
    # MN_ERR_BAUD_FAILED_PORTS_2_1,		// 0x80040806: Port 2&1 problem
    # /**
    # 0x80040807: Port opened OK but doesn't support the requested baud rate.
    # Problems detected at port index: 2 & 1 & 0.
    # **/
    # MN_ERR_BAUD_FAILED_PORTS_2_1_0		// 0x80040807: Port 2&1&0 problem
    #
    # """
