
name = "Abraham Solute Descriptors" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
    index = 30,
    label = "O2d",
    group = 
"""
1 * O2d u0
""",
    solute = SoluteData(
        S = 0.30655023327431585,
        B = 0.2450998927778984,
        E = -0.064471412193714,
        L = 0.500175538536143,
        A = -0.013565423644882486,
    ),
    )


entry(
    index = -4,
    label = "O",
    group = 
"""
1 * [O2s,O2d,O4tc] u0
""",
    solute = None,
)


entry(
    index = 57,
    label = "Cdd",
    group = 
"""
1 * Cdd u0
""",
    solute = SoluteData(
        S = -0.07012517229075227,
        B = -0.18403832831087039,
        E = 0.04795501317604041,
        L = 0.3833482077884118,
        A = -0.008885345698685642,
    ),
    )


entry(
    index = -2,
    label = "C",
    group = 
"""
1 * C u0
""",
    solute = None,
)


entry(
    index = 26,
    label = "OssH",
    group = 
"""
1 * O2s u0 {2,S}
2   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.031940075618920254,
        B = 0.27425596985399037,
        E = -0.03315983377098718,
        L = 0.5256741866798154,
        A = 0.3066600530732876,
    ),
    )


entry(
    index = -10,
    label = "Oss",
    group = 
"""
1 * O2s u0
""",
    solute = None,
)


entry(
    index = 31,
    label = "S2s",
    group = 
"""
1 * S2s u0 p2
""",
    solute = SoluteData(
        S = 0.13888640358973,
        B = 0.0808233295375245,
        E = 0.289882867136059,
        L = 1.1201123529578658,
        A = -0.015406642328084167,
    ),
    )


entry(
    index = 36,
    label = "S",
    group = 
"""
1 * S u0
""",
    solute = SoluteData(S=0.643,B=0.0,E=0.465,L=0.554,A=0,comment=''),
)


entry(
    index = 36,
    label = "S",
    group = 
"""
1 * S u0
""",
    solute = SoluteData(
        S = 0.32556970979000777,
        B = -0.07729266861698503,
        E = 0.3201119475716309,
        L = 1.21372869384724,
        A = 0.09127567293414228,
    ),
    )


entry(
    index = 33,
    label = "S2d",
    group = 
"""
1 * S2d u0 p2
""",
    solute = SoluteData(
        S = 0.18230871855612946,
        B = 0.1497778478446204,
        E = 0.33012010445460466,
        L = 1.241874721049742,
        A = -0.019451044818589877,
    ),
    )


entry(
    index = 10,
    label = "N3sH2",
    group = 
"""
1 * N3s u0 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.1799872176350086,
        B = 0.34761759628843675,
        E = 0.12090581815853127,
        L = 0.9017070860826646,
        A = 0.17618213409109196,
    ),
    )


entry(
    index = -7,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    solute = None,
)


entry(
    index = -8,
    label = "N",
    group = 
"""
1 * N u0
""",
    solute = None,
)


entry(
    index = 18,
    label = "N3d",
    group = 
"""
1 * N3d u0
""",
    solute = SoluteData(
        S = 0.09540210269413013,
        B = 0.15475802190247812,
        E = 0.10253019931287417,
        L = 0.5094671478390581,
        A = -0.004025937282096531,
    ),
    )


entry(
    index = 21,
    label = "N3t",
    group = 
"""
1 * N3t u0 {2,T}
2   Ct  u0 {1,T}
""",
    solute = SoluteData(
        S = 0.41942754850507785,
        B = 0.12996717571463925,
        E = -0.053179650015117444,
        L = 0.6414077320419165,
        A = 0.009525467827677336,
    ),
    )


entry(
    index = 9,
    label = "Ct",
    group = 
"""
1 * Ct u0
""",
    solute = SoluteData(
        S = 0.09054377701381834,
        B = 0.06779220695210324,
        E = 0.059249276024227075,
        L = 0.5625714500601018,
        A = 0.026853664524230055,
    ),
    )


entry(
    index = 1,
    label = "CssH3",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   R  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.12633681895852264,
        B = 0.00904266239959729,
        E = -0.14120704548650745,
        L = 0.3541704427345205,
        A = -0.009161394692630257,
    ),
    )


entry(
    index = -1,
    label = "Css",
    group = 
"""
1 * Cs u0
""",
    solute = None,
)


entry(
    index = 2,
    label = "CssH2",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   R!H u0 {1,S}
5   R!H u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0008218580088242796,
        B = 0.008036814164325412,
        E = -0.003306193768717802,
        L = 0.5009986577796668,
        A = -0.001138371393547164,
    ),
    )


