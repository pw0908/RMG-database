#!/usr/bin/env python
# encoding: utf-8
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
    thermo = None,
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.057622482072578377, 0.17474024464254836, 0.311792904762241, 0.24510026073262686, 0.5184526068838221],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1094,
    label = "O2d",
    group = 
"""
1 * O2d u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.16765545805721072, 0.09712570517971927, -0.14293844382567344, -0.04667503477914288, -0.10718338952215001],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.31527439725819306, -0.29089971992880675, 0.19436461319422368, 0.1446020234012803, 0.3614116150788995],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 34,
    label = "Cdd",
    group = 
"""
1 * Cdd u0
""",
    thermo = u"Cdd-CdsCds",
)


entry(
    index = 1,
    label = "C",
    group = 
"""
1 * C u0
""",
    thermo = u"Cs-CsCsCsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21864463322912153, 0.19757592311839944, 0.33482846159623697, 0.14358375330901088, 0.7246988102227039],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1097,
    label = "O2s",
    group = 
"""
1 * O2s u0
""",
    thermo = u"O2s-(Cds-Cd)(Cds-Cd)",
)


entry(
    index = 2029,
    label = "S4dd",
    group = 
"""
1 * S4dd u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21301321850392785, 0.08759242663831689, 0.0032367121209344336, -0.009961213572676712, 0.9479829033380569],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1400,
    label = "S",
    group = 
"""
1 * S ux
""",
    thermo = u"S2s-CsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.12901771982510019, 0.11304513598666677, 0.2947166951702199, -0.4086088465564136, -0.7449415507848307],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.23949060048443763, 0.08515327722199316, -0.07811448481365166, 0.22993040019972177, 0.8059931934097169],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.26995010700892624, 0.32080739979060874, -0.06818128502819976, 0.034474252071277585, 1.0672381975676606],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = -1,
    label = "S2d",
    group = 
"""
1 * S2d u0
""",
    thermo = None,
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3646688321920818, -0.5145814145396542, 0.06960745439677776, -0.03654726344911728, 0.2659900279891605],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2189081306486821, 0.43892639278724266, 0.11742506563941452, 0.26862292940798693, 0.9638901582625524],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1888,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    thermo = u"N3s-CsHH",
)


entry(
    index = 1887,
    label = "N",
    group = 
"""
1 * N u0
""",
    thermo = u"N3s",
)


entry(
    index = 1400,
    label = "S",
    group = 
"""
1 * S ux
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.37014612422486964, 0.4529229379146193, -0.05505933829872851, -0.10565530691927981, 1.4733823363855207],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1887,
    label = "N",
    group = 
"""
1 * N u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.029446765643455972, 0.05492717100016502, 0.032384737330761464, 0.07288583310062678, 0.3447831868143331],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18799533839692384, -0.11998491263243677, -0.27590852606326965, -0.45072019120622386, -0.2776007607130251],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
)


entry(
    index = 20,
    label = "Ct",
    group = 
"""
1 * Ct u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.004968142746888298, 0.40333660306310115, 0.514396251606174, 0.5419721450492493, 1.195545596747779],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.018496361241801377, -0.15559127173847193, -0.06262055930322875, -0.007394552109665074, 0.30049166582142917],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsHHH",
)


entry(
    index = 329,
    label = "Cs",
    group = 
"""
1 * Cs u0
""",
    thermo = u"Cs-CsCsCsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.0016820040114119523, -0.0013230223081476438, 0.00030753594481087933, 0.0019299454648373069, 0.503133640544118],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.02001394140883743, 0.15743689062429433, 0.0431482592082537, 0.02534745655770116, 0.6402840790843334],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsCsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.02151979506678784, 0.2552765401150035, 0.17186664293438503, 0.04960204354868436, 0.7401586600837752],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsCsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.19876331103608683, 0.03329079208927007, 0.21927923648263742, 0.337691099112622, 0.7271609359616406],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.00127483569905993, 0.5240374171398738, -0.02190402374347701, 0.1680542988093538, 0.9038117922986748],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18896392297812725, -0.3214127092085912, -0.1340513536899093, 0.042138316295172853, 0.16799065487900477],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"O2s-Cs(Cds-Cd)",
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
    thermo = u"O2s-(Cds-Cd)(Cds-Cd)",
)


entry(
    index = 1095,
    label = "O2d-Cd",
    group = 
"""
1 * O2d u0 {2,D}
2   CO  u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.02925538388400748, 0.2349494729074858, -0.0015934048511310438, 0.09313214206620302, 0.28119155062254264],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08265186039027814, 0.12121308323858795, 0.0650185003190027, 0.1421758539173969, 0.6881718665008474],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CsCsH",
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
    thermo = u"Cs-(Cds-Cds)CsCsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.18223111109557943, 0.5104186606170619, 0.1119429929471637, 0.06065578867219075, 0.7032764165537895],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsOsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.025643800105327914, -0.04335002561198516, -0.033318851531181734, 0.09474295641009392, 0.4312627565187697],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)HHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.04143624400967874, 0.08980125291079233, 0.026843432478263672, -0.09054562299036721, 0.5133599027973436],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-CdsCsCs",
)


