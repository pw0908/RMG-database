
name = "Non Atom Centered Platts Groups" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
    index = -3,
    label = "R",
    group = 
"""
1 * R u0
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)
entry(
    index = 8,
    label = "OssH",
    group = 
"""
1 * O2s                 u0 {2,S} {3,S}
2   H                  u0 {1,S}
3   [Cs,Cd,Ct,CO,O2s,H] u0 {1,S}
""",
    solute = SoluteData(
        S = 0,
        B = 0,
        E = 0,
        L = 0,
        A = 0.345,
    ),
    shortDesc = u"""-OH (connected to aliphatic) correction for A""",
    longDesc = 
u"""

""",
)


entry(
    index = 1,
    label = "Oss(CdsOd)",
    group = 
"""
1 * CO                         u0 {2,S} {3,S} {4,D}
2   O2s                        u0 {1,S} {5,S}
3   [Cs,Cd,Cdd,Ct,Cb,Cbf,CO,H] u0 {1,S}
4   O2d                        u0 {1,D}
5   R!H                        u0 {2,S}
""",
    solute = SoluteData(
        S = -0.18745831281722858,
        B = -0.1654960749559993,
        E = -0.11791863732854453,
        L = -0.3631851379372545,
        A = 0.02138550694772676,
    ),
    )


entry(
    index = -2,
    label = "CO",
    group = 
"""
1 * CO u0
""",
    solute = None,
)


entry(
    index = 9,
    label = "OxRing",
    group = "OR{OxR3, OxR4, OxR5, OxR6, OxR7}",
    solute = SoluteData(
        S = -0.19678485547387053,
        B = -0.14381869210034795,
        E = -0.0706881251840469,
        L = -0.2304575644392322,
        A = 0.04521044101932433,
    ),
    )
entry(
    index = 10,
    label = "OxR3",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   R!H u0 {1,S} {3,[S,D,B]}
3   R!H u0 {1,S} {2,[S,D,B]}
""",
    solute = None,
    shortDesc = u"""O in a 3 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "OxR4",
    group = 
"""
1 * O2s  u0 {2,S} {4,S}
2   R!H u0 {1,S} {3,[S,D,B]}
3   R!H u0 {2,[S,D,B]} {4,[S,D,B]}
4   R!H u0 {1,S} {3,[S,D,B]}
""",
    solute = None,
    shortDesc = u"""O in a 4 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "OxR5",
    group = 
"""
1 * O2s  u0 {2,S} {5,S}
2   R!H u0 {1,S} {3,[S,D,B]}
3   R!H u0 {2,[S,D,B]} {4,[S,D,B]}
4   R!H u0 {3,[S,D,B]} {5,[S,D,B]}
5   R!H u0 {1,S} {4,[S,D,B]}
""",
    solute = None,
    shortDesc = u"""O in a 5 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "OxR6",
    group = 
"""
1 * O2s  u0 {2,S} {6,S}
2   R!H u0 {1,S} {3,[S,D,B]}
3   R!H u0 {2,[S,D,B]} {4,[S,D,B]}
4   R!H u0 {3,[S,D,B]} {5,[S,D,B]}
5   R!H u0 {4,[S,D,B]} {6,[S,D,B]}
6   R!H u0 {1,S} {5,[S,D,B]}
""",
    solute = None,
    shortDesc = u"""O in a 6 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "OxR7",
    group = 
"""
1 * O2s  u0 {2,S} {7,S}
2   R!H u0 {1,S} {3,[S,D,B]}
3   R!H u0 {2,[S,D,B]} {4,[S,D,B]}
4   R!H u0 {3,[S,D,B]} {5,[S,D,B]}
5   R!H u0 {4,[S,D,B]} {6,[S,D,B]}
6   R!H u0 {5,[S,D,B]} {7,[S,D,B]}
7   R!H u0 {1,S} {6,[S,D,B]}
""",
    solute = None,
    shortDesc = u"""O in a 7 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Oss(CdsOd)Oss",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   O2s u0 {1,S} {5,S}
3   O2s u0 {1,S} {6,S}
4   O2d u0 {1,D}
5   R!H u0 {2,S}
6   R!H u0 {3,S}
""",
    solute = SoluteData(
        S = -0.27528458890201524,
        B = -0.38576085311976505,
        E = -0.20140636088422806,
        L = -0.5494269951161994,
        A = -0.0478561665359565,
    ),
    )


entry(
    index = 15,
    label = "Lac",
    group = "OR{Lac3, Lac4, Lac5, Lac6}",
    solute = SoluteData(
        S = 0.44986347703082696,
        B = -0.00986265336873121,
        E = -0.0622079088454078,
        L = 0.3780487451157537,
        A = -0.013581901073342168,
    ),
    )
