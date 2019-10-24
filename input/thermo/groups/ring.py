#!/usr/bin/env python
# encoding: utf-8
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
        Cpdata = ([-1.466424430803679, 0.24658465775375948, 0.04003591471636028, -1.034396904079428, -1.4819360025583723],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )
entry(
    index = 96,
    label = "Ring",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Dummy Root""",
    longDesc = 
u"""

""",
    rank = 10,
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
    thermo = u"Cyclooctane",
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
        Cpdata = ([0.10719668275365024, -0.10213528761245762, -0.00668993309775659, 0.02858108794718955, 0.11983325010870902],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.08414232483181838, -0.00136912099829695, -0.02686985246630617, -0.048787883321045764, 0.11466565630322721],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cyclopropane",
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
        Cpdata = ([0.054583264057461736, -0.002129283738605473, -0.06901546011503687, -0.0032818174428132004, 0.0851922215777268],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cyclobutane",
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
        Cpdata = ([0.010608529201089262, -0.02820240513634143, -0.02564955852332515, -0.005840140106030733, 0.04643314809080812],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cyclopentane",
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
        Cpdata = ([-0.12358404644059481, -0.05792779886913141, 0.01688423435704445, 0.023504542615196806, -0.25665301463575474],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cyclohexane",
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
    thermo = u"Cyclohexane",
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
        Cpdata = ([0.12987640570029696, 0.07852821106042303, -0.03475114945117943, 0.009512326675684213, 0.22439222651584229],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cycloheptane",
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
        Cpdata = ([0.2136786847366941, -0.023714489124159632, -0.031059194617890504, 0.027975679941523727, 0.38434248339998206],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cyclononane",
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
        Cpdata = ([0.08966908248341574, -0.014791895025311481, -0.01931157082837251, -0.03291158634043759, -0.09428499377037348],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cyclodecane",
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
        Cpdata = ([0.3088506706662036, 0.028778665076063456, 0.00628474565557242, 0.02825802395739585, 0.550491457255636],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.03437803509887697, -0.11155262541695776, 0.0178456026981245, -0.12279863289096475, -0.014059315009520346],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.03810270141939798, -0.0640789833942131, -0.02086478432866845, -0.04446771555329718, 0.003203431409602317],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cyclohexene",
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
        Cpdata = ([0.11170214650962992, -0.11398213659845494, -0.046559018124915315, -0.06321559339671573, 0.2978424686093366],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.1582401515300027, -0.093935509186876, -0.04653354123383362, -0.06577291447288398, 0.29680023351278917],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.14596705764405393, -0.02056150203626439, 0.07320482671081813, -0.12641000785063744, -0.5213871983960277],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.012724706150757163, -0.1345971327670009, -0.03037525853574936, -0.006466874012065416, -0.12597581703975336],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"1,3-Cyclohexadiene",
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
        Cpdata = ([0.1646620762970248, 0.1489069082680301, 0.019792895223474494, -0.03921991948952194, 0.7879404667710606],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"1,4-Cyclohexadiene",
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
        Cpdata = ([0.13130511717761592, -0.10086955066012833, -0.041041538975781694, -0.04752009314779731, 0.13320110837786944],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.12638979978923967, -0.10867054446528088, -0.0077420124419857305, -0.009401735653280556, 0.0009985254664052479],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.20201004916388612, -0.41925768260013646, -0.03060443371920947, -0.04537917327194298, -0.7985411088720544],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.002939741673257276, -0.11171196264424971, -0.042436048561442424, -0.11450305585160835, -0.21881788648843675],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.01421504333845272, 0.09210820142846947, 0.012009462077506342, -0.04012318043162119, 0.17877377478143897],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.06929989888214863, 0.20886141509482462, 0.02885188235176832, 0.07620232814764673, 0.5713414670200905],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"Cyclohexanone",
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
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([10,10,10,10,10,10,0],'cal/(mol*K)'), H298=(10,'kcal/mol'), S298=(10,'cal/(mol*K)'), comment="""ring(six-sidedoubles)"""),
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
        Cpdata = ([0.0470961534902588, 0.2628299916674, -0.005755779915107169, -0.1218970061217821, 0.3643792174083885],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.1790347103293007, 0.30105426003410946, -0.025017167596619642, 0.025817289217246023, 0.5885250264892876],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.058611858574762185, -0.3875512273901718, -0.06981740749595246, -0.23377109187562725, -0.6169595716156342],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.08962042532896852, 0.38499631351985564, -0.08548125299490479, -0.07862240135306175, 0.32674985220713726],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.07331177843633493, -0.5856258000280441, 0.02356446107523559, -0.2975154733239251, -0.4561643522854073],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.09067507281102172, -0.06262652535922228, -0.03885307057582676, -0.05078353925932243, 0.41777157121925595],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.1987758560743025, 0.06729479574564733, -0.01721059842677491, -0.0801198048476643, 0.6191984463604263],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.023675505182041645, 0.34237577196364644, -0.08239420775585896, -0.16691322618302246, 0.2782783197571041],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.05969344188802348, -0.04198797667399754, -0.0618880916256493, 0.020565757711144484, -0.07151637183014631],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.16631454693179065, -0.041131866157551655, 0.006000064823721101, 0.08120488763803622, 0.5818785584900927],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.20285255195216148, -0.041085238745969914, 0.006025541714801001, 0.0786475665618663, 0.6743363233935471],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.21739055697253284, -0.041038611334391725, 0.0060510186058822055, 0.07609024548570043, 0.7177940882970031],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.25292856199290287, -0.04099198392281908, 0.00607649549696229, 0.07353292440952917, 0.7312518532004244],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.03546096856372085, 0.11637587286101238, 0.002193909283291582, 0.06960934597164684, 0.18698009261614978],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.11476408528405563, 0.32461479276256594, 0.1394406532924656, -0.0925148183228735, 0.6178799516566911],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.07782304132002177, 0.042411646955733934, 0.06331226902351306, -0.2601746512386054, 0.30247010395293894],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"14methylenecyclohexane",
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
        Cpdata = ([0.15089965241306688, 0.5610877327085866, -0.020723876632881784, -0.06688216188465236, 1.071371843708379],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.10975940201103755, 0.6399485897286449, -0.009175645007259264, 0.06468825288968924, 0.875493508770407],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.28265589639269684, 0.5313431809118841, -0.0299680779376821, 0.05853285973160867, 0.9085895469129216],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.0792689476643818, 0.5053679579441925, 0.010473141819182226, -0.19693901573591557, 0.47632617483393747],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.1194233636557957, 0.3702404321405843, 0.10599792703454072, -0.16158719414291717, 0.4183432618896791],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.2317777978846951, -0.09365812840665781, 0.004634004997636228, 0.008522633521710038, 0.38936751276824877],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.02127211283362722, -0.07616787513420563, -0.09967040406019337, -0.06716720519627642, -0.18116857904428096],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.11953411907155317, -0.2736620815791202, 0.15714018832565357, 0.30903517964100397, 0.31914497885943993],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"oxylene",
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
        Cpdata = ([0.05507466911518406, -0.6430995172696593, 0.015259809665247275, -0.071712771301019, 0.22578624321551266],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"pxylene",
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
        Cpdata = ([0.06055567791077443, 0.01997772068502214, -0.06318499631162625, -0.01531595996962938, -0.03413074032880753],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.0076123449359622635, 0.050617658398000656, -0.053975678167475845, -0.02359967899598339, -0.055092306238519226],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.15964180277464812, -0.6156648127772427, 0.005581600884579818, -0.4292031220108352, 0.026542120557916382],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.053326928926844264, -0.009564038644486544, -0.041520454862714044, -0.0803907521020514, -0.12917892124919073],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.2438471334220798, 0.14166996211072064, 0.06556224963326601, -0.05637943955406682, 0.8846252295275067],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
    thermo = u"14cyclohexadiene3methylene",
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
        Cpdata = ([0.05437296102795159, 0.0545667786618891, -0.06810719852948681, -0.01316466014643847, 0.09252694289154834],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.42079331745086873, -0.3687671113955647, 0.44894237105123636, 0.14678034744531265, 0.4945691822770406],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([0.042553766408180246, -0.07132265512866101, -0.037896232581255754, -0.006553729946432045, -0.218176555193915],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
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
        Cpdata = ([-0.32254920837933554, 0.9175802025355546, 0.6798623811904133, 0.777906651868792, 1.25064215728667],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )

tree(
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
)