entry(
    index = 50,
    label = "Cds",
    group = 
"""
1 * [Cd,CO,CS] u0
""",
    thermo = u"Cds-CdsCsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.07517080819963837, 0.08859783971057807, 0.03560203386204147, 0.13992759984078837, 0.5804945723941599],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-OdCsOs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.044108654215937196, -0.12128984822076137, -0.06330401585650533, -0.008262156909609058, 0.2667819585276463],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-CdsHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.0649399151169382, -0.11164901689978177, -0.046064276645476146, 0.06237846997528179, 0.4118352713142143],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)HHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.002871615337235277, 0.01713599223928216, -0.013752600407536082, -0.040623111450428386, 0.492180562534636],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-CdsCsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.06045074613144029, 0.0005969498232066221, -0.005147310510834684, 0.08662566646601959, 0.5271476506624828],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CsHH",
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
    thermo = u"Cs-(Cds-Cds)CsHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09669804782583144, 0.33281755422911485, 0.1918333025833604, 0.1587102396373982, 0.6893772188442913],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CsCsCs",
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
    thermo = u"Cs-(Cds-Cds)CsCsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.06529941615676567, -0.04404586706620807, -0.05421430540979391, -0.007169034608233742, 0.2994425790691605],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08403131549693166, -0.018556575436920093, -0.03308366363750398, 0.015590023059492855, 0.6571596778963877],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cdd-CdsCds",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.05005631693658533, -0.05834148344160012, -0.032158529651459725, 0.022437616685434335, 0.4128694604715554],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.06924309922017555, -0.025704383624615523, -0.022055775758336844, 0.01039334870632697, 0.4765731185975736],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.03352011561692331, 0.032637099816992136, 0.010102753893123536, 0.027955732020894603, 0.53830365812604],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09941510893294418, 0.06663680324030051, 0.0001315690394805935, 0.03337813549347835, 0.6019639557870144],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-Cds(Cds-Cds)H",
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
    thermo = u"Cds-Cds(Cds-Cds)H",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.022027902060207542, 0.17684228444877859, 0.055542433917988396, 0.025727635433794385, 0.6515719627759804],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-Cds(Cds-Cds)Cs",
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
    thermo = u"Cds-Cds(Cds-Cds)Cs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08622701351743245, 0.09791129945095361, 0.030308261679366587, 0.043867196062685444, 1.1403109743780888],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13961200144081773, 0.0017912249982516698, 0.03352678939030613, 0.213996690540214, 0.5384753646119643],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)HH",
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)HH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13190909500013606, 0.21337321953455549, 0.0854325455555802, 0.20853190836323687, 0.294622058384309],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)CsH",
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)CsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.06894534156297874, -0.0032885652029266826, 0.007191683325840503, 0.03934498047076042, 0.36154073776925616],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1293358178464183, -0.18482422875782065, -0.12840243193500175, 0.03466143291531956, 0.5295010907501086],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.029048476460015155, 0.11510711368915896, 0.06588069383495268, 0.04025017130003471, 0.3923708089007957],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Ct-CtCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13724966776817138, -0.024921491113949507, -0.05401751682611425, 0.023575902315251654, 0.6428979944631802],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.026179939865519183, 0.19278701244019592, 0.12720480836267972, 0.20526595168516465, 1.027071130180508],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.12530042629222132, -0.07682843692045434, -0.11424649384559822, -0.1521216185638971, 0.07546566535880217],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Ct-Ct(Cds-Cds)",
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
    thermo = u"Ct-Ct(Cds-Cds)",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.12953639900891997, 0.0649644104182592, 0.007052179445612332, 0.021280996450751676, 0.642981680248103],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.44263397785066805, -0.6840599264023391, -0.15350288946220775, 0.24949106144471167, 0.17405741130637037],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.19279925148986105, 0.3454648073129718, 0.0042404532437657644, 0.04908908887756673, 0.5402928820381634],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.21994638838012986, 0.44684749951949354, 0.07300334883679661, 0.05275610009905109, 0.5961701508673811],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsOsHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.17530016559472095, 0.6983197803534978, 0.20510345465773003, 0.2163093014381869, 0.6507130817368125],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsCsOs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.04841813574507599, -0.16929136675760922, -0.08702317014635293, 0.05095036080953498, 0.02195511288592189],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"O2s-(Cds-Cd)(Cds-Cd)",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09583745023298051, 0.0897414853490858, 0.02184432555478129, 0.09211169378370497, 0.5827965672843056],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([18.08,21.17,24.43,27.41,32.22,35.73,40.97],'J/(mol*K)'), H298=(36.4,'kJ/mol'), S298=(33.51,'J/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1646413979127375, -0.4429219002517437, -0.21564560562764884, 0.05172087004302618, 0.0029104361125882328],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.16298420794012214, 0.4530235105328294, 0.10474993635920427, 0.16626898348925528, 0.6254989764812898],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([28.42,35.65,40.62,44.31,49.79,53.92,60.6],'J/(mol*K)','+|-',[3.38,3.38,3.38,3.38,3.38,3.38,3.38]), H298=(-26.6,'kJ/mol','+|-',2.88), S298=(34.59,'J/(mol*K)','+|-',3.95)),
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
    thermo = u"Cs-(Cds-Cds)OsHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.4696354293703974, 0.7174387192965624, 0.15633396409448772, -0.08555571292160641, 0.46976995239542896],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.4249644635387055, 0.7743223982418233, 0.2104542146408671, -0.11516331659879836, 0.5852191427412169],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsOsOsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.38236079621830665, 0.9581049654307527, 0.4825253909581299, 0.030269065232023606, 0.9605051676046529],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsOsOs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1000655839653585, 0.08488613500495837, -0.0025810385702850144, 0.021027760357236927, 0.6776316219538261],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.01965107421424714, 0.11186345837241045, 0.03868674185560481, 0.037738298453426924, 0.42499723216347796],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cb-Cs",
)


entry(
    index = 6,
    label = "Cb",
    group = 
"""
1 * Cb u0
""",
    thermo = u"Cb-Cs",
)


