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
1 * R u0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1096,
    label = "O2d-O2d",
    group = 
"""
1 * O2d u0 {2,D}
2   O2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.05174899380970027, -0.1325241992817245, -0.02575797725235244, -0.023478502437983474, -0.10118755310015973],"cal/(mol*K)"),
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
    thermo = u"O2d-Cd",
)


entry(
    index = 1093,
    label = "O",
    group = 
"""
1 * O u0
""",
    thermo = u"O2s-CsCs",
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
        Cpdata = ([0.23908840585840652, 0.5049002182148893, -0.025664316348627453, -0.025335047859298687, 1.3696897532772287],"cal/(mol*K)"),
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
    thermo = u"O2s-(Cds-Cd)(Cds-Cd)",
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
        Cpdata = ([-0.10349798761947673, 0.014951601436474008, -0.001515954504723094, 0.05304299512399152, 0.5786248937990788],"cal/(mol*K)"),
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
        Cpdata = ([0.1640009033290339, 0.2562562890625965, 0.3895300859107864, 0.1545138435657854, 0.975579521089694],"cal/(mol*K)"),
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
        Cpdata = ([0.4103658053980258, 0.03854586796035071, -0.011443983652633044, 0.12342998740042782, 1.141195112044754],"cal/(mol*K)"),
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
    index = -1,
    label = "S2s",
    group = 
"""
1 * S2s u0
""",
    thermo = None,
)


entry(
    index = 1400,
    label = "S",
    group = 
"""
1 * S u0
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
3   O    ux p2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.02669323292507131, 0.3992561233838114, -0.22133160356625708, -0.2769925329811275, 0.5087790868063307],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 2029,
    label = "S4dd",
    group = 
"""
1 * S4dd u0
""",
    thermo = u"S4dd-OdOd",
)


entry(
    index = 2024,
    label = "O2d-S2d",
    group = 
"""
1 * O2d u0 {2,D}
2   S   ux {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11990438972776318, -0.0021522609736317477, 0.22490782453077396, 0.16501776405257895, 0.3949229034966777],"cal/(mol*K)"),
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
        Cpdata = ([0.3960102104959856, 0.10140018163798808, 0.14987801003725693, 0.02435501084111441, 1.2294127973120499],"cal/(mol*K)"),
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
        Cpdata = ([-0.012508198115368852, -0.08644858020143897, -0.20139396454196995, -0.07131201571706994, 0.42821209648768077],"cal/(mol*K)"),
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
        Cpdata = ([0.26959597089359616, 0.515140512054025, 0.22523690306378064, 0.2782854070810114, 1.4625221309796876],"cal/(mol*K)"),
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
        Cpdata = ([0.11097461069621331, 0.0639435697513529, 0.024520291412763618, 0.1424342378642199, 0.6723519688635623],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3s-CHH)"""),
)


entry(
    index = 1920,
    label = "N3t-CtH",
    group = 
"""
1   Ct  u0 {2,T} {3,S}
2 * N3t u0 p1 {1,T}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.0027257046771925197, -0.04449098709266366, 0.2543782776846371, -0.01633989998604028, 0.05748292509753229],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3t)"""),
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
        Cpdata = ([0.10677630770338106, 0.4394425885292048, 0.07410576781064816, 0.10938289511005099, 1.2920419687020803],"cal/(mol*K)"),
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
    index = 20,
    label = "Ct",
    group = 
"""
1 * Ct u0
""",
    thermo = u"Ct-CtCs",
)


