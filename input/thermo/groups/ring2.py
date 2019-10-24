name = "Ring Corrections" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
    index = 157,
    label = "octasulfur",
    group = 
"""
1 * S2s u0 {2,S} {8,S}
2   S2s u0 {1,S} {3,S}
3   S2s u0 {2,S} {4,S}
4   S2s u0 {3,S} {5,S}
5   S2s u0 {4,S} {6,S}
6   S2s u0 {5,S} {7,S}
7   S2s u0 {6,S} {8,S}
8   S2s u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.03789952361821408,
        B = -1.160238376562268,
        E = -1.5695221761465261,
        L = -2.211227320269482,
        A = -0.06600445896604455,
    ),
    )


entry(
    index = 102,
    label = "EightMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {8,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {1,[S,D]} {7,[S,D]}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 59,
    label = "Cyclooctane",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.12289457384009299,
        B = 0.03690417910443148,
        E = 0.10174311461609618,
        L = 0.06959198509702834,
        A = -0.008583337782420174,
    ),
    )


entry(
    index = 1,
    label = "Cyclopropane",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.00768752803915192,
        B = -0.04836878737422211,
        E = 0.08792053795363841,
        L = 0.0826810775324536,
        A = -0.02599916891994444,
    ),
    )


entry(
    index = 97,
    label = "ThreeMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {3,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {1,[S,D]} {2,[S,D]}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 13,
    label = "Cyclobutane",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.0068756569135358814,
        B = -0.0027628134974619876,
        E = 0.05938731023573348,
        L = 0.08931529423647072,
        A = -0.06655408698567898,
    ),
    )


entry(
    index = 98,
    label = "FourMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {4,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {1,[S,D]} {3,[S,D]}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 21,
    label = "Cyclopentane",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.01763261809844347,
        B = -0.009386383190166193,
        E = 0.0207404760348399,
        L = 0.07449936447804617,
        A = -0.02456533793131052,
    ),
    )


entry(
    index = 99,
    label = "FiveMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {5,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D,T]}
5   R!H u0 {1,[S,D]} {4,[S,D,T]}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 32,
    label = "Cyclohexane",
    group = 
"""
1 * Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.04349707582537152,
        B = 0.020919723144906335,
        E = -0.11633332880170685,
        L = -0.21898843663653023,
        A = 0.018573958818337004,
    ),
    )