entry(
    index = 7,
    label = "Cb-H",
    group = 
"""
1 * Cb u0 {2,S}
2   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.059755765068965225, 0.07797223183043052, -0.005795078738248473, 0.024006246125984166, 0.5381967259805268],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.13037364774348456, 0.5191253226692321, 0.16598173839055075, 0.2203109876305388, 0.6149527903479999],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([29.84,38.86,43.83,46.37,48.34,49.06,49.94],'J/(mol*K)','+|-',[3.74,3.74,3.74,3.74,3.74,3.74,3.74]), H298=(-24,'kJ/mol','+|-',3.19), S298=(-61.06,'J/(mol*K)','+|-',4.36)),
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
    thermo = u"Cs-(Cds-Cds)CsOsH",
)


entry(
    index = 1919,
    label = "N3t",
    group = 
"""
1 * N3t u0 p1 {2,T}
2   R!H u0 {1,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.039105766572242344, -0.25631572521205526, -0.48568991655009985, -0.26673413999023615, -0.61019095766348],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.06656273764670309, 0.5057296668811239, 0.150607304148856, 0.1612163812344362, 0.9268728276959266],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08714443387786686, 0.7630976435399245, 0.44044994647482555, 0.4492481097474999, 1.5718096908327435],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.3371983490756616, 1.1870451030564713, 0.1912706005340911, -0.07397755835214437, 1.2380623073044412],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2292188650278021, -0.4015977824768294, 0.2900811303940349, 0.04811981177681619, 0.5748532854121347],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16722080954008886, 0.053373257257843504, -0.10670362621389334, 0.1707456256481744, 0.6654615502970003],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-OdCsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.024581262302755466, 0.08675404923855799, 0.013859585892082693, 0.11168039408051669, 0.5572705103073091],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.04904142688799726, 0.24800822944654355, 0.10333557305757718, 0.1352717759628963, 0.7538722796318731],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.04630355666054371, 0.37240763374139474, 0.17850713230086315, 0.1897791312502442, 0.8649847550699752],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.19214470931539096, -0.02667385688443897, -0.06978411789859479, 0.1368981808967206, 0.6554567319915792],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-O2d(Cds-Cds)H",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.19894050762269752, 0.1313706333290382, 0.23511924404945916, 0.10928920560956303, 0.3838803095748867],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11605540005313329, 0.05707754388123344, -0.03273695324034106, 0.0857291482381432, 0.5414387878921083],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-O2d(Cds-Cds)Cs",
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
    thermo = u"Cds-OdCsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21380946960050215, 0.13811299262546756, 0.0007130846842852787, 0.1939634943110834, 0.7991141127783978],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2138094696004984, 0.13811299262547222, 0.0007130846842891767, 0.19396349431108278, 0.7991141127784003],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cdd-CdsOd",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.06029537080066849, 0.060634294439938216, -0.02335372315227764, 0.1906840157234267, 0.5433210225777506],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2856609747177523, 0.23133101007218113, -0.019948791111982056, 0.0499945394010609, 0.9670417772974611],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([27.31,34,39.42,43.77,50.16,54.55,60.77],'J/(mol*K)','+|-',[4.9,4.9,4.9,4.9,4.9,4.9,4.9]), H298=(-128.3,'kJ/mol','+|-',5.9), S298=(129.26,'J/(mol*K)','+|-',5.71)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.020693372991827504, 0.127635068602047, 0.0022647234284150688, 0.1516363434931235, 0.6246812875811448],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.12987256535277836, 0.05206031767294925, 0.04234247979258615, 0.11761971719356154, 0.6032113700439855],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([24.94,31.41,36.47,40.49,46.72,51.49,59.29],'J/(mol*K)','+|-',[3.34,3.34,3.34,3.34,3.34,3.34,3.34]), H298=(-16.9,'kJ/mol','+|-',2.85), S298=(40.18,'J/(mol*K)','+|-',3.9)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21689392942426905, 0.0014868074097100226, -0.05390342990500236, 0.11906372320540938, 0.7561626136395064],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.0743795940405497, 0.24020397531639026, -0.003207123026800652, 0.07971110810064796, 0.6701499340033616],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.12130736949288559, 0.19901795556084279, -0.04676067507430395, 0.11786316296756685, 0.8318459153683119],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21298733440717427, 0.19031822934840248, 0.01786175094787578, 0.05873355181819224, 0.8575871448304064],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([25.26,30.66,34.68,37.69,41.62,43.93,46.69],'J/(mol*K)','+|-',[4.9,4.9,4.9,4.9,4.9,4.9,4.9]), H298=(-130.4,'kJ/mol','+|-',4.17), S298=(47.38,'J/(mol*K)','+|-',5.71)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.15780747794737057, 0.23146611122734034, 0.17411159075485869, 0.09369639085810366, 0.5507533973499446],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13177655082225997, -0.2414262782843299, 0.034520236005383606, 0.03894331357814204, 0.4656736146941636],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.04101476101412885, 0.0550569687698747, -0.07682105083869646, 0.0853133351222988, 0.6151094369853052],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.07256848899764987, 0.23250413512090756, 0.01345269836852133, 0.011082236094911053, 0.7002753918790436],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cb-(Cds-Cds)",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.14424287823957144, 0.03521924752680442, -0.034540516780401424, 0.08782764687532058, 0.6397685857190536],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21504586169990092, 0.9232700387323811, -0.012308192329580931, -0.12961537239030238, 1.8958978443541774],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = None,
)


entry(
    index = -1,
    label = "S2s",
    group = 
"""
1 * S2s u0
""",
    thermo = None,
)