entry(
    index = 330,
    label = "Cs-HHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   H  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.10349798761943349, -0.2650483985634415, -0.05151595450471452, -0.04695700487597748, 0.19762489379969422],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
    index = 1095,
    label = "O2d-Cd",
    group = 
"""
1 * O2d u0 {2,D}
2   CO u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""In this case the C is treated as the central atom""",
    longDesc = 
u"""

""",
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
        Cpdata = ([-0.08817861020433392, -0.11154366715177329, -0.01240118966490523, -0.006819497256893879, 0.4447711727093905],"cal/(mol*K)"),
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
        Cpdata = ([0.0014619949796302223, -4.6627411575768407e-05, -2.5476891079474827e-05, 0.0025573210761705607, 0.5125422350965644],"cal/(mol*K)"),
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
        Cpdata = ([0.1284977092395355, 0.11650617592152128, -9.679210751118664e-05, 0.0156750494259312, 0.574962591147235],"cal/(mol*K)"),
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
        Cpdata = ([0.1506591516288669, 0.12642142004743437, 0.025919266286549867, 0.08646110824305733, 0.4800213431762251],"cal/(mol*K)"),
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
        Cpdata = ([0.2593957007255649, 0.37772580422992647, 0.0620747896782675, 0.2698703727476093, 0.7523706118931824],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cs-NCsCsCs)"""),
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
        Cpdata = ([0.1511559421220307, 0.5318399274805011, 0.08157787611501595, 0.00898891562567447, 1.3475624327414515],"cal/(mol*K)"),
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
        Cpdata = ([0.07015787344989385, -0.01623946908685444, -0.010041182370047278, -0.01779808809910504, 0.18298273991376018],"cal/(mol*K)"),
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
        Cpdata = ([0.009600404188746692, -0.08626110859580843, -0.0019842551363445926, 0.2039516908690073, 0.06042937950023375],"cal/(mol*K)"),
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
        Cpdata = ([-0.021385536009011306, -0.0685438825022266, 0.07900284006635881, 0.004317476904691076, 0.39264354424122194],"cal/(mol*K)"),
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
        Cpdata = ([0.2444062383170216, 0.2470686596372263, 0.03468970913281251, 0.15073381909687555, 1.0593352235803668],"cal/(mol*K)"),
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
        Cpdata = ([0.0032169804237659853, 0.14676105821378002, -0.1592237519032595, 0.24142646174368063, 0.5398156348541737],"cal/(mol*K)"),
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
        Cpdata = ([-0.017666340001603144, -0.08178126377642456, -0.028479218329732346, -0.010302622815706847, 0.4514212037543067],"cal/(mol*K)"),
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
        Cpdata = ([-0.06422650747007042, -0.13831352711084965, -0.02413637798371939, -0.042282724740394746, 0.34259238023842287],"cal/(mol*K)"),
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
        Cpdata = ([0.08156573865725104, 0.10023880898505744, 0.009872225679255133, 0.07807829396532306, 0.803796263332035],"cal/(mol*K)"),
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
        Cpdata = ([-0.005012296238638877, -0.06783107973552037, -0.012482754899990737, -0.03137818141699275, 0.2849987614966051],"cal/(mol*K)"),
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
        Cpdata = ([0.187566070881568, 0.19880405293810233, 0.0032418740757979413, 0.03223312588205441, 0.1628659118319064],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0.140312,0.293187,-0.0339797,-0.0983181,1.16656],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0.140312,0.293187,-0.0339797,-0.0983181,1.16656],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
        Cpdata = ([0.12287895453380542, 0.24215860006665396, -0.05410065722940908, -0.1219411661712528, 1.026635009499073],"cal/(mol*K)"),
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
        Cpdata = ([0.11281400769305958, 0.07552616050458377, -0.002613940098187546, 0.022302771049495414, 0.6521457503339556],"cal/(mol*K)"),
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
        Cpdata = ([0.1898583335340007, 0.21342038480691347, 0.019538208653000728, 0.07160595202088993, 0.8378067171637523],"cal/(mol*K)"),
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
        Cpdata = ([-0.08027529549539009, -0.19896011408663036, -0.05306263302848413, -0.08292294135132419, -0.2545491596666851],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([-0.0476981,-0.199592,-0.0508303,-0.0500219,-0.406987],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)')),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([-0.00857685,-0.346971,0.00741042,0.0738776,-0.122549],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cs-CdsCdsHH)"""),
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
        Cpdata = ([-0.02065053724027461, -0.12238604678588276, -0.004760926127643827, -0.03987923512570969, -0.21591198962206162],"cal/(mol*K)"),
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
        Cpdata = ([0.050226670100668815, 0.1076942863006422, 0.042317215367813917, 0.03588769103787681, 0.706735126420129],"cal/(mol*K)"),
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
        Cpdata = ([-0.009488712014182651, -0.4099444191163158, -0.11719777530419022, -0.02016263353708732, -0.013547722336324348],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
        Cpdata = ([-0.004572924512920285, -0.3946143172567452, -0.05878784160894353, -0.04766929937056359, -0.3257673679220584],"cal/(mol*K)"),
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
        Cpdata = ([0.05154547417047921, 0.1285480985648559, -0.05437758114767541, 0.03881384237579395, 0.6651327884857163],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 28,
    label = "Ct-Ct(Cds-Cds)",
    group = 
"""
1 * Ct u0 {2,S} {3,T}
2   Cd u0 {1,S} {4,D}
3   Ct u0 {1,T}
4   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.11537673923934728, -0.007334731186632398, 0.07948378370101965, 0.018137039306754574, 0.4426739187557425],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 27,
    label = "Ct-Ct(Cds-Cd)",
    group = 
"""
1 * Ct u0 {2,S} {3,T}
2   Cd u0 {1,S} {4,D}
3   Ct u0 {1,T}
4   C  u0 {2,D}
""",
    thermo = u"Ct-Ct(Cds-Cds)",
)


entry(
    index = 25,
    label = "Ct-CtCds",
    group = 
"""
1 * Ct      u0 {2,T} {3,S}
2   Ct      u0 {1,T}
3   [Cd,CO] u0 {1,S}
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
        Cpdata = ([0.1065243360896296, 0.009781514417632932, 0.01692480737983207, 0.025633806524137596, 0.5135773204797062],"cal/(mol*K)"),
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
        Cpdata = ([-0.14299451402611582, -0.19740935823833944, -0.008795867135049151, 0.1802780657153164, 0.14864838588528917],"cal/(mol*K)"),
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
        Cpdata = ([-0.11286266385263241, -0.1480359076847218, 0.004255819154830226, 0.18095822392257283, 0.01351173522118243],"cal/(mol*K)"),
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
        Cpdata = ([0.08375827297972249, 0.03005385496112256, 0.021302712952156314, 0.31544930894204926, -0.3393543112182915],"cal/(mol*K)"),
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
        Cpdata = ([-0.05927393980923218, -0.11156147850072926, -0.11381851987607729, -0.04870844312552804, -0.4212042794464858],"cal/(mol*K)"),
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
        Cpdata = ([0.09518413324435814, 0.102442187222859, 0.11448211179979785, 0.16339960444012083, 0.8613325848592662],"cal/(mol*K)"),
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
        Cpdata = ([0.13349003277960803, 0.3208107454196752, -0.12876480877169358, -0.05978872760383555, 0.5366717425747713],"cal/(mol*K)"),
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
        Cpdata = ([-0.18696825501434627, -0.31078044381184033, -0.05027947416593602, 0.1727412063398462, -0.4510589382937473],"cal/(mol*K)"),
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
        Cpdata = ([-0.2103791368969507, -0.41434985242289124, 0.015845330818206882, 0.2369303900330098, -0.5291774534681317],"cal/(mol*K)"),
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
        Cpdata = ([-0.14140139314983274, -0.3388563638731864, 0.0684699937113876, 0.30053001714718014, -0.6124088431007131],"cal/(mol*K)"),
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
        Cpdata = ([-0.0015112669331127648, -0.21699122053117226, 0.18088178632453056, 0.33007917496722866, -0.3792815467150348],"cal/(mol*K)"),
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
        Cpdata = ([-0.0455718079746138, -0.2701648990393659, 0.0036876975568059522, 0.2660682217647612, -0.45644743296277723],"cal/(mol*K)"),
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
        Cpdata = ([0.11650201238060338, -0.05504839856344852, 0.3784840454952907, 0.14304299512403262, 1.2876248937997157],"cal/(mol*K)"),
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
        Cpdata = ([0.10895805070936429, 0.4179351664215367, -0.10705340337067974, 0.3609423464415978, 1.43175965201448],"cal/(mol*K)"),
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
        Cpdata = ([0.013949872355841596, 0.02318322474983064, 0.05191861073962919, 0.005464570871987618, 0.3005188387802521],"cal/(mol*K)"),
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
        Cpdata = ([0.13121668315531207, 0.1326384858268037, 0.08188810696145513, 0.020848264992249874, 0.40691959599288674],"cal/(mol*K)"),
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
        Cpdata = ([0.21988172880783083, 0.26806520508199244, 0.1732513952597779, 0.10205380857883335, 0.5024789298237347],"cal/(mol*K)"),
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
        Cpdata = ([0.11993919769589739, 0.2641815803490529, -0.027446856173485853, 0.23029726831373598, 1.1496595065794213],"cal/(mol*K)"),
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
        Cpdata = ([-0.023370594710247383, -0.5883692926380295, 0.17153732317978587, 0.14281416390712173, -0.5482750955266138],"cal/(mol*K)"),
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
        Cpdata = ([0.09819558467131484, 0.37249078506659516, -0.09631642271305516, 0.27332516689871944, 1.0909336042606632],"cal/(mol*K)"),
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
        Cpdata = ([0.05362305784679292, 0.24279300136988974, 0.0025847027247016957, 0.46498416129528436, 0.895989884300585],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
    thermo = u"Cds-(Cdd-O2d)HH",
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
        Cpdata = ([0.07953686919202033, 0.22891448415260368, 0.06773553004131012, 0.18695505869048942, 0.7955790586296179],"cal/(mol*K)"),
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
        Cpdata = ([0.1729205965217786, 0.3080083074967346, -0.09402187427368144, 0.12616407022910564, 1.078439090387891],"cal/(mol*K)"),
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
        Cpdata = ([0.1550954864306915, 0.25836069709456794, 0.09719711201949514, 0.2601061575213107, 0.8896656601875774],"cal/(mol*K)"),
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
        Cpdata = ([-0.045806243457230104, -0.1821605428845519, 0.0728023300735204, -0.04649382222682699, -0.11430467777359025],"cal/(mol*K)"),
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
        Cpdata = ([0.1324397408186046, 0.5899035277407433, -0.1612513332433686, 0.4106796814373438, 1.6635397173628486],"cal/(mol*K)"),
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
        Cpdata = ([0.1872908587684597, 0.45451497976107114, -0.10627154174164107, 0.22475609788295792, 1.1614787105221145],"cal/(mol*K)"),
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
        Cpdata = ([-0.053574787482876834, -0.4049394764061343, 0.167953863233862, 0.1366726242033774, -0.2586400918664702],"cal/(mol*K)"),
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
        Cpdata = ([0.08603677110637886, -0.40118862164602664, 0.13018230958020283, -0.17275701708193036, -0.07778574812675532],"cal/(mol*K)"),
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
        Cpdata = ([0.1324857518192006, 0.17107885207456772, 0.0735874031591478, 0.09608791517936895, 0.7603044949246538],"cal/(mol*K)"),
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
        Cpdata = ([0.048566961576904114, -0.2574127153155954, -0.076243584956518, -0.3157294564258411, -0.30779398009265757],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1180,
    label = "Cds-CdsSsH",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   S2s u0 {1,S}
4   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.1056477212490562, 0.16834002959106079, 0.04027883390013993, 0.19990609143627666, 1.1746980777228362],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
        Cpdata = ([0.11635374539968647, 0.08721462058909364, -0.11177421555101735, 0.1988281636206561, 0.39525879148617804],"cal/(mol*K)"),
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
        Cpdata = ([0.2523423294326518, 0.42747739866528167, 0.258545935352788, 0.175341977212892, 1.397693823958265],"cal/(mol*K)"),
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
        Cpdata = ([0.11119439360571903, 0.1140031711126948, 0.2719932250421545, 0.09625631475322224, 0.46207170128933694],"cal/(mol*K)"),
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
        Cpdata = ([0.1601918881613275, 0.15489433496546365, -0.013522511870179, 0.2298172389181077, 0.9361822576335705],"cal/(mol*K)"),
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
        Cpdata = ([-0.007086397414638269, 0.09518965442199853, -0.10520316097521559, 0.15428410678002993, 0.5058384208836937],"cal/(mol*K)"),
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
        Cpdata = ([-0.04949382096964332, 0.24223220534783768, -0.05672898790173134, 0.03141144897023577, 0.30975163896957536],"cal/(mol*K)"),
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
        Cpdata = ([0.12217804097829457, 0.3056005277766957, 0.04692741933553224, 0.12606193406398286, 1.0379162136692417],"cal/(mol*K)"),
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
        Cpdata = ([0.030593675351341176, -0.09382249110325587, -0.16696645395438264, 0.029004645024046902, 0.039529544660500265],"cal/(mol*K)"),
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
        Cpdata = ([0.06466321064250184, 0.14068625097710985, -0.10505564065040592, 0.1274605590822193, 0.4421806609233174],"cal/(mol*K)"),
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
        Cpdata = ([0.11899558300108659, 0.34500587144887146, 0.6455134342458826, 0.12541851189331496, 1.3698447757795156],"cal/(mol*K)"),
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
        Cpdata = ([0.027956658805021684, -0.06180930479821606, -0.18563731194039837, 0.00211808952686815, -0.07027492467067353],"cal/(mol*K)"),
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
        Cpdata = ([0.06408483119942919, 0.12151569024854958, 0.029692713310975317, 0.04296259309507928, 0.5354669785506457],"cal/(mol*K)"),
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
        Cpdata = ([0.026725704677216564, 0.19550901290734146, -0.05562172231535659, 0.16366010001398032, 0.9675829250975851],"cal/(mol*K)"),
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
        Cpdata = ([0.009121291658808772, 0.34292644841695463, -0.10163772696139194, 0.165746784145577, 0.7434389967590014],"cal/(mol*K)"),
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
        Cpdata = ([0.08931382281280811, 0.5116633088677148, -0.09324121979708383, 0.19504584573342534, 0.8909145657546872],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([-0.292646,-0.735,-0.116265,0.0193397,-1.33201],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cs-CtCsCsH)"""),
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
        Cpdata = ([0.19426153529021978, 0.4701400143626694, -0.08841815332063675, 0.28411859178466614, 0.69426940696944],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0.0218762,-0.259026,-0.137546,0.138637,-0.232954],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cs-CtCsCsCs)"""),
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
        Cpdata = ([0.14662379341522808, 0.16507826113859472, -0.09587149896285427, 0.13485049751916248, 0.687820939399964],"cal/(mol*K)"),
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
        Cpdata = ([0.13461855214889068, 0.16560380379461903, -0.07300612600190329, 0.2562454475700832, 0.7555693411048606],"cal/(mol*K)"),
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
        Cpdata = ([-0.06989064607332779, -0.09497111844120593, -0.05323732762754618, 0.15724920935931677, 0.20041111159334649],"cal/(mol*K)"),
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
        Cpdata = ([0.13469839078353707, -0.0014093763401369502, -0.17396951287364817, 0.26775570734191484, 0.34122850949566413],"cal/(mol*K)"),
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
        Cpdata = ([-0.11422540224586288, -0.28542177247760714, 0.0027036267833581967, 0.001890903298071435, -0.16108805897055511],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3s-CCC)"""),
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
        Cpdata = ([0.04110778851011651, 0.16336221452938338, -0.03718989814629497, 0.19671253163487018, 0.9320758488732187],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cs-NHHH)"""),
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
        Cpdata = ([0.12342648557710745, 0.16790980670554545, 0.005140299848775515, 0.20301309009499952, 0.8235795465644142],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cs-NCsHH)"""),
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
        Cpdata = ([0.022949396973831998, 0.4360664243781413, 0.0002725098739962302, 0.2942772049039323, 0.9145409563954829],"cal/(mol*K)"),
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
        Cpdata = ([0.2238379177235277, 0.17910516742695257, 0.028540106162243395, 0.2356508726902368, 0.7789270181596326],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cs-NCsCsH)"""),
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
        Cpdata = ([-0.07023631740904676, -0.15106181670355265, 0.08223099565427966, 0.17604668800077783, 0.21758030368458897],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3s-CCH)"""),
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
        Cpdata = ([-0.06957220816125115, 0.33099483650293415, 0.21838412995237144, 0.05738922295092734, 0.5673110952943086],"cal/(mol*K)"),
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
        Cpdata = ([0.3434327839340734, 0.3534860999267689, 0.17774219467438038, 0.2132416807159216, 1.3807667598680011],"cal/(mol*K)"),
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
        Cpdata = ([0.025425821630996548, -0.30611044285083483, 0.05698092626305324, 0.36066741544045267, 0.06716443813819484],"cal/(mol*K)"),
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
        Cpdata = ([0.1280782949443001, 0.11970781967266295, -0.026569903825774576, 0.382971777407357, 0.8306414281051522],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0.312414,0.122851,-0.122774,0.294177,0.843567],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3d-CsR)"""),
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
        Cpdata = ([-0.07128228001039266, 0.29273922708749955, 0.3128664523250443, 0.17262451657240147, 0.6766481087982033],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cs-N3dCHH)"""),
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
        Cpdata = ([0.16176664057104168, 0.1407601378642831, 0.11213168971386844, 0.06952579525835123, 0.8975657928836449],"cal/(mol*K)"),
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
        Cpdata = ([0.09471480819769339, 0.24950973393494205, -0.006678393793754831, 0.05667049740973626, 0.747270637095609],"cal/(mol*K)"),
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
        Cpdata = ([0.09471480819693902, 0.24950973393510736, -0.006678393793692635, 0.05667049740917465, 0.7472706370948429],"cal/(mol*K)"),
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
        Cpdata = ([0.04711406672194045, 0.3683899797030187, 0.3147515100493812, 0.2278352510787584, 0.9864048447151786],"cal/(mol*K)"),
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
        Cpdata = ([0.25181369986094193, 0.750172554212288, 0.09723546226782186, 0.2666028424230906, 2.0372671632829267],"cal/(mol*K)"),
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
        Cpdata = ([0.29701390204644157, 0.6483259985282269, 0.05054673037639235, 0.37384471186407014, 1.9297674862133032],"cal/(mol*K)"),
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
        Cpdata = ([0.017161805291419363, 0.2535931928871638, -0.057591951287852355, -0.08452325917346284, 0.8423897001920877],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(O2s-CN)"""),
)


