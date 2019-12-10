name = "Functional Group Additivity Values" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
    index = -1,
    label = "R",
    group = 
"""
1 * R ux
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1093,
    label = "O",
    group = 
"""
1 * O u0
""",
    solute = SoluteData(
        S = 0.17474024464254836,
        B = 0.24510026073262686,
        E = 0.057622482072578377,
        L = 0.5184526068838221,
        A = 0.311792904762241,
    ),
    )


entry(
    index = 1094,
    label = "O2d",
    group = 
"""
1 * O2d u0
""",
    solute = SoluteData(
        S = 0.09712570517971927,
        B = -0.04667503477914288,
        E = -0.16765545805721072,
        L = -0.10718338952215001,
        A = -0.14293844382567344,
    ),
    )


entry(
    index = 35,
    label = "Cdd-OdOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   O2d u0 {1,D}
3   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = -0.29089971992880675,
        B = 0.1446020234012803,
        E = 0.31527439725819306,
        L = 0.3614116150788995,
        A = 0.19436461319422368,
    ),
    )


entry(
    index = 34,
    label = "Cdd",
    group = 
"""
1 * Cdd u0
""",
    solute = u"Cdd-CdsCds",
)


entry(
    index = 1,
    label = "C",
    group = 
"""
1 * C u0
""",
    solute = u"Cs-CsCsCsCs",
)


entry(
    index = 1099,
    label = "O2s-OsH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.19757592311839944,
        B = 0.14358375330901088,
        E = 0.21864463322912153,
        L = 0.7246988102227039,
        A = 0.33482846159623697,
    ),
    )


entry(
    index = 1097,
    label = "O2s",
    group = 
"""
1 * O2s u0
""",
    solute = u"O2s-(Cds-Cd)(Cds-Cd)",
)


entry(
    index = 2029,
    label = "S4dd",
    group = 
"""
1 * S4dd u0
""",
    solute = SoluteData(
        S = 0.08759242663831689,
        B = -0.009961213572676712,
        E = 0.21301321850392785,
        L = 0.9479829033380569,
        A = 0.0032367121209344336,
    ),
    )


entry(
    index = 1400,
    label = "S",
    group = 
"""
1 * S ux
""",
    solute = u"S2s-CsCs",
)


entry(
    index = 2011,
    label = "S4dd-OdOd",
    group = 
"""
1 * S4dd u0 p1 {2,D} {3,D}
2   O2d  ux p2 {1,D}
3   O2d  ux p2 {1,D}
""",
    solute = SoluteData(
        S = 0.11304513598666677,
        B = -0.4086088465564136,
        E = -0.12901771982510019,
        L = -0.7449415507848307,
        A = 0.2947166951702199,
    ),
    )


entry(
    index = 2024,
    label = "O2d-Sd",
    group = 
"""
1 * O2d u0 {2,D}
2   S   ux {1,D}
""",
    solute = SoluteData(
        S = 0.08515327722199316,
        B = 0.22993040019972177,
        E = 0.23949060048443763,
        L = 0.8059931934097169,
        A = -0.07811448481365166,
    ),
    )


entry(
    index = 1160,
    label = "S2d-C",
    group = 
"""
1 * S2d u0 {2,D}
2   C   u0 {1,D}
""",
    solute = SoluteData(
        S = 0.32080739979060874,
        B = 0.034474252071277585,
        E = 0.26995010700892624,
        L = 1.0672381975676606,
        A = -0.06818128502819976,
    ),
    )


entry(
    index = -1,
    label = "S2d",
    group = 
"""
1 * S2d u0
""",
    solute = None,
)


entry(
    index = 1466,
    label = "Cdd-OdSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   O2d u0 {1,D}
3   S2d u0 {1,D}
""",
    solute = SoluteData(
        S = -0.5145814145396542,
        B = -0.03654726344911728,
        E = 0.3646688321920818,
        L = 0.2659900279891605,
        A = 0.06960745439677776,
    ),
    )


entry(
    index = 1811,
    label = "N3s-N3sHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.43892639278724266,
        B = 0.26862292940798693,
        E = 0.2189081306486821,
        L = 0.9638901582625524,
        A = 0.11742506563941452,
    ),
    )


entry(
    index = 1888,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    solute = u"N3s-CsHH",
)


entry(
    index = 1887,
    label = "N",
    group = 
"""
1 * N u0
""",
    solute = u"N3s",
)


entry(
    index = 1400,
    label = "S",
    group = 
"""
1 * S ux
""",
    solute = SoluteData(
        S = 0.4529229379146193,
        B = -0.10565530691927981,
        E = 0.37014612422486964,
        L = 1.4733823363855207,
        A = -0.05505933829872851,
    ),
    )


entry(
    index = 1887,
    label = "N",
    group = 
"""
1 * N u0
""",
    solute = SoluteData(
        S = 0.05492717100016502,
        B = 0.07288583310062678,
        E = 0.029446765643455972,
        L = 0.3447831868143331,
        A = 0.032384737330761464,
    ),
    )


entry(
    index = 1920,
    label = "N3t-CtH",
    group = 
"""
1 * N3t u0 p1 {2,T}
2   Ct  u0 {1,T} {3,S}
3   H   u0 {2,S}
""",
    solute = SoluteData(
        S = -0.11998491263243677,
        B = -0.45072019120622386,
        E = 0.18799533839692384,
        L = -0.2776007607130251,
        A = -0.27590852606326965,
    ),
    )


entry(
    index = 1919,
    label = "N3t",
    group = 
"""
1 * N3t u0 p1 {2,T}
2   R!H u0 {1,T}
""",
    solute = None,
)


entry(
    index = 20,
    label = "Ct",
    group = 
"""
1 * Ct u0
""",
    solute = SoluteData(
        S = 0.40333660306310115,
        B = 0.5419721450492493,
        E = 0.004968142746888298,
        L = 1.195545596747779,
        A = 0.514396251606174,
    ),
    )


entry(
    index = 332,
    label = "Cs-CsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.15559127173847193,
        B = -0.007394552109665074,
        E = -0.018496361241801377,
        L = 0.30049166582142917,
        A = -0.06262055930322875,
    ),
    )


entry(
    index = 331,
    label = "Cs-CHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = u"Cs-CsHHH",
)


entry(
    index = 329,
    label = "Cs",
    group = 
"""
1 * Cs u0
""",
    solute = u"Cs-CsCsCsCs",
)


entry(
    index = 346,
    label = "Cs-CsCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0013230223081476438,
        B = 0.0019299454648373069,
        E = -0.0016820040114119523,
        L = 0.503133640544118,
        A = 0.00030753594481087933,
    ),
    )


entry(
    index = 345,
    label = "Cs-CCHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = u"Cs-CsCsHH",
)


entry(
    index = 390,
    label = "Cs-CsCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.15743689062429433,
        B = 0.02534745655770116,
        E = 0.02001394140883743,
        L = 0.6402840790843334,
        A = 0.0431482592082537,
    ),
    )


entry(
    index = 389,
    label = "Cs-CCCH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = u"Cs-CsCsCsH",
)


entry(
    index = 520,
    label = "Cs-CsCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2552765401150035,
        B = 0.04960204354868436,
        E = 0.02151979506678784,
        L = 0.7401586600837752,
        A = 0.17186664293438503,
    ),
    )


entry(
    index = 519,
    label = "Cs-CCCC",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
    solute = u"Cs-CsCsCsCs",
)


entry(
    index = 1808,
    label = "N3s-CsHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03329079208927007,
        B = 0.337691099112622,
        E = 0.19876331103608683,
        L = 0.7271609359616406,
        A = 0.21927923648263742,
    ),
    )


entry(
    index = 1938,
    label = "N3s-CHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1804,
    label = "Cs-N3sCsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5240374171398738,
        B = 0.1680542988093538,
        E = 0.00127483569905993,
        L = 0.9038117922986748,
        A = -0.02190402374347701,
    ),
    )


entry(
    index = 1930,
    label = "Cs-NCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1127,
    label = "O2s-Cs(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.3214127092085912,
        B = 0.042138316295172853,
        E = 0.18896392297812725,
        L = 0.16799065487900477,
        A = -0.1340513536899093,
    ),
    )


entry(
    index = 1126,
    label = "O2s-CdsCs",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
""",
    solute = u"O2s-Cs(Cds-Cd)",
)


entry(
    index = 1115,
    label = "O2s-CC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    solute = u"O2s-(Cds-Cd)(Cds-Cd)",
)


entry(
    index = 1095,
    label = "O2d-Cd",
    group = 
"""
1 * O2d u0 {2,D}
2   CO  u0 {1,D}
""",
    solute = SoluteData(
        S = 0.2349494729074858,
        B = 0.09313214206620302,
        E = -0.02925538388400748,
        L = 0.28119155062254264,
        A = -0.0015934048511310438,
    ),
    )


entry(
    index = 394,
    label = "Cs-(Cds-Cds)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.12121308323858795,
        B = 0.1421758539173969,
        E = 0.08265186039027814,
        L = 0.6881718665008474,
        A = 0.0650185003190027,
    ),
    )


entry(
    index = 393,
    label = "Cs-(Cds-Cd)CsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = u"Cs-(Cds-Cds)CsCsH",
)


entry(
    index = 391,
    label = "Cs-CdsCsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)CsCsH",
)


entry(
    index = 1039,
    label = "Cs-CsCsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5104186606170619,
        B = 0.06065578867219075,
        E = -0.18223111109557943,
        L = 0.7032764165537895,
        A = 0.1119429929471637,
    ),
    )


entry(
    index = 1038,
    label = "Cs-CCOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = u"Cs-CsCsOsH",
)


entry(
    index = 334,
    label = "Cs-(Cds-O2d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.04335002561198516,
        B = 0.09474295641009392,
        E = 0.025643800105327914,
        L = 0.4312627565187697,
        A = -0.033318851531181734,
    ),
    )


entry(
    index = 333,
    label = "Cs-CdsHHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)HHH",
)


entry(
    index = 201,
    label = "Cds-CdsCsCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08980125291079233,
        B = -0.09054562299036721,
        E = -0.04143624400967874,
        L = 0.5133599027973436,
        A = 0.026843432478263672,
    ),
    )


entry(
    index = 200,
    label = "Cds-CdCC",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    solute = u"Cds-CdsCsCs",
)


entry(
    index = 50,
    label = "Cds",
    group = 
"""
1 * [Cd,CO,CS] u0
""",
    solute = u"Cds-CdsCsCs",
)


entry(
    index = 66,
    label = "Cds-OdCsOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08859783971057807,
        B = 0.13992759984078837,
        E = 0.07517080819963837,
        L = 0.5804945723941599,
        A = 0.03560203386204147,
    ),
    )


entry(
    index = 65,
    label = "Cds-OdCOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = u"Cds-OdCsOs",
)


entry(
    index = 121,
    label = "Cds-CdsHH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.12128984822076137,
        B = -0.008262156909609058,
        E = 0.044108654215937196,
        L = 0.2667819585276463,
        A = -0.06330401585650533,
    ),
    )


entry(
    index = 120,
    label = "Cds-CdHH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = u"Cds-CdsHH",
)


entry(
    index = 336,
    label = "Cs-(Cds-Cds)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = -0.11164901689978177,
        B = 0.06237846997528179,
        E = 0.0649399151169382,
        L = 0.4118352713142143,
        A = -0.046064276645476146,
    ),
    )


entry(
    index = 335,
    label = "Cs-(Cds-Cd)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = u"Cs-(Cds-Cds)HHH",
)


entry(
    index = 136,
    label = "Cds-CdsCsH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.01713599223928216,
        B = -0.040623111450428386,
        E = 0.002871615337235277,
        L = 0.492180562534636,
        A = -0.013752600407536082,
    ),
    )


entry(
    index = 135,
    label = "Cds-CdCH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = u"Cds-CdsCsH",
)


entry(
    index = 350,
    label = "Cs-(Cds-Cds)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.0005969498232066221,
        B = 0.08662566646601959,
        E = 0.06045074613144029,
        L = 0.5271476506624828,
        A = -0.005147310510834684,
    ),
    )


entry(
    index = 349,
    label = "Cs-(Cds-Cd)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = u"Cs-(Cds-Cds)CsHH",
)


entry(
    index = 347,
    label = "Cs-CdsCsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)CsHH",
)


entry(
    index = 524,
    label = "Cs-(Cds-Cds)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.33281755422911485,
        B = 0.1587102396373982,
        E = 0.09669804782583144,
        L = 0.6893772188442913,
        A = 0.1918333025833604,
    ),
    )


entry(
    index = 523,
    label = "Cs-(Cds-Cd)CsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    solute = u"Cs-(Cds-Cds)CsCsCs",
)


entry(
    index = 521,
    label = "Cs-CdsCsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)CsCsCs",
)


entry(
    index = 122,
    label = "Cds-CddHH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.04404586706620807,
        B = -0.007169034608233742,
        E = 0.06529941615676567,
        L = 0.2994425790691605,
        A = -0.05421430540979391,
    ),
    )


entry(
    index = 49,
    label = "Cdd-CdsCds",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   Cd  u0 {1,D}
""",
    solute = SoluteData(
        S = -0.018556575436920093,
        B = 0.015590023059492855,
        E = 0.08403131549693166,
        L = 0.6571596778963877,
        A = -0.03308366363750398,
    ),
    )


entry(
    index = 41,
    label = "Cdd-CdCd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   C   u0 {1,D}
""",
    solute = u"Cdd-CdsCds",
)


entry(
    index = 335,
    label = "Cs-(Cds-Cd)HHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = SoluteData(
        S = -0.05834148344160012,
        B = 0.022437616685434335,
        E = 0.05005631693658533,
        L = 0.4128694604715554,
        A = -0.032158529651459725,
    ),
    )


entry(
    index = 135,
    label = "Cds-CdCH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.025704383624615523,
        B = 0.01039334870632697,
        E = 0.06924309922017555,
        L = 0.4765731185975736,
        A = -0.022055775758336844,
    ),
    )


entry(
    index = 200,
    label = "Cds-CdCC",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   C  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.032637099816992136,
        B = 0.027955732020894603,
        E = 0.03352011561692331,
        L = 0.53830365812604,
        A = 0.010102753893123536,
    ),
    )


entry(
    index = 140,
    label = "Cds-Cds(Cds-Cds)H",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.06663680324030051,
        B = 0.03337813549347835,
        E = 0.09941510893294418,
        L = 0.6019639557870144,
        A = 0.0001315690394805935,
    ),
    )


entry(
    index = 139,
    label = "Cds-Cds(Cds-Cd)H",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   H  u0 {1,S}
5   C  u0 {2,D}
""",
    solute = u"Cds-Cds(Cds-Cds)H",
)


entry(
    index = 137,
    label = "Cds-CdsCdsH",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    solute = u"Cds-Cds(Cds-Cds)H",
)


entry(
    index = 205,
    label = "Cds-Cds(Cds-Cds)Cs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.17684228444877859,
        B = 0.025727635433794385,
        E = 0.022027902060207542,
        L = 0.6515719627759804,
        A = 0.055542433917988396,
    ),
    )


entry(
    index = 204,
    label = "Cds-Cds(Cds-Cd)Cs",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cs u0 {1,S}
5   C  u0 {2,D}
""",
    solute = u"Cds-Cds(Cds-Cds)Cs",
)


entry(
    index = 202,
    label = "Cds-CdsCdsCs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    solute = u"Cds-Cds(Cds-Cds)Cs",
)


entry(
    index = 349,
    label = "Cs-(Cds-Cd)CsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.09791129945095361,
        B = 0.043867196062685444,
        E = 0.08622701351743245,
        L = 1.1403109743780888,
        A = 0.030308261679366587,
    ),
    )


entry(
    index = 362,
    label = "Cs-(Cds-Cds)(Cds-Cds)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = 0.0017912249982516698,
        B = 0.213996690540214,
        E = 0.13961200144081773,
        L = 0.5384753646119643,
        A = 0.03352678939030613,
    ),
    )


entry(
    index = 361,
    label = "Cs-(Cds-Cd)(Cds-Cd)HH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)HH",
)


entry(
    index = 354,
    label = "Cs-CdsCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)HH",
)


entry(
    index = 408,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = 0.21337321953455549,
        B = 0.20853190836323687,
        E = 0.13190909500013606,
        L = 0.294622058384309,
        A = 0.0854325455555802,
    ),
    )


entry(
    index = 407,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)CsH",
)


entry(
    index = 400,
    label = "Cs-CdsCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)CsH",
)


entry(
    index = 21,
    label = "Ct-CtH",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0032885652029266826,
        B = 0.03934498047076042,
        E = 0.06894534156297874,
        L = 0.36154073776925616,
        A = 0.007191683325840503,
    ),
    )


entry(
    index = 340,
    label = "Cs-CtHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.18482422875782065,
        B = 0.03466143291531956,
        E = 0.1293358178464183,
        L = 0.5295010907501086,
        A = -0.12840243193500175,
    ),
    )


entry(
    index = 24,
    label = "Ct-CtCs",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.11510711368915896,
        B = 0.04025017130003471,
        E = -0.029048476460015155,
        L = 0.3923708089007957,
        A = 0.06588069383495268,
    ),
    )


entry(
    index = 23,
    label = "Ct-CtC",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   C  u0 {1,S}
""",
    solute = u"Ct-CtCs",
)