entry(
    index = 50,
    label = "Cds",
    group = 
"""
1 * [Cd,CO,CS] u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15144897046417094, 0.22458129600242557, 0.010502657500858709, 0.10936459334524362, 0.8001413281348664],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.033803802229159616, -0.17607218192072727, 0.007018568398203862, 0.05394580547433734, 0.30076514344623084],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-CdsS2H",
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
    thermo = u"Cds-CdsSsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1424681590755672, 0.15961116557053717, 0.021000114516465846, 0.21130650218287556, 0.6788721912530469],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.40303825306205215, -0.21694560700474388, 0.1445090507445071, 0.3076267437556488, 0.6430097017197416],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"O2s-CsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11192906103303449, 0.06720490110199091, 0.3270177491011773, 0.15154867373823216, 0.49624151790943505],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"O2s-(Cds-Cd)H",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1432807418960764, 0.03356401411110284, -0.12179381354676581, 0.1921427463075143, 0.6100011891845667],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-Cds(Cds-Cds)O2s",
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
    thermo = u"Cds-CdsCsOs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1480458809583663, 0.05683120061325293, -0.00017751720901848164, 0.15965704213679838, 0.6285885448330331],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.012028894237656296, -0.020703358945534045, -0.07150885911154184, 0.004944669406582586, 0.1904624649637905],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.0049606718891953075, 0.21132464964534797, 0.0038651057449578165, -0.019394216310876358, 0.6399333005835575],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([12.79,15.86,19.67,22.91,26.55,27.85,28.45],'J/(mol*K)','+|-',[5.1,5.1,5.1,5.1,5.1,5.1,5.1]), H298=(33,'kJ/mol','+|-',4.34), S298=(-50.89,'J/(mol*K)','+|-',5.94)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.14553402348118974, 0.044302255069011115, 0.0784165744220532, 0.009233776081999781, 0.6632690843383064],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([28.33,37.84,44.54,49.34,55.45,58.73,60.61],'J/(mol*K)','+|-',[7.46,7.46,7.46,7.46,7.46,7.46,7.46]), H298=(-218.6,'kJ/mol','+|-',6.36), S298=(33.44,'J/(mol*K)','+|-',8.7)),
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
    thermo = u"Cds-O2d(Cds-Cds)O2s",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15401578146686645, -0.09647913980989586, 0.042933928326937265, 0.2049599406032971, 0.5142584236738479],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.14646803244354556, 0.15242644362795515, 0.049415913209227474, 0.1304284258351825, 0.7187111997612463],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10135854821605103, 0.04866309203398413, 0.45185770763553534, 0.028792593927901178, 0.5847881936560481],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.2341052801055017, 0.5328644023282001, -0.13460066596387232, -0.028908081480774034, 0.7191225358398923],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CsCsOs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.17332792516903245, 0.0688362232477942, 0.06359298559625295, 0.07317162105036487, 0.8838319124683678],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CtHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16892481383816998, 0.01656977210278801, -0.026272304381818736, 0.08873798408575569, 0.8664261028654147],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11240824293919321, 0.22648792219736302, -0.02862968241402079, 0.09632576161964736, 0.8823848588020993],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10628690258417178, 0.4239832706019591, 0.034439592845266084, 0.11944497382938091, 1.1066199878755512],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([3.99,5.61,6.85,7.78,9.1,9.9,11.12],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]), H298=(-1.72,'kcal/mol','+|-',0.27), S298=(-11.19,'cal/(mol*K)','+|-',0.15)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.12741389756357446, 0.4233435873182082, 0.09158937352786511, 0.2109216404147516, 1.0259511054011456],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([4.37,6.79,8.09,8.78,9.19,8.96,7.63],'cal/(mol*K)','+|-',[0.13,0.13,0.13,0.13,0.13,0.13,0.13]), H298=(2.81,'kcal/mol','+|-',0.27), S298=(-35.18,'cal/(mol*K)','+|-',0.15)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.23995147183590843, 0.7703088558165031, 0.006270986784226449, 0.11217360764232676, 1.4590574412915935],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.12093557171614418, 0.08062787640049801, 0.41127005117651744, 0.40241265064960335, 1.0042489432917734],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.052085106667015886, 0.6819784043627537, 0.04227588341846801, 0.12145713011797979, 1.3373696205645262],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([3.5,3.88,4.88,4.18,4.86,5.4,6.01],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]), H298=(8.11,'kcal/mol','+|-',0.24), S298=(-13.02,'cal/(mol*K)','+|-',0.12)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16894454428499286, 0.03072362808427548, -0.019215688117775874, 0.2476232524457948, 0.9044635818031377],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CtHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22632213028409273, 1.1730515428384456, 0.07808359351861802, 0.21426895560277748, 1.921406446760762],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([3.23,4.59,5.41,5.93,6.48,6.74,7.02],'cal/(mol*K)','+|-',[0.1,0.1,0.1,0.1,0.1,0.1,0.1]), H298=(8.81,'kcal/mol','+|-',0.24), S298=(-13.51,'cal/(mol*K)','+|-',0.12)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08653887458638056, -0.17212829227776782, 0.39750055272537477, 0.15405712115264433, 0.43570282461684073],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
)


entry(
    index = 329,
    label = "Cs",
    group = 
"""
1 * Cs u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08105175087750756, 0.24539529467837767, -0.1002636622831654, 0.11425380519348241, 0.7833252562880013],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.00953299965458, 0.05438259035657654, -0.17872791179567593, 0.12588647038658332, 0.5062882512099705],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.010819976653408035, 0.15062166917753586, -0.11979330235495222, 0.1533371138770775, 0.5894650428729526],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21408750714413968, 0.6979915704273855, 0.414933779321552, 0.3173601169117469, 1.7897133756808254],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22388614653254735, 0.18978785377492458, 0.14896766569345576, 0.14622401432849538, 1.1438073696961606],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.013803306497719145, 0.2384755202106973, -0.07147480001348655, 0.1253861005313028, 0.641443992762889],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.12986319734840635, -0.13201232057415058, 0.32641701947121543, 0.31100435527943526, 0.5755160163785056],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.23063910622696635, 0.023155851120408973, 0.2620701317850661, 0.3568447813784441, 0.8081368852172954],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.23843014148906688, 1.2165115645223024, 0.3421075103079388, 0.18114131245480852, 2.1560989084808453],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13560342905278883, 0.2655844697248846, 0.4117553784480716, 0.1471186599910318, 0.9785907112128088],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.27383833831008053, 0.033298190179390036, 0.22130029704664134, 0.21728683469860346, 0.8292912325002468],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.0880772963356637, -0.13130163797620975, -0.08379889547819555, 0.3191248265565328, 0.1458000262280593],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1904,
    label = "N3d",
    group = 
"""
1 * N3d u0
""",
    thermo = None,
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.30195195419900783, -0.2518300212962564, 0.2953966028272987, 0.30194125818860895, 0.5711360710180097],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(21.3,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.3662811766239633, 0.32583252848502675, -0.16533106134535236, 0.2099824740876563, 0.14122307353710584],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21651537890337055, -0.015633809955237696, 0.30386411658212975, 0.16000227235965137, 0.768193540776347],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.5832773387792887, -0.7438317696833582, -0.06558373221781497, 0.02679367575449121, 0.35847360605012746],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.26367111736522875, 0.7014408561377896, 0.021682877888627716, 0.1358001286993729, 0.6479650881501877],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08073905090685027, 0.24363355847690218, -0.004067788962660369, 0.05651026451558802, 0.7115153760979602],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08073905090684799, 0.2436335584769008, -0.0040677889626589084, 0.056510264515587494, 0.7115153760979557],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21414986831366856, 0.24113305203957008, 0.36289358234364705, 0.24071122090030722, 1.045465054187356],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21794150742953716, 0.4077808067144683, -0.020593304533139692, 0.14732920431788019, 1.1106001354365853],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15474758658811585, 0.325505519751366, 0.012463933611839548, 0.1488530679467087, 0.9400260356337147],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13087068248820777, 0.12529623829366227, 0.2971280152471465, 0.13919251553747336, 0.768011132184713],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16404308458557776, -0.21910895863665086, -0.0304833654722142, 0.0894339213387472, 0.25313169300894706],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = None,
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
)