entry(
    index = 3,
    label = "CssH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   H   u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
5   R!H u0 {1,S}
""",
    solute = SoluteData(
        S = 0.09161764675201409,
        B = 0.053653674278718914,
        E = 0.138299052564778,
        L = 0.5672983721568636,
        A = -0.015232166346925464,
    ),
    )


entry(
    index = 4,
    label = "Css-noH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
5   R!H u0 {1,S}
""",
    solute = SoluteData(
        S = 0.26195494701957944,
        B = 0.11205831745454553,
        E = 0.25078818585736296,
        L = 0.5999979405163025,
        A = 0.021892946144118488,
    ),
    )


entry(
    index = 27,
    label = "Oss-noncyclic",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
""",
    solute = SoluteData(
        S = 0.19283657066793608,
        B = 0.2720479693900289,
        E = 0.023541354142276993,
        L = 0.4207372890019638,
        A = -0.017394966675148473,
    ),
    )


entry(
    index = 7,
    label = "Cds-noH",
    group = 
"""
1 * [Cd,CO] u0 {2,S} {3,S} {4,D}
2   R!H     u0 {1,S}
3   R!H     u0 {1,S}
4   R!H     u0 {1,D}
""",
    solute = SoluteData(
        S = 0.12305268939475882,
        B = -0.015102189174575856,
        E = 0.21207528074650428,
        L = 0.6212526657394501,
        A = 0.004710321496376734,
    ),
    )


entry(
    index = 0,
    label = "Cds",
    group = 
"""
1 * [Cd,CO] u0
""",
    solute = None,
)


entry(
    index = 5,
    label = "CdsH2",
    group = 
"""
1 * [Cd,CO] u0 {2,S} {3,S} {4,D}
2   H       u0 {1,S}
3   H       u0 {1,S}
4   R!H     u0 {1,D}
""",
    solute = SoluteData(
        S = -0.15615100948556343,
        B = 0.011261279236724382,
        E = -0.07105873885359572,
        L = 0.3046587954655304,
        A = -0.01653405277728295,
    ),
    )


entry(
    index = 6,
    label = "CdsH",
    group = 
"""
1 * [Cd,CO] u0 {2,S} {3,S} {4,D}
2   H       u0 {1,S}
3   R!H     u0 {1,S}
4   R!H     u0 {1,D}
""",
    solute = SoluteData(
        S = 0.033081717487341816,
        B = 0.025575033125849928,
        E = 0.06573784124381597,
        L = 0.5200146888569882,
        A = 0.001313681642588929,
    ),
    )


entry(
    index = 15,
    label = "N3s-noH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
""",
    solute = SoluteData(
        S = 0.27954329518653837,
        B = 0.4106445500930877,
        E = 0.26248972318702835,
        L = 0.7582872954562664,
        A = -0.030917163615546105,
    ),
    )


entry(
    index = 12,
    label = "N3sH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   R!H u0 {1,S}
4   R!H u0 {1,S}
""",
    solute = SoluteData(
        S = 0.18973449257511332,
        B = 0.3623710778767924,
        E = 0.1335002573058265,
        L = 0.8062840509267878,
        A = 0.1480105660167663,
    ),
    )


entry(
    index = 34,
    label = "S4d",
    group = 
"""
1 * S4d u0 p1 {2,S} {3,S}
2   R   u0 {1,S}
3   R   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.7651916583472896,
        B = 0.44984742552508306,
        E = 0.5128505932362812,
        L = 1.9104318098284054,
        A = 0.04569871336129165,
    ),
    )


entry(
    index = 35,
    label = "S6dd-OdOdOR",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  u0 p2 {1,D}
3   O2d  u0 p2 {1,D}
4   O2s  u0 p2 {1,S}
5   R    u0 {1,S}
""",
    solute = SoluteData(
        S = 0.4432472235779724,
        B = -0.17024401439724943,
        E = 0.2978980041741218,
        L = 1.1476962316697497,
        A = -0.01169820571103057,
    ),
    )

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
tree(
"""
L1: R
	L2: N
		L3: N3t
		L3: N3d
		L3: N3s
			L4: N3sH
			L4: N3s-noH
			L4: N3sH2
	L2: S
		L3: S6dd-OdOdOR
		L3: S4d
		L3: S2d
		L3: S2s
	L2: C
		L3: Cds
			L4: CdsH
			L4: CdsH2
			L4: Cds-noH
		L3: Css
			L4: Css-noH
			L4: CssH
			L4: CssH2
			L4: CssH3
		L3: Ct
		L3: Cdd
	L2: O
		L3: Oss
			L4: Oss-noncyclic
			L4: OssH
		L3: O2d
""")