entry(
    index = 105,
    label = "sixnosidedouble",
    group = 
"""
1 * [Cs,O2s,N,S2s] u0 {2,S} {6,S}
2   [Cs,O2s,N,S2s] u0 {1,S} {3,S}
3   [Cs,O2s,N,S2s] u0 {2,S} {4,S}
4   [Cs,O2s,N,S2s] u0 {3,S} {5,S}
5   [Cs,O2s,N,S2s] u0 {4,S} {6,S}
6   [Cs,O2s,N,S2s] u0 {1,S} {5,S}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 100,
    label = "SixMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {6,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D,T]}
4   R!H u0 {3,[S,D,T]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D,T]}
6   R!H u0 {1,[S,D]} {5,[S,D,T]}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 55,
    label = "Cycloheptane",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.07536940607541287,
        B = 0.007857340235134768,
        E = 0.1270091040477334,
        L = 0.2000751598597507,
        A = -0.035435642320286925,
    ),
    )


entry(
    index = 101,
    label = "SevenMember",
    group = 
"""
1 * R!H u0 {2,[S,D,T]} {7,[S,D]}
2   R!H u0 {1,[S,D,T]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {1,[S,D]} {6,[S,D]}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 64,
    label = "Cyclononane",
    group = 
"""
1 * Cs u0 {2,S} {9,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {7,S} {9,S}
9   Cs u0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.03241871312630225,
        B = 0.0249540790676415,
        E = 0.2071231931275025,
        L = 0.34690997636354604,
        A = -0.034499761521535666,
    ),
    )


entry(
    index = 103,
    label = "NineMember",
    group = 
"""
1 * R!H u0 {2,[S,D]} {9,[S,D]}
2   R!H u0 {1,[S,D]} {3,[S,D]}
3   R!H u0 {2,[S,D]} {4,[S,D]}
4   R!H u0 {3,[S,D]} {5,[S,D]}
5   R!H u0 {4,[S,D]} {6,[S,D]}
6   R!H u0 {5,[S,D]} {7,[S,D]}
7   R!H u0 {6,[S,D]} {8,[S,D]}
8   R!H u0 {7,[S,D]} {9,[S,D]}
9   R!H u0 {1,[S,D]} {8,[S,D]}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 67,
    label = "Cyclodecane",
    group = 
"""
1  * Cs u0 {2,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.03220052299432791,
        B = -0.033815499316474706,
        E = 0.07925655368738886,
        L = -0.14408339581255702,
        A = -0.025509867196577926,
    ),
    )


entry(
    index = 104,
    label = "TenMember",
    group = 
"""
1  * R!H u0 {2,[S,D]} {10,[S,D]}
2    R!H u0 {1,[S,D]} {3,[S,D]}
3    R!H u0 {2,[S,D]} {4,[S,D]}
4    R!H u0 {3,[S,D]} {5,[S,D]}
5    R!H u0 {4,[S,D]} {6,[S,D]}
6    R!H u0 {5,[S,D]} {7,[S,D]}
7    R!H u0 {6,[S,D]} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {8,[S,D]} {10,[S,D]}
10   R!H u0 {1,[S,D]} {9,[S,D]}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 96,
    label = "Ring",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.01593863857356334,
        B = 0.024796254338229583,
        E = 0.30595778781041433,
        L = 0.5130353952655149,
        A = -0.00016229008871032364,
    ),
    )


entry(
    index = 22,
    label = "Cyclopentene",
    group = 
"""
1   [Cs,N] u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5 * [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.10409942184336726,
        B = -0.08499904437124355,
        E = -0.02094131502769977,
        L = 0.06015850339700404,
        A = 0.03853993644956502,
    ),
    )


entry(
    index = 33,
    label = "Cyclohexene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.05562366114361756,
        B = -0.04172159047860207,
        E = -0.04801575941526171,
        L = -0.020542904591729545,
        A = -0.020903425164558537,
    ),
    )


entry(
    index = 114,
    label = "six-inringonedouble",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 56,
    label = "Cycloheptene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.12684458230165968,
        B = -0.06299444374147731,
        E = 0.10596754881936458,
        L = 0.26239791596318324,
        A = -0.05086567752634101,
    ),
    )


entry(
    index = 60,
    label = "cis-Cyclooctene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.10639917544798011,
        B = -0.06561510580288911,
        E = 0.15273356182630302,
        L = 0.2626642341965212,
        A = -0.05078092762340832,
    ),
    )


entry(
    index = 23,
    label = "Cyclopentadiene",
    group = 
"""
1 * [Cs,N]     u0 {2,S} {5,S}
2   [Cd,N,O,S] u0 {1,S} {3,D}
3   [Cd,N,O,S] u0 {2,D} {4,S}
4   [Cd,N,O,S] u0 {3,S} {5,D}
5   [Cd,N,O,S] u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.0678471257420789,
        B = -0.1763708245983082,
        E = -0.12778932722692277,
        L = -0.41825679455668774,
        A = 0.059004588154677295,
    ),
    )


entry(
    index = 34,
    label = "1,3-Cyclohexadiene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3 * Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.14258415902905558,
        B = -0.007564399448461734,
        E = 0.007909534576216674,
        L = -0.1501467149952843,
        A = -0.034121253638964844,
    ),
    )


entry(
    index = 115,
    label = "six-inringtwodouble-13",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   Cd       u0 {3,S} {5,D}
5   Cd       u0 {4,D} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 35,
    label = "1,4-Cyclohexadiene",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2 * Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.12897740348704892,
        B = -0.05389111383004524,
        E = 0.12529413040635512,
        L = 0.6432076126271216,
        A = -0.0012747977869742404,
    ),
    )