entry(
    index = 1945,
    label = "O2s-N",
    group = 
"""
1 * O2s u0 {2,S}
2   N   u0 {1,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
)


entry(
    index = 1943,
    label = "O2d-N3d",
    group = 
"""
1 * O2d u0 {2,D}
2   N3d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.05551585053202886, 0.1069796248718951, -0.08002105616841382, 0.0004435983083975713, 0.17067758412635012],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16404308458557695, -0.21910895863665478, -0.030483365472217038, 0.08943392133874764, 0.25313169300894034],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.14554884376516522, -0.14193761435353655, 0.31634616202445454, 0.11758969396918706, 0.508378972052146],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1591022469432372, 0.03697908762877255, 0.20166647143032462, 0.11415062105588111, 0.6571756049103026],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11175027456358, 0.21581876233500136, 0.061374855027650846, 0.04569821182533086, 0.7529532331016894],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15903691772029294, -0.26639416475116, 0.14624281020400778, 0.014895436171307907, 0.40586032576713493],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.22882282172641494, 0.24000472598481334, -0.2791943336412518, -0.08292764564065523, 0.2495710006433245],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 34,
    label = "Cdd",
    group = 
"""
1 * Cdd u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.27542864446296944, 0.179189864537593, 0.020707822308455946, -0.027792624112526622, 0.942874993261251],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.3198059407534673, 0.004222771483501919, -0.30363422810870583, 0.024546837330943094, -0.07595472230077194],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.27289368232370276, -0.25645307399984096, -0.42263590901389153, 0.0634760089731928, 0.2970484598315589],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = None,
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09368670221921821, 0.6343915046825417, 0.3935019190419293, 0.16379909732240763, 1.5491305484967393],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.14915229482925207, 0.27170735154068065, -0.1310169995589393, 0.22834240321162227, 0.4621395487054196],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.0755125630145767, 0.12521384507269956, -0.13396966421817053, -0.07135488699528249, 0.433098415002399],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2056137912840038, -0.05328953910970621, 0.010183923474966883, 0.2586440033040178, 0.7091025553315695],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)CsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.01175186936143481, 0.25016189178282877, -0.04671248977250801, -0.013004603893432554, 0.4844240951787292],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"O2s-O2s(Cds-Cd)",
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
    thermo = u"O2s-OsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.07284164624578227, 0.3405125829708828, 0.03697287953421528, 0.11041681096316024, 0.6908864312827996],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.16722856283589047, 0.7599318736374159, 0.20927812985987496, 0.20721708933497204, 0.6959092223588759],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([29.24,37.61,40.84,41.46,40.06,38.2,35.08],'J/(mol*K)','+|-',[3.81,3.81,3.81,3.81,3.81,3.81,3.81]), H298=(-14.6,'kJ/mol','+|-',3.24), S298=(-153.23,'J/(mol*K)','+|-',4.44)),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.017393648302531706, 0.8682307845707695, 0.19933883023755045, 0.22872428943246986, 1.5013950665889364],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.13643682581316696, 0.5207575930310251, 0.10253237630265677, 0.07972624785610685, 0.7898229608101704],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13756332592764026, 0.6654076425996981, -0.3871840640972999, 0.4384919779297695, 0.9857459464860626],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"S4d-OdCsCs",
)


entry(
    index = 2041,
    label = "S4d-Od",
    group = 
"""
1 * S4d u0 p1 {2,D}
2   O2d ux {1,D}
""",
    thermo = u"S4d-OdCC",
)


entry(
    index = 2030,
    label = "S4d",
    group = 
"""
1 * S4d u0
""",
    thermo = u"S4d-Od",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.07872844312833517, 0.2825463421768132, 0.1688737702738733, 0.08494825072422409, 0.904555927018521],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-S2sHHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.05239199746318775, 0.399411386265705, 0.2155790138404284, 0.13045184486143935, 0.9691929253751932],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsS2HH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.03092823092334429, 1.0574900710273383, -0.002353395280755448, -0.3395371034614496, 1.1319305073072317],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"S6dd-OdOdCsCs",
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
    thermo = u"S6dd-OdOdCC",
)


entry(
    index = 2031,
    label = "S6dd",
    group = 
"""
1 * S6dd u0
""",
    thermo = u"S6dd-OdOd",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.019358906672488407, -0.0753542171295154, 0.07122927194810211, 0.2898127357969278, 0.27660989731017205],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.0313330905771982, -0.5168837507969509, -0.2752072455911552, 0.6365513974164151, -0.5454108839879808],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.03245693686591595, 0.14449963607883565, 0.14072151713691539, -0.32166921086398614, 0.4609417845634458],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"O2s-CS4",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.606311122322764, -0.9085065281450098, 0.28352238070332414, 0.39959232407941436, -0.619042230396798],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsSS",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21600021932488056, 0.06417028025397656, -0.3349623698586216, 0.09871066068377558, 0.4340709987934558],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21600021932487629, 0.06417028025397964, -0.33496236985862055, 0.09871066068377568, 0.4340709987934556],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"S2s-S2sC",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1668252006840307, 0.45377405998112275, 0.36713826355995466, 0.17787167167341505, 1.534854054416747],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3160632671259397, -0.7582631091505541, -0.005149704400695829, -0.08769655029953673, 0.3245684408993599],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cdd-S2dS2d",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18520274349131766, -0.7187555089268083, -0.287961901675379, -0.08430087881814856, -0.4292101278501259],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08520534402495153, 0.28948491853501124, 0.29198864148292514, 0.05482415760476328, 1.335704011795067],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16506925623198754, 0.5292876250721607, -0.10226765840813018, 0.24445599859974976, 1.2807264337606634],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10013805067097267, 0.405356826379151, 0.3530255877729147, 0.09754103464955473, 1.4673197081950782],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4211775882420876, 0.006705575991767632, -0.4614154444894743, -0.026471371288318946, 0.681932504044609],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16170692357434696, -0.5095279813980993, -0.7205877231114852, 0.1239679032618512, -0.49316660903959464],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.04185445286060353, -0.962112487176229, -0.006338363492629791, 0.22662104770007913, -0.519088542923736],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"S6dd-OdOdCsOs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.1536981871651648, 2.0223560073720614, 0.3463924614802385, -0.16741954412999743, 1.7353619465850931],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"O2s-S_nonDeH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.09717398552051931, 0.40280161579083723, -0.015337402817400543, 0.23218964987349605, 0.72678504555392],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.07670528204560925, -1.1035871134389228, -0.07638232372487673, 0.2956723684836035, -0.9511097514035018],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.03398978116194987, 0.5935517022944085, 0.07786989562003557, 0.17252813367552866, 1.06827760348034],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10002411331871108, -0.03167486562593394, -0.05358028926431038, 0.0011741842248008186, 0.6119286947157916],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.5042251468844626, -0.39660448886147903, 0.3759518611520089, 0.032736912841271275, 0.695938282741593],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10206636645658405, -0.06597801122566914, 0.07859411453602025, 0.1439771957803206, 0.5282418351719798],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16403841136057573, -0.4130501355033674, -0.1111148337415467, 0.15790877653481572, 0.3438990603751597],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.12905812472080913, 0.43164912291714386, 0.09868569562838511, 0.0839983554777719, 0.951716643462438],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15295697444685752, 0.26053944660502193, 0.10992543601675366, -7.622446238213926e-05, 0.911256431689948],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cb-(Cds-Cds)",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.06404917011339523, -0.07090668164627464, -0.08755267497599915, 0.06314971391614396, 0.34531921220054496],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.06701289968558061, 0.13900081101897038, -0.02622747422065416, 0.051429512200566505, 0.5178635961025511],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.025884265014523837, 0.03876090276007182, 0.023545789568395446, 0.02995931741688069, 0.4520014412269978],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.025884265014524184, 0.03876090276007174, 0.02354578956839596, 0.029959317416882188, 0.4520014412270042],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09905660113011927, 0.18156948412074247, 0.023307114836825328, 0.02813193473236902, 0.649692220729015],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15059215450949281, 0.0599025153168235, -0.05945993569839768, 0.1424062294549058, 0.6415489938645546],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CbHH",
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
    thermo = u"Cs-(Cds-Cds)CbHH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18248944576721476, 0.376893282988189, 0.07883192399983552, 0.1851966393742619, 0.25325131164943615],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.318120486923846, 0.2674782588954025, 0.017122275021834707, -0.028173580848631592, 0.5360328416354776],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 2,
    label = "Cbf",
    group = 
"""
1 * Cbf u0
""",
    thermo = u"Cbf-CbCbCbf",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13991553292821562, 0.3030559086989299, 0.009646332375142785, 0.05857457691314788, 0.7758423641705412],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.17755820087545926, 0.18805916461850014, 0.1182133638786369, 0.28550678127723306, 0.6679917501786721],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22570858233852675, 0.23696208525820794, -0.018926210637968177, -0.0015744117794760232, 0.967475110176238],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.011893185451660404, 0.03280758371567577, -0.00958827848506294, 0.16697797904196254, 0.4178018683860407],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CbCsH",
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
    thermo = u"Cs-(Cds-Cds)CbCsH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.36077558210885874, 0.2646637296994367, 0.02143253279455637, -0.019849620711917513, 0.5871537938163469],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.31088286213934513, 0.2128225074714188, 0.19318149852760794, 0.2526305776010523, 0.992150180561995],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.06706054441443156, 0.33032712957352256, -0.020885325943328, 0.03344814231844764, 0.7784201932270324],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.48860602573777334, 0.26767767203906373, 0.01120679763436715, -0.10906487680939055, -0.03614768233050503],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 2,
    label = "Cbf",
    group = 
"""
1 * Cbf u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.32337308981282503, 0.20915146580565075, 0.00404268001500618, -0.10931177596717807, 0.05090711999214559],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.6736429608658729, -0.9861795468959604, 0.01637963986632742, -0.23155023071043684, 0.3697534978727556],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1990626988990153, 0.46965640244481055, 0.23521202616777173, 0.6276759747587248, 1.3269349054128234],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.008752074365636298, -0.16508051508939353, 0.02364002253140386, 0.1751384435084849, 0.13640734531512289],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.1025064108808243, 0.480125151708637, 0.17861434688896483, 0.24788549247221198, 0.8247667847223752],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.09261079828376056, 0.683992111823051, 0.1491110523019412, 0.12107398126483909, 0.7489819464537932],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09347373267424691, 0.08394724767191142, 0.028738206990184176, 0.14210926848613403, 0.7349380857557088],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.26224523051247917, -0.04803540742893092, 0.33308868812871567, 0.012035576533221678, 0.6080756814128914],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.03851473916434206, 0.17652391406263268, 0.12251323821905526, 0.16418576971102944, 0.6209480613422969],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-Cds(Cds-Cds)Cb",
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
    thermo = u"Cds-Cds(Cds-Cds)Cb",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.042043671816779205, -0.2870068991778536, 0.10896537566953461, 0.07796892580626857, 0.14736774150859733],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11068867695337645, 0.13550300559072487, -0.0024593362658544976, -0.04138288445414867, 0.7000143346505407],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-O2d(Cds-Cds)(Cds-Cds)",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.03370249636563874, 0.03997272247846417, 0.017363566091889448, 0.2840205070948774, 0.4947804490134111],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.29658050945203907, -0.422413105391416, -0.043870449163375645, -0.07901125824001284, 0.2907467624450265],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.27976996077411725, -0.051180872441117645, 0.2577139576785884, 0.053893042387591156, 0.7276728073339981],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.052490336234710236, 0.08095618220078937, -0.04380400347380553, 0.09309071540585824, 0.5023351335586136],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.019480593254957206, 0.22763855853532597, 0.11912198935753354, 0.09898029342738564, 0.6206296042763836],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.07859075596067744, 0.24921651530076044, 0.09407635833113567, 0.11926538599170816, 1.0030238288206386],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.20297351944880077, 0.3687022983072419, 0.14405886119014288, 0.21411329849514144, 1.2104469721720224],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16432627850064568, -0.09441213638305873, -0.059163509317695165, 0.13901134709383084, 0.8359276548904961],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2479102460774542, 0.6915212147828939, 0.44216075028748303, 0.519208884835395, 1.7890227272914925],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11123818597705934, -0.23622096194370767, 0.012119300751383111, 0.1339019727742625, 0.19381986158472506],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 6,
    label = "Cb",
    group = 