entry(
    index = 16,
    label = "Lac3",
    group = 
"""
1   O2d  u0 {2,D}
2 * CO  u0 {1,D} {3,S} {4,S}
3   O2s  u0 {2,S} {4,S}
4   R!H u0 {2,S} {3,S}
""",
    solute = None,
    shortDesc = u"""lactone, 3 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "Lac4",
    group = 
"""
1   O2d  u0 {2,D}
2 * CO  u0 {1,D} {3,S} {5,S}
3   O2s  u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {2,S} {4,S}
""",
    solute = None,
    shortDesc = u"""lactone, 4 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "Lac5",
    group = 
"""
1   O2d  u0 {2,D}
2 * CO  u0 {1,D} {3,S} {6,S}
3   O2s  u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {4,S} {6,S}
6   R!H u0 {2,S} {5,S}
""",
    solute = None,
    shortDesc = u"""lactone, 5 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "Lac6",
    group = 
"""
1   O2d  u0 {2,D}
2 * CO  u0 {1,D} {3,S} {7,S}
3   O2s  u0 {2,S} {4,S}
4   R!H u0 {3,S} {5,S}
5   R!H u0 {4,S} {6,S}
6   R!H u0 {5,S} {7,S}
7   R!H u0 {2,S} {6,S}
""",
    solute = None,
    shortDesc = u"""lactone, 6 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Cs(OssH)Cs(OssH)",
    group = 
"""
1  * Cs  u0 {2,S} {3,S} {5,S} {6,S}
2    Cs  u0 {1,S} {4,S} {7,S} {8,S}
3    O2s u0 {1,S} {9,S}
4    O2s u0 {2,S} {10,S}
5    R   u0 {1,S}
6    R   u0 {1,S}
7    R   u0 {2,S}
8    R   u0 {2,S}
9    H   u0 {3,S}
10   H   u0 {4,S}
""",
    solute = SoluteData(
        S = -0.009097854024002558,
        B = -0.015619837705317892,
        E = 0.05439541454152819,
        L = 0.03634825604341232,
        A = -0.07160003298357345,
    ),
    )


entry(
    index = 3,
    label = "OssH(CdsOd)",
    group = 
"""
1 * CO                         u0 {2,S} {3,S} {4,D}
2   O2s                        u0 {1,S} {5,S}
3   [Cs,Cd,Cdd,Ct,Cb,Cbf,CO,H] u0 {1,S}
4   O2d                        u0 {1,D}
5   H                          u0 {2,S}
""",
    solute = SoluteData(
        S = -0.20692129507734722,
        B = -0.23632008013304073,
        E = -0.14943455057401264,
        L = -0.29496450594122764,
        A = 0.23503375771297016,
    ),
    )


entry(
    index = 32,
    label = "Cd(O2d)NHR",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   R!H u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.1499671718171346,
        B = -0.047107565257047984,
        E = 0.032367464342344436,
        L = 0.1310999816653118,
        A = 0.168495565334001,
    ),
    )


entry(
    index = 28,
    label = "OsCd(O2d)N",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.12424911004456844,
        B = -0.3866548871190411,
        E = -0.09717542943544817,
        L = -0.1709867998629248,
        A = 0.0052466261355685155,
    ),
    )


entry(
    index = 20,
    label = "Cd(O2d)N",
    group = 
"""
1 * CO        u0 {2,D} {3,S}
2   O2d       u0 {1,D}
3   [N3s,N3d] u0 {1,S}
""",
    solute = SoluteData(S=0.175,B=-0.287,E=0.0,L=0.603,A=0.0,comment=''),
)


entry(
    index = 36,
    label = "CdsNdNsNs",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S} {5,S} {6,S}
3   N3s u0 {1,S} {7,S} {8,S}
4   N3d u0 {1,D} {9,S}
5   H   u0 {2,S}
6   H   u0 {2,S}
7   H   u0 {3,S}
8   H   u0 {3,S}
9   H   u0 {4,S}
""",
    solute = SoluteData(
        S = -0.4764202436753729,
        B = 0.14172120167569904,
        E = -0.035197217822289656,
        L = -0.32102044835597143,
        A = 0.007925819678510462,
    ),
    )


entry(
    index = 31,
    label = "Cd(O2d)NH2",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.08458690263045343,
        B = -0.006849159246660675,
        E = -0.04414021956008543,
        L = 0.08854082823360776,
        A = 0.2338625634801933,
    ),
    )


entry(
    index = 20,
    label = "Cd(O2d)N",
    group = 
"""
1 * CO        u0 {2,D} {3,S}
2   O2d       u0 {1,D}
3   [N3s,N3d] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10740464080507939,
        B = -0.030374539919852925,
        E = -0.005927682503613982,
        L = 0.174268684479367,
        A = 0.029680717717300152,
    ),
    )