entry(
    index = 116,
    label = "six-inringtwodouble-14",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 57,
    label = "1,3-Cycloheptadiene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.09495975885291277,
        B = -0.04964476230037405,
        E = 0.13430208794982934,
        L = 0.14179770246959778,
        A = -0.04217291179157738,
    ),
    )


entry(
    index = 58,
    label = "1,3,5-Cycloheptatriene",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.0973945915931761,
        B = -0.023550625811318456,
        E = 0.11496748239011065,
        L = -0.034742483930565185,
        A = -0.016927815125554614,
    ),
    )


entry(
    index = 63,
    label = "Cyclooctatetraene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cd u0 {6,S} {8,D}
8   Cd u0 {1,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.3929576215803798,
        B = -0.05738628783014849,
        E = -0.19474502539454433,
        L = -0.7645277060957214,
        A = -0.03096786497337758,
    ),
    )


entry(
    index = 127,
    label = "1,4-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.14215026463429686,
        B = -0.11120188594605417,
        E = -0.013367695150194418,
        L = -0.2833075799999834,
        A = -0.04951754099014411,
    ),
    )


entry(
    index = 31,
    label = "methylenecyclopentane",
    group = 
"""
1 * Cd     u0 {2,S} {3,S} {6,D}
2   [Cs,N] u0 {1,S} {4,S}
3   [Cs,N] u0 {1,S} {5,S}
4   [Cs,N] u0 {2,S} {5,S}
5   [Cs,N] u0 {3,S} {4,S}
6   [Cd,N] u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.0708013707675322,
        B = -0.09160978671035494,
        E = -0.02841845002259209,
        L = 0.04174543846852852,
        A = -0.013022382201393515,
    ),
    )


entry(
    index = 87,
    label = "Cyclohexanone",
    group = 
"""
1 * CO u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.16842177804324174,
        B = 0.07014743266185576,
        E = 0.05495241561635801,
        L = 0.469209808444968,
        A = 0.02144750030841329,
    ),
    )


entry(
    index = 107,
    label = "six-onesidedouble",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 106,
    label = "six-sidedoubles",
    group = 
"""
1   [C,O]   u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [C,O]   u0 {2,S} {4,S}
4   [C,O]   u0 {3,S} {5,S}
5   [C,O]   u0 {4,S} {6,S}
6   [C,O]   u0 {1,S} {5,S}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 69,
    label = "Ethylene_oxide",
    group = 
"""
1 * O2s    u0 {2,S} {3,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.2748857979155336,
        B = -0.125147068293418,
        E = 0.044631047474340796,
        L = 0.3939940792963517,
        A = -0.005151797540875264,
    ),
    )


entry(
    index = 70,
    label = "Oxetane",
    group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [Cs,N,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.2848749290727944,
        B = 0.02193459095942417,
        E = 0.1677195884995452,
        L = 0.531476223727499,
        A = -0.030884902150352382,
    ),
    )


entry(
    index = 71,
    label = "Tetrahydrofuran",
    group = 
"""
1 * O      u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.41631580226566844,
        B = -0.22887562065948722,
        E = -0.06901557077036123,
        L = -0.6766745383388629,
        A = -0.07493063603660387,
    ),
    )


entry(
    index = 73,
    label = "1,3-Dioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2 * Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.3585020515399915,
        B = -0.07509923554451572,
        E = 0.08172483328246231,
        L = 0.27867922958215546,
        A = -0.08720732575238901,
    ),
    )


entry(
    index = 111,
    label = "Oxane",
    group = 
"""
1 * Cs  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   Cs  u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.566261954164156,
        B = -0.30107075028800584,
        E = -0.053700456156689835,
        L = -0.401835980702249,
        A = 0.04091746410845263,
    ),
    )


