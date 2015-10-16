import mnBitstruct as bs


# interpreter complains that BitStruct is not defined if "class AppConfigReg(BitStruct):"
class AppConfigReg(bs.BitStruct):
    def populate(self):
        self.addField('Trigger Group', (1, 0))
        self.addField('GPI-O Node stop', 2)
        self.addField('A After Start', 3)
        self.addField('B Before Start', 4)
        self.addField('At Position', 5)
        self.addField('Enable HardStop Foldback', 8)
        self.addField('Enable Move Done Foldback', 9)
        self.addField('Limit Switch Mode', (12, 13, 14))
        return


class StatusReg(bs.BitStruct):
    def populate(self):
        self.addField('Warning', 0)
        self.addField('User Alert', 1)
        self.addField('Not Ready', 2)
        self.addField('Move Buffer Available', 3)
        self.addField('IEX Risen Item(s)', 4)
        self.addField('IEX Fallen Item(s)', 5)
        self.addField('IEX Status Change', 6)
        self.addField('In Pos Limit', 8)
        self.addField('In Neg Limit', 9)
        self.addField('Motion Blocked', 10)
        self.addField('Node Stopped', 16)
        self.addField('Move Done', 17)
        self.addField('Out of Range', 18)
        self.addField('B from End', 19)
        self.addField('PLA Out/Feedback-0', 20)
        self.addField('PLA Out/Feedback-1', 21)
        self.addField('GPI-0', 22)
        self.addField('GPI-1', 23)
        self.addField('GPI-2/+Limit', 24)
        self.addField('GPI-3/-Limit', 25)
        self.addField('At Position', 26)
        self.addField('IEX Masked', 27)
        self.addField('A From Start', 28)
        self.addField('Command Negative', 29)
        self.addField('Disabled', 30)
        self.addField('Timer Expired', 31)
        self.addField('In Motion', (33, 32))
        self.addField('In Controlled Stop', 35)
        self.addField('Fan On', 36)
        self.addField('Vector Search', 37)
        self.addField('Move Cmd Done', 38)
        self.addField('Hard Stopped', 39)
        self.addField('Shutdown State', (40, 41))
        self.addField('Hardware Failed', 42)
        self.addField('Awaiting Trigger', 43)
        self.addField('Motor Index Detected', 45)
        self.addField('Load Index Detected', 46)


class UserOutputReg(bs.BitStruct):
    def populate(self):
        self.addField('GPO-0', 0)
        self.addField('GPO-1', 1)
        self.addField('Enable', 2)
        self.addField('Capture', 3)
        self.addField('Trigger', 4)
        self.addField('Node Stop', 5)
        self.addField('Reset Timer', 6)
        self.addField('PLA/Attn Out-0', 7)
        self.addField('PLA/Attn Out-1', 8)
        self.addField('Positive Trq/Frc Foldback', 12)
        self.addField('Negative Trq/Frc Foldback', 13)


# nodetypes = {
# 0:  ("NODEID_UNK", "Unknown"),
# 1:  ("NODEID_NC", "Network Controller"),
# 2:  ("NODEID_TG", "Trajectory Generator"),
# 3:  ("NODEID_SC", "ControlPoint Integrated Servo Controller"),
# 4:  ("NODEID_IO", "IO Cluster"),
# 5:  ("NODEID_DA", "SSt and Eclipse Drives"),
# 6:  ("NODEID_NS", "eFoundation NC"),
# 7:  ("NODEID_PS", "Amazon Power Supply"),
# 8:  ("NODEID_MD", "Meridian Integrated Servo Controller"),
# 9:  ("NODEID_AS", "Meridian ASUM (Comm. Node)"),
# 10: ("NODEID_AA", " Meridian ASUM (App. Processor)")
# }
#
# r_nodetypes = {}
# for (id, data) in nodetypes.iteritems():
#     r_nodetypes[data[0]] = id

NODEID_UNK = 0  # "Unknown"),
NODEID_NC = 1  # "Network Controller"),
NODEID_TG = 2  # "Trajectory Generator"),
NODEID_SC = 3  # "ControlPoint Integrated Servo Controller"),
NODEID_IO = 4  # "IO Cluster"),
NODEID_DA = 5  # "SSt and Eclipse Drives"),
NODEID_NS = 6  # "eFoundation NC"),
NODEID_PS = 7  # "Amazon Power Supply"),
NODEID_MD = 8  # "Meridian Integrated Servo Controller"),
NODEID_AS = 9  # "Meridian ASUM (Comm. Node)"),
NODEID_AA = 10  # "Meridian ASUM (App. Processor)")

low_attn_regs = {
    0: 'Warning',
    1: 'User Alert',
    2: 'Not Ready',
    3: 'Move Buffer Available',
    4: 'IEX Risen Item(s)',
    5: 'IEX Fallen Item(s)',
    6: 'IEX Status Change',
    7: 'Zero',
    8: 'In Pos. Limit',
    9: 'In Neg. Limit',
    10: 'Motion Blocked',
    11: 'Zero',
    12: 'Zero',
    13: 'Zero',
    14: 'Zero',
    15: 'Zero'
}

in_reg = {
    0: 'Node Stopped',
    1: 'Move Done',
    2: 'Out of Range',
    3: 'B from End',
    4: 'PLA Out/Feedback-0',
    5: 'PLA Out/Feedback-1',
    6: 'GPI-0',
    7: 'GPI-1',
    8: 'GPI-2/+Limit',
    9: 'GPI-3/-Limit',
    10: 'At Position',
    11: 'IEX Masked',
    12: 'A From Start',
    13: 'Command Negative',
    14: 'Disabled',
    15: 'Timer Expired'
}