entry(
    index = 1945,
    label = "O2s-N",
    group = 
"""
1 * O2s u0 {2,S}
2   N   u0 {1,S}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(O2s-N)"""),
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
        Cpdata = ([0.016895380778866487, -0.08049257138012869, 0.18672353074002485, 0.0565209591150619, 0.09371517551945618],"cal/(mol*K)"),
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
        Cpdata = ([0.043135408320750704, -0.07293055813106801, -0.19254784047374274, -0.15040705084748568, -0.0801923701865051],"cal/(mol*K)"),
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
        Cpdata = ([-0.27545907462227753, -0.08680678254199548, -0.09786845127699523, 0.08048052614305884, 0.028965456302515867],"cal/(mol*K)"),
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
        Cpdata = ([0.3177561366441792, 0.10787133353292236, 0.06252022660530988, 0.0029939664453722398, 1.3096213296613357],"cal/(mol*K)"),
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
    index = 1163,
    label = "Cs-CsSsHH",
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
        Cpdata = ([0.00896901773821368, 0.1224370374636074, -0.08174886598035477, 0.1576208571146736, 0.6881943258407561],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
    thermo = u"Cs-CsSsHH",
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
        Cpdata = ([-0.29264605022248585, -0.7349998011659743, -0.11626465049288233, 0.019339695871849402, -1.332007149694934],"cal/(mol*K)"),
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
        Cpdata = ([0.19146312540917432, 0.5784257437445098, 0.14231188832380293, 0.09260095417324689, 1.582040174451168],"cal/(mol*K)"),
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
        Cpdata = ([0.3024743317694407, -0.19844551227288318, 0.04151040433462163, 0.09907825897353942, 0.17823216237875306],"cal/(mol*K)"),
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
        Cpdata = ([0.03965414651557095, 0.4604730962662001, 0.09551022009026218, 0.06781416451551468, 0.9685227668505958],"cal/(mol*K)"),
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
        Cpdata = ([-0.10176946718387267, -0.1424939141441118, 0.005737051011094073, 0.08412594070886631, -0.16543914786391464],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
        Cpdata = ([-0.06852707964194532, -0.4528600645035395, -0.04769232322143914, 0.17965515278189464, -0.6095973032834552],"cal/(mol*K)"),
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
        Cpdata = ([-0.05120269285253781, -0.13949095564490188, 0.0025852726674486792, 0.16924853052657227, -0.7767559087819247],"cal/(mol*K)"),
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
        Cpdata = ([0.40791745731941986, 0.8855437794109894, -0.09746587354284172, 0.3416885401824878, 1.7145209697489046],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
    label = "Cs-SsHHH",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   S  u0 {1,S}
3   H  u0 {1,S}
4   H  u0 {1,S}
5   H  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.08717663936255854, 0.10695221362497234, -0.1011978318629384, 0.10447492574240129, 0.7134808236945618],"cal/(mol*K)"),
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
        Cpdata = ([0.023824359411981688, 0.671391114918523, -0.2629005540750524, -0.0590953156375299, 0.9170032295324986],"cal/(mol*K)"),
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
        Cpdata = ([-0.3628305785610139, 1.5015556666557677, -0.20642881435506424, 0.3088695664378468, 1.773112253310558],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 2025,
    label = "O2s-CsS6dd",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   S6dd ux {1,S}
3   Cs   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22625641976915534, -0.17874041339763885, -0.13865552747054766, -0.22320911542480384, 0.320185030862584],"cal/(mol*K)"),
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
    thermo = u"O2s-CsS6dd",
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
        Cpdata = ([0.3747038584141154, 0.9037553028065494, -0.16043429033321358, 0.13145496753094527, 1.683205252279147],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1148,
    label = "S2s-SsCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cs  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.34951121940560737, 0.1242800747697004, 0.07763795832806301, -0.042831638938289146, 1.1057417297551126],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = -1,
    label = "S2s-SsC",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   C   u0 {1,S}
""",
    thermo = u"S2s-SsCs",
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
    thermo = u"S2s-SsC",
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
        Cpdata = ([-0.03838527021640695, 0.0197163569530501, -0.07466459574902129, 0.1262297030648891, 0.32512574825525475],"cal/(mol*K)"),
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
2   S2d u0 {1,D}
3   S2d u0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.019518408611384874, -0.20784876183943757, -0.3512719745792252, -0.06566702655819995, 0.43179929917551974],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1463,
    label = "S2s-CsCO",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CO  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2112224938865655, 0.12261621438172962, 0.006097886166251176, 0.028846660124582722, 0.9700497353318895],"cal/(mol*K)"),
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
        Cpdata = ([0.25504877384730623, 0.26688807124428526, -0.01918728904185991, 0.2687982564013782, 1.2936141019316933],"cal/(mol*K)"),
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
        Cpdata = ([0.3634188205915564, 0.03658622093894234, -0.02794777856125455, 0.08602195721389187, 1.0353597639752354],"cal/(mol*K)"),
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
        Cpdata = ([-0.34556480714090887, 0.14653343754780163, -0.3817730048459227, 0.266036701297199, 0.14709386038368155],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 2026,
    label = "O2s-S4dH",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   S4d ux {1,S}
3   H   ux {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22921065895027412, 1.3232121410778666, 0.13790575646450065, 0.00954460582419997, 1.7184804600977697],"cal/(mol*K)"),
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
    thermo = u"O2s-S4dH",
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
        Cpdata = ([0.18915331621227086, 0.24797714618300223, -0.10948271537149448, 0.007183450450385237, 1.1294982553212423],"cal/(mol*K)"),
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
        Cpdata = ([0.23357016280781118, 0.08741360315554181, -0.0022218221431889616, 0.010600658893164371, 0.5408812802728902],"cal/(mol*K)"),
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
        Cpdata = ([0.11728142126276281, 0.1607547256783448, -0.031835825045370636, 0.04386958091108159, 0.4624352526655179],"cal/(mol*K)"),
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
    index = 226,
    label = "Cds-CdsCtCds",
    group = 
"""
1 * Cd      u0 {2,D} {3,S} {4,S}
2   Cd      u0 {1,D}
3   Ct      u0 {1,S}
4   [Cd,CO] u0 {1,S}
""",
    thermo = u"Cds-Cds(Cds-Cds)Ct",
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
        Cpdata = ([-0.1659837027521116, -0.6125694452301499, -0.07392526350455925, -0.13711981137087081, -1.6304674207188143],"cal/(mol*K)"),
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
    index = 549,
    label = "Cs-(Cds-Cds)CtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.031232831248208227, 0.3011485330291084, -0.008020948142621165, 0.680303639034897, -0.1712478041291292],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 548,
    label = "Cs-(Cds-Cd)CtCsCs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Ct u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
6   C  u0 {2,D}
""",
    thermo = u"Cs-(Cds-Cds)CtCsCs",
)