entry(
    index = 370,
    label = "Cs-CtCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.024921491113949507,
        B = 0.023575902315251654,
        E = 0.13724966776817138,
        L = 0.6428979944631802,
        A = -0.05401751682611425,
    ),
    )


entry(
    index = 144,
    label = "Cds-CdsCtH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.19278701244019592,
        B = 0.20526595168516465,
        E = 0.026179939865519183,
        L = 1.027071130180508,
        A = 0.12720480836267972,
    ),
    )


entry(
    index = 28,
    label = "Ct-Ct(Cds-Cds)",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cd u0 {1,S} {4,D}
4   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = -0.07682843692045434,
        B = -0.1521216185638971,
        E = 0.12530042629222132,
        L = 0.07546566535880217,
        A = -0.11424649384559822,
    ),
    )


entry(
    index = 27,
    label = "Ct-Ct(Cds-Cd)",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cd u0 {1,S} {4,D}
4   C  u0 {3,D}
""",
    solute = u"Ct-Ct(Cds-Cds)",
)


entry(
    index = 25,
    label = "Ct-CtCds",
    group = 
"""
1 * Ct         u0 {2,T} {3,S}
2   Ct         u0 {1,T}
3   [Cd,CO,CS] u0 {1,S}
""",
    solute = u"Ct-Ct(Cds-Cds)",
)


entry(
    index = 32,
    label = "Ct-CtCt",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Ct u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0649644104182592,
        B = 0.021280996450751676,
        E = 0.12953639900891997,
        L = 0.642981680248103,
        A = 0.007052179445612332,
    ),
    )


entry(
    index = 1129,
    label = "O2s-CsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.6840599264023391,
        B = 0.24949106144471167,
        E = 0.44263397785066805,
        L = 0.17405741130637037,
        A = -0.15350288946220775,
    ),
    )


entry(
    index = 342,
    label = "Cs-OsHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.3454648073129718,
        B = 0.04908908887756673,
        E = -0.19279925148986105,
        L = 0.5402928820381634,
        A = 0.0042404532437657644,
    ),
    )


entry(
    index = 1083,
    label = "Cs-CsOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.44684749951949354,
        B = 0.05275610009905109,
        E = -0.21994638838012986,
        L = 0.5961701508673811,
        A = 0.07300334883679661,
    ),
    )


entry(
    index = 1082,
    label = "Cs-COsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = u"Cs-CsOsHH",
)


entry(
    index = 841,
    label = "Cs-CsCsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.6983197803534978,
        B = 0.2163093014381869,
        E = -0.17530016559472095,
        L = 0.6507130817368125,
        A = 0.20510345465773003,
    ),
    )


entry(
    index = 840,
    label = "Cs-CCCOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = u"Cs-CsCsCsOs",
)


entry(
    index = 1125,
    label = "O2s-(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.16929136675760922,
        B = 0.05095036080953498,
        E = -0.04841813574507599,
        L = 0.02195511288592189,
        A = -0.08702317014635293,
    ),
    )


entry(
    index = 1122,
    label = "O2s-CdsCds",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    solute = u"O2s-(Cds-Cd)(Cds-Cd)",
)


entry(
    index = 126,
    label = "Cds-CdsOsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0897414853490858,
        B = 0.09211169378370497,
        E = 0.09583745023298051,
        L = 0.5827965672843056,
        A = 0.02184432555478129,
    ),
    )


entry(
    index = 125,
    label = "Cds-CdOsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1128,
    label = "O2s-Cs(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   C   u0 {2,D}
""",
    solute = SoluteData(
        S = -0.4429219002517437,
        B = 0.05172087004302618,
        E = 0.1646413979127375,
        L = 0.0029104361125882328,
        A = -0.21564560562764884,
    ),
    )


entry(
    index = 1087,
    label = "Cs-(Cds-Cds)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.4530235105328294,
        B = 0.16626898348925528,
        E = -0.16298420794012214,
        L = 0.6254989764812898,
        A = 0.10474993635920427,
    ),
    )


entry(
    index = 1086,
    label = "Cs-(Cds-Cd)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1084,
    label = "Cs-CdsOsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s     u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)OsHH",
)


entry(
    index = 343,
    label = "Cs-OsOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.7174387192965624,
        B = -0.08555571292160641,
        E = -0.4696354293703974,
        L = 0.46976995239542896,
        A = 0.15633396409448772,
    ),
    )


entry(
    index = 1028,
    label = "Cs-CsOsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.7743223982418233,
        B = -0.11516331659879836,
        E = -0.4249644635387055,
        L = 0.5852191427412169,
        A = 0.2104542146408671,
    ),
    )


entry(
    index = 1027,
    label = "Cs-COsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = u"Cs-CsOsOsH",
)


entry(
    index = 972,
    label = "Cs-CsCsOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.9581049654307527,
        B = 0.030269065232023606,
        E = -0.38236079621830665,
        L = 0.9605051676046529,
        A = 0.4825253909581299,
    ),
    )


entry(
    index = 971,
    label = "Cs-CCOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = u"Cs-CsCsOsOs",
)


entry(
    index = 379,
    label = "Cs-CbCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08488613500495837,
        B = 0.021027760357236927,
        E = 0.1000655839653585,
        L = 0.6776316219538261,
        A = -0.0025810385702850144,
    ),
    )


entry(
    index = 10,
    label = "Cb-Cs",
    group = 
"""
1 * Cb u0 {2,S}
2   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.11186345837241045,
        B = 0.037738298453426924,
        E = -0.01965107421424714,
        L = 0.42499723216347796,
        A = 0.03868674185560481,
    ),
    )


entry(
    index = 9,
    label = "Cb-C",
    group = 
"""
1 * Cb u0 {2,S}
2   C  u0 {1,S}
""",
    solute = u"Cb-Cs",
)


entry(
    index = 6,
    label = "Cb",
    group = 
"""
1 * Cb u0
""",
    solute = u"Cb-Cs",
)


entry(
    index = 7,
    label = "Cb-H",
    group = 
"""
1 * Cb u0 {2,S}
2   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.07797223183043052,
        B = 0.024006246125984166,
        E = 0.059755765068965225,
        L = 0.5381967259805268,
        A = -0.005795078738248473,
    ),
    )


entry(
    index = 1043,
    label = "Cs-(Cds-Cds)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.5191253226692321,
        B = 0.2203109876305388,
        E = -0.13037364774348456,
        L = 0.6149527903479999,
        A = 0.16598173839055075,
    ),
    )


entry(
    index = 1042,
    label = "Cs-(Cds-Cd)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1040,
    label = "Cs-CdsCsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   O2s     u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)CsOsH",
)


entry(
    index = 1919,
    label = "N3t",
    group = 
"""
1 * N3t u0 p1 {2,T}
2   R!H u0 {1,T}
""",
    solute = SoluteData(
        S = -0.25631572521205526,
        B = -0.26673413999023615,
        E = -0.039105766572242344,
        L = -0.61019095766348,
        A = -0.48568991655009985,
    ),
    )


entry(
    index = 1038,
    label = "Cs-CCOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5057296668811239,
        B = 0.1612163812344362,
        E = -0.06656273764670309,
        L = 0.9268728276959266,
        A = 0.150607304148856,
    ),
    )


entry(
    index = 1850,
    label = "Ct-N3tCs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.7630976435399245,
        B = 0.4492481097474999,
        E = 0.08714443387786686,
        L = 1.5718096908327435,
        A = 0.44044994647482555,
    ),
    )


entry(
    index = 1942,
    label = "Ct-N3tC",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 971,
    label = "Cs-CCOsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   O2s u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 1.1870451030564713,
        B = -0.07397755835214437,
        E = -0.3371983490756616,
        L = 1.2380623073044412,
        A = 0.1912706005340911,
    ),
    )


entry(
    index = 51,
    label = "Cds-OdHH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.4015977824768294,
        B = 0.04811981177681619,
        E = 0.2292188650278021,
        L = 0.5748532854121347,
        A = 0.2900811303940349,
    ),
    )


entry(
    index = 55,
    label = "Cds-OdCsH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.053373257257843504,
        B = 0.1707456256481744,
        E = 0.16722080954008886,
        L = 0.6654615502970003,
        A = -0.10670362621389334,
    ),
    )


entry(
    index = 54,
    label = "Cds-OdCH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = u"Cds-OdCsH",
)


entry(
    index = 348,
    label = "Cs-(Cds-O2d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.08675404923855799,
        B = 0.11168039408051669,
        E = 0.024581262302755466,
        L = 0.5572705103073091,
        A = 0.013859585892082693,
    ),
    )


entry(
    index = 392,
    label = "Cs-(Cds-O2d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.24800822944654355,
        B = 0.1352717759628963,
        E = 0.04904142688799726,
        L = 0.7538722796318731,
        A = 0.10333557305757718,
    ),
    )


entry(
    index = 522,
    label = "Cs-(Cds-O2d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.37240763374139474,
        B = 0.1897791312502442,
        E = 0.04630355666054371,
        L = 0.8649847550699752,
        A = 0.17850713230086315,
    ),
    )


entry(
    index = 57,
    label = "Cds-O2d(Cds-O2d)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.02667385688443897,
        B = 0.1368981808967206,
        E = 0.19214470931539096,
        L = 0.6554567319915792,
        A = -0.06978411789859479,
    ),
    )


entry(
    index = 56,
    label = "Cds-OdCdsH",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    solute = u"Cds-O2d(Cds-Cds)H",
)


entry(
    index = 1041,
    label = "Cs-(Cds-O2d)CsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.1313706333290382,
        B = 0.10928920560956303,
        E = -0.19894050762269752,
        L = 0.3838803095748867,
        A = 0.23511924404945916,
    ),
    )


entry(
    index = 79,
    label = "Cds-O2d(Cds-O2d)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.05707754388123344,
        B = 0.0857291482381432,
        E = 0.11605540005313329,
        L = 0.5414387878921083,
        A = -0.03273695324034106,
    ),
    )


entry(
    index = 78,
    label = "Cds-OdCdsCs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    solute = u"Cds-O2d(Cds-Cds)Cs",
)


entry(
    index = 76,
    label = "Cds-OdCC",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = u"Cds-OdCsCs",
)


entry(
    index = 123,
    label = "Cds-(Cdd-O2d)HH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cdd u0 {1,D} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.13811299262546756,
        B = 0.1939634943110834,
        E = 0.21380946960050215,
        L = 0.7991141127783978,
        A = 0.0007130846842852787,
    ),
    )


entry(
    index = 37,
    label = "Cdd-CdsOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   Cd  u0 {1,D}
3   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.13811299262547222,
        B = 0.19396349431108278,
        E = 0.2138094696004984,
        L = 0.7991141127784003,
        A = 0.0007130846842891767,
    ),
    )


entry(
    index = 36,
    label = "Cdd-CdOd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   C   u0 {1,D}
3   O2d u0 {1,D}
""",
    solute = u"Cdd-CdsOd",
)


entry(
    index = 1999,
    label = "Cd-Cd(CO)H",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   Cd  u0 {1,D}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.060634294439938216,
        B = 0.1906840157234267,
        E = 0.06029537080066849,
        L = 0.5433210225777506,
        A = -0.02335372315227764,
    ),
    )


entry(
    index = 59,
    label = "Cds-O2d(Cds-Cds)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.23133101007218113,
        B = 0.0499945394010609,
        E = 0.2856609747177523,
        L = 0.9670417772974611,
        A = -0.019948791111982056,
    ),
    )


entry(
    index = 58,
    label = "Cds-O2d(Cds-Cd)H",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   H   u0 {1,S}
5   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1996,
    label = "Cd-CdCs(CO)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cd  u0 {1,D}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.127635068602047,
        B = 0.1516363434931235,
        E = -0.020693372991827504,
        L = 0.6246812875811448,
        A = 0.0022647234284150688,
    ),
    )


entry(
    index = 357,
    label = "Cs-(Cds-O2d)(Cds-Cds)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {3,D}
7   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.05206031767294925,
        B = 0.11761971719356154,
        E = 0.12987256535277836,
        L = 0.6032113700439855,
        A = 0.04234247979258615,
    ),
    )


entry(
    index = 356,
    label = "Cs-(Cds-O2d)(Cds-Cd)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {7,D}
3   Cd  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {3,D}
7   O2d u0 {2,D}
""",
    solute = None,
)


entry(
    index = 54,
    label = "Cds-OdCH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0014868074097100226,
        B = 0.11906372320540938,
        E = 0.21689392942426905,
        L = 0.7561626136395064,
        A = -0.05390342990500236,
    ),
    )


entry(
    index = 25,
    label = "Ct-CtCds",
    group = 
"""
1 * Ct         u0 {2,T} {3,S}
2   Ct         u0 {1,T}
3   [Cd,CO,CS] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.24020397531639026,
        B = 0.07971110810064796,
        E = 0.0743795940405497,
        L = 0.6701499340033616,
        A = -0.003207123026800652,
    ),
    )


entry(
    index = 77,
    label = "Cds-OdCsCs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.19901795556084279,
        B = 0.11786316296756685,
        E = 0.12130736949288559,
        L = 0.8318459153683119,
        A = -0.04676067507430395,
    ),
    )


entry(
    index = 81,
    label = "Cds-O2d(Cds-Cds)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.19031822934840248,
        B = 0.05873355181819224,
        E = 0.21298733440717427,
        L = 0.8575871448304064,
        A = 0.01786175094787578,
    ),
    )


entry(
    index = 80,
    label = "Cds-O2d(Cds-Cd)Cs",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   Cs  u0 {1,S}
5   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 1085,
    label = "Cs-(Cds-O2d)OsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.23146611122734034,
        B = 0.09369639085810366,
        E = -0.15780747794737057,
        L = 0.5507533973499446,
        A = 0.17411159075485869,
    ),
    )


entry(
    index = 355,
    label = "Cs-(Cds-O2d)(Cds-O2d)HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.2414262782843299,
        B = 0.03894331357814204,
        E = 0.13177655082225997,
        L = 0.4656736146941636,
        A = 0.034520236005383606,
    ),
    )


entry(
    index = 400,
    label = "Cs-CdsCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0550569687698747,
        B = 0.0853133351222988,
        E = 0.04101476101412885,
        L = 0.6151094369853052,
        A = -0.07682105083869646,
    ),
    )


entry(
    index = 12,
    label = "Cb-(Cds-O2d)",
    group = 
"""
1 * Cb  u0 {2,S}
2   CO  u0 {1,S} {3,D}
3   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.23250413512090756,
        B = 0.011082236094911053,
        E = 0.07256848899764987,
        L = 0.7002753918790436,
        A = 0.01345269836852133,
    ),
    )