non_attn_regs = {
    0: 'In Motion 1',
    1: 'In Motion 2',
    2: 'Zero',
    3: 'In Controlled Stop',
    4: 'Fan On',
    5: 'Vector Search',
    6: 'Move Cmd Done',
    7: 'Hard Stopped',
    8: 'Shutdown State 1',
    9: 'Shutdown State 2',
    10: 'Hardware Failed',
    11: 'Awaiting Trigger',
    12: 'Zero',
    13: 'Motor Index Detected',
    14: 'Load Index Detected',
    15: 'Zero'
}


def parse_regs(val, reg):
    res = {}
    for bit, name in reg.iteritems():
        if val & (1 << bit) > 0:
            res[name] = True
        else:
            res[name] = False
    return res


def parse_all_regs(status):
    a = parse_regs(status[0], low_attn_regs)
    b = parse_regs(status[1], in_reg)
    c = parse_regs(status[2], non_attn_regs)
    return dict(a.items() + b.items() + c.items())


iscParams = {
    0: ("ISC_P_NODEID", "Device ID"),
    1: ("ISC_P_FW_VERSION", "FW version"),
    2: ("ISC_P_HW_VERSION", "HW version"),
    3: ("ISC_P_RESELLER_ID", "Reseller ID"),
    4: ("ISC_P_SER_NUM", "Unit serial number"),
    5: ("ISC_P_OPTION_REG", "Unit options"),
    6: ("ISC_P_ROM_SUM_ACK", "Firmware update ack"),
    7: ("ISC_P_ROM_SUM", "Firmware checksum"),
    8: ("ISC_P_SAMPLE_PERIOD", "Sample period (nsec)"),
    9: ("ISC_P_ALERT_REG", "Shutdown register"),
    10: ("ISC_P_STOP_TYPE", "Node Stop Type"),
    11: ("ISC_P_WATCHDOG_TIME", "Watchdog time constant"),
    12: ("ISC_P_NET_STAT", "Network Status"),
    13: ("ISC_P_STATUS_ACCUM_REG", "Status accum register"),
    14: ("ISC_P_STATUS_ATTN_RISE_REG", "Status attn/rise register"),
    15: ("ISC_P_STATUS_ATTN_MASK", "Status mask register"),
    16: ("ISC_P_STATUS_RT_REG", "Status reg (realtime)"),
    17: ("ISC_P_TIMESTAMP", "8-bit timestamp"),
    18: ("ISC_P_TIMESTAMP16", "16-bit timestamp"),
    19: ("ISC_P_PART_NUM", "Part Number String"),
    20: ("ISC_P_EE_UPD_ACK", "EE Update Acknowlegde"),
    21: ("ISC_P_EE_VER", "EE Version Number"),
    22: ("ISC_P_STATUS_FALL_REG", "Status fall register"),
    23: ("ISC_P_HW_CONFIG_REG", "Hardware config/setup reg"),
    24: ("ISC_P_APP_CONFIG_REG", "Feature config/setup reg"),
    30: ("ISC_P_USER_IN_REG", "User input value"),
    31: ("ISC_P_IN_SRC_REG", "Input source"),
    32: ("ISC_P_OUT_REG", "Output register"),
    33: ("ISC_P_OUT_RISE_REG", "Output rise edge"),
    34: ("ISC_P_OUT_FALL_REG", "Output fall edge"),
    35: ("ISC_P_CTL_STOP_OUT_REG", "Controlled output register"),
    36: ("ISC_P_USER_OUT_REG", "User output register"),
    37: ("ISC_P_OUT_PLA_SRC_REG", "Output source definition"),
    38: ("ISC_P_GP_TIMER_PERIOD", "Gen. purpose timer period"),
    39: ("ISC_P_PLA_OUT_REG", "PLA output"),
    40: ("ISC_P_IN_POLARITY_REG", "Input polarity register"),
    42: ("ISC_P_POSN_CAP_INDEX", "Encoder index position"),
    43: ("ISC_P_POSN_CAP_GPI1", "Encoder capture with GPI1"),
    44: ("ISC_P_POSN_CAP_PLA", "Encoder capture with PLA"),
    45: ("ISC_P_POSN_CAP_INDEX_LD", "Load Encoder index position"),
    46: ("ISC_P_RAS_MAX_VELOCIY", "Maximum velocity for current RAS"),
    47: ("ISC_P_VEL_LIM", "Trapezoidal velocity limit"),
    48: ("ISC_P_ACC_LIM", "Trapezoidal acceleration limit"),
    49: ("ISC_P_JERK_LIM", "Jerk limit"),
    50: ("ISC_P_ACC_MAX", "Test Point: Max Acc."),
    51: ("ISC_P_POSN_TRIG_PT", "At Position location"),
    52: ("ISC_P_A_START", "A after start point"),
    53: ("ISC_P_B_END", "B before end point"),
    54: ("ISC_P_POSN_TRK_RANGE", "Tracking in range window"),
    56: ("ISC_P_POSN_TRK", "Position tracking error"),
    59: ("ISC_P_STOP_ACC_LIM", "Stop acceleration limit"),
    60: ("ISC_P_POSN_MEAS_MTR", "Encoder 0 (motor) measured position"),
    61: ("ISC_P_POSN_MEAS", "Measured position"),
    62: ("ISC_P_POSN_CMD", "Commanded position"),
    63: ("ISC_P_VEL_CMD", "Commanded velocity"),
    64: ("ISC_P_VEL_MEAS", "Measured velocity"),
    65: ("ISC_P_DEC_LIM", "Deceleration Limit"),
    66: ("ISC_P_HEAD_DISTANCE", "Head distance"),
    67: ("ISC_P_TAIL_DISTANCE", "Tail distance"),
    68: ("ISC_P_HEADTAIL_VEL", "Head/Tail velocity"),
    69: ("ISC_P_POSN_MEAS_LD", "Encoder 1 measured position"),
    70: ("ISC_P_WARN_REG", "Warnings pending"),
    71: ("ISC_P_WARN_MASK", "Warnings for attention"),
    72: ("ISC_P_ALERT_MASK", "Alert selection"),
    74: ("ISC_P_MOVE_DWELL", "Post move dwell time (sec)"),
    89: ("ISC_P_ON_TIME", "59 Unit On Time"),
    90: ("ISC_P_USER_RAM0", "User RAM parameter"),
    91: ("ISC_P_USER_DATA_NV0", "User NV (13-bytes)"),
    92: ("ISC_P_USER_DATA_NV1", "User NV (13-bytes)"),
    93: ("ISC_P_USER_DATA_NV2", "User NV (13-bytes)"),
    94: ("ISC_P_USER_DATA_NV3", "User NV (13-bytes)"),
    104: ("ISC_P_NETERR_APP_CHKSUM", "Application Net Checksum counter"),
    105: ("ISC_P_NETERR_APP_FRAG", "Application Net Fragment counter"),
    106: ("ISC_P_NETERR_APP_STRAY", "Application Net Stray data counter"),
    107: ("ISC_P_NETERR_APP_OVERRUN", "Application Net Overrun counter"),
    108: ("ISC_P_NETERR_DIAG_CHKSUM", "Diagnostic Net Checksum counter"),
    109: ("ISC_P_NETERR_DIAG_FRAG", "Diagnostic Net Fragment counter"),
    110: ("ISC_P_NETERR_DIAG_STRAY", "Diagnostic Net Stray data counter"),
    111: ("ISC_P_NETERR_DIAG_OVERRUN", "Diagnostic Net Overrun counter"),
    116: ("ISC_P_NETERR_LOW_VOLTS", "Link Voltage Low Event counter"),
    257: ("ISC_P_DRV_I_MAX", "Current Full Scale (A)"),
    258: ("ISC_P_DRV_RMS_MAX", "Factory RMS limit"),
    259: ("ISC_P_DRV_FACT_IR_CAL", "Ir Sensor Calibration"),
    260: ("ISC_P_DRV_FACT_IS_CAL", "Is Sensor Calibration"),
    262: ("ISC_P_DRV_ADC_MAX", "ADC full scale (A)"),
    263: ("ISC_P_DRV_CONFIG_CHANGED", "Configuration changed"),
    264: ("ISC_P_DRV_VECTOR_RATE", "Encoder Dens. (/[turn/pole-pair])"),
    265: ("ISC_P_DRV_USTEPS_PER_REV", "Stepper uSteps (/[turn/pole-pair])"),
    266: ("ISC_P_DRV_ENC_DENS", "Encoder Dens. (/[turn/pole-pair])"),
    267: ("ISC_P_DRV_ENC_RES", "Encoder step distance (microns/.01)"),
    268: ("ISC_P_DRV_MTR_POLES", "Motor Pole Count"),
    269: ("ISC_P_DRV_MTR_KE", "Motor: Ke (V/KRPM)"),
    270: ("ISC_P_DRV_MTR_OHMS", "Motor: Resistance (ohm)"),
    271: ("ISC_P_DRV_MTR_ELEC_TC", "Motor: Elect Time Constant (ms)"),
    272: ("ISC_P_DRV_COM_RO", "Commutation Reference Offset"),
    273: ("ISC_P_DRV_RMS_LIM", "RMS shutdown limit (A)"),
    274: ("ISC_P_DRV_RMS_TC", "RMS time constant (sec) @ 100% trq"),
    275: ("ISC_P_DRV_MTR_SPEED_LIM", "Motor Speed Limit (quads/msec)"),
    276: ("ISC_P_DRV_COM_CAP", "Commutation Edge Capture"),
    277: ("ISC_P_DRV_COM_ANGLE", "Commutation Angle Reference (quads)"),
    278: ("ISC_P_DRV_KIP", "Vector Torque: Kip"),
    279: ("ISC_P_DRV_KII", "Vector Torque: Kii"),
    280: ("ISC_P_DRV_LD_SPEED_LIM", "Load Speed Limit (quads/msec)"),
    281: ("ISC_P_DRV_KPL", "Compensator: Kpl"),
    282: ("ISC_P_DRV_KV", "Compensator: Kv"),
    283: ("ISC_P_DRV_KP", "Compensator: Kp"),
    284: ("ISC_P_DRV_KI", "Compensator: Ki"),
    285: ("ISC_P_DRV_KFV", "Compensator: Kfv"),
    286: ("ISC_P_DRV_KFA", "Compensator: Kfa"),
    287: ("ISC_P_DRV_KFJ", "Compensator: Kfj (jerk ff)"),
    288: ("ISC_P_DRV_KFF", "Compensator: Kff (fric. ff)"),
    289: ("ISC_P_DRV_KNV", "Compensator: Knv"),
    290: ("ISC_P_DRV_AHFUZZ2", "Compensator: Antihunt 2"),
    291: ("ISC_P_DRV_TRQ_BIAS", "Compensator: Torque Bias (A)"),
    292: ("ISC_P_DRV_FUZZY_APERTURE", "Fuzzy Aperture"),
    293: ("ISC_P_DRV_FUZZY_HYST", "Fuzzy Hystersis"),
    294: ("ISC_P_DRV_FAN_SPEED", "Drive Fan Speed (RPM)"),
    295: ("ISC_P_DRV_FAN_WARN_SPEED", "Drive Fan Warning Min Speed (RPM)"),
    296: ("ISC_P_TRK_ERR_MAX", "Accumulated maximum error"),
    297: ("ISC_P_TRK_ERR_MIN", "Accumulated minimum error"),
    298: ("ISC_P_AH_HOLDOFF", "Anti-hunt holdoff"),
    299: ("ISC_P_DRV_LD_MTR_RATIO", "Load to motor encoder ratio"),
    301: ("ISC_P_DRV_TUNE_CONFIG_REG", ""),
    302: ("ISC_P_DRV_SENSORLESS_RAMPUP_TIME", "Sensorless start torque rampup time (ms)"),
    303: ("ISC_P_DRV_SENSORLESS_SWEEP_TIME", "Sensorless start angle sweep time (ms)"),
    304: ("ISC_P_DRV_SENSORLESS_SETTLE_TIME", "Sensorless start settle time (ms)"),
    305: ("ISC_P_DRV_SENSORLESS_TRQ", "Sensorless start torque"),
    306: ("ISC_P_DRV_HARDSTOP_ENTRY_SPD", "Hard-stop speed qualifier"),
    307: ("ISC_P_DRV_TRQ_LIM", "Torque Limit  (A)"),
    308: ("ISC_P_DRV_POS_FLDBK_TRQ", "+ Torque foldback limit (A)"),
    309: ("ISC_P_DRV_POS_FLDBK_TRQ_TC", "+ Torque foldback time const (ms)"),
    310: ("ISC_P_DRV_NEG_FLDBK_TRQ", "- Torque foldback limit (A)"),
    311: ("ISC_P_DRV_NEG_FLDBK_TRQ_TC", "- Torque foldback time const (ms)"),
    312: ("ISC_P_DRV_HARDSTOP_FLDBK_TRQ", "Hardstop foldback limit (A)"),
    313: ("ISC_P_DRV_HARDSTOP_FLDBK_TRQ_TC", "Hardstop foldback time const (ms)"),
    314: ("ISC_P_DRV_MOVEDONE_FLDBK_TRQ", "Move Done Foldback Limit (A)"),
    315: ("ISC_P_DRV_MOVEDONE_FLDBK_TRQ_TC", "Move Done Foldback time const (ms)"),
    316: ("ISC_P_DRV_HARDSTOP_ENTRY_TRQ", "Foldback Torque Trip Level (A)"),
    317: ("ISC_P_DRV_HARDSTOP_ENTRY_TC", "Hard Stop: entry delay (ms)"),
    318: ("ISC_P_DRV_TRQ_CMD", "Torque/Force Commanded"),
    319: ("ISC_P_DRV_TRQ_MEAS", "Torque/Force Measured"),
    320: ("ISC_P_DRV_RMS_LVL", "RMS level"),
    321: ("ISC_P_DRV_TRK_ERR_LIM", "Tracking Error Limit (quad cnts)"),
    322: ("ISC_P_DRV_MV_DN_TC", "Move Done: Time Constant (ms)"),
    323: ("ISC_P_DRV_STEPPER_TRQ", "Recovery window maximum"),
    324: ("ISC_P_DRV_STEP_IDLE_TRQ", "Stepper idle torque (A)"),
    325: ("ISC_P_DRV_STEP_ACC_TRQ", "Stepper accel torque (A)"),
    326: ("ISC_P_DRV_STEP_FLDBK_TRQ_TC", "Stepper trq foldback time const (ms)"),
    327: ("ISC_P_DRV_BUS_VOLTS", "Bus Voltage (V)"),
    328: ("ISC_P_DRV_TP_IOP", "I/O testpoint"),
    329: ("ISC_P_DRV_TP_IR", "R Channel testpoint"),
    330: ("ISC_P_DRV_TP_IS", "S Channel testpoint"),
    331: ("ISC_P_DRV_TP_IR_FILT", "R Channel testpoint/filter"),
    332: ("ISC_P_DRV_TP_IS_FILT", "S Channel testpoint/filter"),
    333: ("ISC_P_HEATSINK_TEMP", "Heatsink temperature"),
    334: ("ISC_P_AMBIENT_TEMP", "Internal temperature"),
    335: ("ISC_P_DRV_TP_5V", "5V testpoint"),
    336: ("ISC_P_DRV_TP_12V", "12V testpoint"),
    337: ("ISC_P_DRV_TRQ_MEAS_FILT_TC", "Trq Measured Filter Time Const"),
    338: ("ISC_P_DRV_TEMP_SIM", "Temp Simulator"),
    339: ("ISC_P_DRV_FACT_KM_FACTOR", "Km Factor"),
    340: ("ISC_P_DRV_FACT_MTR_MIN_RES", "Mtr Min Res"),
    341: ("ISC_P_FACT_FAN_ON_TEMP", "Fan On Temp"),
    342: ("ISC_P_DRV_PARTID", "Part ID"),
    343: ("ISC_P_DRV_FACT_IB_TC", "IB TC"),
    344: ("ISC_P_DRV_FACT_IB_TRIP", "IB Trip Point (A)"),
    345: ("ISC_P_DRV_FACT_PHASE_TRIP", "Phase Trip Point (A)"),
    346: ("ISC_P_DRV_IB_LVL", "IB Level"),
    347: ("ISC_P_DRV_TSPD", "Tspd phase delay"),
    349: ("ISC_P_DRV_COMM_CHK_ANGLE_LIM  ", "Comm check angle limit"),
    350: ("ISC_P_DRV_CPL_ERR_LIM", "Coupling Error Limit (quad cnts)"),
    357: ("ISC_P_IEX_STATUS", "Current IEX status info"),
    358: ("ISC_P_IEX_USER_OUT_REG", "IEX output register"),
    359: ("ISC_P_IEX_STOP_OUT_REG", "IEX output register when stopped"),
    360: ("ISC_P_IEX_OUT_REG", "IEX last output register"),
    361: ("ISC_P_IEX_IN_REG", "IEX input register"),
    362: ("ISC_P_IEX_IN_RISE_REG", "IEX input rise register"),
    363: ("ISC_P_IEX_IN_FALL_REG", "IEX input fall register"),
    364: ("ISC_P_IEX_IN_REG_MASK", "IEX input register"),
    365: ("ISC_P_IEX_IN_RISE_REG_MASK", "IEX input rise register"),
    366: ("ISC_P_IEX_IN_FALL_REG_MASK", "IEX input fall register"),
    367: ("ISC_P_IEX_GLITCH_LIM", "IEX glitch limit"),
    368: ("ISC_P_DRV_SOFT_LIM_POSN_POS", "Software limit positive position"),
    369: ("ISC_P_DRV_SOFT_LIM_POSN_NEG", "Software limit negative position")
}