entry(
    index = 79,
    label = "3,4-Dihydro-2H-pyran",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5 * Cd  u0 {4,S} {6,D}
6   Cd  u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.05755471579605535,
        B = -0.061580718565718784,
        E = 0.08878251803884508,
        L = 0.4150513563037531,
        A = -0.04448875479151691,
    ),
    )


entry(
    index = 74,
    label = "1,4-Dioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3 * O2s u0 {2,S} {4,S}
4   Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.05615017080594915,
        B = -0.08411631842263106,
        E = 0.19008669450209292,
        L = 0.5764326982776424,
        A = -0.023289091124415313,
    ),
    )


entry(
    index = 75,
    label = "1,3,5-Trioxane",
    group = 
"""
1   Cs  u0 {2,S} {6,S}
2   O2s u0 {1,S} {3,S}
3   Cs  u0 {2,S} {4,S}
4 * O2s u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.2972421059044847,
        B = -0.15479774517455264,
        E = -0.0032729860634015118,
        L = 0.187611875791602,
        A = -0.08495835175425234,
    ),
    )


entry(
    index = 86,
    label = "Cyclopentanone",
    group = 
"""
1 * [CO,CS] u0 {2,S} {5,S}
2   [Cs,N]  u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [Cs,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.05832325044430341,
        B = 0.025235853784452478,
        E = -0.03833161407069138,
        L = -0.04377248272295782,
        A = -0.05507431755401619,
    ),
    )


entry(
    index = 88,
    label = "Cycloheptanone",
    group = 
"""
1 * CO u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.07455294582837035,
        B = 0.0844767199654741,
        E = 0.15255005376026803,
        L = 0.5007197235941963,
        A = 6.213118650331972e-05,
    ),
    )


entry(
    index = 89,
    label = "Cyclooctanone",
    group = 
"""
1 * CO u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.07410753897469399,
        B = 0.08185605790405935,
        E = 0.1893160667672074,
        L = 0.5944860418275505,
        A = 0.000146881089434908,
    ),
    )


entry(
    index = 90,
    label = "Cyclononanone",
    group = 
"""
1 * CO u0 {2,S} {9,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {7,S} {9,S}
9   Cs u0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.07366213212101816,
        B = 0.07923539584265006,
        E = 0.20408207977414272,
        L = 0.6392523600608768,
        A = 0.00023163099236588828,
    ),
    )


entry(
    index = 91,
    label = "Cyclodecanone",
    group = 
"""
1  * CO u0 {2,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.07321672526734448,
        B = 0.07661473378123715,
        E = 0.23984809278107913,
        L = 0.6540186782942125,
        A = 0.00031638089529949665,
    ),
    )


entry(
    index = 144,
    label = "thiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [Cd,N] u0 {3,S} {5,D}
5   [Cd,N] u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.17259680166106345,
        B = 0.10742688763276576,
        E = 0.061789455652129836,
        L = 0.35373010175514197,
        A = 0.03201695691065915,
    ),
    )


entry(
    index = 106,
    label = "six-sidedoubles",
    group = 
"""
1   [C,O]   u0 {2,S} {6,S}
2 * [Cd,CO] u0 {1,S} {3,S}
3   [C,O]   u0 {2,S} {4,S}
4   [C,O]   u0 {3,S} {5,S}
5   [C,O]   u0 {4,S} {6,S}
6   [C,O]   u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.08993631674108582,
        B = -0.13190186788337277,
        E = -0.0071916625162875,
        L = -0.12560634349827238,
        A = 0.10719313735532793,
    ),
    )


entry(
    index = 36,
    label = "14methylenecyclohexane",
    group = 
"""
1   Cs u0 {2,S} {6,S}
2 * Cd u0 {1,S} {3,S} {7,D}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,S} {8,D}
6   Cs u0 {1,S} {5,S}
7   Cd u0 {2,D}
8   Cd u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.011841529023841245,
        B = -0.25076600509772073,
        E = 0.05990462229079943,
        L = 0.1900576989668304,
        A = 0.056733447848272195,
    ),
    )