"""
1 * Cb u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.05992039186372425, 0.40651791793953324, 0.020415926230628174, 0.02728796565663333, 0.8679425423576561],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.0541628381388439, 0.15613442307380393, -0.02111035147261006, 0.12370142649459688, 0.6134853322600321],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.04762727711094644, 0.017045487655742656, 0.005245644969681375, 0.12585897495016946, 0.4956704985505885],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.26324337741271886, 0.22115807495365652, 0.01861400065476021, 0.25257049694180445, 1.2719313980431535],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.286553676904022, 0.39942797170835076, 0.3051465690083045, 0.010078332456806564, 1.0832166494637583],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.26368630859033915, -0.05521984398601747, 0.16028848506091548, 0.20959010556726873, 0.7247274609298302],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15450241093865183, 0.023305591306994555, 0.4288562605510648, 0.17332380951374274, 0.7559473903257337],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13940249998543397, 0.02113236205102259, -0.006414499085536998, 0.2872881887707217, 0.8837452239738912],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3849228269463869, 0.5882710669722634, 0.1922640705393514, 0.22517544633968206, 1.2497758652393214],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1888,
    label = "N3s",
    group = 
"""
1 * N3s u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.05399829091911655, -0.9050612707351176, 0.17938149127066788, 0.31188427134567487, -0.2987790903604344],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22550700366000215, 0.17674248604777615, 0.3322437079687421, 0.08115501480176004, 0.9001122863585567],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.04478113566232851, -0.007085486466144389, -0.066178501989258, 0.10916496991084312, 0.4915209338113762],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-Cds(Cds-O2d)(Cds-Cds)",
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
    thermo = u"Cds-Cds(Cds-Cds)(Cds-Cds)",
)