ISC_P_NODEID = 0
ISC_P_FW_VERSION = 1
ISC_P_HW_VERSION = 2
ISC_P_RESELLER_ID = 3
ISC_P_SER_NUM = 4
ISC_P_OPTION_REG = 5
ISC_P_ROM_SUM_ACK = 6
ISC_P_ROM_SUM = 7
ISC_P_SAMPLE_PERIOD = 8
ISC_P_ALERT_REG = 9
ISC_P_STOP_TYPE = 10
ISC_P_WATCHDOG_TIME = 11
ISC_P_NET_STAT = 12
ISC_P_STATUS_ACCUM_REG = 13
ISC_P_STATUS_ATTN_RISE_REG = 14
ISC_P_STATUS_ATTN_MASK = 15
ISC_P_STATUS_RT_REG = 16
ISC_P_TIMESTAMP = 17
ISC_P_TIMESTAMP16 = 18
ISC_P_PART_NUM = 19
ISC_P_EE_UPD_ACK = 20
ISC_P_EE_VER = 21
ISC_P_STATUS_FALL_REG = 22
ISC_P_HW_CONFIG_REG = 23
ISC_P_APP_CONFIG_REG = 24
ISC_P_USER_IN_REG = 30
ISC_P_IN_SRC_REG = 31
ISC_P_OUT_REG = 32
ISC_P_OUT_RISE_REG = 33
ISC_P_OUT_FALL_REG = 34
ISC_P_CTL_STOP_OUT_REG = 35
ISC_P_USER_OUT_REG = 36
ISC_P_OUT_PLA_SRC_REG = 37
ISC_P_GP_TIMER_PERIOD = 38
ISC_P_PLA_OUT_REG = 39
ISC_P_IN_POLARITY_REG = 40
ISC_P_POSN_CAP_INDEX = 42
ISC_P_POSN_CAP_GPI1 = 43
ISC_P_POSN_CAP_PLA = 44
ISC_P_POSN_CAP_INDEX_LD = 45
ISC_P_RAS_MAX_VELOCIY = 46
ISC_P_VEL_LIM = 47
ISC_P_ACC_LIM = 48
ISC_P_JERK_LIM = 49
ISC_P_ACC_MAX = 50
ISC_P_POSN_TRIG_PT = 51
ISC_P_A_START = 52
ISC_P_B_END = 53
ISC_P_POSN_TRK_RANGE = 54
ISC_P_POSN_TRK = 56
ISC_P_STOP_ACC_LIM = 59
ISC_P_POSN_MEAS_MTR = 60
ISC_P_POSN_MEAS = 61
ISC_P_POSN_CMD = 62
ISC_P_VEL_CMD = 63
ISC_P_VEL_MEAS = 64
ISC_P_DEC_LIM = 65
ISC_P_HEAD_DISTANCE = 66
ISC_P_TAIL_DISTANCE = 67
ISC_P_HEADTAIL_VEL = 68
ISC_P_POSN_MEAS_LD = 69
ISC_P_WARN_REG = 70
ISC_P_WARN_MASK = 71
ISC_P_ALERT_MASK = 72
ISC_P_MOVE_DWELL = 74
ISC_P_ON_TIME = 89
ISC_P_USER_RAM0 = 90
ISC_P_USER_DATA_NV0 = 91
ISC_P_USER_DATA_NV1 = 92
ISC_P_USER_DATA_NV2 = 93
ISC_P_USER_DATA_NV3 = 94
ISC_P_NETERR_APP_CHKSUM = 104
ISC_P_NETERR_APP_FRAG = 105
ISC_P_NETERR_APP_STRAY = 106
ISC_P_NETERR_APP_OVERRUN = 107
ISC_P_NETERR_DIAG_CHKSUM = 108
ISC_P_NETERR_DIAG_FRAG = 109
ISC_P_NETERR_DIAG_STRAY = 110
ISC_P_NETERR_DIAG_OVERRUN = 111
ISC_P_NETERR_LOW_VOLTS = 116
ISC_P_DRV_I_MAX = 257
ISC_P_DRV_RMS_MAX = 258
ISC_P_DRV_FACT_IR_CAL = 259
ISC_P_DRV_FACT_IS_CAL = 260
ISC_P_DRV_ADC_MAX = 262
ISC_P_DRV_CONFIG_CHANGED = 263
ISC_P_DRV_VECTOR_RATE = 264
ISC_P_DRV_USTEPS_PER_REV = 265
ISC_P_DRV_ENC_DENS = 266
ISC_P_DRV_ENC_RES = 267
ISC_P_DRV_MTR_POLES = 268
ISC_P_DRV_MTR_KE = 269
ISC_P_DRV_MTR_OHMS = 270
ISC_P_DRV_MTR_ELEC_TC = 271
ISC_P_DRV_COM_RO = 272
ISC_P_DRV_RMS_LIM = 273
ISC_P_DRV_RMS_TC = 274
ISC_P_DRV_MTR_SPEED_LIM = 275
ISC_P_DRV_COM_CAP = 276
ISC_P_DRV_COM_ANGLE = 277
ISC_P_DRV_KIP = 278
ISC_P_DRV_KII = 279
ISC_P_DRV_LD_SPEED_LIM = 280
ISC_P_DRV_KPL = 281
ISC_P_DRV_KV = 282
ISC_P_DRV_KP = 283
ISC_P_DRV_KI = 284
ISC_P_DRV_KFV = 285
ISC_P_DRV_KFA = 286
ISC_P_DRV_KFJ = 287
ISC_P_DRV_KFF = 288
ISC_P_DRV_KNV = 289
ISC_P_DRV_AHFUZZ2 = 290
ISC_P_DRV_TRQ_BIAS = 291
ISC_P_DRV_FUZZY_APERTURE = 292
ISC_P_DRV_FUZZY_HYST = 293
ISC_P_DRV_FAN_SPEED = 294
ISC_P_DRV_FAN_WARN_SPEED = 295
ISC_P_TRK_ERR_MAX = 296
ISC_P_TRK_ERR_MIN = 297
ISC_P_AH_HOLDOFF = 298
ISC_P_DRV_LD_MTR_RATIO = 299
ISC_P_DRV_TUNE_CONFIG_REG = 301
ISC_P_DRV_SENSORLESS_RAMPUP_TIME = 302
ISC_P_DRV_SENSORLESS_SWEEP_TIME = 303
ISC_P_DRV_SENSORLESS_SETTLE_TIME = 304
ISC_P_DRV_SENSORLESS_TRQ = 305
ISC_P_DRV_HARDSTOP_ENTRY_SPD = 306
ISC_P_DRV_TRQ_LIM = 307
ISC_P_DRV_POS_FLDBK_TRQ = 308
ISC_P_DRV_POS_FLDBK_TRQ_TC = 309
ISC_P_DRV_NEG_FLDBK_TRQ = 310
ISC_P_DRV_NEG_FLDBK_TRQ_TC = 311
ISC_P_DRV_HARDSTOP_FLDBK_TRQ = 312
ISC_P_DRV_HARDSTOP_FLDBK_TRQ_TC = 313
ISC_P_DRV_MOVEDONE_FLDBK_TRQ = 314
ISC_P_DRV_MOVEDONE_FLDBK_TRQ_TC = 315
ISC_P_DRV_HARDSTOP_ENTRY_TRQ = 316
ISC_P_DRV_HARDSTOP_ENTRY_TC = 317
ISC_P_DRV_TRQ_CMD = 318
ISC_P_DRV_TRQ_MEAS = 319
ISC_P_DRV_RMS_LVL = 320
ISC_P_DRV_TRK_ERR_LIM = 321
ISC_P_DRV_MV_DN_TC = 322
ISC_P_DRV_STEPPER_TRQ = 323
ISC_P_DRV_STEP_IDLE_TRQ = 324
ISC_P_DRV_STEP_ACC_TRQ = 325
ISC_P_DRV_STEP_FLDBK_TRQ_TC = 326
ISC_P_DRV_BUS_VOLTS = 327
ISC_P_DRV_TP_IOP = 328
ISC_P_DRV_TP_IR = 329
ISC_P_DRV_TP_IS = 330
ISC_P_DRV_TP_IR_FILT = 331
ISC_P_DRV_TP_IS_FILT = 332
ISC_P_HEATSINK_TEMP = 333
ISC_P_AMBIENT_TEMP = 334
ISC_P_DRV_TP_5V = 335
ISC_P_DRV_TP_12V = 336
ISC_P_DRV_TRQ_MEAS_FILT_TC = 337
ISC_P_DRV_TEMP_SIM = 338
ISC_P_DRV_FACT_KM_FACTOR = 339
ISC_P_DRV_FACT_MTR_MIN_RES = 340
ISC_P_FACT_FAN_ON_TEMP = 341
ISC_P_DRV_PARTID = 342
ISC_P_DRV_FACT_IB_TC = 343
ISC_P_DRV_FACT_IB_TRIP = 344
ISC_P_DRV_FACT_PHASE_TRIP = 345
ISC_P_DRV_IB_LVL = 346
ISC_P_DRV_TSPD = 347
ISC_P_DRV_COMM_CHK_ANGLE_LIM = 349
ISC_P_DRV_CPL_ERR_LIM = 350
ISC_P_IEX_STATUS = 357
ISC_P_IEX_USER_OUT_REG = 358
ISC_P_IEX_STOP_OUT_REG = 359
ISC_P_IEX_OUT_REG = 360
ISC_P_IEX_IN_REG = 361
ISC_P_IEX_IN_RISE_REG = 362
ISC_P_IEX_IN_FALL_REG = 363
ISC_P_IEX_IN_REG_MASK = 364
ISC_P_IEX_IN_RISE_REG_MASK = 365
ISC_P_IEX_IN_FALL_REG_MASK = 366
ISC_P_IEX_GLITCH_LIM = 367
ISC_P_DRV_SOFT_LIM_POSN_POS = 368
ISC_P_DRV_SOFT_LIM_POSN_NEG = 369