entry(
    index = 34,
    label = "N3sHCd(O2d)N3sH",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * N3s u0 {1,S} {5,S}
3   N3s u0 {1,S} {6,S}
4   O2d u0 {1,D}
5   H   u0 {2,S}
6   H   u0 {3,S}
""",
    solute = SoluteData(
        S = -0.052660359597488805,
        B = 0.10166363427135142,
        E = -0.05514005008546953,
        L = -0.09301350951203725,
        A = 0.09127756149576456,
    ),
    )


entry(
    index = 27,
    label = "NCd(O2d)N",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   N3s u0 {1,S}
4   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.011778374572329182,
        B = -0.47505773704744547,
        E = 0.019790841568688967,
        L = 0.060408502430625455,
        A = 0.1031455337552854,
    ),
    )


entry(
    index = 35,
    label = "N3sCd(O2d)N3sH",
    group = 
"""
1   CO  u0 {2,S} {3,S} {4,D}
2 * N3s u0 {1,S} {5,S} {6,S}
3   N3s u0 {1,S} {7,S}
4   O2d u0 {1,D}
5   R!H u0 {2,S}
6   R!H u0 {2,S}
7   H   u0 {3,S}
""",
    solute = SoluteData(
        S = -0.12755866010107894,
        B = 0.2346184682098787,
        E = -0.04472915030393574,
        L = -0.16508546566858193,
        A = -0.14619997325700002,
    ),
    )


entry(
    index = 29,
    label = "Cd(O2d)NCd(O2d)",
    group = 
"""
1   N3s u0 {2,S} {3,S}
2 * CO  u0 {1,S} {4,D}
3   CO  u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.188435654042587,
        B = -0.14162183268517536,
        E = -0.01665481870733418,
        L = -0.16162480665781542,
        A = 0.014224322462721402,
    ),
    )


entry(
    index = 5,
    label = "Cd(O2d)Cd=CdCd(O2d)",
    group = 
"""
1    Cd  u0 {2,D} {3,S} {5,S}
2    Cd  u0 {1,D} {4,S} {6,S}
3  * CO  u0 {1,S} {7,D} {8,S}
4    CO  u0 {2,S} {9,S} {10,D}
5    R   u0 {1,S}
6    R   u0 {2,S}
7    O2d u0 {3,D}
8    R   u0 {3,S}
9    R   u0 {4,S}
10   O2d u0 {4,D}
""",
    solute = SoluteData(
        S = -0.2546460545733042,
        B = -0.03246011307988197,
        E = -0.04764880419066146,
        L = -0.2847367179203103,
        A = -0.10205314214251797,
    ),
    )


entry(
    index = 26,
    label = "SdOdOdN",
    group = 
"""
1 * S6dd u0 {2,D} {3,D} {4,S}
2   O2d  u0 {1,D}
3   O2d  u0 {1,D}
4   N    u0 {1,S}
""",
    solute = SoluteData(
        S = -0.20757185966535377,
        B = -0.15588999800831915,
        E = 0.05795001896957059,
        L = -0.15238110856359802,
        A = 0.0959737691634327,
    ),
    )


entry(
    index = 21,
    label = "Lactam",
    group = "OR{Lactam4, Lactam5, Lactam6, Lactam7}",
    solute = SoluteData(
        S = -0.04248341838358793,
        B = 0.04766841357601884,
        E = -0.018087155908026516,
        L = -0.23726176404473398,
        A = -0.1330606891005969,
    ),
    )
entry(
    index = 22,
    label = "Lactam4",
    group = 
"""
1   O2d u0 {2,D}
2 * CO u0 {1,D} {3,S} {5,S}
3   N  u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {2,S} {4,S}
""",
    solute = None,
    shortDesc = u"""lactam, 4 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "Lactam5",
    group = 
"""
1   O2d u0 {2,D}
2 * CO u0 {1,D} {3,S} {6,S}
3   N  u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {2,S} {5,S}
""",
    solute = None,
    shortDesc = u"""lactam, 5 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Lactam6",
    group = 
"""
1   O2d u0 {2,D}
2 * CO u0 {1,D} {3,S} {7,S}
3   N  u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {2,S} {6,S}
""",
    solute = None,
    shortDesc = u"""lactam, 6 membered ring""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "Lactam7",
    group = 
"""
1   O2d u0 {2,D}
2 * CO u0 {1,D} {3,S} {8,S}
3   N  u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {2,S} {7,S}
""",
    solute = None,
    shortDesc = u"""lactam, 7 membered ring""",
    longDesc = 
u"""

""",
)
tree(
"""
L1: R
	L2: SdOdOdN
	L2: N3sCd(O2d)N3sH
	L2: N3sHCd(O2d)N3sH
	L2: Cd(O2d)NH2
	L2: CdsNdNsNs
	L2: Cd(O2d)NHR
	L2: Cs(OssH)Cs(OssH)
	L2: OxRing
	L2: CO
		L3: Lactam
		L3: Cd(O2d)Cd=CdCd(O2d)
		L3: Cd(O2d)N
			L4: Cd(O2d)NCd(O2d)
			L4: NCd(O2d)N
		L3: Cd(O2d)N
			L4: OsCd(O2d)N
		L3: OssH(CdsOd)
		L3: Lac
		L3: Oss(CdsOd)Oss
		L3: Oss(CdsOd)
	L2: OssH
"""
)