entry(
    index = 11,
    label = "Cb-Cds",
    group = 
"""
1 * Cb         u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
    solute = u"Cb-(Cds-Cds)",
)


entry(
    index = 76,
    label = "Cds-OdCC",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03521924752680442,
        B = 0.08782764687532058,
        E = 0.14424287823957144,
        L = 0.6397685857190536,
        A = -0.034540516780401424,
    ),
    )


entry(
    index = 1141,
    label = "S2s-CdCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.9232700387323811,
        B = -0.12961537239030238,
        E = 0.21504586169990092,
        L = 1.8958978443541774,
        A = -0.012308192329580931,
    ),
    )


entry(
    index = -1,
    label = "S2s-CC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = -1,
    label = "S2s",
    group = 
"""
1 * S2s u0
""",
    solute = None,
)


entry(
    index = 50,
    label = "Cds",
    group = 
"""
1 * [Cd,CO,CS] u0
""",
    solute = SoluteData(
        S = 0.22458129600242557,
        B = 0.10936459334524362,
        E = 0.15144897046417094,
        L = 0.8001413281348664,
        A = 0.010502657500858709,
    ),
    )


entry(
    index = 1180,
    label = "Cds-CdsS2H",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.17607218192072727,
        B = 0.05394580547433734,
        E = 0.033803802229159616,
        L = 0.30076514344623084,
        A = 0.007018568398203862,
    ),
    )


entry(
    index = 1180,
    label = "Cds-CdsSH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = u"Cds-CdsS4H",
)


entry(
    index = -1,
    label = "Cds-CdSH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   S  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = u"Cds-CdsSsH",
)


entry(
    index = 53,
    label = "Cds-OdOsOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.15961116557053717,
        B = 0.21130650218287556,
        E = 0.1424681590755672,
        L = 0.6788721912530469,
        A = 0.021000114516465846,
    ),
    )


entry(
    index = 1106,
    label = "O2s-CsH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.21694560700474388,
        B = 0.3076267437556488,
        E = 0.40303825306205215,
        L = 0.6430097017197416,
        A = 0.1445090507445071,
    ),
    )


entry(
    index = 1101,
    label = "O2s-CH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
""",
    solute = u"O2s-CsH",
)


entry(
    index = 1105,
    label = "O2s-(Cds-Cd)H",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cd  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   C   u0 {2,D}
""",
    solute = SoluteData(
        S = 0.06720490110199091,
        B = 0.15154867373823216,
        E = 0.11192906103303449,
        L = 0.49624151790943505,
        A = 0.3270177491011773,
    ),
    )


entry(
    index = 1103,
    label = "O2s-CdsH",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
""",
    solute = u"O2s-(Cds-Cd)H",
)


entry(
    index = 171,
    label = "Cds-Cds(Cds-O2d)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.03356401411110284,
        B = 0.1921427463075143,
        E = 0.1432807418960764,
        L = 0.6100011891845667,
        A = -0.12179381354676581,
    ),
    )


entry(
    index = 170,
    label = "Cds-CdsCdsOs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    solute = u"Cds-Cds(Cds-Cds)O2s",
)


entry(
    index = 168,
    label = "Cds-CdCO",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = u"Cds-CdsCsOs",
)


entry(
    index = 52,
    label = "Cds-OdOsH",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.05683120061325293,
        B = 0.15965704213679838,
        E = 0.1480458809583663,
        L = 0.6285885448330331,
        A = -0.00017751720901848164,
    ),
    )


entry(
    index = 1124,
    label = "O2s-(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {4,D}
4   C   u0 {3,D}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.020703358945534045,
        B = 0.004944669406582586,
        E = -0.012028894237656296,
        L = 0.1904624649637905,
        A = -0.07150885911154184,
    ),
    )


entry(
    index = 169,
    label = "Cds-CdsCsOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.21132464964534797,
        B = -0.019394216310876358,
        E = 0.0049606718891953075,
        L = 0.6399333005835575,
        A = 0.0038651057449578165,
    ),
    )


entry(
    index = 1995,
    label = "Cd-CdCsOs",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   C   u0 {1,D}
""",
    solute = None,
)


entry(
    index = 70,
    label = "Cds-O2d(Cds-Cds)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.044302255069011115,
        B = 0.009233776081999781,
        E = 0.14553402348118974,
        L = 0.6632690843383064,
        A = 0.0784165744220532,
    ),
    )


entry(
    index = 69,
    label = "Cds-O2d(Cds-Cd)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 67,
    label = "Cds-OdCdsOs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    solute = u"Cds-O2d(Cds-Cds)O2s",
)


entry(
    index = 65,
    label = "Cds-OdCOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.09647913980989586,
        B = 0.2049599406032971,
        E = 0.15401578146686645,
        L = 0.5142584236738479,
        A = 0.042933928326937265,
    ),
    )


entry(
    index = 68,
    label = "Cds-O2d(Cds-O2d)O2s",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   CO  u0 {1,S} {5,D}
3   O2d u0 {1,D}
4   O2s u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.15242644362795515,
        B = 0.1304284258351825,
        E = 0.14646803244354556,
        L = 0.7187111997612463,
        A = 0.049415913209227474,
    ),
    )


entry(
    index = 1104,
    label = "O2s-(Cds-O2d)H",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   H   u0 {1,S}
4   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.04866309203398413,
        B = 0.028792593927901178,
        E = 0.10135854821605103,
        L = 0.5847881936560481,
        A = 0.45185770763553534,
    ),
    )


entry(
    index = 843,
    label = "Cs-(Cds-O2d)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.5328644023282001,
        B = -0.028908081480774034,
        E = -0.2341052801055017,
        L = 0.7191225358398923,
        A = -0.13460066596387232,
    ),
    )


entry(
    index = 842,
    label = "Cs-CdsCsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)CsCsOs",
)


entry(
    index = 372,
    label = "Cs-(Cds-O2d)CtHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Ct  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.0688362232477942,
        B = 0.07317162105036487,
        E = 0.17332792516903245,
        L = 0.8838319124683678,
        A = 0.06359298559625295,
    ),
    )


entry(
    index = 371,
    label = "Cs-CtCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)CtHH",
)


entry(
    index = 1863,
    label = "Cs-(CtN3t)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.01656977210278801,
        B = 0.08873798408575569,
        E = 0.16892481383816998,
        L = 0.8664261028654147,
        A = -0.026272304381818736,
    ),
    )


entry(
    index = 1832,
    label = "Cs-(CtN3t)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.22648792219736302,
        B = 0.09632576161964736,
        E = 0.11240824293919321,
        L = 0.8823848588020993,
        A = -0.02862968241402079,
    ),
    )


entry(
    index = 1833,
    label = "Cs-(CtN3t)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.4239832706019591,
        B = 0.11944497382938091,
        E = 0.10628690258417178,
        L = 1.1066199878755512,
        A = 0.034439592845266084,
    ),
    )


entry(
    index = 398,
    label = "Cs-CtCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1834,
    label = "Cs-(CtN3t)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S} {6,T}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.4233435873182082,
        B = 0.2109216404147516,
        E = 0.12741389756357446,
        L = 1.0259511054011456,
        A = 0.09158937352786511,
    ),
    )


entry(
    index = 528,
    label = "Cs-CtCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1836,
    label = "Cds-CdsH(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Ct  u0 {1,S} {5,T}
3   Cd  u0 {1,D}
4   H   u0 {1,S}
5   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.7703088558165031,
        B = 0.11217360764232676,
        E = 0.23995147183590843,
        L = 1.4590574412915935,
        A = 0.006270986784226449,
    ),
    )


entry(
    index = 1851,
    label = "Ct-N3tCd",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08062787640049801,
        B = 0.40241265064960335,
        E = 0.12093557171614418,
        L = 1.0042489432917734,
        A = 0.41127005117651744,
    ),
    )


entry(
    index = 1858,
    label = "Cd-CdCs(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S} {6,S}
3   Ct  u0 {1,S} {7,T}
4   Cs  u0 {1,S}
5   R   u0 {2,S}
6   R   u0 {2,S}
7   N3t u0 {3,T}
""",
    solute = SoluteData(
        S = 0.6819784043627537,
        B = 0.12145713011797979,
        E = 0.052085106667015886,
        L = 1.3373696205645262,
        A = 0.04227588341846801,
    ),
    )


entry(
    index = 225,
    label = "Cds-CdsCtCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
""",
    solute = None,
)


entry(
    index = 374,
    label = "Cs-(Cds-Cds)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.03072362808427548,
        B = 0.2476232524457948,
        E = 0.16894454428499286,
        L = 0.9044635818031377,
        A = -0.019215688117775874,
    ),
    )


entry(
    index = 373,
    label = "Cs-(Cds-Cd)CtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = u"Cs-(Cds-Cds)CtHH",
)


entry(
    index = 1837,
    label = "Cds-Cd(CtN3t)(CtN3t)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   Ct  u0 {1,S} {5,T}
3   Ct  u0 {1,S} {6,T}
4   Cd  u0 {1,D}
5   N3t u0 {2,T}
6   N3t u0 {3,T}
""",
    solute = SoluteData(
        S = 1.1730515428384456,
        B = 0.21426895560277748,
        E = 0.22632213028409273,
        L = 1.921406446760762,
        A = 0.07808359351861802,
    ),
    )


entry(
    index = 233,
    label = "Cds-CdsCtCt",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Ct u0 {1,S}
4   Ct u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1810,
    label = "N3s-CsCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.17212829227776782,
        B = 0.15405712115264433,
        E = 0.08653887458638056,
        L = 0.43570282461684073,
        A = 0.39750055272537477,
    ),
    )


entry(
    index = 1939,
    label = "N3s-CCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 329,
    label = "Cs",
    group = 
"""
1 * Cs u0
""",
    solute = SoluteData(
        S = 0.24539529467837767,
        B = 0.11425380519348241,
        E = 0.08105175087750756,
        L = 0.7833252562880013,
        A = -0.1002636622831654,
    ),
    )


entry(
    index = 1800,
    label = "Cs-N3sHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.05438259035657654,
        B = 0.12588647038658332,
        E = 0.00953299965458,
        L = 0.5062882512099705,
        A = -0.17872791179567593,
    ),
    )


entry(
    index = 1919,
    label = "Cs-NHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1802,
    label = "Cs-N3sCsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.15062166917753586,
        B = 0.1533371138770775,
        E = 0.010819976653408035,
        L = 0.5894650428729526,
        A = -0.11979330235495222,
    ),
    )


entry(
    index = 1921,
    label = "Cs-NCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1942,
    label = "Ct-N3tC",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.6979915704273855,
        B = 0.3173601169117469,
        E = 0.21408750714413968,
        L = 1.7897133756808254,
        A = 0.414933779321552,
    ),
    )


entry(
    index = 378,
    label = "Cs-CtCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.18978785377492458,
        B = 0.14622401432849538,
        E = 0.22388614653254735,
        L = 1.1438073696961606,
        A = 0.14896766569345576,
    ),
    )


entry(
    index = 1803,
    label = "Cs-N3sCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2384755202106973,
        B = 0.1253861005313028,
        E = 0.013803306497719145,
        L = 0.641443992762889,
        A = -0.07147480001348655,
    ),
    )


entry(
    index = 1927,
    label = "Cs-NCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1809,
    label = "N3s-CsCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.13201232057415058,
        B = 0.31100435527943526,
        E = 0.12986319734840635,
        L = 0.5755160163785056,
        A = 0.32641701947121543,
    ),
    )


entry(
    index = 1938,
    label = "N3s-CCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1938,
    label = "N3s-CHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.023155851120408973,
        B = 0.3568447813784441,
        E = 0.23063910622696635,
        L = 0.8081368852172954,
        A = 0.2620701317850661,
    ),
    )


entry(
    index = 1853,
    label = "Ct-N3tN3s",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 1.2165115645223024,
        B = 0.18114131245480852,
        E = 0.23843014148906688,
        L = 2.1560989084808453,
        A = 0.3421075103079388,
    ),
    )


entry(
    index = 1826,
    label = "N3s-(CO)CsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.2655844697248846,
        B = 0.1471186599910318,
        E = 0.13560342905278883,
        L = 0.9785907112128088,
        A = 0.4117553784480716,
    ),
    )


entry(
    index = 1889,
    label = "N3s-CdHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.033298190179390036,
        B = 0.21728683469860346,
        E = 0.27383833831008053,
        L = 0.8292912325002468,
        A = 0.22130029704664134,
    ),
    )


entry(
    index = 1906,
    label = "N3d-CdH",
    group = 
"""
1 * N3d      u0 {2,D} {3,S}
2   [Cd,Cdd] u0 {1,D}
3   H        u0 {1,S}
""",
    solute = SoluteData(
        S = -0.13130163797620975,
        B = 0.3191248265565328,
        E = 0.0880772963356637,
        L = 0.1458000262280593,
        A = -0.08379889547819555,
    ),
    )


entry(
    index = 1904,
    label = "N3d",
    group = 
"""
1 * N3d u0
""",
    solute = None,
)


entry(
    index = 1905,
    label = "N3d-CdCs",
    group = 
"""
1 * N3d      u0 {2,D} {3,S}
2   [Cd,Cdd] u0 {1,D}
3   Cs       u0 {1,S}
""",
    solute = SoluteData(
        S = -0.2518300212962564,
        B = 0.30194125818860895,
        E = 0.30195195419900783,
        L = 0.5711360710180097,
        A = 0.2953966028272987,
    ),
    )


entry(
    index = 1911,
    label = "N3d-CsR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cs  u0 {1,S}
3   R!H u0 {1,D}
""",
    solute = None,
)


entry(
    index = 1871,
    label = "Cs-(N3dCd)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.32583252848502675,
        B = 0.2099824740876563,
        E = -0.3662811766239633,
        L = 0.14122307353710584,
        A = -0.16533106134535236,
    ),
    )


entry(
    index = 1925,
    label = "Cs-N3dCHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1938,
    label = "N3s-CCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.015633809955237696,
        B = 0.16000227235965137,
        E = 0.21651537890337055,
        L = 0.768193540776347,
        A = 0.30386411658212975,
    ),
    )


entry(
    index = 1130,
    label = "O2s-CsCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.7438317696833582,
        B = 0.02679367575449121,
        E = 0.5832773387792887,
        L = 0.35847360605012746,
        A = -0.06558373221781497,
    ),
    )


entry(
    index = 8,
    label = "Cb-O2s",
    group = 
"""
1 * Cb  u0 {2,S}
2   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.7014408561377896,
        B = 0.1358001286993729,
        E = -0.26367111736522875,
        L = 0.6479650881501877,
        A = 0.021682877888627716,
    ),
    )


entry(
    index = 1907,
    label = "N3d-N3dCs",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.24363355847690218,
        B = 0.05651026451558802,
        E = 0.08073905090685027,
        L = 0.7115153760979602,
        A = -0.004067788962660369,
    ),
    )


entry(
    index = 1805,
    label = "Cs-(N3dN3d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.2436335584769008,
        B = 0.056510264515587494,
        E = 0.08073905090684799,
        L = 0.7115153760979557,
        A = -0.0040677889626589084,
    ),
    )


entry(
    index = 1825,
    label = "N3s-(CO)HH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.24113305203957008,
        B = 0.24071122090030722,
        E = 0.21414986831366856,
        L = 1.045465054187356,
        A = 0.36289358234364705,
    ),
    )


entry(
    index = 1823,
    label = "Cds-OdN3sH",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   H   u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.4077808067144683,
        B = 0.14732920431788019,
        E = 0.21794150742953716,
        L = 1.1106001354365853,
        A = -0.020593304533139692,
    ),
    )


entry(
    index = 1824,
    label = "Cds-OdN3sCs",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
4   O2d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.325505519751366,
        B = 0.1488530679467087,
        E = 0.15474758658811585,
        L = 0.9400260356337147,
        A = 0.012463933611839548,
    ),
    )


entry(
    index = 1827,
    label = "N3s-(CO)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.12529623829366227,
        B = 0.13919251553747336,
        E = 0.13087068248820777,
        L = 0.768011132184713,
        A = 0.2971280152471465,
    ),
    )


entry(
    index = 1847,
    label = "O2s-Cs(N3dOd)",
    group = 
"""
1 * O2s u0 {2,S} {4,S}
2   N3d u0 {1,S} {3,D}
3   O2d u0 {2,D}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.21910895863665086,
        B = 0.0894339213387472,
        E = 0.16404308458557776,
        L = 0.25313169300894706,
        A = -0.0304833654722142,
    ),
    )


entry(
    index = 1875,
    label = "O2s-CsN3d",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   N3d u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1935,
    label = "O2s-CN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   N   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1945,
    label = "O2s-N",
    group = 
"""
1 * O2s u0 {2,S}
2   N   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1943,
    label = "O2d-N3d",
    group = 
"""
1 * O2d u0 {2,D}
2   N3d u0 {1,D}
""",
    solute = SoluteData(
        S = 0.1069796248718951,
        B = 0.0004435983083975713,
        E = -0.05551585053202886,
        L = 0.17067758412635012,
        A = -0.08002105616841382,
    ),
    )