paramTypes = {
    0: ("PT_NONE", "Parameter is not present"),
    1: ("PT_RO", "Read only paramater"),
    2: ("PT_VOL", "Volatile R/W paramater"),
    4: ("PT_NV", "Non-volatile R/W paramater"),
    8: ("PT_RT", "Real-time non-cached value"),
    16: ("PR_CLR", "Clear on read type"),
    32: ("PR_RAM", "RAM R/W type"),
}

unitTypes = {
    1: ("NO_UNIT", "No intrinsic unit"),
    2: ("BIT_FIELD", "Value is a bit field"),
    3: ("DX_TICK", "Distance: the encoder tick"),
    4: ("DX_INCH", "Distance: inches"),
    5: ("DX_MM", "Distance: millimeters"),
    6: ("DX_REV", "Distance: revolution"),
    7: ("VOLT", "Voltage in volts"),
    8: ("CURRENT", "Current in amperes"),
    9: ("TIME_S", "Time in seconds"),
    10: ("TIME_MSEC", "Time in milliseconds"),
    11: ("TIME_USEC", "Time in microseconds"),
    12: ("TIME_SAMPLE", "Time in sample times"),
    13: ("VEL_TICK_MSEC", "Velocity is encoder counts / ms"),
    14: ("VEL_TICK_MSEC2", "Velocity is encoder counts / ms^2"),
    15: ("VEL_TICK_SAMPLE", "Velocity is encoder counts / sample time"),
    16: ("VEL_TICK_SAMPLE2", "Velocity is encoder counts / sample time^2"),
    17: ("VEL_STEPS_S", "Velocity is steps / second"),
    18: ("VEL_STEPS_MS", "Velocity is steps / millisecond"),
    19: ("VEL_RPM", "Velocity is revolutions per minute"),
    20: ("VEL_RPS", "Velocity is revolutions per second"),
    21: ("VEL_IPS", "Velocity is inches per second"),
    22: ("VEL_MMPS", "Velocity is mm per second"),
    23: ("STRING8", "String value (fixed 8 bytes)"),
    24: ("OSTRING", "OLESTR"),
    25: ("FW_VERS", "Firmware version structure"),
    26: ("HW_VERS", "Hardware version structure"),
    27: ("DEV_ID", "Device ID"),
    28: ("IOC_HZ", "IOC filter corner frequency"),
    29: ("UNIT_HZ", "Frequency in Hz"),
}