entry(
    index = 11,
    label = "Cb-Cds",
    group = 
"""
1 * Cb         u0 {2,S}
2   [Cd,CO,CS] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08372573300930806, 0.06918616675843645, 0.06840928802150274, 0.06635417153518532, 0.6422708713867056],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.07846905085435807, 0.1572100293636227, -0.03229823539101577, 0.1310856432541848, 0.659120511886745],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.02768768758723599, 0.03742644483359077, 0.0246990502578512, 0.1355923309693925, 0.5163916825147838],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.06405302078980477, -0.1112225878591653, 0.02214257606162187, 0.012862047571323264, 0.21104840817397894],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1254699023900724, 0.17711747107416534, 0.17152037798309383, 0.4017013642965962, 0.8795910964414086],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.27846763026366195, 0.1979720575617241, 0.1530388492910235, 0.15257510771626356, 0.33818193334725055],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.010141366531176175, -0.04247718995848413, -0.03138666472760324, 0.05335404689545457, 0.4410835915177297],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.20211500263983045, -0.05289192707840458, 0.43124527881430363, 0.02925628336229237, 0.6585664574888561],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4112547018398815, -0.2161487947706454, -0.040072796964572416, -0.16837694389491437, 0.795134667843814],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.31259814467772745, -0.4528390039071464, -0.35396681050871026, -0.11289703042796484, -0.016291170646929032],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18197800048372187, -0.012841310412733408, -0.13940917503546815, 0.19580643468566522, 0.47378194383251293],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.08607841333561764, -0.04929382663498108, 0.17503199020990723, -0.3236175622479156, -0.05408238567724763],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10232634937364662, 1.1455503034236159, 0.2822532047981598, -0.338620637884072, 1.1388997596188792],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15640799926647192, 0.39866822292497905, 0.22057808953920385, 0.15046645353581237, 0.813268239454422],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.01273056970123665, -0.03052742895836663, -0.01864343981608428, 0.18415104605236707, 0.374942080593767],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22456844025733008, 0.4924946395237318, 0.25047124016651323, 0.34393226985472947, 1.1420284109517551],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.03442106991266092, -0.1629181799324099, -0.255812059639148, 0.026940348779406792, 0.39298771064041715],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.07059659132829027, 0.13378084621463593, -0.06808334757036352, 0.10970450401364215, 0.5539181101836925],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.0754739749756509, 0.016320272850541634, 0.0348135763534409, -0.0005089993781796434, 0.0382182401844723],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.20521083393825873, -0.3318726565117219, -0.12702379401665384, -0.02283684727764465, 0.1980527750118617],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21814661735560184, 0.12753347391512668, 0.020049399592382486, 0.0953688254499516, 0.9705537622622331],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.17544482221138186, 0.45637002298589807, 0.33491704895661495, 0.08121131145581167, 1.6861113678821023],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.34599701046459824, -0.7546472184259692, 0.00721807834670447, -0.3124233356475785, 0.08122940545087956],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.601861714255426, -0.02633933982823921, -0.17229296821347623, -0.3385025234300235, 1.289911377658591],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.38964277869827696, -0.0887558959167197, 0.0963414594010301, 0.21966605511223097, 0.8137503330552882],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1312133897717019, -0.019706141369486535, -0.1054457892814793, -0.039822299828625035, 0.35785413090649587],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.07251730005514297, 0.12334790801098416, 0.003961355156224325, 0.11189256336252996, 0.47507120905533473],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.27499875720464156, -0.10956496432752055, -0.44921230166874976, -0.06846791692182679, 0.34197292878218244],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4402609382004234, 0.2834689653704807, 0.010160223528582972, 0.2641050258306068, 1.1937798442074734],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.20597862521903507, 0.4116826393410578, 0.1221230385204426, 0.17557713920644602, 1.1369712443039668],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.16281543171286256, 0.2502847761326399, 0.12061786321365052, -0.34805722739651596, 0.4903567553189372],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.14956925078673147, 0.041670753032611745, 0.1910544190568772, 0.34865503290025734, 0.6389471041170941],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(29.2,'kcal/mol'), S298=(-13.8,'cal/(mol*K)')),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1800384110916115, 0.39887499154659595, 0.09935271712548085, -0.16494907756761212, 0.8870644759342239],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.05548696999622357, -0.21517086700615823, -0.08108928901530299, 0.10163113493253126, 0.014745644259316126],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09378609406810362, 0.17277202074430695, 0.028578600126531007, 0.07792888569583485, 0.6609172851656846],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-Cds(Cds-Cds)(Cds-Cds)",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1982747964728306, 0.39657619484995665, 0.28370386234957085, 0.08768920261741717, 1.2139692793526438],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-Cds(Cds-Cds)O2s",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.05566125357873409, 0.5198409336460749, 0.05372155288051664, 0.18372471039728858, 1.0085279109437555],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10959027301009734, 0.7655838122949516, 0.04308743323066683, 0.048935494738087164, 1.2674592623883445],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-Cds(Cds-Cds)Ct",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.12550903259693352, -0.10770650084065952, 0.19697888252657075, 0.3251918903233371, 0.1876204364158236],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.05569793662447388, 0.2912227603772067, -0.04624457933198731, 0.0849404196936073, 0.7491119252276477],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.6454011258385005, 0.7600519404046293, 0.6013795279096188, 0.07882002529567725, 2.703481678284068],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2820827888760842, -0.38327962515418496, 0.04390938641169456, 0.10364198342806141, 0.27526674411381935],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2820827888760848, -0.38327962515418557, 0.04390938641169566, 0.10364198342806161, 0.27526674411382257],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.5970226066139421, 0.450916143715174, -0.1810459200690338, 0.12813061754016933, 1.0690320171022807],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.2982966468953846, -0.3569565551947327, 0.5958661246777496, -0.13619622529850875, -0.22111524511714498],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.2982966468953846, -0.3569565551947327, 0.5958661246777496, -0.13619622529850875, -0.22111524511714498],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1173761804826958, 0.6597048887324907, 0.47380383394624753, 0.2484603239111828, 1.5400067893819331],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11852538145631568, 0.3792063846061014, 0.03275270018257624, 0.18363256988349014, 0.8765784453253261],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.09450483863650447, 0.36513899171078107, 0.3600791706355209, 0.08819233834236948, 0.9474985330111153],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.5026773293801252, -0.1783455721332315, 0.32424352841990256, 0.2060152223568904, 1.5538829286966467],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsSH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.17785413894223873, -0.7464258130771685, -0.027839559617060056, 0.37510012949435156, 0.13253250825503038],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08560773389717244, -0.24788215739961023, -0.1194543409341037, 0.28304723685208544, 0.5067702972287942],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10553316799494677, 0.5450524647668932, 0.4119948517280676, 0.1665439868059026, 1.478166391673851],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsCsS2H",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.21980306946463402, 0.5056343476017979, -0.18319869013001358, 0.040618152675351404, 0.9910672898812359],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.04505508319877924, 0.10725149251304988, 0.13825228105137344, -0.07441760992413073, 0.9557834280114053],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2701917324589999, 0.8471214362802257, 0.5169005976957107, 0.09047205574214491, 2.2764117932576964],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.15022622411494777, 0.5150484877718924, -0.0338506522421263, 0.15138996554601464, 1.0677210384840858],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.06847826498988273, 0.6140588598195716, 0.6624087798909557, -0.11186820463848828, 1.2454046986620186],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-CsOsS2H",
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
    thermo = u"Cs-CsOsSH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18701275234956638, -0.13950040841677958, 0.157772652018009, 0.014773186147527519, 0.094795282089634],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.06976849566151319, 1.1246945835692428, 0.2684580983055458, -0.06834134577873274, 1.0987606196950808],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)CbCsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.012333740092320501, -0.026825349995100188, 0.01573180119192242, -0.011211472651539208, 0.3823736733718368],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cds-CdsCsS2",
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
    thermo = None,
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2561494375816057, -0.1995804581820876, -0.14623939931020263, -0.1325393450712009, 0.7664983193973043],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18299961650259727, 0.0778909421158693, 0.007545267789981852, 0.05197441218783918, 0.6128105950417962],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.12606351229462584, 0.2943609248338298, -0.3377610348410798, 0.4926077404314505, 0.3288306420991319],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3527781042983569, 1.146786835926914, 0.375452831518661, 0.2331623092205972, 0.8200715389940614],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)CsCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.10472741384605519, -0.017775735048488617, 0.33881015519132585, 0.20931975373867684, 0.3765241611648794],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.40139767047555763, 0.24589755259763107, 0.006184214400441895, 0.4508165019303533, 1.0819226452281316],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08802313703340454, -0.36187081448213493, 0.1962410614875744, -0.30950022034309693, 0.08917429809759253],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.08150812994953947, 0.3875932937623118, 0.08859514559424157, 0.2709056662479846, 0.8371730264637574],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.028675622045830018, -0.3931365921829727, 0.0194796332973084, 0.08929749104279731, 0.16115780773627597],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.34805102469869137, 0.4307137205721421, -0.08522682699879348, 0.1755683052782913, 1.4524977340607808],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.23155698740916486, -0.17278916831612806, -0.3598948614767424, 0.01681625202128848, 0.24950342516535493],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"S2s-S2sCs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3377423498581759, -0.22099430719252156, -0.0728304959288554, -0.06389049529251839, 0.7357435987255514],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3965024728713409, 0.0996795538872194, -0.0041162214562220556, 0.11264880965578614, 1.1650225998923895],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"S2s-SsSs",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22473189470121802, 0.899488171390992, 0.7148878886420258, 0.12400323132906399, 2.301796571153439],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.16287257868399402, -0.05323711083088481, -0.37687842389576975, -0.23373380099479102, 0.2370023724877336],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.006155279187819232, 0.7293468263948929, 0.060598550854288565, 0.07067667706426002, 1.0441273826845734],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.04305339721549087, 0.2655283927212688, -0.07582687343985971, 0.10112876480844922, 0.7640303090131402],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1919,
    label = "CJ2_singlet",
    group = 
"""
1 * C u0 p1
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.10743157581311454, -0.13571088039322196, -0.07105475756246488, -0.05689174786994966, 0.24300770104283573],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.05258150092902092, 0.31972667156218537, -0.040221694922162265, 0.042652420722006354, 0.83576228235607],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.013038476994465684, 0.5548279463965562, -0.04172912125451941, 0.1760168085507567, 1.0925811330751487],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.01620269758739576, 0.6183148228804959, 0.007791650484769493, 0.20473590905967426, 1.229952431043524],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3140768578103957, -0.05050342121619761, -0.3339054649478014, -0.026117603391514033, 0.49012864337100304],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2168181082735448, -0.13414143880297436, -0.09923125254745133, -0.07977664760647665, 0.35714166893153076],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.23673887080111786, 0.004151224905899205, -0.1910169006488292, 0.2219743552098975, 0.6705503605173065],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.048490264807414155, 0.15940315599414154, 0.2198593935199073, 0.06918608520625973, 0.6116410897259892],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.00481929455187266, -0.17811155382872285, 0.2155245629833072, 0.20876771036262443, 0.196395362171784],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)CbH",
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)CbH",
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.34497425491487843, -0.3532119503733878, 0.24268925835553334, -0.07179057708669978, 0.678196445201926],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3380595539209284, -0.31023920990852183, 0.36016851178471604, 0.3117588802540209, 0.0025384978306891015],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4848331853323451, 0.19924726691539513, 0.1500837421848292, 0.020751386914279503, 1.550053870015726],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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