entry(
    index = 108,
    label = "sixmembd-allsingles-twosidedoubles-para",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cs,O2s] u0 {3,S} {5,S}
5   [Cd,CO]  u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 83,
    label = "Beta-Propiolactone",
    group = 
"""
1 * O2s      u0 {2,S} {4,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {2,S} {4,S}
4   [CO,CS]  u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.5441040189504404,
        B = -0.06765365124222136,
        E = 0.14313487168575617,
        L = 1.0214253573429257,
        A = -0.02312482961975349,
    ),
    )


entry(
    index = 25,
    label = "butyrolactone",
    group = 
"""
1 * [CO,CS] u0 {2,S} {5,S}
2   O2s     u0 {1,S} {3,S}
3   [Cs,N]  u0 {2,S} {4,S}
4   [Cs,N]  u0 {3,S} {5,S}
5   [Cs,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.6236897789653552,
        B = 0.06330170983208784,
        E = 0.10574349515195629,
        L = 0.8386967981119787,
        A = -0.009476984005163853,
    ),
    )


entry(
    index = 160,
    label = "oxepane",
    group = 
"""
1 * C   u0 {2,S} {7,S}
2   C   u0 {1,S} {3,S}
3   C   u0 {2,S} {4,S}
4   C   u0 {3,S} {5,S}
5   C   u0 {4,S} {6,S}
6   C   u0 {5,S} {7,S}
7   O2s u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.5186719939641721,
        B = 0.05821332110137197,
        E = 0.277056373052127,
        L = 0.8693563568650418,
        A = -0.032189065769241264,
    ),
    )


entry(
    index = 92,
    label = "Ethyleneimine",
    group = 
"""
1 * N        u0 {2,S} {3,S}
2   [Cs,N,S] u0 {1,S} {3,S}
3   [Cs,N,S] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.4939054479802562,
        B = -0.19712138089891498,
        E = 0.07322932924909024,
        L = 0.4494377104212189,
        A = 0.007131171880321499,
    ),
    )


entry(
    index = 93,
    label = "Azetidine",
    group = 
"""
1 * N          u0 {2,S} {4,S}
2   [Cs,N,O,S] u0 {1,S} {3,S}
3   [Cs,N,O,S] u0 {2,S} {4,S}
4   [Cs,N,O,S] u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.3476966837337231,
        B = -0.1633194191599666,
        E = 0.10913049196346312,
        L = 0.3685913976602828,
        A = 0.09799741694316152,
    ),
    )


entry(
    index = 82,
    label = "2,5-Furandione",
    group = 
"""
1 * O       u0 {2,S} {5,S}
2   [CO,CS] u0 {1,S} {3,S}
3   [Cd,N]  u0 {2,S} {4,D}
4   [Cd,N]  u0 {3,D} {5,S}
5   [CO,CS] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.11042318302386026,
        B = 0.0027213444258589597,
        E = 0.21777591323836065,
        L = 0.34464451578319366,
        A = -0.0019339034076239006,
    ),
    )


entry(
    index = 141,
    label = "thiolane",
    group = 
"""
1 * S     u0 {2,S} {5,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {2,S} {4,S}
4   [C,N] u0 {3,S} {5,S}
5   [C,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.10298326866652409,
        B = -0.10738554814719456,
        E = 0.0020052266427249416,
        L = -0.28864040086599196,
        A = -0.12711103358618253,
    ),
    )


entry(
    index = 54,
    label = "obenzoquinone",
    group = 
"""
1 * CO u0 {5,S} {6,S}
2   Cd u0 {3,D} {6,S}
3   Cd u0 {2,D} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   CO u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.6467634988681339,
        B = 0.0472571744479019,
        E = -0.15960038380567987,
        L = 0.04466298373367933,
        A = -0.03202658403933708,
    ),
    )