r_unitTypes = {}
for (id, data) in unitTypes.iteritems():
    r_unitTypes[data[0]] = id

r_iscParams = {}
for (id, data) in iscParams.iteritems():
    r_iscParams[data[0]] = id

STOP_TYPE_ABRUPT = 0x00
STOP_TYPE_RAMP = 0x01
STOP_TYPE_AFTER_CYCLE = 0x02
STOP_TYPE_IGNORE = 0x03
STOP_TYPE_ESTOP_EBRUPT = 0x10
STOP_TYPE_ESTOP_RAMP = 0x11
STOP_TYPE_CTRLD_ABRUPT = 0x20
STOP_TYPE_CTRLD_RAMP = 0x21
STOP_TYPE_ESTOP_CTRLD_ABRUPT = 0x30
STOP_TYPE_ESTOP_CTRLD_RAMP = 0x31
STOP_TYPE_ESTOP_CTRLD = 0x33
STOP_TYPE_CLR_ESTOP = 0x18
STOP_TYPE_CLR_CTRLD = 0x28
STOP_TYPE_CLR_ALL = 0xf8

nodeStopCodes = {
    0x00: ('STOP_TYPE_ABRUPT', 'Stop the executing motion and flush any pending motion commands immediately.'),
    0x01: ('STOP_TYPE_RAMP', ' Kill Motion with decel limit'),
    0x02: ('STOP_TYPE_AFTER_CYCLE', 'After cycle completes'),
    0x03: ('STOP_TYPE_IGNORE', ' Node stop ignored'),
    0x10: ('STOP_TYPE_ESTOP_EBRUPT', ''),
    0x11: ('STOP_TYPE_ESTOP_RAMP', ''),
    0x20: ('STOP_TYPE_CTRLD_ABRUPT', ''),
    0x21: ('STOP_TYPE_CTRLD_RAMP', ''),
    0x30: ('STOP_TYPE_ESTOP_CTRLD_ABRUPT', ''),
    0x31: ('STOP_TYPE_ESTOP_CTRLD_RAMP', ''),
    0x33: ('STOP_TYPE_ESTOP_CTRLD', ''),
    0x18: ('STOP_TYPE_CLR_ESTOP', 'Clear E-stop'),
    0x28: ('STOP_TYPE_CLR_CTRLD', 'Clear controlled stop'),
    0xf8: ('STOP_TYPE_CLR_ALL', 'Clear all modifiers')
}

