dog_ids = [
    251,
    268,
    256,
    253,
    255,
    254,
    257,
    159,
    211,
    210,
    212,
    214,
    213,
    216,
    215,
    219,
    220,
    221,
    217,
    218,
    207,
    209,
    206,
    205,
    208,
    193,
    202,
    194,
    191,
    204,
    187,
    203,
    185,
    192,
    183,
    199,
    195,
    181,
    184,
    201,
    186,
    200,
    182,
    188,
    189,
    190,
    197,
    196,
    198,
    179,
    180,
    177,
    178,
    175,
    163,
    174,
    176,
    160,
    162,
    161,
    164,
    168,
    173,
    170,
    169,
    165,
    166,
    167,
    172,
    171,
    264,
    263,
    266,
    265,
    267,
    262,
    246,
    242,
    243,
    248,
    247,
    229,
    233,
    234,
    228,
    231,
    232,
    230,
    227,
    226,
    235,
    225,
    224,
    223,
    222,
    236,
    252,
    237,
    250,
    249,
    241,
    239,
    238,
    240,
    244,
    245,
    259,
    261,
    260,
    258,
    154,
    153,
    158,
    152,
    155,
    151,
    157,
    156,
]


class MyDogsIDS:
    def __init__(self, class_ids):
        self.class_ids = class_ids
        super(MyDogsIDS, self).__init__()

    def get_dogs_ids(self):
        ids = self.class_ids
        return ids


def get_class_ids():
    my_class_ids = MyDogsIDS(dog_ids)
    my_ids = my_class_ids.get_dogs_ids()
    return my_ids


if __name__ == "__main__":
    res = get_class_ids()
    print(res)
