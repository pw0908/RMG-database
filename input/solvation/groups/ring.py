name = "Ring Corrections" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
    index = 96,
    label = "Ring",
    group = 
"""
1 * R u0
""",
    solute = None,
    shortDesc = u"""Dummy Root""",
    longDesc = 
u"""

""",
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
    solute = SoluteData(
        S = -0.2573877226758499,
        B = 0.03094166242444367,
        E = 0.19585773311241017,
        L = -0.36781839066966615,
        A = -0.16740597142450755,
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
    solute = SoluteData(
        S = -0.06250627002975487,
        B = -0.05084413154400583,
        E = 0.2743774652300864,
        L = -0.05544302153066985,
        A = -0.14874203737608727,
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
    solute = u"Cyclopropane",
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
    solute = SoluteData(
        S = -0.03778086038947451,
        B = 0.03996492065656551,
        E = 0.2166282798250901,
        L = -0.1385069823195015,
        A = -0.12567202047592388,
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
    solute = u"Cyclobutane",
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
    solute = SoluteData(
        S = -0.1175222872112483,
        B = -0.04549602352464411,
        E = 0.203895300231983,
        L = -0.13919510175106464,
        A = -0.13506478960672985,
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
    solute = u"Cyclopentane",
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
    solute = SoluteData(
        S = -0.13498921950565462,
        B = -0.030333119215090052,
        E = 0.19485144720297923,
        L = -0.222943056752925,
        A = -0.1095028473957951,
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
    solute = u"Cyclohexane",
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
    solute = u"Cyclohexane",
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
    solute = SoluteData(
        S = -0.028225740087343174,
        B = 0.007039862642455787,
        E = 0.2819741050139061,
        L = -0.07326962029768269,
        A = -0.10925022651093502,
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
    solute = u"Cycloheptane",
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
    solute = SoluteData(
        S = -0.17794237716993822,
        B = 0.04628394291877951,
        E = 0.3454877906955133,
        L = -0.06791355223626216,
        A = -0.09459413576965037,
    ),
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
    solute = SoluteData(
        S = -0.10589373591856027,
        B = 0.030498130689300323,
        E = 0.35867586521981637,
        L = 0.10401448151872528,
        A = -0.12311264149092509,
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
    solute = u"Cyclononane",
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
    solute = SoluteData(
        S = -0.10790404694374645,
        B = 0.028568185224466074,
        E = 0.3863578692312326,
        L = 0.06788084097461955,
        A = -0.12342017743573384,
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
    solute = u"Cyclodecane",
)


entry(
    index = 96,
    label = "Ring",
    group = 
"""
1 * R u0
""",
    solute = SoluteData(
        S = -0.04189165720698555,
        B = -0.015550823122535105,
        E = 0.45108253774087,
        L = 0.34632864757814963,
        A = -0.10184689858026219,
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
    solute = SoluteData(
        S = -0.06842247768104973,
        B = -0.10632233804397413,
        E = 0.19859049857589353,
        L = -0.08482648933189668,
        A = -0.02660546091718666,
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
    solute = SoluteData(
        S = -0.07961607345191954,
        B = -0.06946587929848592,
        E = 0.1854675742663782,
        L = -0.07288992646182046,
        A = -0.12595591495184907,
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
    solute = u"Cyclohexene",
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
    solute = SoluteData(
        S = -0.3116280904253711,
        B = -0.020936015057016522,
        E = 0.22356293984260472,
        L = -0.25293474224355655,
        A = -0.14044759642980378,
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
    solute = SoluteData(
        S = -0.16682210446172493,
        B = -0.04847293804750782,
        E = 0.320046774252085,
        L = 0.1568538474639683,
        A = -0.10494259639958961,
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
    solute = SoluteData(
        S = 0.09169201781251167,
        B = -0.12682972140701432,
        E = 0.06319913747520389,
        L = -0.12840678182126097,
        A = -0.009579525760230044,
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
    solute = SoluteData(
        S = -0.15816713334636612,
        B = -0.07369971064595084,
        E = 0.24187249093526547,
        L = -0.14352095340672283,
        A = -0.09894429163948762,
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
    solute = u"1,3-Cyclohexadiene",
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
    solute = SoluteData(
        S = 0.004369249374584341,
        B = -0.16920907973243393,
        E = 0.18976134974831682,
        L = 0.10819728168052034,
        A = -0.14100803702689751,
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
    solute = u"1,4-Cyclohexadiene",
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
    solute = SoluteData(
        S = -0.16406477786676854,
        B = -0.06943937263995625,
        E = 0.2711705443519602,
        L = -0.04967314247770099,
        A = -0.10428312664412609,
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
    solute = SoluteData(
        S = -0.2192587320073623,
        B = -0.11501105577025106,
        E = 0.20094781329672756,
        L = -0.39964747679462687,
        A = -0.14806013919024952,
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
    solute = SoluteData(
        S = -0.45974273549172495,
        B = -0.13577313010479858,
        E = -0.011357390319744663,
        L = -0.8286668102613595,
        A = -0.14256482677293353,
    ),
    )


entry(
    index = 128,
    label = "1,5-cyclooctadiene",
    group = 
"""
1 * Cd u0 {2,D} {8,S}
2   Cd u0 {1,D} {3,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cd u0 {4,S} {6,D}
6   Cd u0 {5,D} {7,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    solute = SoluteData(
        S = -0.0696125653627521,
        B = -0.0776701830900291,
        E = 0.2894099237290416,
        L = -0.042297239907637174,
        A = -0.054976143264257094,
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
    solute = SoluteData(
        S = -0.01912382830058537,
        B = -0.06107081135216259,
        E = 0.3047450369566532,
        L = 0.07737411113691894,
        A = -0.1012132989765577,
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
    solute = SoluteData(
        S = 0.1929527304371786,
        B = 0.047535689492587775,
        E = 0.292689534960959,
        L = 0.3896277856202306,
        A = -0.09048586345933314,
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
    solute = SoluteData(
        S = 0.1888348920542434,
        B = -0.1468350781542248,
        E = 0.1674833156524181,
        L = 0.06316180697106935,
        A = -0.10886914530615129,
    ),
    )


entry(
    index = 96,
    label = "Benzene",
    group = 
"""
1 * Cb u0 {2,B} {6,B}
2   Cb u0 {1,B} {3,B}
3   Cb u0 {2,B} {4,B}
4   Cb u0 {3,B} {5,B}
5   Cb u0 {4,B} {6,B}
6   Cb u0 {1,B} {5,B}
""",
    solute = SoluteData(
        S = -0.2607427090387112,
        B = -0.02804289209142287,
        E = 0.239470784206943,
        L = -0.17548241409120274,
        A = -0.046820143228487494,
    ),
    )


entry(
    index = 96,
    label = "Aromatic",
    group = 
"""
1 * Cb u0
""",
    solute = None,
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
    solute = SoluteData(
        S = 0.2110496954226142,
        B = 0.014066178503635451,
        E = 0.28379482604342304,
        L = 0.2387145166955293,
        A = -0.12248316101685813,
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
    solute = SoluteData(
        S = -0.04711439453220974,
        B = -0.14956423402364186,
        E = 0.16759384949432068,
        L = -0.0824920612646669,
        A = -0.06776364659719836,
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
    solute = SoluteData(
        S = 0.34124680775444294,
        B = 0.05359016489602252,
        E = 0.28715740459946637,
        L = 0.31839529885976586,
        A = -0.11867996370093889,
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
    solute = SoluteData(
        S = -0.37536277373282523,
        B = -0.12004434151089466,
        E = 0.24655657461103866,
        L = -0.2758311331219825,
        A = -0.1779563429045446,
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
    solute = SoluteData(
        S = 0.023274686059480756,
        B = 0.03673078943681104,
        E = 0.26579066392094153,
        L = 0.2947058280291732,
        A = -0.002121968247461716,
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
    solute = SoluteData(
        S = -0.2017761427707429,
        B = 0.0034189274701566554,
        E = 0.3019281137783286,
        L = 0.09634702064298728,
        A = -0.1227206266818346,
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
    solute = SoluteData(
        S = 0.49627670093781506,
        B = 0.11494914195399522,
        E = 0.20620592881815164,
        L = 0.355151460678502,
        A = -0.1372550352186579,
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
    solute = SoluteData(
        S = -0.14239782967879078,
        B = -0.0059720029117821954,
        E = 0.16155146839467174,
        L = -0.3066511410230278,
        A = -0.1202620248428466,
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
    solute = SoluteData(
        S = -0.1456548173047054,
        B = 0.05404533731892865,
        E = 0.21270424003855512,
        L = 0.02622101682953662,
        A = -0.1186239130959298,
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
    solute = SoluteData(
        S = -0.11883174728219473,
        B = 0.0691760787888719,
        E = 0.2814769869750524,
        L = 0.2249317872527444,
        A = -0.12210751009506801,
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
    solute = SoluteData(
        S = -0.11750872497404835,
        B = 0.06724613332403315,
        E = 0.32115899098646555,
        L = 0.3267981467086199,
        A = -0.12241504603987663,
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
    solute = SoluteData(
        S = -0.11618570266589605,
        B = 0.06531618785919717,
        E = 0.3388409949978793,
        L = 0.3796645061645214,
        A = -0.122722581984687,
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
    solute = SoluteData(
        S = -0.11486268035775346,
        B = 0.06338624239436016,
        E = 0.3775229990092898,
        L = 0.40253086562039453,
        A = -0.12303011792949843,
    ),
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
    solute = SoluteData(
        S = -0.13931518263626907,
        B = -0.0834853620644492,
        E = 0.14532498894762547,
        L = -0.2588781965974281,
        A = -0.107042668145067,
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
    solute = SoluteData(
        S = 0.11664541730260677,
        B = -0.052891193110804396,
        E = 0.16404095952005632,
        L = -0.0012591769489287419,
        A = -0.04663123881599632,
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
    solute = SoluteData(
        S = -0.7000550521585769,
        B = 0.07373594039479797,
        E = 0.1263609975288331,
        L = -1.0219280807847844,
        A = -0.1194448213739897,
    ),
    )


entry(
    index = 110,
    label = "sixmembd-allsingles-twosidedoubles-meta",
    group = 
"""
1   [Cs,O2s] u0 {2,S} {6,S}
2 * [Cd,CO]  u0 {1,S} {3,S}
3   [Cs,O2s] u0 {2,S} {4,S}
4   [Cd,CO]  u0 {3,S} {5,S}
5   [Cs,O2s] u0 {4,S} {6,S}
6   [Cs,O2s] u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = 0.39246517067377396,
        B = -0.15082569052831188,
        E = 0.13121526216965382,
        L = 0.09350232968859695,
        A = -0.029391807629759622,
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
    solute = SoluteData(
        S = -0.011599363460234963,
        B = -0.2874602325465851,
        E = 0.19953446071501046,
        L = -0.05511213717628427,
        A = -0.10024245817455416,
    ),
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
    solute = SoluteData(
        S = 0.48862559358358687,
        B = -0.06363516677044759,
        E = 0.25783980190603395,
        L = 0.7001284312103617,
        A = -0.11649202691054407,
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
    solute = SoluteData(
        S = 0.5821575145042661,
        B = 0.10391036095992606,
        E = 0.24113453567783397,
        L = 0.6088307046955974,
        A = -0.11257904452203998,
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
    solute = SoluteData(
        S = 0.2679237682752592,
        B = 0.045860376293244506,
        E = 0.32525033125862735,
        L = 0.3743513862139438,
        A = -0.15028021266932884,
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
    solute = SoluteData(
        S = 0.39298938300238845,
        B = -0.20375384646285194,
        E = 0.20171684618731217,
        L = 0.1788634260545699,
        A = -0.06119166073752597,
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
    solute = SoluteData(
        S = 0.275443694957883,
        B = -0.19835657465540713,
        E = 0.23114233449998178,
        L = 0.10646509336614451,
        A = 0.02134977483678323,
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
    solute = SoluteData(
        S = -0.1616341994749081,
        B = 0.016506973095044293,
        E = 0.2983028973335151,
        L = -0.19861689404491334,
        A = -0.11448150307621421,
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
    solute = SoluteData(
        S = -0.14897150470377882,
        B = -0.03962587268840554,
        E = 0.1323906693219155,
        L = -0.06761627865211206,
        A = -0.007945353982069529,
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
    solute = SoluteData(
        S = 0.3015633883907287,
        B = -0.010676910441143245,
        E = 0.32514284189376175,
        L = 0.2876349310037912,
        A = -0.21163620821761406,
    ),
    )


entry(
    index = 42,
    label = "124trioxane",
    group = 
"""
1   O2s u0 {2,S} {6,S}
2   Cs  u0 {1,S} {3,S}
3   O2s u0 {2,S} {4,S}
4 * Cs  u0 {3,S} {5,S}
5   Cs  u0 {4,S} {6,S}
6   O2s u0 {1,S} {5,S}
""",
    solute = SoluteData(
        S = 0.01986430439619942,
        B = 0.14661958063317676,
        E = 0.06445304232939457,
        L = 0.5406601728191278,
        A = 0.3071613259363937,
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
    solute = SoluteData(
        S = 0.16337934007011717,
        B = -0.1017942326294035,
        E = 0.6028344188481115,
        L = 0.32961454198618323,
        A = -0.4663234761449075,
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
    solute = u"oxylene",
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
    solute = SoluteData(
        S = -0.7106149568492567,
        B = -0.16337966810225713,
        E = 0.35960319426071835,
        L = -0.5003557293226941,
        A = -0.045081969184381884,
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
    solute = u"pxylene",
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
    solute = SoluteData(
        S = 0.0024222777688056307,
        B = 0.028052569790168132,
        E = 0.24763519282769178,
        L = -0.023440130096391204,
        A = -0.10510150332154855,
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
    solute = SoluteData(
        S = 0.005010914510912498,
        B = 0.005662454768923228,
        E = 0.22882083483902546,
        L = -0.06008286162348081,
        A = -0.10573931509716544,
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
    solute = SoluteData(
        S = -0.09591292100638743,
        B = -0.08927100729196394,
        E = 0.22185239459075878,
        L = -0.1774118541388976,
        A = -0.04880616880252821,
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
    solute = SoluteData(
        S = -1.0439405740605812,
        B = -0.8045594667838613,
        E = 0.3685802320384517,
        L = -1.1619790787345938,
        A = -0.43462078966095474,
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
    solute = SoluteData(
        S = 0.028026279145819885,
        B = -0.1199045187337057,
        E = 0.06550985564369037,
        L = -0.2568336692629024,
        A = 0.0012493919617422144,
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
    solute = SoluteData(
        S = 0.19728086119285201,
        B = -0.11174192548271478,
        E = 0.40503220981552546,
        L = 0.42721245860014545,
        A = 0.05935787240573083,
    ),
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
    solute = SoluteData(
        S = 0.053261374665246386,
        B = 0.05193303843366122,
        E = 0.1984827427909298,
        L = -0.08199292136631109,
        A = -0.16428774375023597,
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
    solute = SoluteData(
        S = -0.27900081683355765,
        B = 0.029546372295055447,
        E = 0.37402550469913354,
        L = 0.1895905641792709,
        A = 0.3155453040360181,
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
    solute = SoluteData(
        S = 0.04890989881962585,
        B = -0.12179955850833776,
        E = 0.2891466408517444,
        L = -0.27086268077698705,
        A = -0.04759534191112566,
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
    solute = SoluteData(
        S = -0.13783398092954496,
        B = 0.012201981282060237,
        E = 0.17798045622749925,
        L = -0.48542797131588106,
        A = -0.12697572689143777,
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
    solute = SoluteData(
        S = -0.48726242804677394,
        B = 0.3485841482655111,
        E = 0.13264788492291515,
        L = -0.9118632407580572,
        A = 0.35857842226150605,
    ),
    )

tree(
"""
L1: Ring
	L2: TenMember
	L2: SevenMember
	L2: FiveMember
		L3: 2,3-dihydrothiophene
		L3: 1,3-Dioxolane
		L3: Furan
		L3: Pyrrolidine
		L3: thiolane
		L3: 2,5-Furandione
		L3: butyrolactone
		L3: thiophene
	L2: SixMember
		L3: six-oneside-twoindoubles-25
		L3: six-twoin14-twoout
		L3: sixnosidedouble
		L3: six-twoin14-twoout
			L4: pbenzoquinone
		L3: six-twoin13-twoout
			L4: fg6
			L4: obenzoquinone
	L2: Aromatic
		L3: Benzene
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
		L3: six-sidedoubles
			L4: sixmembd-allsingles-twosidedoubles-para
			L4: sixmembd-allsingles-twosidedoubles-meta
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
			L4: 124trioxane
			L4: 1,3,5-Trioxane
			L4: 1,4-Dioxane
			L4: Oxane
			L4: 1,3-Dioxane
			L4: Cyclohexane
	L2: FiveMember
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
		L3: 1,5-cyclooctadiene
		L3: Cyclooctatetraene
		L3: cis-Cyclooctene
		L3: Cyclooctane
""",
)