entry(
    index = 1909,
    label = "N3d-OdOs",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d u0 {1,D}
3   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.21910895863665478,
        B = 0.08943392133874764,
        E = 0.16404308458557695,
        L = 0.25313169300894034,
        A = -0.030483365472217038,
    ),
    )


entry(
    index = 1829,
    label = "N3s-(CO)(CO)H",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   H   u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.14193761435353655,
        B = 0.11758969396918706,
        E = 0.14554884376516522,
        L = 0.508378972052146,
        A = 0.31634616202445454,
    ),
    )


entry(
    index = 1939,
    label = "N3s-CCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03697908762877255,
        B = 0.11415062105588111,
        E = 0.1591022469432372,
        L = 0.6571756049103026,
        A = 0.20166647143032462,
    ),
    )


entry(
    index = 399,
    label = "Cs-CbCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.21581876233500136,
        B = 0.04569821182533086,
        E = 0.11175027456358,
        L = 0.7529532331016894,
        A = 0.061374855027650846,
    ),
    )


entry(
    index = 1830,
    label = "N3s-(CO)(CO)Cs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   CO  u0 {1,S} {6,D}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
6   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.26639416475116,
        B = 0.014895436171307907,
        E = 0.15903691772029294,
        L = 0.40586032576713493,
        A = 0.14624281020400778,
    ),
    )


entry(
    index = 1925,
    label = "Cs-N3dCHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.24000472598481334,
        B = -0.08292764564065523,
        E = -0.22882282172641494,
        L = 0.2495710006433245,
        A = -0.2791943336412518,
    ),
    )


entry(
    index = 34,
    label = "Cdd",
    group = 
"""
1 * Cdd u0
""",
    solute = SoluteData(
        S = 0.179189864537593,
        B = -0.027792624112526622,
        E = 0.27542864446296944,
        L = 0.942874993261251,
        A = 0.020707822308455946,
    ),
    )


entry(
    index = 1870,
    label = "Cs-(N3dCd)HHH",
    group = 
"""
1 * Cs       u0 {2,S} {3,S} {4,S} {5,S}
2   N3d      u0 {1,S} {6,D}
3   H        u0 {1,S}
4   H        u0 {1,S}
5   H        u0 {1,S}
6   [Cd,Cdd] u0 {2,D}
""",
    solute = SoluteData(
        S = 0.004222771483501919,
        B = 0.024546837330943094,
        E = -0.3198059407534673,
        L = -0.07595472230077194,
        A = -0.30363422810870583,
    ),
    )


entry(
    index = 1920,
    label = "Cs-N3dHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1133,
    label = "S2s-CsH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.25645307399984096,
        B = 0.0634760089731928,
        E = 0.27289368232370276,
        L = 0.2970484598315589,
        A = -0.42263590901389153,
    ),
    )


entry(
    index = -1,
    label = "S2s-CH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = -1,
    label = "Cs-CSHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.6343915046825417,
        B = 0.16379909732240763,
        E = 0.09368670221921821,
        L = 1.5491305484967393,
        A = 0.3935019190419293,
    ),
    )


entry(
    index = 398,
    label = "Cs-CtCsCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.27170735154068065,
        B = 0.22834240321162227,
        E = -0.14915229482925207,
        L = 0.4621395487054196,
        A = -0.1310169995589393,
    ),
    )


entry(
    index = 1123,
    label = "O2s-(Cds-O2d)(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   CO  u0 {1,S} {5,D}
4   O2d u0 {2,D}
5   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = 0.12521384507269956,
        B = -0.07135488699528249,
        E = 0.0755125630145767,
        L = 0.433098415002399,
        A = -0.13396966421817053,
    ),
    )


entry(
    index = 531,
    label = "Cs-(Cds-O2d)(Cds-O2d)CsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   CO  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   O2d u0 {2,D}
7   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.05328953910970621,
        B = 0.2586440033040178,
        E = 0.2056137912840038,
        L = 0.7091025553315695,
        A = 0.010183923474966883,
    ),
    )


entry(
    index = 530,
    label = "Cs-CdsCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)CsCs",
)


entry(
    index = 1111,
    label = "O2s-O2s(Cds-O2d)",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   O2s u0 {1,S}
4   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.25016189178282877,
        B = -0.013004603893432554,
        E = -0.01175186936143481,
        L = 0.4844240951787292,
        A = -0.04671248977250801,
    ),
    )


entry(
    index = 1110,
    label = "O2s-OsCds",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   O2s     u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    solute = u"O2s-O2s(Cds-Cd)",
)


entry(
    index = 1108,
    label = "O2s-OsC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   C   u0 {1,S}
""",
    solute = u"O2s-OsCs",
)


entry(
    index = 1091,
    label = "Cs-CtOsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.3405125829708828,
        B = 0.11041681096316024,
        E = -0.07284164624578227,
        L = 0.6908864312827996,
        A = 0.03697287953421528,
    ),
    )


entry(
    index = 845,
    label = "Cs-(Cds-Cds)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.7599318736374159,
        B = 0.20721708933497204,
        E = -0.16722856283589047,
        L = 0.6959092223588759,
        A = 0.20927812985987496,
    ),
    )


entry(
    index = 844,
    label = "Cs-(Cds-Cd)CsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
""",
    solute = None,
)


entry(
    index = 840,
    label = "Cs-CCCOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.8682307845707695,
        B = 0.22872428943246986,
        E = 0.017393648302531706,
        L = 1.5013950665889364,
        A = 0.19933883023755045,
    ),
    )


entry(
    index = 1082,
    label = "Cs-COsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5207575930310251,
        B = 0.07972624785610685,
        E = -0.13643682581316696,
        L = 0.7898229608101704,
        A = 0.10253237630265677,
    ),
    )


entry(
    index = 2001,
    label = "S4d-OdCsCs",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cs  ux {1,S}
4   Cs  ux {1,S}
""",
    solute = SoluteData(
        S = 0.6654076425996981,
        B = 0.4384919779297695,
        E = 0.13756332592764026,
        L = 0.9857459464860626,
        A = -0.3871840640972999,
    ),
    )


entry(
    index = 2001,
    label = "S4d-OdCC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    solute = u"S4d-OdCsCs",
)


entry(
    index = 2041,
    label = "S4d-Od",
    group = 
"""
1 * S4d u0 p1 {2,D}
2   O2d ux {1,D}
""",
    solute = u"S4d-OdCC",
)


entry(
    index = 2030,
    label = "S4d",
    group = 
"""
1 * S4d u0
""",
    solute = u"S4d-Od",
)


entry(
    index = 1162,
    label = "Cs-S4HHH",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   [S4s,S4d,S4b,S4t] u0 {1,S}
3   H                 u0 {1,S}
4   H                 u0 {1,S}
5   H                 u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2825463421768132,
        B = 0.08494825072422409,
        E = 0.07872844312833517,
        L = 0.904555927018521,
        A = 0.1688737702738733,
    ),
    )


entry(
    index = 1162,
    label = "Cs-SsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = u"Cs-S2sHHH",
)


entry(
    index = 1163,
    label = "Cs-CsS4HH",
    group = 
"""
1 * Cs                u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                u0 {1,S}
3   [S4s,S4d,S4b,S4t] u0 {1,S}
4   H                 u0 {1,S}
5   H                 u0 {1,S}
""",
    solute = SoluteData(
        S = 0.399411386265705,
        B = 0.13045184486143935,
        E = 0.05239199746318775,
        L = 0.9691929253751932,
        A = 0.2155790138404284,
    ),
    )


entry(
    index = 1163,
    label = "Cs-CsSHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = u"Cs-CsS2HH",
)


entry(
    index = 2013,
    label = "S6dd-OdOdCsCs",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    solute = SoluteData(
        S = 1.0574900710273383,
        B = -0.3395371034614496,
        E = 0.03092823092334429,
        L = 1.1319305073072317,
        A = -0.002353395280755448,
    ),
    )


entry(
    index = 2013,
    label = "S6dd-OdOdCC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    solute = u"S6dd-OdOdCsCs",
)


entry(
    index = 2044,
    label = "S6dd-OdOd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
""",
    solute = u"S6dd-OdOdCC",
)


entry(
    index = 2031,
    label = "S6dd",
    group = 
"""
1 * S6dd u0
""",
    solute = u"S6dd-OdOd",
)


entry(
    index = 1163,
    label = "Cs-CsS6HH",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   Cs                      u0 {1,S}
3   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
4   H                       u0 {1,S}
5   H                       u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0753542171295154,
        B = 0.2898127357969278,
        E = -0.019358906672488407,
        L = 0.27660989731017205,
        A = 0.07122927194810211,
    ),
    )


entry(
    index = 2020,
    label = "S6dd-OdOdOO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   O    ux {1,S}
5   O    ux {1,S}
""",
    solute = SoluteData(
        S = -0.5168837507969509,
        B = 0.6365513974164151,
        E = -0.0313330905771982,
        L = -0.5454108839879808,
        A = -0.2752072455911552,
    ),
    )


entry(
    index = 2025,
    label = "O2s-CS6",
    group = 
"""
1 * O2s                     u0 {2,S} {3,S}
2   [S6s,S6d,S6dd,S6t,S6td] ux {1,S}
3   C                       ux {1,S}
""",
    solute = SoluteData(
        S = 0.14449963607883565,
        B = -0.32166921086398614,
        E = 0.03245693686591595,
        L = 0.4609417845634458,
        A = 0.14072151713691539,
    ),
    )


entry(
    index = 2028,
    label = "O2s-CS",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   C   ux {1,S}
""",
    solute = u"O2s-CS4",
)


entry(
    index = 1202,
    label = "Cs-CsCsSS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.9085065281450098,
        B = 0.39959232407941436,
        E = -0.606311122322764,
        L = -0.619042230396798,
        A = 0.28352238070332414,
    ),
    )


entry(
    index = -1,
    label = "Cs-CCSS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   S  u0 {1,S}
""",
    solute = u"Cs-CsCsSS",
)


entry(
    index = 2003,
    label = "S4d-OdCS",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d ux {1,D}
3   C   ux {1,S}
4   S   ux {1,S}
""",
    solute = SoluteData(
        S = 0.06417028025397656,
        B = 0.09871066068377558,
        E = 0.21600021932488056,
        L = 0.4340709987934558,
        A = -0.3349623698586216,
    ),
    )


entry(
    index = -1,
    label = "S2s-S46C",
    group = 
"""
1 * S2s                                 u0 {2,S} {3,S}
2   [S4s,S4d,S4b,S4t,S6d,S6dd,S6t,S6td] u0 {1,S}
3   C                                   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.06417028025397964,
        B = 0.09871066068377568,
        E = 0.21600021932487629,
        L = 0.4340709987934556,
        A = -0.33496236985862055,
    ),
    )


entry(
    index = -1,
    label = "S2s-SC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   C   ux {1,S}
""",
    solute = u"S2s-S2sC",
)


entry(
    index = 1164,
    label = "Cs-CdsSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.45377405998112275,
        B = 0.17787167167341505,
        E = 0.1668252006840307,
        L = 1.534854054416747,
        A = 0.36713826355995466,
    ),
    )


entry(
    index = 1199,
    label = "Cdd-S2dS2d",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   S2d u0 {1,D}
3   S2d u0 {1,D}
""",
    solute = SoluteData(
        S = -0.7582631091505541,
        B = -0.08769655029953673,
        E = 0.3160632671259397,
        L = 0.3245684408993599,
        A = -0.005149704400695829,
    ),
    )


entry(
    index = 1199,
    label = "Cdd-SdSd",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   S   u0 {1,D}
3   S   u0 {1,D}
""",
    solute = u"Cdd-S2dS2d",
)


entry(
    index = 1463,
    label = "S2s-Cs(C=O)",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   CO  u0 {1,S} {4,D}
4   O2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.7187555089268083,
        B = -0.08430087881814856,
        E = 0.18520274349131766,
        L = -0.4292101278501259,
        A = -0.287961901675379,
    ),
    )


entry(
    index = 1162,
    label = "Cs-S2sHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   S2s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.28948491853501124,
        B = 0.05482415760476328,
        E = 0.08520534402495153,
        L = 1.335704011795067,
        A = 0.29198864148292514,
    ),
    )


entry(
    index = 1455,
    label = "CO-CsSs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   S2s u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5292876250721607,
        B = 0.24445599859974976,
        E = 0.16506925623198754,
        L = 1.2807264337606634,
        A = -0.10226765840813018,
    ),
    )


entry(
    index = 1163,
    label = "Cs-CsS2HH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.405356826379151,
        B = 0.09754103464955473,
        E = 0.10013805067097267,
        L = 1.4673197081950782,
        A = 0.3530255877729147,
    ),
    )


entry(
    index = 1139,
    label = "S2s-CsCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Ct  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.006705575991767632,
        B = -0.026471371288318946,
        E = 0.4211775882420876,
        L = 0.681932504044609,
        A = -0.4614154444894743,
    ),
    )


entry(
    index = 1137,
    label = "S2s-CsCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.5095279813980993,
        B = 0.1239679032618512,
        E = 0.16170692357434696,
        L = -0.49316660903959464,
        A = -0.7205877231114852,
    ),
    )


entry(
    index = 2016,
    label = "S6dd-OdOdCsOs",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
5   O    ux {1,S}
""",
    solute = SoluteData(
        S = -0.962112487176229,
        B = 0.22662104770007913,
        E = 0.04185445286060353,
        L = -0.519088542923736,
        A = -0.006338363492629791,
    ),
    )


entry(
    index = 2016,
    label = "S6dd-OdOdCO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    solute = u"S6dd-OdOdCsOs",
)


entry(
    index = 2026,
    label = "O2s-S_DeH",
    group = 
"""
1 * O2s            u0 {2,S} {3,S}
2   [S4d,S6d,S6dd] ux {1,S}
3   H              ux {1,S}
""",
    solute = SoluteData(
        S = 2.0223560073720614,
        B = -0.16741954412999743,
        E = -0.1536981871651648,
        L = 1.7353619465850931,
        A = 0.3463924614802385,
    ),
    )


entry(
    index = 2027,
    label = "O2s-SH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   H   ux {1,S}
""",
    solute = u"O2s-S_nonDeH",
)


entry(
    index = 1162,
    label = "Cs-S6HHH",
    group = 
"""
1 * Cs                      u0 {2,S} {3,S} {4,S} {5,S}
2   [S6s,S6d,S6dd,S6t,S6td] u0 {1,S}
3   H                       u0 {1,S}
4   H                       u0 {1,S}
5   H                       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.40280161579083723,
        B = 0.23218964987349605,
        E = -0.09717398552051931,
        L = 0.72678504555392,
        A = -0.015337402817400543,
    ),
    )


entry(
    index = 2016,
    label = "S6dd-OdOdCO",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   O    ux {1,S}
""",
    solute = SoluteData(
        S = -1.1035871134389228,
        B = 0.2956723684836035,
        E = -0.07670528204560925,
        L = -0.9511097514035018,
        A = -0.07638232372487673,
    ),
    )


entry(
    index = 1197,
    label = "Cb-S",
    group = 
"""
1 * Cb u0 {2,S}
2   S  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5935517022944085,
        B = 0.17252813367552866,
        E = 0.03398978116194987,
        L = 1.06827760348034,
        A = 0.07786989562003557,
    ),
    )


entry(
    index = 341,
    label = "Cs-CbHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.03167486562593394,
        B = 0.0011741842248008186,
        E = 0.10002411331871108,
        L = 0.6119286947157916,
        A = -0.05358028926431038,
    ),
    )


entry(
    index = 1107,
    label = "O2s-CbH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.39660448886147903,
        B = 0.032736912841271275,
        E = 0.5042251468844626,
        L = 0.695938282741593,
        A = 0.3759518611520089,
    ),
    )


entry(
    index = 75,
    label = "Cds-OdCbOs",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.06597801122566914,
        B = 0.1439771957803206,
        E = 0.10206636645658405,
        L = 0.5282418351719798,
        A = 0.07859411453602025,
    ),
    )


entry(
    index = 1113,
    label = "O2s-OsCs",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   O2s u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.4130501355033674,
        B = 0.15790877653481572,
        E = 0.16403841136057573,
        L = 0.3438990603751597,
        A = -0.1111148337415467,
    ),
    )


entry(
    index = 529,
    label = "Cs-CbCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.43164912291714386,
        B = 0.0839983554777719,
        E = 0.12905812472080913,
        L = 0.951716643462438,
        A = 0.09868569562838511,
    ),
    )


entry(
    index = 14,
    label = "Cb-(Cds-Cds)",
    group = 
"""
1 * Cb u0 {2,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.26053944660502193,
        B = -7.622446238213926e-05,
        E = 0.15295697444685752,
        L = 0.911256431689948,
        A = 0.10992543601675366,
    ),
    )