entry(
    index = 546,
    label = "Cs-CtCdsCsCs",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   Ct      u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   Cs      u0 {1,S}
5   Cs      u0 {1,S}
""",
    thermo = u"Cs-(Cds-Cds)CtCsCs",
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
        Cpdata = ([-0.043886016109329, 0.028998576951545292, -0.07212222294408371, 0.09841706797825953, 0.5186378109353935],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 93,
    label = "Cds-O2d(Cds-Cds)(Cds-Cds)",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   Cd  u0 {2,D}
6   Cd  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13326103386735838, 0.08536417212049575, -0.1704420761972626, 0.025787605701770112, 0.353168874883575],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 92,
    label = "Cds-O2d(Cds-Cd)(Cds-Cd)",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   Cd  u0 {1,S} {5,D}
3   Cd  u0 {1,S} {6,D}
4   O2d u0 {1,D}
5   C   u0 {2,D}
6   C   u0 {3,D}
""",
    thermo = u"Cds-O2d(Cds-Cds)(Cds-Cds)",
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
    thermo = u"Cds-O2d(Cds-Cds)(Cds-Cds)",
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
        Cpdata = ([0.2663495575443363, -0.09054377098007194, 0.015270471302568332, -0.1203217346379085, 0.3123617150734789],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 580,
    label = "Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S}
6   Cd u0 {2,D}
7   Cd u0 {3,D}
8   Cd u0 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.03771247639712467, -0.13180428593210208, 0.03434948500679875, 0.13683665651690746, -0.31316511179946216],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 579,
    label = "Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cd u0 {1,S} {7,D}
4   Cd u0 {1,S} {8,D}
5   Cs u0 {1,S}
6   C  u0 {2,D}
7   C  u0 {3,D}
8   C  u0 {4,D}
""",
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs",
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs",
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
        Cpdata = ([0.27423878744553887, 0.26075300240062116, 0.09858880316100391, 0.06296115320654708, 1.1092527453705436],"cal/(mol*K)"),
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
        Cpdata = ([0.15566253623617182, 0.2995641041699259, 0.051623132216746914, -0.06298693795854601, 0.19661835953377835],"cal/(mol*K)"),
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
    index = 859,
    label = "Cs-(Cds-Cds)(Cds-Cds)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.030671527170142154, -0.734835914345683, -0.13753776247378066, 0.3008296783234448, -0.9179605663548673],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 858,
    label = "Cs-(Cds-Cd)(Cds-Cd)CsOs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   Cs  u0 {1,S}
5   O2s u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)CsOs",
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
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)CsOs",
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
        Cpdata = ([0.021876180700109327, -0.25902615879735347, -0.13754582644271213, 0.13863709756403667, -0.2329535699064831],"cal/(mol*K)"),
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
        Cpdata = ([0.3664757120511802, 0.31264709891846426, 0.12327599957607252, 0.2600465994653661, 1.7027571940293575],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cds-CCN)"""),
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
        Cpdata = ([0.36829602122493366, 0.1362398547973307, 0.09222851281831305, 0.19915031779553602, 1.1737947730498028],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3s-NCH)"""),
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
        Cpdata = ([0.0373762630661546, 0.022935209866071588, -0.015888896663354222, 0.11285318726011696, 0.43854201835435647],"cal/(mol*K)"),
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
        Cpdata = ([0.2689464048446008, 0.26363624294826443, 0.1618515837132139, 0.1560493330211602, 1.2663542940108936],"cal/(mol*K)"),
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
        Cpdata = ([0.08192699483194575, 0.3794346706437147, 0.1486811330066968, 0.37854829522316435, 1.0742873081028899],"cal/(mol*K)"),
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
        Cpdata = ([0.24393494276855396, 0.07383078829768255, 0.03952435350721902, -0.1358333676954369, 0.7714108878212244],"cal/(mol*K)"),
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
        Cpdata = ([0.5096678772807497, 0.07708228582979043, 0.052846323296315126, -0.26966304224594995, 0.9601093892224265],"cal/(mol*K)"),
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
        Cpdata = ([0.2482761724529325, 0.2704671049136069, 0.060101168841009744, 0.22605336029727813, 1.410280407760864],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(Cds-CNH)"""),
)


