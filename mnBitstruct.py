import pprint


class BitStruct(object):
    def __init__(self, data=0):
        self.fields = {}
        self.lowbit = {}
        self.members = {}
        self.populate()
        self.data = data
        self.unpack()
        return

    def populate(self):
        return

    def pirint_data(self):
        pprint.pprint(self.members)

    def addField(self, name, bits):
        self.fields[name] = bits
        if type(bits) == tuple:
            t = list(bits)
            t.sort()
            self.lowbit[name] = t[0]
        else:
            self.lowbit[name] = 0
        return

    def __getitem__(self, key):
        return self.members[key]

    def __setitem__(self, key, value):
        if not self.members.has_key(key):
            raise KeyError("Member does not exist")

        if type(self.fields[key]) in (int, long) and type(value) != bool:
            raise ValueError("Value is wrong type (got %s expected bool)" % (type(value)))

        if type(self.fields[key]) == tuple and type(value) not in (int, long):
            raise ValueError("Value is wrong type (got %s expected int or long)" % (type(value)))

        self.members[key] = value
        self.pack()
        return

    def unpack(self, data=None):
        ret = {}
        if data == None:
            data = self.data

        for name, bits in self.fields.iteritems():
            # build bit mask from bitspec

            # for single bit spec, we treat the output as a bool
            if type(bits) in (int, long):
                if data & (1 << bits) == 0:
                    ret[name] = False
                else:
                    ret[name] = True

            # for multiple bit tuple spec, we treat the output as an long
            elif type(bits) == tuple:
                mask = 0
                for bit in bits:
                    mask |= (1 << bit)

                ret[name] = (data & mask) >> self.lowbit[name]

            else:
                raise Exception("Invalid bitspec %s" % (type(bits)))

        self.members = ret
        return ret

    def pack(self, d=None):
        ret = 0
        if d == None:
            d = self.members

        for name, value in d.iteritems():
            if not self.fields.has_key(name):
                raise Exception("Struct does not contain named member '%s'" % (name))

            if type(value) == bool:
                if type(self.fields[name]) not in (long, int):
                    raise Exception("Provided data type does not match struct definition for member '%s'" % (name))

                if value is True:
                    ret |= (1 << self.fields[name])
                continue

            elif type(value) in (long, int):
                if type(self.fields[name]) != tuple:
                    raise Exception("Provided data type does not match struct definition for member '%s'" % (name))

                ret |= (value << self.lowbit[name])

            else:
                raise Exception(
                    "Provided data type does not match struct definition for member '%s', %s" % (name, type(value)))

        self.data = ret
        return ret

#
# class BitTest(BitStruct):
#     def populate(self):
#         for bit in range(32):
#             self.addField('Bit%d' % (bit), bit)
#         self.addField('byte1', tuple(range(0, 8)))
#         self.addField('byte2', tuple(range(8, 16)))
#         self.addField('byte3', tuple(range(16, 24)))
#         self.addField('byte4', tuple(range(24, 32)))
#         return
#
#
# if __name__ == '__main__':
#     t = BitTest()
#     import pprint
#     pprint.pprint(t.unpack(12))
#     pprint.pprint(t.unpack(13))
#     pprint.pprint(t.unpack(14))
#     pprint.pprint(t.unpack(15))
#     pprint.pprint(t.unpack(16))
#