r_nodeStopCodes = {}
for (id, data) in nodeStopCodes.iteritems():
    r_nodeStopCodes[data[0]] = id

plaOutReg = {
    0: 'Gpo0',
    1: 'Gpo1',
    2: 'Enable',
    3: 'Capture',
    4: 'Trigger',
    5: 'NodeStop',
    6: 'ResetTimer',
    7: 'PLAattn0',
    8: 'PLAattn1',
    9: 'pad0',
    10: 'pad1',
    11: 'pad2',
    12: 'PosTrqFldBk',
    13: 'NegTrqFldBk',
    14: 'pad3',
    15: 'pad4',
}

PLAOUT_GPO0 = 1
PLAOUT_GPO1 = 2
PLAOUT_ENABLE = 4
PLAOUT_CAPTURE = 8
PLAOUT_TRIGGER = 16
PLAOUT_NODESTOP = 32
PLAOUT_RESETTIMER = 64
PLAOUT_PLAATTN0 = 128
PLAOUT_PLAATTN1 = 256
PLAOUT_PAD0 = 512
PLAOUT_PAD1 = 1024
PLAOUT_PAD2 = 2048
PLAOUT_POSTRQFLDBK = 4096
PLAOUT_NEGTRQFLDBK = 8192
PLAOUT_PAD3 = 16384
PLAOUT_PAD4 = 32768