entry(
    index = 120,
    label = "six-twoin13-twoout",
    group = 
"""
1   [CO,Cd] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4   Cd      u0 {3,S} {5,D}
5   Cd      u0 {4,D} {6,S}
6 * [Cd,CO] u0 {1,S} {5,S}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 53,
    label = "pbenzoquinone",
    group = 
"""
1 * CO u0 {4,S} {5,S}
2   Cd u0 {5,D} {6,S}
3   Cd u0 {4,D} {6,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {1,S} {2,D}
6   CO u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.5594521513708802,
        B = -0.04531778433266585,
        E = 0.06380032102793379,
        L = 0.17894963625416693,
        A = 0.05683753287177999,
    ),
    )


entry(
    index = 121,
    label = "six-twoin14-twoout",
    group = 
"""
1   [Cd,CO] u0 {2,S} {6,S}
2   Cd      u0 {1,S} {3,D}
3   Cd      u0 {2,D} {4,S}
4 * [Cd,CO] u0 {3,S} {5,S}
5   Cd      u0 {4,S} {6,D}
6   Cd      u0 {1,S} {5,D}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 95,
    label = "Piperidine",
    group = 
"""
1 * N  u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.00516897470462294,
        B = -0.011737431562595615,
        E = 0.06394513276993644,
        L = -0.043773655264726125,
        A = -0.06113306809469965,
    ),
    )


entry(
    index = 94,
    label = "Pyrrolidine",
    group = 
"""
1 * N      u0 {2,S} {5,S}
2   [Cs,N] u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   [Cs,N] u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.07409513083460269,
        B = -0.01682564386639231,
        E = 0.015374166839024886,
        L = 0.006989011887837384,
        A = -0.04943870353830457,
    ),
    )


entry(
    index = 52,
    label = "pxylene",
    group = 
"""
1 * Cd u0 {5,S} {6,S} {7,D}
2   Cd u0 {3,S} {4,S} {8,D}
3   Cd u0 {2,S} {6,D}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {1,S} {4,D}
6   Cd u0 {1,S} {3,D}
7   Cd u0 {1,D}
8   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.3899933652422633,
        B = -0.6769603840679681,
        E = 0.2592829037563838,
        L = -0.01602690516745897,
        A = -0.026382243424323243,
    ),
    )


entry(
    index = 78,
    label = "Furan",
    group = 
"""
1   [Cd,N] u0 {2,D} {5,S}
2   [Cd,N] u0 {1,D} {3,S}
3   [Cd,N] u0 {2,S} {4,D}
4   [Cd,N] u0 {3,D} {5,S}
5 * O      u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.023797546744378006,
        B = -0.10693856303464028,
        E = -0.05224869391248596,
        L = -0.05102689797823956,
        A = -0.057417168148371306,
    ),
    )


entry(
    index = 47,
    label = "14cyclohexadiene3methylene",
    group = 
"""
1   Cd u0 {2,D} {6,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {3,S} {5,D}
5   Cd u0 {4,D} {6,S}
6 * Cd u0 {1,S} {5,S} {7,D}
7   Cd u0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.1980364474644479,
        B = -0.08756885472908012,
        E = 0.24844181250601144,
        L = 0.948739733238454,
        A = 0.05955908972046799,
    ),
    )


entry(
    index = 118,
    label = "six-oneside-twoindoubles-25",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2   Cd       u0 {1,S} {3,D}
3   Cd       u0 {2,D} {4,S}
4 * [Cd,CO]  u0 {3,S} {5,S}
5   Cd       u0 {4,S} {6,D}
6   Cd       u0 {1,S} {5,D}
""",
    thermo = None,
    solute = None,
)


entry(
    index = 77,
    label = "1,3-Dioxolane",
    group = 
"""
1 * [Cs,N] u0 {2,S} {5,S}
2   O      u0 {1,S} {3,S}
3   [Cs,N] u0 {2,S} {4,S}
4   [Cs,N] u0 {3,S} {5,S}
5   O      u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 0.025741931651977405,
        B = -0.008669205248780008,
        E = 0.03907876918914034,
        L = 0.025199427884059905,
        A = -0.07198470107869448,
    ),
    )