entry(
    index = 13,
    label = "Cb-(Cds-Cd)",
    group = 
"""
1 * Cb u0 {2,S}
2   Cd u0 {1,S} {3,D}
3   C  u0 {2,D}
""",
    solute = u"Cb-(Cds-Cds)",
)


entry(
    index = 145,
    label = "Cds-CdsCbH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.07090668164627464,
        B = 0.06314971391614396,
        E = 0.06404917011339523,
        L = 0.34531921220054496,
        A = -0.08755267497599915,
    ),
    )


entry(
    index = 234,
    label = "Cds-CdsCbCs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.13900081101897038,
        B = 0.051429512200566505,
        E = -0.06701289968558061,
        L = 0.5178635961025511,
        A = -0.02622747422065416,
    ),
    )


entry(
    index = 18,
    label = "Cb-Ct",
    group = 
"""
1 * Cb u0 {2,S}
2   Ct u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03876090276007182,
        B = 0.02995931741688069,
        E = 0.025884265014523837,
        L = 0.4520014412269978,
        A = 0.023545789568395446,
    ),
    )


entry(
    index = 33,
    label = "Ct-CtCb",
    group = 
"""
1 * Ct u0 {2,T} {3,S}
2   Ct u0 {1,T}
3   Cb u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03876090276007174,
        B = 0.029959317416882188,
        E = 0.025884265014524184,
        L = 0.4520014412270042,
        A = 0.02354578956839596,
    ),
    )


entry(
    index = 19,
    label = "Cb-Cb",
    group = 
"""
1 * Cb u0 {2,S}
2   Cb u0 {1,S}
""",
    solute = SoluteData(
        S = 0.18156948412074247,
        B = 0.02813193473236902,
        E = 0.09905660113011927,
        L = 0.649692220729015,
        A = 0.023307114836825328,
    ),
    )


entry(
    index = 383,
    label = "Cs-(Cds-Cds)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.0599025153168235,
        B = 0.1424062294549058,
        E = 0.15059215450949281,
        L = 0.6415489938645546,
        A = -0.05945993569839768,
    ),
    )


entry(
    index = 382,
    label = "Cs-(Cds-Cd)CbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = u"Cs-(Cds-Cds)CbHH",
)


entry(
    index = 380,
    label = "Cs-CbCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)CbHH",
)


entry(
    index = 518,
    label = "Cs-CbCbCbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.376893282988189,
        B = 0.1851966393742619,
        E = 0.18248944576721476,
        L = 0.25325131164943615,
        A = 0.07883192399983552,
    ),
    )


entry(
    index = 3,
    label = "Cbf-CbCbCbf",
    group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cb  u0 {1,B}
4   Cbf u0 {1,B}
""",
    solute = SoluteData(
        S = 0.2674782588954025,
        B = -0.028173580848631592,
        E = 0.318120486923846,
        L = 0.5360328416354776,
        A = 0.017122275021834707,
    ),
    )


entry(
    index = 2,
    label = "Cbf",
    group = 
"""
1 * Cbf u0
""",
    solute = u"Cbf-CbCbCbf",
)


entry(
    index = 432,
    label = "Cs-CbCbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.3030559086989299,
        B = 0.05857457691314788,
        E = 0.13991553292821562,
        L = 0.7758423641705412,
        A = 0.009646332375142785,
    ),
    )


entry(
    index = 519,
    label = "Cs-CCCC",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   C  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.18805916461850014,
        B = 0.28550678127723306,
        E = 0.17755820087545926,
        L = 0.6679917501786721,
        A = 0.1182133638786369,
    ),
    )


entry(
    index = 388,
    label = "Cs-CbCbHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.23696208525820794,
        B = -0.0015744117794760232,
        E = 0.22570858233852675,
        L = 0.967475110176238,
        A = -0.018926210637968177,
    ),
    )


entry(
    index = 426,
    label = "Cs-(Cds-Cds)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.03280758371567577,
        B = 0.16697797904196254,
        E = -0.011893185451660404,
        L = 0.4178018683860407,
        A = -0.00958827848506294,
    ),
    )


entry(
    index = 425,
    label = "Cs-(Cds-Cd)CbCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
""",
    solute = u"Cs-(Cds-Cds)CbCsH",
)


entry(
    index = 423,
    label = "Cs-CbCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)CbCsH",
)


entry(
    index = 4,
    label = "Cbf-CbCbfCbf",
    group = 
"""
1 * Cbf u0 {2,B} {3,B} {4,B}
2   Cb  u0 {1,B}
3   Cbf u0 {1,B}
4   Cbf u0 {1,B}
""",
    solute = SoluteData(
        S = 0.2646637296994367,
        B = -0.019849620711917513,
        E = 0.36077558210885874,
        L = 0.5871537938163469,
        A = 0.02143253279455637,
    ),
    )


entry(
    index = 1817,
    label = "N3s-CbHH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2128225074714188,
        B = 0.2526305776010523,
        E = 0.31088286213934513,
        L = 0.992150180561995,
        A = 0.19318149852760794,
    ),
    )


entry(
    index = 1821,
    label = "Cb-N3s",
    group = 
"""
1 * Cb  u0 {2,S}
2   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.33032712957352256,
        B = 0.03344814231844764,
        E = 0.06706054441443156,
        L = 0.7784201932270324,
        A = -0.020885325943328,
    ),
    )


entry(
    index = 5,
    label = "Cbf-CbfCbfCbf",
    group = 
"""
1  * Cbf u0 p0 c0 {2,B} {3,B} {6,B}
2    Cbf u0 p0 c0 {1,B} {4,B} {5,B}
3    Cbf u0 p0 c0 {1,B} {8,B} {9,B}
4    Cbf u0 p0 c0 {2,B} {10,B} {11,B}
5    Cbf u0 p0 c0 {2,B} {13,B} {14,B}
6    Cbf u0 p0 c0 {1,B} {15,B} {16,B}
7    C   u0 p0 c0 {8,B} {16,B}
8    C   u0 p0 c0 {3,B} {7,B}
9    C   u0 p0 c0 {3,B} {10,B}
10   C   u0 p0 c0 {4,B} {9,B}
11   C   u0 p0 c0 {4,B} {12,B}
12   C   u0 p0 c0 {11,B} {13,B}
13   C   u0 p0 c0 {5,B} {12,B}
14   C   u0 p0 c0 {5,B} {15,B}
15   C   u0 p0 c0 {6,B} {14,B}
16   C   u0 p0 c0 {6,B} {7,B}
""",
    solute = SoluteData(
        S = 0.26767767203906373,
        B = -0.10906487680939055,
        E = 0.48860602573777334,
        L = -0.03614768233050503,
        A = 0.01120679763436715,
    ),
    )


entry(
    index = 2,
    label = "Cbf",
    group = 
"""
1 * Cbf u0
""",
    solute = SoluteData(
        S = 0.20915146580565075,
        B = -0.10931177596717807,
        E = 0.32337308981282503,
        L = 0.05090711999214559,
        A = 0.00404268001500618,
    ),
    )


entry(
    index = 1131,
    label = "O2s-CbCb",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.9861795468959604,
        B = -0.23155023071043684,
        E = 0.6736429608658729,
        L = 0.3697534978727556,
        A = 0.01637963986632742,
    ),
    )


entry(
    index = 561,
    label = "Cs-CbCtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.46965640244481055,
        B = 0.6276759747587248,
        E = 0.1990626988990153,
        L = 1.3269349054128234,
        A = 0.23521202616777173,
    ),
    )


entry(
    index = 243,
    label = "Cds-CdsCbCb",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cb u0 {1,S}
4   Cb u0 {1,S}
""",
    solute = SoluteData(
        S = -0.16508051508939353,
        B = 0.1751384435084849,
        E = -0.008752074365636298,
        L = 0.13640734531512289,
        A = 0.02364002253140386,
    ),
    )


entry(
    index = 1072,
    label = "Cs-CbCsOsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   O2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.480125151708637,
        B = 0.24788549247221198,
        E = -0.1025064108808243,
        L = 0.8247667847223752,
        A = 0.17861434688896483,
    ),
    )


entry(
    index = 850,
    label = "Cs-CbCsCsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.683992111823051,
        B = 0.12107398126483909,
        E = -0.09261079828376056,
        L = 0.7489819464537932,
        A = 0.1491110523019412,
    ),
    )


entry(
    index = 381,
    label = "Cs-(Cds-O2d)CbHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CO  u0 {1,S} {6,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.08394724767191142,
        B = 0.14210926848613403,
        E = 0.09347373267424691,
        L = 0.7349380857557088,
        A = 0.028738206990184176,
    ),
    )


entry(
    index = 1819,
    label = "N3s-CbCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.04803540742893092,
        B = 0.012035576533221678,
        E = 0.26224523051247917,
        L = 0.6080756814128914,
        A = 0.33308868812871567,
    ),
    )


entry(
    index = 238,
    label = "Cds-Cds(Cds-Cds)Cb",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.17652391406263268,
        B = 0.16418576971102944,
        E = 0.03851473916434206,
        L = 0.6209480613422969,
        A = 0.12251323821905526,
    ),
    )


entry(
    index = 237,
    label = "Cds-Cds(Cds-Cd)Cb",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Cb u0 {1,S}
5   C  u0 {2,D}
""",
    solute = u"Cds-Cds(Cds-Cds)Cb",
)


entry(
    index = 235,
    label = "Cds-CdsCbCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = u"Cds-Cds(Cds-Cds)Cb",
)


entry(
    index = 85,
    label = "Cds-OdCdsCds",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = -0.2870068991778536,
        B = 0.07796892580626857,
        E = -0.042043671816779205,
        L = 0.14736774150859733,
        A = 0.10896537566953461,
    ),
    )


entry(
    index = 93,
    label = "Cds-O2d(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   Cd  u0 {3,D}
6   Cd  u0 {4,D}
""",
    solute = SoluteData(
        S = 0.13550300559072487,
        B = -0.04138288445414867,
        E = 0.11068867695337645,
        L = 0.7000143346505407,
        A = -0.0024593362658544976,
    ),
    )


entry(
    index = 92,
    label = "Cds-O2d(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * CO  u0 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,S} {6,D}
5   C   u0 {3,D}
6   C   u0 {4,D}
""",
    solute = u"Cds-O2d(Cds-Cds)(Cds-Cds)",
)


entry(
    index = 235,
    label = "Cds-CdsCbCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Cb      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.03997272247846417,
        B = 0.2840205070948774,
        E = 0.03370249636563874,
        L = 0.4947804490134111,
        A = 0.017363566091889448,
    ),
    )


entry(
    index = 1115,
    label = "O2s-CC",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.422413105391416,
        B = -0.07901125824001284,
        E = 0.29658050945203907,
        L = 0.2907467624450265,
        A = -0.043870449163375645,
    ),
    )


entry(
    index = 1818,
    label = "N3s-CbCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.051180872441117645,
        B = 0.053893042387591156,
        E = 0.27976996077411725,
        L = 0.7276728073339981,
        A = 0.2577139576785884,
    ),
    )


entry(
    index = 178,
    label = "Cds-CdsCbOs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cb  u0 {1,S}
4   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.08095618220078937,
        B = 0.09309071540585824,
        E = 0.052490336234710236,
        L = 0.5023351335586136,
        A = -0.04380400347380553,
    ),
    )


entry(
    index = 1839,
    label = "Cb-(CtN3t)",
    group = 
"""
1 * Cb  u0 {2,S}
2   Ct  u0 {1,S} {3,T}
3   N3t u0 {2,T}
""",
    solute = SoluteData(
        S = 0.22763855853532597,
        B = 0.09898029342738564,
        E = 0.019480593254957206,
        L = 0.6206296042763836,
        A = 0.11912198935753354,
    ),
    )


entry(
    index = 423,
    label = "Cs-CbCdsCsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.24921651530076044,
        B = 0.11926538599170816,
        E = 0.07859075596067744,
        L = 1.0030238288206386,
        A = 0.09407635833113567,
    ),
    )


entry(
    index = 553,
    label = "Cs-CbCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = 0.3687022983072419,
        B = 0.21411329849514144,
        E = 0.20297351944880077,
        L = 1.2104469721720224,
        A = 0.14405886119014288,
    ),
    )


entry(
    index = 387,
    label = "Cs-CbCtHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Ct u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.09441213638305873,
        B = 0.13901134709383084,
        E = 0.16432627850064568,
        L = 0.8359276548904961,
        A = -0.059163509317695165,
    ),
    )


entry(
    index = 1852,
    label = "Ct-N3tOs",
    group = 
"""
1 * Ct  u0 {2,T} {3,S}
2   N3t u0 {1,T}
3   O2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.6915212147828939,
        B = 0.519208884835395,
        E = 0.2479102460774542,
        L = 1.7890227272914925,
        A = 0.44216075028748303,
    ),
    )


entry(
    index = 1912,
    label = "N3d-CbR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cb  u0 {1,S}
3   R!H u0 {1,D}
""",
    solute = SoluteData(
        S = -0.23622096194370767,
        B = 0.1339019727742625,
        E = 0.11123818597705934,
        L = 0.19381986158472506,
        A = 0.012119300751383111,
    ),
    )


entry(
    index = 6,
    label = "Cb",
    group = 
"""
1 * Cb u0
""",
    solute = SoluteData(
        S = 0.40651791793953324,
        B = 0.02728796565663333,
        E = 0.05992039186372425,
        L = 0.8679425423576561,
        A = 0.020415926230628174,
    ),
    )


entry(
    index = 1924,
    label = "Cds-CCN",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   N  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.15613442307380393,
        B = 0.12370142649459688,
        E = 0.0541628381388439,
        L = 0.6134853322600321,
        A = -0.02111035147261006,
    ),
    )


entry(
    index = 137,
    label = "Cds-CdsCdsH",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.017045487655742656,
        B = 0.12585897495016946,
        E = 0.04762727711094644,
        L = 0.4956704985505885,
        A = 0.005245644969681375,
    ),
    )


entry(
    index = 528,
    label = "Cs-CtCsCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Ct u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.22115807495365652,
        B = 0.25257049694180445,
        E = 0.26324337741271886,
        L = 1.2719313980431535,
        A = 0.01861400065476021,
    ),
    )


entry(
    index = 1820,
    label = "N3s-CbCbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.39942797170835076,
        B = 0.010078332456806564,
        E = 0.286553676904022,
        L = 1.0832166494637583,
        A = 0.3051465690083045,
    ),
    )


entry(
    index = 1814,
    label = "N3s-N3sCbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N3s u0 {1,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.05521984398601747,
        B = 0.20959010556726873,
        E = 0.26368630859033915,
        L = 0.7247274609298302,
        A = 0.16028848506091548,
    ),
    )


entry(
    index = 1940,
    label = "N3s-NCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1828,
    label = "N3s-(CO)CbH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   CO  u0 {1,S} {5,D}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.023305591306994555,
        B = 0.17332380951374274,
        E = 0.15450241093865183,
        L = 0.7559473903257337,
        A = 0.4288562605510648,
    ),
    )


entry(
    index = 389,
    label = "Cs-CCCH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.02113236205102259,
        B = 0.2872881887707217,
        E = 0.13940249998543397,
        L = 0.8837452239738912,
        A = -0.006414499085536998,
    ),
    )


entry(
    index = 1945,
    label = "O2s-N",
    group = 
"""
1 * O2s u0 {2,S}
2   N   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5882710669722634,
        B = 0.22517544633968206,
        E = 0.3849228269463869,
        L = 1.2497758652393214,
        A = 0.1922640705393514,
    ),
    )


entry(
    index = 1888,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    solute = SoluteData(
        S = -0.9050612707351176,
        B = 0.31188427134567487,
        E = -0.05399829091911655,
        L = -0.2987790903604344,
        A = 0.17938149127066788,
    ),
    )


entry(
    index = 1940,
    label = "N3s-NCH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.17674248604777615,
        B = 0.08115501480176004,
        E = 0.22550700366000215,
        L = 0.9001122863585567,
        A = 0.3322437079687421,
    ),
    )