MG_MOVE_RELATIVE = 1
MG_MOVE_WAIT = 2
MG_MOVE_DWELL = 4
MG_MOVE_ASYM = 8
MG_MOVE_TAIL = 16
MG_MOVE_HEAD = 32
MG_MOVE_REPEAT = 64
MG_MOVE_RECIPROCATE = 128

MG_MOVE_STYLE_NORM_ABS = 0x00  # Move triangle / trapezoid abs target
MG_MOVE_STYLE_ASYM_ABS = 0x08  # Move / programmable Acc/Dec limit  abs target
MG_MOVE_STYLE_TAIL_ABS = 0x10  # Move / tail velocity segment  abs target
MG_MOVE_STYLE_HEAD_ABS = 0x20  # Move / head velocity segment  abs target
MG_MOVE_STYLE_HEADTAIL_ABS = 0x30  # Move / head-tail velocity segments  abs target

MG_MOVE_STYLE_NORM = 0x01  # Move triangle / trapezoid
MG_MOVE_STYLE_ASYM = 0x09  # Move / programmable Acc/Dec limit
MG_MOVE_STYLE_TAIL = 0x11  # Move / tail velocity segment
MG_MOVE_STYLE_HEAD = 0x21  # Move / head velocity segment
MG_MOVE_STYLE_HEADTAIL = 0x31  # Move / head-tail velocity segments