entry(
    index = 1055,
    label = "Cs-(Cds-Cds)(Cds-Cds)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   Cd  u0 {2,D}
7   Cd  u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.19741945063070104, -0.49815146918306796, -0.041188672915756105, 0.11164489589741283, -1.082058005433716],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1054,
    label = "Cs-(Cds-Cd)(Cds-Cd)OsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S} {6,D}
3   Cd  u0 {1,S} {7,D}
4   O2s u0 {1,S}
5   H   u0 {1,S}
6   C   u0 {2,D}
7   C   u0 {3,D}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([29.82,38.47,43.27,45.7,47.5,48.09,48.78],'J/(mol*K)','+|-',[3.64,3.64,3.64,3.64,3.64,3.64,3.64]), H298=(-17.4,'kJ/mol','+|-',3.1), S298=(-64.14,'J/(mol*K)','+|-',4.24)),
)


entry(
    index = 1047,
    label = "Cs-CdsCdsOsH",
    group = 
"""
1 * Cs      u0 {2,S} {3,S} {4,S} {5,S}
2   [Cd,CO] u0 {1,S}
3   [Cd,CO] u0 {1,S}
4   O2s     u0 {1,S}
5   H       u0 {1,S}
""",
    thermo = u"Cs-(Cds-Cds)(Cds-Cds)OsH",
)