entry(
    index = 212,
    label = "Cds-Cds(Cds-O2d)(Cds-Cds)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   Cd  u0 {3,D}
6   O2d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.007085486466144389,
        B = 0.10916496991084312,
        E = 0.04478113566232851,
        L = 0.4915209338113762,
        A = -0.066178501989258,
    ),
    )


entry(
    index = 211,
    label = "Cds-Cds(Cds-O2d)(Cds-Cd)",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   CO  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {5,D}
4   Cd  u0 {1,D}
5   C   u0 {3,D}
6   O2d u0 {2,D}
""",
    solute = u"Cds-Cds(Cds-O2d)(Cds-Cds)",
)


entry(
    index = 209,
    label = "Cds-CdsCdsCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = u"Cds-Cds(Cds-Cds)(Cds-Cds)",
)


entry(
    index = 11,
    label = "Cb-Cds",
    group = 
"""
1 * Cb         u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.06918616675843645,
        B = 0.06635417153518532,
        E = 0.08372573300930806,
        L = 0.6422708713867056,
        A = 0.06840928802150274,
    ),
    )


entry(
    index = 1923,
    label = "Cds-CNH",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   N  u0 {1,S}
4   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.1572100293636227,
        B = 0.1310856432541848,
        E = 0.07846905085435807,
        L = 0.659120511886745,
        A = -0.03229823539101577,
    ),
    )


entry(
    index = 1864,
    label = "Cs-(CdN3d)CsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    solute = SoluteData(
        S = 0.03742644483359077,
        B = 0.1355923309693925,
        E = -0.02768768758723599,
        L = 0.5163916825147838,
        A = 0.0246990502578512,
    ),
    )


entry(
    index = 1855,
    label = "Cd-N3dCsCs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.1112225878591653,
        B = 0.012862047571323264,
        E = -0.06405302078980477,
        L = 0.21104840817397894,
        A = 0.02214257606162187,
    ),
    )


entry(
    index = 1812,
    label = "N3s-N3sCsH",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   H   u0 {1,S}
4   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.17711747107416534,
        B = 0.4017013642965962,
        E = 0.1254699023900724,
        L = 0.8795910964414086,
        A = 0.17152037798309383,
    ),
    )


entry(
    index = 1084,
    label = "Cs-CdsOsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   O2s     u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.1979720575617241,
        B = 0.15257510771626356,
        E = -0.27846763026366195,
        L = 0.33818193334725055,
        A = 0.1530388492910235,
    ),
    )


entry(
    index = 1862,
    label = "Cs-(CdN3d)HHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
""",
    solute = SoluteData(
        S = -0.04247718995848413,
        B = 0.05335404689545457,
        E = -0.010141366531176175,
        L = 0.4410835915177297,
        A = -0.03138666472760324,
    ),
    )


entry(
    index = 1898,
    label = "N3s-(CdCd)CsCs",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.05289192707840458,
        B = 0.02925628336229237,
        E = 0.20211500263983045,
        L = 0.6585664574888561,
        A = 0.43124527881430363,
    ),
    )


entry(
    index = 1136,
    label = "S2s-CbH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.2161487947706454,
        B = -0.16837694389491437,
        E = 0.4112547018398815,
        L = 0.795134667843814,
        A = -0.040072796964572416,
    ),
    )


entry(
    index = 1140,
    label = "S2s-CsCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.4528390039071464,
        B = -0.11289703042796484,
        E = 0.31259814467772745,
        L = -0.016291170646929032,
        A = -0.35396681050871026,
    ),
    )


entry(
    index = 2001,
    label = "S4d-OdCC",
    group = 
"""
1 * S4d u0 p1 {2,D} {3,S} {4,S}
2   O2d u0 {1,D}
3   C   ux {1,S}
4   C   ux {1,S}
""",
    solute = SoluteData(
        S = -0.012841310412733408,
        B = 0.19580643468566522,
        E = 0.18197800048372187,
        L = 0.47378194383251293,
        A = -0.13940917503546815,
    ),
    )


entry(
    index = 2013,
    label = "S6dd-OdOdCC",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D} {4,S} {5,S}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
4   C    ux {1,S}
5   C    ux {1,S}
""",
    solute = SoluteData(
        S = -0.04929382663498108,
        B = -0.3236175622479156,
        E = -0.08607841333561764,
        L = -0.05408238567724763,
        A = 0.17503199020990723,
    ),
    )


entry(
    index = 2044,
    label = "S6dd-OdOd",
    group = 
"""
1 * S6dd u0 p0 {2,D} {3,D}
2   O2d  ux {1,D}
3   O2d  ux {1,D}
""",
    solute = SoluteData(
        S = 1.1455503034236159,
        B = -0.338620637884072,
        E = 0.10232634937364662,
        L = 1.1388997596188792,
        A = 0.2822532047981598,
    ),
    )


entry(
    index = 1103,
    label = "O2s-CdsH",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.39866822292497905,
        B = 0.15046645353581237,
        E = 0.15640799926647192,
        L = 0.813268239454422,
        A = 0.22057808953920385,
    ),
    )


entry(
    index = 209,
    label = "Cds-CdsCdsCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = -0.03052742895836663,
        B = 0.18415104605236707,
        E = -0.01273056970123665,
        L = 0.374942080593767,
        A = -0.01864343981608428,
    ),
    )


entry(
    index = 562,
    label = "Cs-CbCbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cb u0 {1,S}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
""",
    solute = SoluteData(
        S = 0.4924946395237318,
        B = 0.34393226985472947,
        E = 0.22456844025733008,
        L = 1.1420284109517551,
        A = 0.25047124016651323,
    ),
    )


entry(
    index = 851,
    label = "Cs-CdsCdsCsOs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   O2s     u0 {1,S}
""",
    solute = SoluteData(
        S = -0.1629181799324099,
        B = 0.026940348779406792,
        E = -0.03442106991266092,
        L = 0.39298771064041715,
        A = -0.255812059639148,
    ),
    )


entry(
    index = 1860,
    label = "Cd-CdHN3s",
    group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.13378084621463593,
        B = 0.10970450401364215,
        E = 0.07059659132829027,
        L = 0.5539181101836925,
        A = -0.06808334757036352,
    ),
    )


entry(
    index = 1098,
    label = "O2s-HH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.016320272850541634,
        B = -0.0005089993781796434,
        E = -0.0754739749756509,
        L = 0.0382182401844723,
        A = 0.0348135763534409,
    ),
    )


entry(
    index = 1126,
    label = "O2s-CdsCs",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = -0.3318726565117219,
        B = -0.02283684727764465,
        E = 0.20521083393825873,
        L = 0.1980527750118617,
        A = -0.12702379401665384,
    ),
    )


entry(
    index = 170,
    label = "Cds-CdsCdsOs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    solute = SoluteData(
        S = 0.12753347391512668,
        B = 0.0953688254499516,
        E = 0.21814661735560184,
        L = 0.9705537622622331,
        A = 0.020049399592382486,
    ),
    )


entry(
    index = 1166,
    label = "Cs-CbSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.45637002298589807,
        B = 0.08121131145581167,
        E = 0.17544482221138186,
        L = 1.6861113678821023,
        A = 0.33491704895661495,
    ),
    )


entry(
    index = 1146,
    label = "S2s-CbCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cb  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.7546472184259692,
        B = -0.3124233356475785,
        E = 0.34599701046459824,
        L = 0.08122940545087956,
        A = 0.00721807834670447,
    ),
    )


entry(
    index = 1145,
    label = "S2s-CtCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.02633933982823921,
        B = -0.3385025234300235,
        E = 0.601861714255426,
        L = 1.289911377658591,
        A = -0.17229296821347623,
    ),
    )


entry(
    index = 1940,
    label = "N3s-NCC",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.0887558959167197,
        B = 0.21966605511223097,
        E = 0.38964277869827696,
        L = 0.8137503330552882,
        A = 0.0963414594010301,
    ),
    )


entry(
    index = 1935,
    label = "O2s-CN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   C   u0 {1,S}
3   N   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.019706141369486535,
        B = -0.039822299828625035,
        E = 0.1312133897717019,
        L = 0.35785413090649587,
        A = -0.1054457892814793,
    ),
    )


entry(
    index = 202,
    label = "Cds-CdsCdsCs",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = 0.12334790801098416,
        B = 0.11189256336252996,
        E = -0.07251730005514297,
        L = 0.47507120905533473,
        A = 0.003961355156224325,
    ),
    )


entry(
    index = 1138,
    label = "S2s-CsCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   Cd  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.10956496432752055,
        B = -0.06846791692182679,
        E = 0.27499875720464156,
        L = 0.34197292878218244,
        A = -0.44921230166874976,
    ),
    )


entry(
    index = 1941,
    label = "N3s-NCdCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cd  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2834689653704807,
        B = 0.2641050258306068,
        E = 0.4402609382004234,
        L = 1.1937798442074734,
        A = 0.010160223528582972,
    ),
    )


entry(
    index = 1822,
    label = "N3d-N3dN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   N3d u0 {1,D}
3   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.4116826393410578,
        B = 0.17557713920644602,
        E = 0.20597862521903507,
        L = 1.1369712443039668,
        A = 0.1221230385204426,
    ),
    )


entry(
    index = 1165,
    label = "Cs-CtSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Ct  u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2502847761326399,
        B = -0.34805722739651596,
        E = -0.16281543171286256,
        L = 0.4903567553189372,
        A = 0.12061786321365052,
    ),
    )


entry(
    index = 1896,
    label = "N3s-CsCs(N3dOd)",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   N3d u0 {1,S} {5,D}
5   O2d u0 {4,D}
""",
    solute = SoluteData(
        S = 0.041670753032611745,
        B = 0.34865503290025734,
        E = 0.14956925078673147,
        L = 0.6389471041170941,
        A = 0.1910544190568772,
    ),
    )


entry(
    index = 1893,
    label = "N3s-NCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1910,
    label = "N3d-OdN3s",
    group = 
"""
1 * N3d u0 {2,D} {3,S}
2   O2d u0 {1,D}
3   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.39887499154659595,
        B = -0.16494907756761212,
        E = 0.1800384110916115,
        L = 0.8870644759342239,
        A = 0.09935271712548085,
    ),
    )


entry(
    index = 1932,
    label = "Cds-(Cds-Os)CbH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D} {5,S}
3   Cb  u0 {1,S}
4   H   u0 {1,S}
5   O2s u0 {2,S}
""",
    solute = SoluteData(
        S = -0.21517086700615823,
        B = 0.10163113493253126,
        E = -0.05548696999622357,
        L = 0.014745644259316126,
        A = -0.08108928901530299,
    ),
    )


entry(
    index = 217,
    label = "Cds-Cds(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   Cd u0 {2,D}
6   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = 0.17277202074430695,
        B = 0.07792888569583485,
        E = 0.09378609406810362,
        L = 0.6609172851656846,
        A = 0.028578600126531007,
    ),
    )


entry(
    index = 216,
    label = "Cds-Cds(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,S} {6,D}
4   Cd u0 {1,D}
5   C  u0 {2,D}
6   C  u0 {3,D}
""",
    solute = u"Cds-Cds(Cds-Cds)(Cds-Cds)",
)


entry(
    index = 173,
    label = "Cds-Cds(Cds-Cds)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   Cd  u0 {2,D}
""",
    solute = SoluteData(
        S = 0.39657619484995665,
        B = 0.08768920261741717,
        E = 0.1982747964728306,
        L = 1.2139692793526438,
        A = 0.28370386234957085,
    ),
    )


entry(
    index = 172,
    label = "Cds-Cds(Cds-Cd)O2s",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,D}
4   O2s u0 {1,S}
5   C   u0 {2,D}
""",
    solute = u"Cds-Cds(Cds-Cds)O2s",
)


entry(
    index = 226,
    label = "Cds-CdsCtCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5198409336460749,
        B = 0.18372471039728858,
        E = 0.05566125357873409,
        L = 1.0085279109437555,
        A = 0.05372155288051664,
    ),
    )


entry(
    index = 229,
    label = "Cds-Cds(Cds-Cds)Ct",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 0.7655838122949516,
        B = 0.048935494738087164,
        E = 0.10959027301009734,
        L = 1.2674592623883445,
        A = 0.04308743323066683,
    ),
    )


entry(
    index = 228,
    label = "Cds-CdsCt(Cds-Cd)",
    group = 
"""
1 * Cd u0 {2,S} {3,D} {4,S}
2   Cd u0 {1,S} {5,D}
3   Cd u0 {1,D}
4   Ct u0 {1,S}
5   C  u0 {2,D}
""",
    solute = u"Cds-Cds(Cds-Cds)Ct",
)


entry(
    index = 1900,
    label = "N3s-(CdCd)CsN3s",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.10770650084065952,
        B = 0.3251918903233371,
        E = -0.12550903259693352,
        L = 0.1876204364158236,
        A = 0.19697888252657075,
    ),
    )


entry(
    index = 1859,
    label = "Cd-CdCsN3s",
    group = 
"""
1 * Cd  u0 {2,D} {5,S} {6,S}
2   Cd  u0 {1,D} {3,S} {4,S}
3   R   u0 {2,S}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2912227603772067,
        B = 0.0849404196936073,
        E = 0.05569793662447388,
        L = 0.7491119252276477,
        A = -0.04624457933198731,
    ),
    )


entry(
    index = 1135,
    label = "S2s-CtH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Ct  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.7600519404046293,
        B = 0.07882002529567725,
        E = 0.6454011258385005,
        L = 2.703481678284068,
        A = 0.6013795279096188,
    ),
    )


entry(
    index = 1937,
    label = "O2s-NN",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N   u0 {1,S}
3   N   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.38327962515418496,
        B = 0.10364198342806141,
        E = 0.2820827888760842,
        L = 0.27526674411381935,
        A = 0.04390938641169456,
    ),
    )


entry(
    index = 450,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    solute = SoluteData(
        S = -0.38327962515418557,
        B = 0.10364198342806161,
        E = 0.2820827888760848,
        L = 0.27526674411382257,
        A = 0.04390938641169566,
    ),
    )


entry(
    index = 449,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
)


entry(
    index = 433,
    label = "Cs-CdsCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
)


entry(
    index = 1874,
    label = "O2s-CsN3s",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   N3s u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.450916143715174,
        B = 0.12813061754016933,
        E = 0.5970226066139421,
        L = 1.0690320171022807,
        A = -0.1810459200690338,
    ),
    )


entry(
    index = 1175,
    label = "Cs-CsCsCsS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   S  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.3569565551947327,
        B = -0.13619622529850875,
        E = -0.2982966468953846,
        L = -0.22111524511714498,
        A = 0.5958661246777496,
    ),
    )


entry(
    index = -1,
    label = "Cs-CCCS",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   C  u0 {1,S}
5   S  u0 {1,S}
""",
    solute = u"Cs-CsCsCsS",
)


entry(
    index = 1175,
    label = "Cs-CsCsCsS2",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   S2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.6597048887324907,
        B = 0.2484603239111828,
        E = 0.1173761804826958,
        L = 1.5400067893819331,
        A = 0.47380383394624753,
    ),
    )


entry(
    index = 67,
    label = "Cds-OdCdsOs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
""",
    solute = SoluteData(
        S = 0.3792063846061014,
        B = 0.18363256988349014,
        E = 0.11852538145631568,
        L = 0.8765784453253261,
        A = 0.03275270018257624,
    ),
    )


entry(
    index = 1899,
    label = "N3s-(CdCd)CsH",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   Cs  u0 {1,S}
6   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.36513899171078107,
        B = 0.08819233834236948,
        E = 0.09450483863650447,
        L = 0.9474985330111153,
        A = 0.3600791706355209,
    ),
    )


entry(
    index = 1172,
    label = "Cs-CbCsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cb  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.1783455721332315,
        B = 0.2060152223568904,
        E = 0.5026773293801252,
        L = 1.5538829286966467,
        A = 0.32424352841990256,
    ),
    )


entry(
    index = -1,
    label = "Cs-CCSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = u"Cs-CsCsSH",
)


entry(
    index = 433,
    label = "Cs-CdsCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = -0.7464258130771685,
        B = 0.37510012949435156,
        E = 0.17785413894223873,
        L = 0.13253250825503038,
        A = -0.027839559617060056,
    ),
    )


entry(
    index = 354,
    label = "Cs-CdsCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = -0.24788215739961023,
        B = 0.28304723685208544,
        E = 0.08560773389717244,
        L = 0.5067702972287942,
        A = -0.1194543409341037,
    ),
    )


entry(
    index = 1169,
    label = "Cs-CsCsS2H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5450524647668932,
        B = 0.1665439868059026,
        E = 0.10553316799494677,
        L = 1.478166391673851,
        A = 0.4119948517280676,
    ),
    )


entry(
    index = 1169,
    label = "Cs-CsCsSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S}
3   Cs u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = u"Cs-CsCsS2H",
)


entry(
    index = 1928,
    label = "Cs-N3dCsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   N3d u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5056343476017979,
        B = 0.040618152675351404,
        E = -0.21980306946463402,
        L = 0.9910672898812359,
        A = -0.18319869013001358,
    ),
    )


entry(
    index = 380,
    label = "Cs-CbCdsHH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   H       u0 {1,S}
5   H       u0 {1,S}
""",
    solute = SoluteData(
        S = 0.10725149251304988,
        B = -0.07441760992413073,
        E = 0.04505508319877924,
        L = 0.9557834280114053,
        A = 0.13825228105137344,
    ),
    )