MG_MOVE_STYLE_NORM_TRIG_ABS = 0x02  # Move triangle / trapezoid abs target/trigger
MG_MOVE_STYLE_ASYM_TRIG_ABS = 0x0a  # Move / programmable Acc/Dec limit  abs target abs target/trigger
MG_MOVE_STYLE_TAIL_TRIG_ABS = 0x12  # Move / tail velocity segment abs target/trigger
MG_MOVE_STYLE_HEAD_TRIG_ABS = 0x22  # Move / head velocity segment abs target/trigger
MG_MOVE_STYLE_HEADTAIL_TRIG_ABS = 0x32  # Move / head-tail velocity segments  abs target

MG_MOVE_STYLE_NORM_TRIG = 0x03  # Move triangle / trapezoid  / trigger
MG_MOVE_STYLE_ASYM_TRIG = 0x0b  # Move / programmable Acc/Dec limit /trigger
MG_MOVE_STYLE_TAIL_TRIG = 0x13  # Move / tail velocity segment / trigger
MG_MOVE_STYLE_HEAD_TRIG = 0x23  # Move / head velocity segment / trigger
MG_MOVE_STYLE_HEADTAIL_TRIG = 0x33  # Move / head-tail velocity segments / trigger

# 
# mgPosnStyles =  {
# 'MG_MOVE_STYLE_NORM_ABS':          0x00,     # Move triangle / trapezoid abs target
# 'MG_MOVE_STYLE_ASYM_ABS':          0x08,     # Move / programmable Acc/Dec limit  abs target
# 'MG_MOVE_STYLE_TAIL_ABS':          0x10,     # Move / tail velocity segment  abs target
# 'MG_MOVE_STYLE_HEAD_ABS':          0x20,     # Move / head velocity segment  abs target
# 'MG_MOVE_STYLE_HEADTAIL_ABS':      0x30,     # Move / head-tail velocity segments  abs target
# 
# 'MG_MOVE_STYLE_NORM':              0x01,     # Move triangle / trapezoid
# 'MG_MOVE_STYLE_ASYM':              0x09,     # Move / programmable Acc/Dec limit
# 'MG_MOVE_STYLE_TAIL':              0x11,     # Move / tail velocity segment
# 'MG_MOVE_STYLE_HEAD':              0x21,     # Move / head velocity segment
# 'MG_MOVE_STYLE_HEADTAIL':          0x31,     # Move / head-tail velocity segments
# 
# 'MG_MOVE_STYLE_NORM_TRIG_ABS':     0x02,     # Move triangle / trapezoid abs target/trigger
# 'MG_MOVE_STYLE_ASYM_TRIG_ABS':     0x0a,     # Move / programmable Acc/Dec limit  abs target abs target/trigger
# 'MG_MOVE_STYLE_TAIL_TRIG_ABS':     0x12,     # Move / tail velocity segment abs target/trigger
# 'MG_MOVE_STYLE_HEAD_TRIG_ABS':     0x22,     # Move / head velocity segment abs target/trigger
# 'MG_MOVE_STYLE_HEADTAIL_TRIG_ABS': 0x32,     # Move / head-tail velocity segments  abs target
# 
# 'MG_MOVE_STYLE_NORM_TRIG':         0x03,     # Move triangle / trapezoid  / trigger
# 'MG_MOVE_STYLE_ASYM_TRIG':         0x0b,     # Move / programmable Acc/Dec limit /trigger
# 'MG_MOVE_STYLE_TAIL_TRIG':         0x13,     # Move / tail velocity segment / trigger
# 'MG_MOVE_STYLE_HEAD_TRIG':         0x23,     # Move / head velocity segment / trigger
# 'MG_MOVE_STYLE_HEADTAIL_TRIG':     0x33      # Move / head-tail velocity segments / trigger
# }