entry(
    index = 50,
    label = "fg6",
    group = 
"""
1   Cd u0 {2,S} {3,S} {7,D}
2 * CO u0 {1,S} {5,S}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {3,D} {6,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   Cd u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.34650166890436873,
        B = 0.17206076004019447,
        E = 0.4106858623132792,
        L = 0.4431718719418471,
        A = 0.47169831812901997,
    ),
    )


entry(
    index = 133,
    label = "thiirane",
    group = 
"""
1 * S     u0 {2,S} {3,S}
2   [C,N] u0 {1,S} {3,S}
3   [C,N] u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = -0.060985334933552335,
        B = 0.005521861978623116,
        E = 0.043531990064934245,
        L = -0.2037210620170738,
        A = -0.031039321217803097,
    ),
    )


entry(
    index = 142,
    label = "2,3-dihydrothiophene",
    group = 
"""
1 * S      u0 {2,S} {5,S}
2   [Cd,N] u0 {1,S} {3,D}
3   [Cd,N] u0 {2,D} {4,S}
4   [C,N]  u0 {3,S} {5,S}
5   [C,N]  u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0,0,0,0,0,0,0],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    solute = SoluteData(
        S = 1.0122165268754673,
        B = 0.9042564963633848,
        E = -0.30239516185513526,
        L = 1.4565876190932983,
        A = 0.7294103671734851,
    ),
    )


"""
L1: Ring
	L2: TenMember
		L3: Cyclodecanone
		L3: Cyclodecane
	L2: NineMember
		L3: Cyclononanone
		L3: Cyclononane
	L2: SevenMember
		L3: oxepane
		L3: Cycloheptanone
		L3: 1,3,5-Cycloheptatriene
		L3: 1,3-Cycloheptadiene
		L3: Cycloheptene
		L3: Cycloheptane
	L2: SixMember
		L3: six-oneside-twoindoubles-25
			L4: 14cyclohexadiene3methylene
		L3: six-twoin14-twoout
			L4: pxylene
			L4: pbenzoquinone
		L3: six-twoin13-twoout
			L4: fg6
			L4: obenzoquinone
		L3: six-sidedoubles
			L4: sixmembd-allsingles-twosidedoubles-para
				L5: 14methylenecyclohexane
		L3: six-sidedoubles
			L4: six-onesidedouble
				L5: Cyclohexanone
		L3: six-inringtwodouble-14
			L4: 1,4-Cyclohexadiene
		L3: six-inringtwodouble-13
			L4: 1,3-Cyclohexadiene
		L3: six-inringonedouble
			L4: 3,4-Dihydro-2H-pyran
			L4: Cyclohexene
		L3: sixnosidedouble
			L4: Piperidine
			L4: 1,3,5-Trioxane
			L4: 1,4-Dioxane
			L4: Oxane
			L4: 1,3-Dioxane
			L4: Cyclohexane
	L2: FiveMember
		L3: 2,3-dihydrothiophene
		L3: 1,3-Dioxolane
		L3: Furan
		L3: Pyrrolidine
		L3: thiolane
		L3: 2,5-Furandione
		L3: butyrolactone
		L3: thiophene
		L3: Cyclopentanone
		L3: Tetrahydrofuran
		L3: methylenecyclopentane
		L3: Cyclopentadiene
		L3: Cyclopentene
		L3: Cyclopentane
	L2: FourMember
		L3: Azetidine
		L3: Beta-Propiolactone
		L3: Oxetane
		L3: Cyclobutane
	L2: ThreeMember
		L3: thiirane
		L3: Ethyleneimine
		L3: Ethylene_oxide
		L3: Cyclopropane
	L2: EightMember
		L3: Cyclooctanone
		L3: 1,4-cyclooctadiene
		L3: Cyclooctatetraene
		L3: cis-Cyclooctene
		L3: Cyclooctane
		L3: octasulfur
""",