entry(
    index = 1142,
    label = "S2s-CdCt",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cd  u0 {1,S}
3   Ct  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2648334743354864, -0.05126265038367776, -0.16412596531427498, -0.19209211694557513, 0.5351719644831469],"cal/(mol*K)"),
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
        Cpdata = ([0.6415161878764588, 0.7250006230457335, 0.33252595130766216, 0.17331117421271056, 2.4310923097384913],"cal/(mol*K)"),
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
        Cpdata = ([-0.5319196820712153, -0.47397123074143344, -0.7177762495089668, 0.2698791850828831, -1.540455633761403],"cal/(mol*K)"),
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
2   N3d u0 {1,S} {5,D}
3   Cs  u0 {1,S}
4   Cs  u0 {1,S}
5   O2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.08197019598400998, 0.534550784799307, -0.013059063951483443, -0.052400134884820766, 1.0449963338063266],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([-0.0690786,-0.109114,0.0746382,0.082017,0.0969438],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3s-NCsCs)"""),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3s-NCC)"""),
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
        Cpdata = ([0.13051820073487885, 0.2324577667422485, -0.15882692504040885, 0.445513592715229, 0.1916535938380619],"cal/(mol*K)"),
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([0,0,0,0,0,0,0],'cal/(mol*K)'), H298=(0,'kcal/mol'), S298=(0,'cal/(mol*K)'), comment="""group(N3s-NCdCs)"""),
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
        Cpdata = ([0.47666906065452463, 0.5462654036826614, 0.49811009230911735, 0.3330587310582013, 2.174858149219303],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
        Cpdata = ([0.28735559159234814, 0.18081069916937775, 0.1001039800677542, 0.16455927129322137, 0.7141066430115885],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1175,
    label = "Cs-CsCsCsSs",
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
        Cpdata = ([0.16043811958781085, 0.22096119514943507, -0.1359289634214989, 0.3078973348696931, 0.3052876417997916],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = -1,
    label = "Cs-CCCSs",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   C   u0 {1,S}
5   S2s u0 {1,S}
""",
    thermo = None,
)


entry(
    index = 1181,
    label = "Cds-CdsCsSs",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   Cd  u0 {1,D}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.21427093564003652, 0.27451878027474635, 0.01765097524227168, 0.24440026686564859, 1.308273629064355],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = -1,
    label = "Cds-CdCS",
    group = 
"""
1 * Cd  u0 {2,D} {3,S} {4,S}
2   C   u0 {1,D}
3   C   u0 {1,S}
4   S2s u0 {1,S}
""",
    thermo = None,
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
        Cpdata = ([-0.008576846368501617, -0.34697068099819706, 0.007410418011242634, 0.07387760198610646, -0.1225492612729274],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1170,
    label = "Cs-CdsCsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   Cd  u0 {1,S}
3   Cs  u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.06090554901883066, -0.5201988181250574, -0.2911793709881184, 0.2556905450681608, -0.3317620799748201],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = -1,
    label = "Cs-CCSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   C   u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
)


entry(
    index = 1169,
    label = "Cs-CsCsSsH",
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
        Cpdata = ([0.08305041008464004, 0.21878661937853944, -0.07827234115081151, 0.2043851509327074, 0.5775500584580529],"cal/(mol*K)"),
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
        Cpdata = ([0.43291433584479855, 0.06559625060200729, 0.037099399400964544, 0.14183991293834228, 0.865311721639101],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1452,
    label = "Cs-CsOsSsH",
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
        Cpdata = ([0.03395380848586782, -0.38567948917388784, -0.13587464634385618, 0.09583058107383413, -0.9233568342242489],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = -1,
    label = "Cs-COsSsH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   C   u0 {1,S}
3   O2s u0 {1,S}
4   S2s u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = None,
)


entry(
    index = 1451,
    label = "Cs-OsSsHH",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   O2s u0 {1,S}
3   S2s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.20596928160188682, 0.04907811755059244, 0.06586028533932384, 0.3156887079150709, -0.04273324102015463],"cal/(mol*K)"),
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
        Cpdata = ([0.14256540151398794, 0.41051160238146983, 0.04951169958599125, 0.26530809295736585, 0.4420418628107601],"cal/(mol*K)"),
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
        Cpdata = ([-0.06907857832479523, -0.10911396539501901, 0.0746382070022199, 0.0820170454329554, 0.09694379055656938],"cal/(mol*K)"),
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
        Cpdata = ([0.12814530167686625, 0.29494704386843973, 0.30307146718766265, 0.24779808538845657, 1.3526078011317777],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1132,
    label = "S2s-HH",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   H   u0 {1,S}
3   H   u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2065020123806015, 0.05495160143654928, 0.0484840454952927, 0.033042995124033296, 1.2266248937997073],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1149,
    label = "S2s-SsCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   S2s u0 {1,S}
3   Cd  u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18335877584856874, -0.009295862572747272, -0.06426222025127444, -0.0842307193975409, 0.4719014862853958],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
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
        Cpdata = ([0.015822641798511672, 0.1710868430092114, -0.15427421747221398, 0.24540141067469223, 0.5427669895882592],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1924,
    label = "CsJ2_singlet-CsH",
    group = 
"""
1   Cs  u0 {2,S}
2 * C2s u0 p1 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.001560918658161027, 0.15524845624567224, -0.0757176503767896, -0.11500016273980204, 0.7575014949345962],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1923,
    label = "CsJ2_singlet-CH",
    group = 
"""
1   C   u0 {2,S}
2 * C2s u0 p1 {1,S} {3,S}
3   H   u0 {2,S}
""",
    thermo = u"CsJ2_singlet-CsH",
)


entry(
    index = 1919,
    label = "CJ2_singlet",
    group = 
"""
1 * C u0 p1
""",
    thermo = u"CsJ2_singlet-CsH",
)


entry(
    index = 1154,
    label = "S2s-C=SCs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CS  u0 {1,S} {4,D}
3   Cs  u0 {1,S}
4   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3352194211463537, 0.2862891664556937, -0.01684400497445001, -0.09049784314938189, 1.117457612759061],"cal/(mol*K)"),
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
        Cpdata = ([0.31559957154287843, 0.43677975650753487, -0.13989820754088508, 0.34293576732335884, 1.7388011358731665],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1155,
    label = "S2s-C=SCd",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CS  u0 {1,S} {4,D}
3   Cd  u0 {1,S}
4   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.370423294478323, 0.24730945850576236, 0.25968237758515905, 0.028009261891176834, 1.5379586479910112],"cal/(mol*K)"),
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
        Cpdata = ([0.3124143139792266, 0.12285105221723747, -0.1227741206167759, 0.29417711655033707, 0.8435673980214311],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 1159,
    label = "S2s-C=SSs",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   CS  u0 {1,S} {4,D}
3   S2s u0 {1,S}
4   S2d u0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.29733880663174017, 0.36627468033551136, -0.195803916790165, 0.00404548194781279, 1.244862987459793],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )

tree(
"""
L1: R
	L2: N
		L3: N3d
			L4: N3d-CsR
			L4: N3d-N3dN3s
			L4: N3d-CsR
				L5: N3d-N3dCs
				L5: N3d-CdCs
			L4: N3d-CdH
		L3: N3t
			L4: N3t-CtH
		L3: N3s
			L4: N3s-NCC
				L5: N3s-NCsCs
				L5: N3s-NCdCs
					L6: N3s-(CdCd)CsN3s
				L5: N3s-NCsCs
					L6: N3s-CsCs(N3dOd)
			L4: N3s-NCH
				L5: N3s-N3sCsH
				L5: N3s-(CdCd)HN3s
			L4: N3s-CCH
				L5: N3s-(CdCd)CsH
				L5: N3s-(CO)(CO)H
				L5: N3s-(CO)CsH
				L5: N3s-CsCsH
			L4: N3s-CCC
				L5: N3s-(CdCd)CsCs
				L5: N3s-(CO)(CO)Cs
				L5: N3s-CsCsCs
			L4: N3s-CHH
				L5: N3s-(CO)HH
				L5: N3s-CdHH
				L5: N3s-CsHH
			L4: N3s-N3sHH
	L2: S
		L3: S6dd
			L4: S6dd-OdOd
				L5: S6dd-OdOdCO
				L5: S6dd-OdOdOO
				L5: S6dd-OdOdCC
		L3: S4d
			L4: S4d-Od
				L5: S4d-OdCS
				L5: S4d-OdCC
		L3: S4dd
			L4: S4dd-OdOd
		L3: S2s
			L4: S2s-HH
			L4: S2s-SC
				L5: S2s-SsC
					L6: S2s-C=SSs
					L6: S2s-SsCd
					L6: S2s-SsCs
			L4: S2s-CH
				L5: S2s-CtH
				L5: S2s-CdH
				L5: S2s-CsH
			L4: S2s-CC
				L5: S2s-C=SCd
				L5: S2s-C=SCs
				L5: S2s-CdCt
				L5: S2s-CsCd
				L5: S2s-CsCt
				L5: S2s-CsCO
				L5: S2s-CdCd
				L5: S2s-CsCs
			L4: S2s-SS
				L5: S2s-SsSs
	L2: C
		L3: CJ2_singlet
			L4: CsJ2_singlet-CH
				L5: CsJ2_singlet-CsH
		L3: Cds
			L4: Cd-N3dCsH
			L4: Cds-CdCS
				L5: Cds-CdsCsSs
			L4: Cds-CNH
				L5: Cd-CdHN3s
			L4: Cd-N3dCsCs
			L4: Cds-CCN
				L5: Cd-CdCsN3s
			L4: CO-CsSs
			L4: Cds-OdN3sCs
			L4: Cds-OdN3sH
			L4: Cds-OdOsH
			L4: Cds-CdCO
				L5: Cd-CdCsOs
					L6: Cds-CdsCsOs
				L5: Cds-CdsCdsOs
					L6: Cds-Cds(Cds-Cd)O2s
						L7: Cds-Cds(Cds-Cds)O2s
					L6: Cds-Cds(Cds-O2d)O2s
			L4: Cds-OdOsOs
			L4: Cds-CdSH
				L5: Cds-CdsSsH
			L4: Cds-OdCC
				L5: Cds-OdCdsCds
					L6: Cds-O2d(Cds-Cd)(Cds-Cd)
						L7: Cds-O2d(Cds-Cds)(Cds-Cds)
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
			L4: Cds-CdCH
				L5: Cds-CdsCtH
					L6: Cds-CdsH(CtN3t)
				L5: Cds-CdsCdsH
					L6: Cd-Cd(CO)H
					L6: Cds-Cds(Cds-Cd)H
						L7: Cds-Cds(Cds-Cds)H
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
				L5: Cds-CdsCtCds
					L6: Cds-CdsCt(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)Ct
				L5: Cds-CdsCtCt
					L6: Cds-Cd(CtN3t)(CtN3t)
				L5: Cds-CdsCtCs
					L6: Cd-CdCs(CtN3t)
				L5: Cds-CdsCdsCds
					L6: Cds-Cds(Cds-Cd)(Cds-Cd)
						L7: Cds-Cds(Cds-Cds)(Cds-Cds)
					L6: Cds-Cds(Cds-O2d)(Cds-Cd)
						L7: Cds-Cds(Cds-O2d)(Cds-Cds)
				L5: Cds-CdsCdsCs
					L6: Cd-CdCs(CO)
					L6: Cds-Cds(Cds-Cd)Cs
						L7: Cds-Cds(Cds-Cds)Cs
				L5: Cds-CdsCsCs
		L3: Cs
			L4: Cs-SsSsHH
			L4: Cs-OsSsHH
			L4: Cs-COsSsH
				L5: Cs-CsOsSsH
			L4: Cs-CCSsH
				L5: Cs-CsCsSsH
				L5: Cs-CdsCsSsH
			L4: Cs-CCCSs
				L5: Cs-CsCsCsSs
			L4: Cs-SsHHH
			L4: Cs-CSHH
				L5: Cs-CtSsHH
				L5: Cs-CdsSsHH
				L5: Cs-CsSsHH
			L4: Cs-NCsCsH
				L5: Cs-N3sCsCsH
			L4: Cs-NCsHH
				L5: Cs-N3dCHH
					L6: Cs-(N3dN3d)CsHH
					L6: Cs-(N3dCd)CsHH
				L5: Cs-N3sCsHH
			L4: Cs-NHHH
				L5: Cs-N3dHHH
					L6: Cs-(N3dCd)HHH
				L5: Cs-N3sHHH
			L4: Cs-CCOsOs
				L5: Cs-CsCsOsOs
			L4: Cs-COsOsH
				L5: Cs-CsOsOsH
			L4: Cs-OsOsHH
			L4: Cs-CCCOs
				L5: Cs-CdsCdsCsOs
					L6: Cs-(Cds-Cd)(Cds-Cd)CsOs
						L7: Cs-(Cds-Cds)(Cds-Cds)CsOs
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
				L5: Cs-CdsCdsOsH
					L6: Cs-(Cds-Cd)(Cds-Cd)OsH
						L7: Cs-(Cds-Cds)(Cds-Cds)OsH
				L5: Cs-CdsCsOsH
					L6: Cs-(Cds-O2d)CsOsH
					L6: Cs-(Cds-Cd)CsOsH
						L7: Cs-(Cds-Cds)CsOsH
				L5: Cs-CsCsOsH
			L4: Cs-NCsCsCs
				L5: Cs-N3sCsCsCs
			L4: Cs-CCCC
				L5: Cs-CtCsCsCs
				L5: Cs-CdsCdsCdsCs
					L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)Cs
						L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)Cs
				L5: Cs-CtCdsCsCs
					L6: Cs-(Cds-Cd)CtCsCs
						L7: Cs-(Cds-Cds)CtCsCs
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
				L5: Cs-CdsCdsCdsH
					L6: Cs-(Cds-Cd)(Cds-Cd)(Cds-Cd)H
						L7: Cs-(Cds-Cds)(Cds-Cds)(Cds-Cds)H
				L5: Cs-CtCsCsH
				L5: Cs-CtCsCsH
					L6: Cs-(CtN3t)CsCsH
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
				L5: Cs-CdsCdsHH
				L5: Cs-CtCtHH
				L5: Cs-CtCdsHH
					L6: Cs-(Cds-Cd)CtHH
						L7: Cs-(Cds-Cds)CtHH
					L6: Cs-(Cds-O2d)CtHH
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
						L7: Cs-(Cds-Cds)CsHH
				L5: Cs-CsCsHH
			L4: Cs-CHHH
				L5: Cs-C=SHHH
				L5: Cs-CtHHH
					L6: Cs-(CtN3t)HHH
				L5: Cs-CdsHHH
					L6: Cs-(CdN3d)HHH
					L6: Cs-(Cds-Cd)HHH
						L7: Cs-(Cds-Cds)HHH
					L6: Cs-(Cds-O2d)HHH
				L5: Cs-CsHHH
			L4: Cs-HHHH
		L3: Ct
			L4: Ct-CtH
			L4: Ct-CtC
				L5: Ct-CtCt
				L5: Ct-CtCds
					L6: Ct-Ct(Cds-Cd)
						L7: Ct-Ct(Cds-Cds)
				L5: Ct-CtCs
		L3: Cdd
			L4: Cdd-SdSd
			L4: Cdd-CdCd
				L5: Cdd-CdsCds
			L4: Cdd-OdSd
			L4: Cdd-OdOd
	L2: O
		L3: O2s
			L4: O2s-SH
				L5: O2s-S4dH
			L4: O2s-CS
				L5: O2s-CsS6dd
			L4: O2s-HH
			L4: O2s-OsC
				L5: O2s-OsCs
				L5: O2s-OsCds
					L6: O2s-O2s(Cds-O2d)
			L4: O2s-N
				L5: O2s-CN
					L6: O2s-CsN3s
					L6: O2s-CsN3d
						L7: O2s-Cs(N3dOd)
			L4: O2s-CH
				L5: O2s-CdsH
					L6: O2s-(Cds-O2d)H
					L6: O2s-(Cds-Cd)H
				L5: O2s-CsH
			L4: O2s-OsH
			L4: O2s-CC
				L5: O2s-CdsCds
					L6: O2s-(Cds-O2d)(Cds-O2d)
					L6: O2s-(Cds-O2d)(Cds-Cd)
					L6: O2s-(Cds-Cd)(Cds-Cd)
				L5: O2s-CdsCs
					L6: O2s-Cs(Cds-Cd)
					L6: O2s-Cs(Cds-O2d)
				L5: O2s-CsCs
		L3: O2d
			L4: O2d-S2d
			L4: O2d-O2d
"""
)