entry(
    index = -1,
    label = "Cs-CCSH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   C  u0 {1,S}
3   C  u0 {1,S}
4   S  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.8471214362802257,
        B = 0.09047205574214491,
        E = 0.2701917324589999,
        L = 2.2764117932576964,
        A = 0.5169005976957107,
    ),
    )


entry(
    index = 1865,
    label = "Cs-(CdN3d)CsCsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   H   u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    solute = SoluteData(
        S = 0.5150484877718924,
        B = 0.15138996554601464,
        E = 0.15022622411494777,
        L = 1.0677210384840858,
        A = -0.0338506522421263,
    ),
    )


entry(
    index = 1452,
    label = "Cs-CsOsS2H",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.6140588598195716,
        B = -0.11186820463848828,
        E = -0.06847826498988273,
        L = 1.2454046986620186,
        A = 0.6624087798909557,
    ),
    )


entry(
    index = 1452,
    label = "Cs-CsOsSH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cs  u0 {1,S}
3   O2s u0 {1,S}
4   S   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = u"Cs-CsOsS2H",
)


entry(
    index = -1,
    label = "Cs-COsSH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   S   u0 {1,S}
5   H   u0 {1,S}
""",
    solute = u"Cs-CsOsSH",
)


entry(
    index = 1901,
    label = "N3s-(CdCd)HN3s",
    group = 
"""
1 * N3s u0 {2,S} {5,S} {6,S}
2   Cd  u0 {1,S} {3,D} {4,S}
3   Cd  u0 {2,D}
4   R   u0 {2,S}
5   H   u0 {1,S}
6   N3s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.13950040841677958,
        B = 0.014773186147527519,
        E = 0.18701275234956638,
        L = 0.094795282089634,
        A = 0.157772652018009,
    ),
    )


entry(
    index = 556,
    label = "Cs-(Cds-Cds)CbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    solute = SoluteData(
        S = 1.1246945835692428,
        B = -0.06834134577873274,
        E = -0.06976849566151319,
        L = 1.0987606196950808,
        A = 0.2684580983055458,
    ),
    )


entry(
    index = 555,
    label = "Cs-(Cds-Cd)CbCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cb u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    solute = u"Cs-(Cds-Cds)CbCsCs",
)


entry(
    index = 1181,
    label = "Cds-CdsCsS2",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    solute = SoluteData(
        S = -0.026825349995100188,
        B = -0.011211472651539208,
        E = -0.012333740092320501,
        L = 0.3823736733718368,
        A = 0.01573180119192242,
    ),
    )


entry(
    index = 1181,
    label = "Cds-CdsCsSs",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4   S  u0 {1,S}
""",
    solute = u"Cds-CdsCsS2",
)


entry(
    index = -1,
    label = "Cds-CdCS",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {4,S}
2   C  u0 {1,D}
3   C  u0 {1,S}
4   S  u0 {1,S}
""",
    solute = None,
)


entry(
    index = 1143,
    label = "S2s-CdCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.1995804581820876,
        B = -0.1325393450712009,
        E = 0.2561494375816057,
        L = 0.7664983193973043,
        A = -0.14623939931020263,
    ),
    )


entry(
    index = 78,
    label = "Cds-OdCdsCs",
    group = 
"""
1 * CO      u0 {2,D} {3,S} {4,S}
2   O2d     u0 {1,D}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0778909421158693,
        B = 0.05197441218783918,
        E = 0.18299961650259727,
        L = 0.6128105950417962,
        A = 0.007545267789981852,
    ),
    )


entry(
    index = 1933,
    label = "Cs-NNCsH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   N  u0 {1,S}
4   Cs u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2943609248338298,
        B = 0.4926077404314505,
        E = -0.12606351229462584,
        L = 0.3288306420991319,
        A = -0.3377610348410798,
    ),
    )


entry(
    index = 538,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = 1.146786835926914,
        B = 0.2331623092205972,
        E = 0.3527781042983569,
        L = 0.8200715389940614,
        A = 0.375452831518661,
    ),
    )


entry(
    index = 537,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)CsCs",
)


entry(
    index = 530,
    label = "Cs-CdsCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = -0.017775735048488617,
        B = 0.20931975373867684,
        E = -0.10472741384605519,
        L = 0.3765241611648794,
        A = 0.33881015519132585,
    ),
    )


entry(
    index = 563,
    label = "Cs-CdsCdsCdsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   Cs      u0 {1,S}
""",
    solute = SoluteData(
        S = 0.24589755259763107,
        B = 0.4508165019303533,
        E = 0.40139767047555763,
        L = 1.0819226452281316,
        A = 0.006184214400441895,
    ),
    )


entry(
    index = 1122,
    label = "O2s-CdsCds",
    group = 
"""
1 * O2s     u0 {2,S} {3,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
""",
    solute = SoluteData(
        S = -0.36187081448213493,
        B = -0.30950022034309693,
        E = 0.08802313703340454,
        L = 0.08917429809759253,
        A = 0.1962410614875744,
    ),
    )


entry(
    index = 1866,
    label = "Cs-(CdN3d)CsCsCs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D} {7,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   Cs  u0 {1,S}
6   N3d u0 {2,D}
7   R   u0 {2,S}
""",
    solute = SoluteData(
        S = 0.3875932937623118,
        B = 0.2709056662479846,
        E = -0.08150812994953947,
        L = 0.8371730264637574,
        A = 0.08859514559424157,
    ),
    )


entry(
    index = 1856,
    label = "Cd-N3dCsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   N3d u0 {1,D}
3   Cs  u0 {1,S}
4   H   u0 {1,S}
""",
    solute = SoluteData(
        S = -0.3931365921829727,
        B = 0.08929749104279731,
        E = -0.028675622045830018,
        L = 0.16115780773627597,
        A = 0.0194796332973084,
    ),
    )


entry(
    index = 1134,
    label = "S2s-CdH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   H   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.4307137205721421,
        B = 0.1755683052782913,
        E = 0.34805102469869137,
        L = 1.4524977340607808,
        A = -0.08522682699879348,
    ),
    )


entry(
    index = 1148,
    label = "S2s-S2sCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.17278916831612806,
        B = 0.01681625202128848,
        E = 0.23155698740916486,
        L = 0.24950342516535493,
        A = -0.3598948614767424,
    ),
    )


entry(
    index = -1,
    label = "S2s-S2sC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   C   u0 {1,S}
""",
    solute = u"S2s-S2sCs",
)


entry(
    index = 1151,
    label = "S2s-S2sCb",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cb  u0 {1,S}
""",
    solute = SoluteData(
        S = -0.22099430719252156,
        B = -0.06389049529251839,
        E = 0.3377423498581759,
        L = 0.7357435987255514,
        A = -0.0728304959288554,
    ),
    )


entry(
    index = 1152,
    label = "S2s-SsSs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   S2s u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0996795538872194,
        B = 0.11264880965578614,
        E = 0.3965024728713409,
        L = 1.1650225998923895,
        A = -0.0041162214562220556,
    ),
    )


entry(
    index = 1152,
    label = "S2s-SS",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S   ux {1,S}
3   S   ux {1,S}
""",
    solute = u"S2s-SsSs",
)


entry(
    index = 1167,
    label = "Cs-SsSsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   S  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.899488171390992,
        B = 0.12400323132906399,
        E = 0.22473189470121802,
        L = 2.301796571153439,
        A = 0.7148878886420258,
    ),
    )


entry(
    index = 1944,
    label = "O2d-N5dc",
    group = 
"""
1 * O2d  u0 {2,D}
2   N5dc u0 {1,D}
""",
    solute = SoluteData(
        S = -0.05323711083088481,
        B = -0.23373380099479102,
        E = 0.16287257868399402,
        L = 0.2370023724877336,
        A = -0.37687842389576975,
    ),
    )


entry(
    index = 1932,
    label = "Cs-N5dcCsCsCs",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   Cs   u0 {1,S}
5   Cs   u0 {1,S}
""",
    solute = SoluteData(
        S = 0.7293468263948929,
        B = 0.07067667706426002,
        E = -0.006155279187819232,
        L = 1.0441273826845734,
        A = 0.060598550854288565,
    ),
    )


entry(
    index = 1919,
    label = "Cs-NHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.2655283927212688,
        B = 0.10112876480844922,
        E = 0.04305339721549087,
        L = 0.7640303090131402,
        A = -0.07582687343985971,
    ),
    )


entry(
    index = 1919,
    label = "CJ2_singlet",
    group = 
"""
1 * C u0 p1
""",
    solute = SoluteData(
        S = -0.13571088039322196,
        B = -0.05689174786994966,
        E = 0.10743157581311454,
        L = 0.24300770104283573,
        A = -0.07105475756246488,
    ),
    )


entry(
    index = 1921,
    label = "Cs-NCsHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   N  u0 {1,S}
3   Cs u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.31972667156218537,
        B = 0.042652420722006354,
        E = 0.05258150092902092,
        L = 0.83576228235607,
        A = -0.040221694922162265,
    ),
    )


entry(
    index = 1926,
    label = "Cs-N5dcCsHH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    solute = SoluteData(
        S = 0.5548279463965562,
        B = 0.1760168085507567,
        E = -0.013038476994465684,
        L = 1.0925811330751487,
        A = -0.04172912125451941,
    ),
    )


entry(
    index = 1929,
    label = "Cs-N5dcCsCsH",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   N5dc u0 {1,S}
3   Cs   u0 {1,S}
4   Cs   u0 {1,S}
5   H    u0 {1,S}
""",
    solute = SoluteData(
        S = 0.6183148228804959,
        B = 0.20473590905967426,
        E = -0.01620269758739576,
        L = 1.229952431043524,
        A = 0.007791650484769493,
    ),
    )


entry(
    index = 1154,
    label = "S2s-(C=S2d)Cs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs  u0 {1,S}
3   CS  u0 {1,S} {4,D}
4   S2d u0 {3,D}
""",
    solute = SoluteData(
        S = -0.05050342121619761,
        B = -0.026117603391514033,
        E = 0.3140768578103957,
        L = 0.49012864337100304,
        A = -0.3339054649478014,
    ),
    )


entry(
    index = 1922,
    label = "N1dc",
    group = 
"""
1 * N1dc u0 p2 {2,D}
2   R!H  ux {1,D}
""",
    solute = SoluteData(
        S = -0.13414143880297436,
        B = -0.07977664760647665,
        E = 0.2168181082735448,
        L = 0.35714166893153076,
        A = -0.09923125254745133,
    ),
    )


entry(
    index = 1176,
    label = "Cs-C=SHHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   CS  u0 {1,S} {6,D}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
6   S2d u0 {2,D}
""",
    solute = SoluteData(
        S = 0.004151224905899205,
        B = 0.2219743552098975,
        E = 0.23673887080111786,
        L = 0.6705503605173065,
        A = -0.1910169006488292,
    ),
    )


entry(
    index = 1893,
    label = "N3s-NCsCs",
    group = 
"""
1 * N3s u0 {2,S} {3,S} {4,S}
2   N   u0 {1,S}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
""",
    solute = SoluteData(
        S = 0.15940315599414154,
        B = 0.06918608520625973,
        E = 0.048490264807414155,
        L = 0.6116410897259892,
        A = 0.2198593935199073,
    ),
    )


entry(
    index = 487,
    label = "Cs-(Cds-Cds)(Cds-Cds)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
""",
    solute = SoluteData(
        S = -0.17811155382872285,
        B = 0.20876771036262443,
        E = -0.00481929455187266,
        L = 0.196395362171784,
        A = 0.2155245629833072,
    ),
    )


entry(
    index = 486,
    label = "Cs-(Cds-Cd)(Cds-Cd)CbH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cb u0 {1,S}
5   H  u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)CbH",
)


entry(
    index = 479,
    label = "Cs-CbCdsCdsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Cb      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   [Cd,CO] u0 {1,S}
5   H       u0 {1,S}
""",
    solute = u"Cs-(Cds-Cds)(Cds-Cds)CbH",
)


entry(
    index = 1155,
    label = "S2s-(C=S2d)Cmb",
    group = 
"""
1 * S2s           u0 {2,S} {3,S}
2   [Cd,Cb,Ct,CO] u0 {1,S}
3   CS            u0 {1,S} {4,D}
4   S2d           u0 {3,D}
""",
    solute = SoluteData(
        S = -0.3532119503733878,
        B = -0.07179057708669978,
        E = 0.34497425491487843,
        L = 0.678196445201926,
        A = 0.24268925835553334,
    ),
    )


entry(
    index = 1911,
    label = "N3d-CsR",
    group = 
"""
1 * N3d u0 {2,S} {3,D}
2   Cs  u0 {1,S}
3   R!H u0 {1,D}
""",
    solute = SoluteData(
        S = -0.31023920990852183,
        B = 0.3117588802540209,
        E = 0.3380595539209284,
        L = 0.0025384978306891015,
        A = 0.36016851178471604,
    ),
    )


entry(
    index = 1149,
    label = "S2s-S2sCd",
    group = 
"""
1 * S2s        u0 {2,S} {3,S}
2   S2s        u0 {1,S}
3   [Cd,CO,CS] u0 {1,S}
""",
    solute = SoluteData(
        S = 0.19924726691539513,
        B = 0.020751386914279503,
        E = 0.4848331853323451,
        L = 1.550053870015726,
        A = 0.1500837421848292,
    ),
    )

tree(
"""
L1: R
	L2: N
		L3: N1dc
		L3: N3s
			L4: N3s-NCC
				L5: N3s-NCsCs
				L5: N3s-NCsCs
					L6: N3s-CsCs(N3dOd)
				L5: N3s-NCdCs
					L6: N3s-(CdCd)CsN3s
			L4: N3s-NCH
				L5: N3s-(CdCd)HN3s
				L5: N3s-N3sCsH
		L3: N3d
			L4: N3d-CsR
			L4: N3d-OdN3s
			L4: N3d-N3dN3s
			L4: N3d-CbR
			L4: N3d-OdOs
			L4: N3d-CsR
				L5: N3d-N3dCs
				L5: N3d-CdCs
			L4: N3d-CdH
		L3: N3t
		L3: N3t
			L4: N3t-CtH
	L2: S
		L3: S6dd
			L4: S6dd-OdOd
			L4: S6dd-OdOd
				L5: S6dd-OdOdCC
				L5: S6dd-OdOdCO
				L5: S6dd-OdOdCO
					L6: S6dd-OdOdCsOs
				L5: S6dd-OdOdOO
				L5: S6dd-OdOdCC
					L6: S6dd-OdOdCsCs
		L3: S4d
			L4: S4d-Od
				L5: S4d-OdCC
				L5: S4d-OdCS
				L5: S4d-OdCC
					L6: S4d-OdCsCs
		L3: S2s
			L4: S2s-SS
				L5: S2s-SsSs
			L4: S2s-SC
				L5: S2s-S2sC
					L6: S2s-S2sCd
					L6: S2s-S2sCb
					L6: S2s-S2sCs
				L5: S2s-S46C
			L4: S2s-CH
				L5: S2s-CdH
				L5: S2s-CtH
				L5: S2s-CbH
				L5: S2s-CsH
			L4: S2s-CC
				L5: S2s-(C=S2d)Cmb
				L5: S2s-(C=S2d)Cs
				L5: S2s-CdCb
				L5: S2s-CsCd
				L5: S2s-CtCb
				L5: S2s-CbCb
				L5: S2s-CsCb
				L5: S2s-CsCs
				L5: S2s-CsCt
				L5: S2s-Cs(C=O)
				L5: S2s-CdCd
	L2: N
		L3: N3s
			L4: N3s-NCH
				L5: N3s-N3sCbH
			L4: N3s-CCC
				L5: N3s-(CdCd)CsCs
				L5: N3s-CbCsCs
				L5: N3s-(CO)(CO)Cs
			L4: N3s-CCH
				L5: N3s-(CdCd)CsH
				L5: N3s-(CO)CbH
				L5: N3s-CbCbH
				L5: N3s-CbCsH
				L5: N3s-(CO)(CO)H
			L4: N3s-CHH
				L5: N3s-CbHH
				L5: N3s-(CO)HH
				L5: N3s-CdHH
			L4: N3s-CCH
				L5: N3s-(CO)CsH
				L5: N3s-CsCsH
			L4: N3s-CCC
				L5: N3s-(CO)CsCs
				L5: N3s-CsCsCs
			L4: N3s-CHH
				L5: N3s-CsHH
			L4: N3s-N3sHH
	L2: S
		L3: S2d
			L4: S2d-C
		L3: S4dd
			L4: S4dd-OdOd
	L2: C
		L3: CJ2_singlet
		L3: Cb
		L3: Cbf
		L3: Cbf
			L4: Cbf-CbfCbfCbf
			L4: Cbf-CbCbfCbf
			L4: Cbf-CbCbCbf
		L3: Cdd
			L4: Cdd-SdSd
				L5: Cdd-S2dS2d
		L3: Cs
			L4: Cs-NCsHH
				L5: Cs-N5dcCsHH
			L4: Cs-NHHH
			L4: Cs-SsSsHH
			L4: Cs-NNCsH
			L4: Cs-COsSH
				L5: Cs-CsOsSH
					L6: Cs-CsOsS2H
			L4: Cs-CCSH
			L4: Cs-CCSH
				L5: Cs-CsCsSH
					L6: Cs-CsCsS2H
				L5: Cs-CbCsSsH
			L4: Cs-CCCS
				L5: Cs-CsCsCsS
					L6: Cs-CsCsCsS2
			L4: Cs-CCCH
				L5: Cs-CbCdsCdsH
					L6: Cs-(Cds-Cd)(Cds-Cd)CbH
						L7: Cs-(Cds-Cds)(Cds-Cds)CbH
				L5: Cs-CdsCdsCdsH
				L5: Cs-CdsCdsCdsH
					L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H
						L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H
			L4: Cs-CCCC
				L5: Cs-CdsCdsCdsCs
				L5: Cs-CdsCdsCsCs
				L5: Cs-CbCbCsCs
				L5: Cs-CtCsCsCs
				L5: Cs-CbCdsCsCs
					L6: Cs-(Cds-Cd)CbCsCs
						L7: Cs-(Cds-Cds)CbCsCs
				L5: Cs-CbCtCsCs
			L4: Cs-CCSS
				L5: Cs-CsCsSS
			L4: Cs-SsHHH
				L5: Cs-S6HHH
				L5: Cs-S2sHHH
				L5: Cs-S4HHH
			L4: Cs-COsHH
				L5: Cs-CdsOsHH
			L4: Cs-CCCOs
				L5: Cs-CdsCdsCsOs
				L5: Cs-CbCsCsOs
			L4: Cs-CSHH
				L5: Cs-CtSsHH
				L5: Cs-CbSsHH
				L5: Cs-CdsSsHH
				L5: Cs-CsSHH
					L6: Cs-CsS2HH
					L6: Cs-CsS6HH
					L6: Cs-CsS4HH
			L4: Cs-NCsCsH
				L5: Cs-N5dcCsCsH
				L5: Cs-N3dCsCsH
				L5: Cs-N3sCsCsH
			L4: Cs-NCsHH
				L5: Cs-N3dCHH
				L5: Cs-N3dCHH
					L6: Cs-(N3dN3d)CsHH
					L6: Cs-(N3dCd)CsHH
				L5: Cs-N3sCsHH
			L4: Cs-NHHH
				L5: Cs-N3dHHH
					L6: Cs-(N3dCd)HHH
				L5: Cs-N3sHHH
		L3: Cds
			L4: Cd-N3dCsH
			L4: Cds-CdCS
				L5: Cds-CdsCsSs
					L6: Cds-CdsCsS2
			L4: Cd-N3dCsCs
			L4: Cds-CNH
				L5: Cd-CdHN3s
			L4: Cds-CCN
				L5: Cd-CdCsN3s
			L4: CO-CsSs
			L4: Cds-OdN3sCs
			L4: Cds-OdN3sH
			L4: Cds-OdCOs
				L5: Cds-OdCdsOs
				L5: Cds-OdCbOs
			L4: Cds-OdOsH
			L4: Cds-CdCO
				L5: Cds-CdsCdsOs
					L6: Cds-Cds(Cds-Cd)O2s
						L7: Cds-Cds(Cds-Cds)O2s
				L5: Cds-CdsCbOs
				L5: Cd-CdCsOs
					L6: Cds-CdsCsOs
				L5: Cds-CdsCdsOs
					L6: Cds-Cds(Cds-O2d)O2s
			L4: Cds-OdOsOs
			L4: Cds-CdSH
				L5: Cds-CdsSH
					L6: Cds-CdsS2H
		L3: Cb
			L4: Cb-N3s
			L4: Cb-S
			L4: Cb-O2s
			L4: Cb-H
			L4: Cb-C
				L5: Cb-Cds
				L5: Cb-Cb
				L5: Cb-Ct
					L6: Cb-(CtN3t)
				L5: Cb-Cds
					L6: Cb-(Cds-Cd)
						L7: Cb-(Cds-Cds)
					L6: Cb-(Cds-O2d)
				L5: Cb-Cs
		L3: Cds
			L4: Cds-OdCC
				L5: Cds-OdCdsCs
				L5: Cds-OdCdsCds
					L6: Cds-O2d(Cds-Cd)(Cds-Cd)
						L7: Cds-O2d(Cds-Cds)(Cds-Cds)
			L4: Cds-OdCH
			L4: Cds-OdCC
				L5: Cds-OdCsCs
				L5: Cds-OdCdsCs
					L6: Cds-O2d(Cds-Cd)Cs
						L7: Cds-O2d(Cds-Cds)Cs
					L6: Cds-O2d(Cds-O2d)Cs
			L4: Cds-OdCH
				L5: Cds-OdCdsH
					L6: Cds-O2d(Cds-Cd)H
						L7: Cds-O2d(Cds-Cds)H
					L6: Cds-O2d(Cds-O2d)H
				L5: Cds-OdCsH
			L4: Cds-OdHH
			L4: Cds-CdOsH
				L5: Cds-CdsOsH
			L4: Cds-CdCC
				L5: Cds-CdsCtCds
					L6: Cds-CdsCt(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)Ct
				L5: Cds-CdsCdsCs
				L5: Cds-CdsCdsCds
					L6: Cds-Cds(Cds-Cd)(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)(Cds-Cds)
				L5: Cds-CdsCdsCds
					L6: Cds-Cds(Cds-O2d)(Cds-Cd)
						L7: Cds-Cds(Cds-O2d)(Cds-Cds)
				L5: Cds-CdsCbCds
				L5: Cds-CdsCbCds
					L6: Cds-Cds(Cds-Cd)Cb
						L7: Cds-Cds(Cds-Cds)Cb
				L5: Cds-CdsCbCb
				L5: Cds-CdsCbCs
				L5: Cds-CdsCtCt
					L6: Cds-Cd(CtN3t)(CtN3t)
				L5: Cds-CdsCtCs
					L6: Cd-CdCs(CtN3t)
				L5: Cds-CdsCdsCs
					L6: Cd-CdCs(CO)
					L6: Cds-Cds(Cds-Cd)Cs
						L7: Cds-Cds(Cds-Cds)Cs
			L4: Cds-CdCH
				L5: Cds-CdsCdsH
				L5: Cds-CdsCbH
					L6: Cds-(Cds-Os)CbH
				L5: Cds-CdsCtH
					L6: Cds-CdsH(CtN3t)
				L5: Cds-CdsCdsH
					L6: Cd-Cd(CO)H
					L6: Cds-Cds(Cds-Cd)H
						L7: Cds-Cds(Cds-Cds)H
			L4: Cds-CdCH
				L5: Cds-CdsCsH
			L4: Cds-CdHH
				L5: Cds-CddHH
					L6: Cds-(Cdd-O2d)HH
				L5: Cds-CdsHH
			L4: Cds-OdCOs
				L5: Cds-OdCdsOs
					L6: Cds-O2d(Cds-O2d)O2s
					L6: Cds-O2d(Cds-Cd)O2s
						L7: Cds-O2d(Cds-Cds)O2s
				L5: Cds-OdCsOs
			L4: Cds-CdCC
				L5: Cds-CdsCsCs
		L3: Cs
			L4: Cs-CCOsOs
			L4: Cs-CCOsH
				L5: Cs-CbCsOsH
			L4: Cs-CCOsOs
				L5: Cs-CsCsOsOs
			L4: Cs-COsOsH
				L5: Cs-CsOsOsH
			L4: Cs-OsOsHH
			L4: Cs-CCCOs
				L5: Cs-CdsCsCsOs
					L6: Cs-(Cds-Cd)CsCsOs
						L7: Cs-(Cds-Cds)CsCsOs
					L6: Cs-(Cds-O2d)CsCsOs
				L5: Cs-CsCsCsOs
			L4: Cs-COsHH
				L5: Cs-CtOsHH
				L5: Cs-CdsOsHH
					L6: Cs-(Cds-O2d)OsHH
					L6: Cs-(Cds-Cd)OsHH
						L7: Cs-(Cds-Cds)OsHH
				L5: Cs-CsOsHH
			L4: Cs-OsHHH
			L4: Cs-CCOsH
				L5: Cs-CdsCsOsH
					L6: Cs-(Cds-O2d)CsOsH
					L6: Cs-(Cds-Cd)CsOsH
						L7: Cs-(Cds-Cds)CsOsH
				L5: Cs-CsCsOsH
			L4: Cs-NCsCsCs
				L5: Cs-N5dcCsCsCs
				L5: Cs-N3sCsCsCs
			L4: Cs-CCCC
				L5: Cs-CbCsCsCs
				L5: Cs-CdsCdsCsCs
					L6: Cs-(Cds-Cd)(Cds-Cd)CsCs
						L7: Cs-(Cds-Cds)(Cds-Cds)CsCs
					L6: Cs-(Cds-O2d)(Cds-O2d)CsCs
				L5: Cs-CtCsCsCs
					L6: Cs-(CtN3t)CsCsCs
				L5: Cs-CdsCsCsCs
					L6: Cs-(CdN3d)CsCsCs
					L6: Cs-(Cds-O2d)CsCsCs
					L6: Cs-(Cds-Cd)CsCsCs
						L7: Cs-(Cds-Cds)CsCsCs
				L5: Cs-CsCsCsCs
			L4: Cs-CCCH
				L5: Cs-CbCdsCsH
				L5: Cs-CbCdsCsH
					L6: Cs-(Cds-Cd)CbCsH
						L7: Cs-(Cds-Cds)CbCsH
				L5: Cs-CbCbCsH
				L5: Cs-CbCbCbH
				L5: Cs-CtCsCsH
				L5: Cs-CbCsCsH
				L5: Cs-CtCsCsH
					L6: Cs-(CtN3t)CsCsH
				L5: Cs-CdsCdsCsH
				L5: Cs-CdsCdsCsH
					L6: Cs-(Cds-Cd)(Cds-Cd)CsH
						L7: Cs-(Cds-Cds)(Cds-Cds)CsH
				L5: Cs-CdsCsCsH
					L6: Cs-(CdN3d)CsCsH
					L6: Cs-(Cds-O2d)CsCsH
					L6: Cs-(Cds-Cd)CsCsH
						L7: Cs-(Cds-Cds)CsCsH
				L5: Cs-CsCsCsH
			L4: Cs-CCHH
				L5: Cs-CbCdsHH
				L5: Cs-CdsCdsHH
				L5: Cs-CbCtHH
				L5: Cs-CbCbHH
				L5: Cs-CbCdsHH
					L6: Cs-(Cds-O2d)CbHH
					L6: Cs-(Cds-Cd)CbHH
						L7: Cs-(Cds-Cds)CbHH
				L5: Cs-CtCtHH
				L5: Cs-CtCdsHH
					L6: Cs-(Cds-Cd)CtHH
						L7: Cs-(Cds-Cds)CtHH
					L6: Cs-(Cds-O2d)CtHH
				L5: Cs-CbCsHH
				L5: Cs-CtCsHH
					L6: Cs-(CtN3t)CsHH
				L5: Cs-CdsCdsHH
					L6: Cs-(Cds-O2d)(Cds-O2d)HH
					L6: Cs-(Cds-O2d)(Cds-Cd)HH
						L7: Cs-(Cds-O2d)(Cds-Cds)HH
					L6: Cs-(Cds-Cd)(Cds-Cd)HH
						L7: Cs-(Cds-Cds)(Cds-Cds)HH
				L5: Cs-CdsCsHH
					L6: Cs-(CdN3d)CsHH
					L6: Cs-(Cds-O2d)CsHH
					L6: Cs-(Cds-Cd)CsHH
					L6: Cs-(Cds-Cd)CsHH
						L7: Cs-(Cds-Cds)CsHH
				L5: Cs-CsCsHH
			L4: Cs-CHHH
				L5: Cs-C=SHHH
				L5: Cs-CbHHH
				L5: Cs-CtHHH
					L6: Cs-(CtN3t)HHH
				L5: Cs-CdsHHH
					L6: Cs-(CdN3d)HHH
					L6: Cs-(Cds-Cd)HHH
					L6: Cs-(Cds-Cd)HHH
						L7: Cs-(Cds-Cds)HHH
					L6: Cs-(Cds-O2d)HHH
				L5: Cs-CsHHH
		L3: Ct
			L4: Ct-N3tOs
			L4: Ct-N3tN3s
			L4: Ct-N3tC
			L4: Ct-N3tC
				L5: Ct-N3tCd
				L5: Ct-N3tCs
			L4: Ct-CtC
				L5: Ct-CtCb
				L5: Ct-CtCds
				L5: Ct-CtCt
				L5: Ct-CtCds
					L6: Ct-Ct(Cds-Cd)
						L7: Ct-Ct(Cds-Cds)
				L5: Ct-CtCs
			L4: Ct-CtH
		L3: Cdd
			L4: Cdd-CdOd
				L5: Cdd-CdsOd
			L4: Cdd-CdCd
				L5: Cdd-CdsCds
			L4: Cdd-OdSd
			L4: Cdd-OdOd
	L2: O
		L3: O2s
			L4: O2s-HH
			L4: O2s-N
				L5: O2s-NN
				L5: O2s-CN
					L6: O2s-CsN3s
			L4: O2s-CC
				L5: O2s-CdsCds
				L5: O2s-CdsCs
			L4: O2s-SH
				L5: O2s-S_DeH
			L4: O2s-CS
				L5: O2s-CS6
			L4: O2s-OsC
				L5: O2s-OsCs
				L5: O2s-OsCds
					L6: O2s-O2s(Cds-O2d)
			L4: O2s-N
				L5: O2s-CN
					L6: O2s-CsN3d
						L7: O2s-Cs(N3dOd)
			L4: O2s-CH
				L5: O2s-CdsH
				L5: O2s-CbH
				L5: O2s-CdsH
					L6: O2s-(Cds-O2d)H
					L6: O2s-(Cds-Cd)H
				L5: O2s-CsH
			L4: O2s-CC
				L5: O2s-CbCb
				L5: O2s-CsCb
				L5: O2s-CdsCds
					L6: O2s-(Cds-O2d)(Cds-O2d)
					L6: O2s-(Cds-O2d)(Cds-Cd)
					L6: O2s-(Cds-Cd)(Cds-Cd)
				L5: O2s-CsCs
				L5: O2s-CdsCs
					L6: O2s-Cs(Cds-Cd)
					L6: O2s-Cs(Cds-O2d)
			L4: O2s-OsH
		L3: O2d
			L4: O2d-N5dc
			L4: O2d-N3d
			L4: O2d-Cd
			L4: O2d-Sd
""",
)