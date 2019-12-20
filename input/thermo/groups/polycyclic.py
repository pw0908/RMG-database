name = "Polycyclic Ring Corrections" 
shortDesc = u"" 
longDesc = u""" 

""" 
entry(
    index = 92,
    label = "s2_5_6_ane",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {9,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4400043681758866, -0.028601116370652824, -0.38328490121493974, -0.11933712265092067, -0.1108558301875997],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_5_6",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   R!H u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo =None
    )


entry(
    index = 165,
    label = "s3_6_6_ane",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {9,S}
5   R!H u0 {2,S} {8,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {1,S} {9,S}
8   R!H u0 {5,S} {6,S}
9   R!H u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.39697333079403263, -0.2363856047160416, -0.21445294349045613, -0.07532769112782065, -0.40671240228998784],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s3_6_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
9   R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 118,
    label = "s2_6_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,S} {5,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,S} {10,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {5,S} {10,S}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3696463442768042, -0.16790360263398235, -0.0752773252725708, 0.08112901499715691, -0.275977395596933],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_6_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    )


entry(
    index = 64,
    label = "s2_3_5_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.37003622256148405, -0.40160146647308104, -0.20301776135320493, -0.04820711256946567, -0.33156518165250143],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_3_5",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 75,
    label = "s2_4_5_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3750217968487948, -0.3418121105688653, -0.25075205760038016, 0.08869552057010559, -0.44936420261472654],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_4_5",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([-31.7388,-31.3291,-29.3067,-26.4168,-21.8842,-16.2852,-9.99256],'J/(mol*K)'), H298=(199.03,'kJ/mol','+|-',125.18), S298=(240.196,'J/(mol*K)','+|-',34.0902), comment="""polycyclic(s2_4_5)"""),
)


entry(
    index = 61,
    label = "s2_3_4_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3421348426523649, -0.300275211376447, -0.2814397401310597, -0.15389724761168538, -0.8347944621490985],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_3_4",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 3,
    label = "s2-3_5_5_5_ane",
    group = 
"""
1    R!H u0 {2,S} {4,S} {9,S}
2    R!H u0 {1,S} {3,S} {8,S}
3  * R!H u0 {2,S} {5,S} {6,S}
4    R!H u0 {1,S} {5,S} {7,S}
5    R!H u0 {3,S} {4,S}
6    R!H u0 {3,S} {7,S}
7    R!H u0 {4,S} {6,S}
8    R!H u0 {2,S} {10,S}
9    R!H u0 {1,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.49999973957691013, -0.31845773821763557, -0.31595052695897563, -0.10171754517681175, -0.8398933235673826],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 157,
    label = "s3_5_5_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {6,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {4,S}
7   R!H u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3131161908467407, -0.45377655900696734, -0.3224997769807728, -0.007326383947568238, -0.774508258258149],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s3_5_5",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 82,
    label = "s2_5_5_ene_1",
    group = 
"""
1   R!H u0 {2,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S} {6,S}
3 * R!H u0 {2,S} {7,D}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,D} {5,S}
8   R!H u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2001018391665688, 0.1121348215010075, -0.2866104368589875, -0.2875183609681523, -0.6807855635029326],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_5_5_ene",
    group = 'OR{s2_5_5_ene_0, s2_5_5_ene_1}',
    thermo = None,
)


entry(
    index = 0,
    label = "s2_5_5",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([-34.0672,-34.442,-32.5097,-29.5077,-23.6201,-16.0248,-7.87556],'J/(mol*K)'), H298=(95.5881,'kJ/mol','+|-',54.0018), S298=(230.488,'J/(mol*K)','+|-',81.3027), comment="""polycyclic(s2_5_5)"""),
)


entry(
    index = 158,
    label = "s3_5_5_ene_1",
    group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {2,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3278819532312035, -0.449754838366717, -0.20397127184048508, -0.06104790000453819, -0.6060532240774179],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s3_5_5_ene",
    group = 'OR{s3_5_5_ene_1, s3_5_5_ene_side}',
    thermo = None,
)


entry(
    index = 160,
    label = "s3_5_5_diene_1_4",
    group = 
"""
1   R!H u0 {3,S} {6,S} {7,S}
2   R!H u0 {3,S} {4,S} {5,S}
3   R!H u0 {1,S} {2,S}
4 * R!H u0 {2,S} {6,D}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {4,D}
7   R!H u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.201340833805985, -0.5506156952874336, -0.2576744998829199, -0.19524936254657677, 0.1359448285833993],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s3_5_5_diene",
    group = 'OR{s3_5_5_diene_1_4}',
    thermo = None,
)


entry(
    index = 66,
    label = "s2_3_6_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6 * R!H u0 {4,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.31500457253494785, 0.016766189521173147, -0.20245412748690056, 0.011843186938071057, -0.3507229404735933],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_3_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * R!H u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 131,
    label = "s2_6_6_diene_0_8",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {9,S}
4    R!H u0 {1,S} {10,D}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {8,S}
8    R!H u0 {5,S} {7,S}
9    R!H u0 {3,S} {10,S}
10   R!H u0 {4,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3020541531201135, 0.17757921600028637, -0.1952963770501867, -0.08056943414971071, -0.018815239205711154],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_diene",
    group = 'OR{s2_6_6_diene_0_2, s2_6_6_diene_0_3, s2_6_6_diene_0_5, s2_6_6_diene_0_6, s2_6_6_diene_0_8, s2_6_6_diene_1_6, s2_6_6_diene_1_7}',
    thermo = None,
)


entry(
    index = 121,
    label = "s2_6_6_ene_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S}
2    R!H u0 {1,S} {5,S} {6,S}
3    R!H u0 {1,S} {10,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {2,S} {8,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {4,S} {8,S}
8    R!H u0 {5,S} {7,S}
9    R!H u0 {6,S} {10,D}
10   R!H u0 {3,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.44403907710171137, -0.3320116981317486, 0.2301715607285602, 0.039588419456887486, 0.32785923693561536],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_ene",
    group = 'OR{s2_6_6_ene_0, s2_6_6_ene_1, s2_6_6_ene_2, s2_6_6_ene_m}',
    thermo = None,
)


entry(
    index = 185,
    label = "s2_6_6_ben",
    group = 
"""
1    R!H u0 {2,B} {3,B} {5,S}
2    R!H u0 {1,B} {4,B} {6,S}
3    R!H u0 {1,B} {7,B}
4    R!H u0 {2,B} {9,B}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {3,B} {9,B}
8    R!H u0 {6,S} {10,S}
9    R!H u0 {4,B} {7,B}
10   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4863455284574577, -0.4107321628354343, -0.1667818991610432, -0.0826528220792811, -0.3057258444111476],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 179,
    label = "s4_6_6_ane",
    group = 
"""
1 * R!H u0 {3,S} {6,S} {8,S}
2   R!H u0 {4,S} {5,S} {7,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {2,S} {6,S}
6   R!H u0 {1,S} {5,S}
7   R!H u0 {2,S} {8,S}
8   R!H u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3901555279382828, -0.3332970024725101, -0.3339684715311959, -0.2539724480260634, -0.2600040652395723],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s4_6_6",
    group = 
"""
1 * R!H u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
2   R!H u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 80,
    label = "s2_5_5_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3 * R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {8,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.440707463078146, -0.48177459802161937, -0.1360837954812429, -0.17894317765398698, -0.31613166279678195],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 119,
    label = "s2_6_6_ene_0",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,D} {6,S}
3    R!H u0 {1,S} {7,S}
4    R!H u0 {2,D} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {9,S}
7  * R!H u0 {3,S} {8,S}
8    R!H u0 {4,S} {7,S}
9    R!H u0 {6,S} {10,S}
10   R!H u0 {5,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4411798817897706, 0.09803454443629903, -0.16379364418391315, -0.022171939108432764, -0.2500758304314691],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_6_7",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.6965948962000212, 0.4207414109071058, -0.2976341052480086, -0.0002189349532392415, 0.7956290303487921],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 51,
    label = "s1_6_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {8,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S} {11,S}
7    R!H u0 {4,S} {10,S}
8    R!H u0 {2,S} {11,S}
9    R!H u0 {3,S} {10,S}
10 * R!H u0 {7,S} {9,S}
11   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.0322265211646981, -0.00993215219809803, -0.15358066296819625, -0.07330979031658733, -0.2703300864095627],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s1_6_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
7    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
8    R!H u0 {2,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10 * R!H u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
11   R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 0,
    label = "PolycyclicRing",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.5955016377007695, -0.11861514068637054, -0.15845429035868666, -0.06087206646476968, 0.1733960504351581],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 185,
    label = "s2_6_6_naphthalene",
    group = 
"""
1    R!H u0 {2,B} {3,B} {4,B}
2    R!H u0 {1,B} {5,B} {6,B}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {1,B} {8,B}
5    R!H u0 {2,B} {10,B}
6    R!H u0 {2,B} {7,B}
7  * R!H u0 {6,B} {8,B}
8    R!H u0 {4,B} {7,B}
9    R!H u0 {3,B} {10,B}
10   R!H u0 {5,B} {9,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.24485005130933785, -0.5649047371675577, -0.08796206224157388, 0.040207658695087176, 0.15546868785155776],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 123,
    label = "s2_6_6_ben_ene_1",
    group = 
"""
1    R!H u0 {2,B} {3,S} {4,B}
2    R!H u0 {1,B} {5,B} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,B} {8,B}
5    R!H u0 {2,B} {9,B}
6    R!H u0 {2,S} {10,S}
7  * R!H u0 {3,D} {10,S}
8    R!H u0 {4,B} {9,B}
9    R!H u0 {5,B} {8,B}
10   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.43738197785458055, -0.30941972557458014, -0.20204174494797353, -0.11167362874701453, -0.29343355470745625],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_ben_ene",
    group = 'OR{s2_6_6_ben_ene_1, s2_6_6_ben_ene_2}',
    thermo = None,
)


entry(
    index = 117,
    label = "s2_5_6_indene",
    group = 
"""
1 * R!H u0 {2,B} {3,S} {4,B}
2   R!H u0 {1,B} {5,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {1,B} {8,B}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {2,B} {9,B}
7   R!H u0 {3,S} {5,D}
8   R!H u0 {4,B} {9,B}
9   R!H u0 {6,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4823693889064836, -0.25762909743201234, -0.05781934052448841, -0.1302353899193306, -0.25164115195778597],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 184,
    label = "s2_5_6_ben",
    group = 
"""
1 * R!H u0 {2,B} {3,S} {5,B}
2   R!H u0 {1,B} {4,S} {6,B}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,B} {9,B}
6   R!H u0 {2,B} {8,B}
7   R!H u0 {3,S} {4,S}
8   R!H u0 {6,B} {9,B}
9   R!H u0 {5,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4670013840001946, -0.3789590042234058, -0.14419127659113415, -0.09279984734437197, -0.2502093762756358],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 216,
    label = "s2_6_7_ben",
    group = 
"""
1    R!H u0 {2,B} {3,B} {6,[S,D,T,B]}
2    R!H u0 {1,B} {4,B} {5,[S,D,T,B]}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {2,B} {7,B}
5    R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,B} {9,B}
8    R!H u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
9    R!H u0 {3,B} {7,B}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.42654296441484596, -0.23278458134605173, -0.18937192213513926, -0.08914112375177644, -0.1874873688160219],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 123,
    label = "s2_6_6_ben_ene_2",
    group = 
"""
1    R!H u0 {2,B} {4,B} {5,S}
2    R!H u0 {1,B} {3,S} {6,B}
3    R!H u0 {2,S} {8,S}
4    R!H u0 {1,B} {10,B}
5    R!H u0 {1,S} {7,S}
6    R!H u0 {2,B} {9,B}
7  * R!H u0 {5,S} {8,D}
8    R!H u0 {3,S} {7,D}
9    R!H u0 {6,B} {10,B}
10   R!H u0 {4,B} {9,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.49053686603333024, -0.5176584517374313, 0.041847137247156885, -0.11380164275261506, -0.43140238729154046],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 134,
    label = "s2_6_6_diene_1_7",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,S}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {2,S} {8,D}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {10,D}
8    R!H u0 {5,D} {9,S}
9    R!H u0 {6,S} {8,S}
10   R!H u0 {3,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.537977137202525, -0.12883839889684212, -0.4134714920746012, 0.05672516791720189, -0.2638266806106967],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 78,
    label = "s2_4_6_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,S} {6,S}
3   R!H u0 {1,S} {4,S}
4   R!H u0 {2,S} {3,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {2,S} {8,D}
7 * R!H u0 {5,S} {8,S}
8   R!H u0 {6,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.030167546789948818, -0.23697765191412895, 0.4791962854751586, 0.0005269208689954452, -0.42150648543912883],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_4_6_ene",
    group = 'OR{s2_4_6_ene_1}',
    thermo = None,
)


entry(
    index = 0,
    label = "s2_4_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7 * R!H u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = ThermoData(Tdata=([300,400,500,600,800,1000,1500],'K'), Cpdata=([-29.8842,-29.362,-27.4896,-24.5854,-18.8637,-15.6108,-7.57856],'J/(mol*K)'), H298=(165.132,'kJ/mol','+|-',54.7748), S298=(191.241,'J/(mol*K)','+|-',100.116), comment="""polycyclic(s2_4_6)"""),
)


entry(
    index = 101,
    label = "s2_5_6_diene_m_7",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {5,S}
2   R!H u0 {1,D} {4,S} {6,S}
3   R!H u0 {1,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,D}
6   R!H u0 {2,S} {9,S}
7   R!H u0 {4,S} {5,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2900040120614822, 0.08570059029087407, -0.20994622451755277, -0.26946230695546025, -0.20320171372264828],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_diene",
    group = 'OR{s2_5_6_diene_m_7, s2_5_6_diene_1_3}',
    thermo = None,
)


entry(
    index = 39,
    label = "s1_5_6_ane",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {6,S}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {3,S} {7,S}
7    R!H u0 {2,S} {6,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4097465860369113, -0.2563332722779473, -0.2309526632992319, -0.29276283888126475, -0.40325752596210335],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s1_5_6",
    group = 
"""
1    R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3    R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
6  * R!H u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 161,
    label = "s3_5_6_ane",
    group = 
"""
1   R!H u0 {3,S} {5,S} {6,S}
2   R!H u0 {3,S} {4,S} {7,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {5,S}
5   R!H u0 {1,S} {4,S}
6   R!H u0 {1,S} {8,S}
7   R!H u0 {2,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.33076674828866537, -0.32924382619502934, -0.3334615705772341, 0.2518194008600009, -0.6096128141401335],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s3_5_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8 * R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 99,
    label = "s2_5_6_tetraene_1_3_5_8",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,D}
2   R!H u0 {1,S} {3,S} {4,D}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {2,D} {7,S}
5   R!H u0 {1,S} {9,D}
6   R!H u0 {1,D} {7,S}
7   R!H u0 {4,S} {6,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.2098748708229373, 0.2873794110301837, -0.08779511783405644, -0.3334322940409049, -0.22603482361075133],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_tetraene",
    group = 'OR{s2_5_6_tetraene_1_3_5_7, s2_5_6_tetraene_1_3_5_8}',
    thermo = None,
)


entry(
    index = 95,
    label = "s2_5_6_ene_m",
    group = 
"""
1 * R!H u0 {2,D} {5,S} {6,S}
2   R!H u0 {1,D} {3,S} {4,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.5048559681310921, -0.8610344829286389, -0.2450750299141769, -0.19920853269462185, -0.8539313811152033],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_ene",
    group = 'OR{s2_5_6_ene_0, s2_5_6_ene_1, s2_5_6_ene_m, s2_5_6_ene_2, s2_5_6_ene_6}',
    thermo = None,
)


entry(
    index = 94,
    label = "s2_5_6_ene_1",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3248646508930446, -0.09009763184712133, -0.6719590375086397, 0.00842383904415403, -0.7883222074108289],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 217,
    label = "s2_6_7_ben_ene_1",
    group = 
"""
1    R!H u0 {2,B} {3,B} {6,[S,D,T,B]}
2    R!H u0 {1,B} {4,B} {5,[S,D,T,B]}
3    R!H u0 {1,B} {9,B}
4    R!H u0 {2,B} {7,B}
5    R!H u0 {2,[S,D,T,B]} {8,D}
6    R!H u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * R!H u0 {4,B} {9,B}
8    R!H u0 {5,D} {11,[S,D,T,B]}
9    R!H u0 {3,B} {7,B}
10   R!H u0 {6,[S,D,T,B]} {11,[S,D,T,B]}
11   R!H u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.43389744523080587, -0.25917696255850925, -0.20453898638918222, -0.04759670861677914, -0.3056065161108946],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_6_7_ben_ene",
    group = 'OR{s2_6_7_ben_ene_1}',
    thermo = None,
)


entry(
    index = 120,
    label = "s2_6_6_ene_1",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,S}
3    R!H u0 {1,S} {9,D}
4    R!H u0 {2,S} {7,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {4,S} {10,S}
8    R!H u0 {6,S} {9,S}
9    R!H u0 {3,D} {8,S}
10   R!H u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.41481198692592874, -0.005143966265204858, -0.1322620831850559, 0.004261605488051698, -0.0224150683721418],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 99,
    label = "s2_5_6_tetraene_1_3_5_7",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {5,D}
2   R!H u0 {1,S} {3,S} {6,S}
3   R!H u0 {2,S} {8,D}
4   R!H u0 {1,S} {9,D}
5   R!H u0 {1,D} {7,S}
6   R!H u0 {2,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {3,D} {9,S}
9   R!H u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.18567828593094982, -0.22142920041495567, -0.33803569225837143, -0.20417677535869116, -0.6636671559140529],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 125,
    label = "s2_6_6_diene_0_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,S}
2    R!H u0 {1,S} {4,S} {6,D}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {2,S} {10,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,D} {7,S}
7  * R!H u0 {6,S} {8,D}
8    R!H u0 {3,S} {7,D}
9    R!H u0 {5,S} {10,S}
10   R!H u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4692392088143884, -0.15591302630901016, -0.2448442546179928, -0.08220482382393336, -0.3489537035227023],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 123,
    label = "s2_6_6_tetraene_0_2_6_8",
    group = 
"""
1    R!H u0 {2,S} {3,S} {6,S}
2    R!H u0 {1,S} {4,D} {5,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {2,D} {7,S}
5    R!H u0 {2,S} {10,D}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {4,S} {9,D}
8    R!H u0 {3,D} {10,S}
9    R!H u0 {6,S} {7,D}
10   R!H u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.45195340355260893, -0.2946108972651589, -0.27674887030375206, -0.2217352379985602, -0.41034621735507004],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_6_6_tetraene",
    group = 'OR{s2_6_6_tetraene_0_2_6_8}',
    thermo = None,
)


entry(
    index = 128,
    label = "s2_6_6_diene_0_5",
    group = 
"""
1    R!H u0 {2,S} {3,S} {5,D}
2    R!H u0 {1,S} {4,D} {6,S}
3    R!H u0 {1,S} {9,S}
4    R!H u0 {2,D} {7,S}
5    R!H u0 {1,D} {10,S}
6    R!H u0 {2,S} {8,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {6,S} {10,S}
9    R!H u0 {3,S} {7,S}
10   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.63338805272304, 0.11512996480042059, -0.02613148127437826, -0.2089376787612786, 0.6058294634570915],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 99,
    label = "s2_5_6_triene_m_1_7",
    group = 
"""
1 * R!H u0 {2,D} {3,S} {6,S}
2   R!H u0 {1,D} {4,S} {5,S}
3   R!H u0 {1,S} {9,D}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.13733585593861347, -0.654644111650192, -0.18331685596256658, 0.021183800980685258, -1.2221508145687556],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_5_6_triene",
    group = 'OR{s2_5_6_triene_m_1_7}',
    thermo = None,
)


entry(
    index = 96,
    label = "s2_5_6_ene_2",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {2,S} {7,S}
4   R!H u0 {2,S} {8,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {3,S} {5,S}
8   R!H u0 {4,S} {9,D}
9   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.24969249791215992, -0.2717918868411899, -0.20414477005487341, -0.05786431114016721, -0.4195240336964212],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 108,
    label = "s2_5_6_diene_1_3",
    group = 
"""
1 * R!H u0 {2,S} {5,S} {6,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {2,S} {9,D}
4   R!H u0 {2,S} {7,S}
5   R!H u0 {1,S} {8,D}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {4,S} {6,S}
8   R!H u0 {5,D} {9,S}
9   R!H u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([-0.069768495661513, 1.124694583569242, 0.26845809830554507, -0.06834134577873299, 1.098760619695081],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 122,
    label = "s2_6_6_ene_m",
    group = 
"""
1    R!H u0 {2,D} {5,S} {6,S}
2    R!H u0 {1,D} {3,S} {4,S}
3    R!H u0 {2,S} {7,S}
4    R!H u0 {2,S} {8,S}
5    R!H u0 {1,S} {10,S}
6    R!H u0 {1,S} {9,S}
7  * R!H u0 {3,S} {9,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {6,S} {7,S}
10   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.728897899983113, 0.44703102439903303, -0.05469998889233718, -0.11315588775064045, -6.401754253522169],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 126,
    label = "s2_6_6_diene_0_3",
    group = 
"""
1    R!H u0 {2,S} {4,S} {6,D}
2    R!H u0 {1,S} {3,S} {5,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {1,S} {9,S}
5    R!H u0 {2,S} {7,D}
6    R!H u0 {1,D} {8,S}
7  * R!H u0 {5,D} {8,S}
8    R!H u0 {6,S} {7,S}
9    R!H u0 {4,S} {10,S}
10   R!H u0 {3,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.47980507547105716, -0.4107052321579865, -0.2046574096144087, -0.08586464778760533, 0.314548907838176],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 98,
    label = "s2_5_6_ene_6",
    group = 
"""
1 * R!H u0 {2,S} {4,S} {6,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {2,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {7,D}
6   R!H u0 {1,S} {9,S}
7   R!H u0 {4,S} {5,D}
8   R!H u0 {3,S} {9,S}
9   R!H u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.48974269894391576, 0.5210332485314257, -0.44144047038748013, -0.2855257637945886, 0.2537646272116887],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 137,
    label = "s3_4_4_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {5,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3562957920149922, 0.2631784545115102, -0.14795723491172597, -0.13798509076114907, -0.3552200961818275],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s3_4_4",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 87,
    label = "s2_5_5_diene_0_4",
    group = 
"""
1   R!H u0 {2,S} {3,D} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,D} {7,S}
4   R!H u0 {1,S} {8,S}
5   R!H u0 {2,D} {8,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4488941869974893, -0.7627008303349476, -0.18451042369744367, -0.6838632556790574, -0.4205372735460444],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_5_5_diene",
    group = 'OR{s2_5_5_diene_0_4}',
    thermo = None,
)


entry(
    index = 65,
    label = "s2_3_5_ene_1",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,D}
5   R!H u0 {1,S} {6,S}
6   R!H u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.22016373427894825, -0.4868726048867067, -0.2744295775890073, -0.10067390085705456, -0.6655520132979422],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_3_5_ene",
    group = 'OR{s2_3_5_ene_1}',
    thermo = None,
)


entry(
    index = 150,
    label = "s3_4_6_ene_1",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,D}
7   R!H u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.26998491903992433, -0.35130787206915287, -0.2905070560206109, -0.10822876843929587, -0.6524165753038667],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s3_4_6_ene",
    group = 'OR{s3_4_6_ene_1}',
    thermo = None,
)


entry(
    index = 0,
    label = "s3_4_6",
    group = 
"""
1   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 159,
    label = "s3_5_5_ene_side",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {4,S} {5,S} {7,S}
3 * R!H u0 {1,S} {5,S} {8,D}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {3,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {2,S} {6,S}
8   R!H ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3154059947995965, -0.4278454193638141, -0.27264774280717674, -0.056462193102351135, -0.5131985494709075],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 67,
    label = "s2_3_6_ene_1",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,D}
5   R!H u0 {2,S} {7,S}
6 * R!H u0 {4,D} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.296626578196966, -0.3739544358356388, -0.2584913391715076, -0.13084964342677585, -0.36921012912994267],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_3_6_ene",
    group = 'OR{s2_3_6_ene_1, s2_3_6_ene_2}',
    thermo = None,
)


entry(
    index = 68,
    label = "s2_3_6_ene_2",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {3,S} {5,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,S} {6,S}
6 * R!H u0 {5,S} {7,D}
7   R!H u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3001317470355551, -0.4120982153527023, -0.2311662516051112, -0.0987169670682641, -0.32533635183178755],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 148,
    label = "s3_4_6_ane",
    group = 
"""
1   R!H u0 {3,S} {4,S} {6,S}
2   R!H u0 {3,S} {4,S} {5,S}
3 * R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {2,S}
5   R!H u0 {2,S} {7,S}
6   R!H u0 {1,S} {7,S}
7   R!H u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.37993695761013124, -0.5134926394173718, -0.25588462494098957, -0.02799863944428442, -0.4488419803987369],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 41,
    label = "s1_5_6_ene_2",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {8,S}
4    R!H u0 {1,S} {7,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {2,S} {10,S}
7  * R!H u0 {4,S} {9,S}
8    R!H u0 {3,S} {10,D}
9    R!H u0 {5,S} {7,S}
10   R!H u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.46643115352335324, -0.3443590005712704, -0.23405479982980307, -0.052300443007439856, -0.4601105276984253],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s1_5_6_ene",
    group = 'OR{s1_5_6_ene_1, s1_5_6_ene_2, s1_5_6_ene_7}',
    thermo = None,
)


entry(
    index = 0,
    label = "s2_5_7",
    group = 
"""
1  * R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3    R!H u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4    R!H u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6    R!H u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8    R!H u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    R!H u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10   R!H u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.424010263719215, -0.2127300655238102, -0.32650138682082513, -0.09852195644037731, -0.33798199432417075],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 70,
    label = "s2_3_7_ane",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {3,S} {4,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {2,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {8,S}
8   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.35111184076800905, -0.4667466423570214, -0.10519233026928103, 0.0822219825974082, -0.5148750639448814],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s2_3_7",
    group = 
"""
1 * R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
)


entry(
    index = 133,
    label = "s2_6_6_diene_1_6",
    group = 
"""
1    R!H u0 {2,S} {5,S} {6,S}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {2,S} {8,D}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {1,S} {7,D}
7  * R!H u0 {6,D} {10,S}
8    R!H u0 {4,D} {9,S}
9    R!H u0 {5,S} {8,S}
10   R!H u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4546545388887037, -0.34321304765701544, -0.15667070067879735, -0.046606312353697416, -0.37053080194001986],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 129,
    label = "s2_6_6_diene_0_6",
    group = 
"""
1    R!H u0 {2,S} {5,S} {6,D}
2    R!H u0 {1,S} {3,S} {4,S}
3    R!H u0 {2,S} {10,S}
4    R!H u0 {2,S} {9,D}
5    R!H u0 {1,S} {8,S}
6    R!H u0 {1,D} {7,S}
7  * R!H u0 {6,S} {10,S}
8    R!H u0 {5,S} {9,S}
9    R!H u0 {4,D} {8,S}
10   R!H u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4739062778845995, -0.36742231120911883, -0.14751496797133645, -0.007489667808221079, 0.1923638817521568],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 42,
    label = "s1_5_6_ene_7",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {7,S}
3    R!H u0 {1,S} {8,D}
4    R!H u0 {1,S} {6,S}
5    R!H u0 {1,S} {9,S}
6    R!H u0 {4,S} {10,S}
7    R!H u0 {2,S} {10,S}
8  * R!H u0 {3,D} {9,S}
9    R!H u0 {5,S} {8,S}
10   R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3829272147774314, -0.344855424896669, -0.16980458147397726, -0.2699354305471398, -0.36256866604416654],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 81,
    label = "s2_5_5_ene_0",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S}
2   R!H u0 {1,S} {5,D} {6,S}
3 * R!H u0 {1,S} {8,S}
4   R!H u0 {1,S} {7,S}
5   R!H u0 {2,D} {7,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {4,S} {5,S}
8   R!H u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3829272147774301, -0.3448554248966701, -0.16980458147397703, -0.2699354305471401, -0.36256866604416577],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 93,
    label = "s2_5_6_ene_0",
    group = 
"""
1 * R!H u0 {2,S} {3,S} {5,S}
2   R!H u0 {1,S} {4,D} {6,S}
3   R!H u0 {1,S} {7,S}
4   R!H u0 {2,D} {8,S}
5   R!H u0 {1,S} {9,S}
6   R!H u0 {2,S} {7,S}
7   R!H u0 {3,S} {6,S}
8   R!H u0 {4,S} {9,S}
9   R!H u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.3647332829386574, 0.12288724526236722, -0.1909645350505279, -0.20500174493748724, 0.14348927407149392],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 40,
    label = "s1_5_6_ene_1",
    group = 
"""
1    R!H u0 {2,S} {3,S} {4,S} {5,S}
2    R!H u0 {1,S} {6,S}
3    R!H u0 {1,S} {7,D}
4    R!H u0 {1,S} {8,S}
5    R!H u0 {1,S} {9,S}
6  * R!H u0 {2,S} {9,S}
7    R!H u0 {3,D} {10,S}
8    R!H u0 {4,S} {10,S}
9    R!H u0 {5,S} {6,S}
10   R!H u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.44726969351530155, -0.7786452016834928, -0.38150639202668396, -0.05284632844679549, -0.49060282805595473],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 162,
    label = "s3_5_6_ene_1",
    group = 
"""
1   R!H u0 {3,S} {4,S} {7,S}
2   R!H u0 {3,S} {5,S} {6,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {5,S}
5   R!H u0 {2,S} {4,S}
6   R!H u0 {2,S} {8,S}
7   R!H u0 {1,S} {8,D}
8 * R!H u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.20069389534526044, 0.16356378011070785, -0.28809247909614566, -0.023212701329182017, -0.1622882256629129],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s3_5_6_ene",
    group = 'OR{s3_5_6_ene_1}',
    thermo = None,
)


entry(
    index = 9,
    label = "s1_3_6_ane",
    group = 
"""
1   R!H u0 {2,S} {3,S} {4,S} {5,S}
2   R!H u0 {1,S} {3,S}
3   R!H u0 {1,S} {2,S}
4   R!H u0 {1,S} {6,S}
5   R!H u0 {1,S} {7,S}
6   R!H u0 {4,S} {8,S}
7   R!H u0 {5,S} {8,S}
8 * R!H u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],"K"),
        Cpdata = ([0.4641741341490314, -0.1886557157983791, -0.8532594356440065, -0.11248346433898154, -1.090061070218027],"cal/(mol*K)"),
        H298 = (0,"kcal/mol"),
        S298 = (0,"cal/(mol*K)"),
    ),
    )


entry(
    index = 0,
    label = "s1_3_6",
    group = 
"""
1   R!H u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   R!H u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   R!H u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   R!H u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8 * R!H u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
)

tree(
"""
L1: PolycyclicRing
	L2: s1_3_6
		L3: s1_3_6_ane
	L2: s2_3_7
		L3: s2_3_7_ane
	L2: s2_5_7
	L2: s3_4_6
		L3: s3_4_6_ane
		L3: s3_4_6_ene
			L4: s3_4_6_ene_1
	L2: s3_4_4
		L3: s3_4_4_ane
	L2: s3_5_6
		L3: s3_5_6_ene
			L4: s3_5_6_ene_1
		L3: s3_5_6_ane
	L2: s1_5_6
		L3: s1_5_6_ene
			L4: s1_5_6_ene_1
			L4: s1_5_6_ene_7
			L4: s1_5_6_ene_2
		L3: s1_5_6_ane
	L2: s2_4_6
		L3: s2_4_6_ene
			L4: s2_4_6_ene_1
	L2: s1_6_6
		L3: s1_6_6_ane
	L2: s2_6_7
		L3: s2_6_7_ben
			L4: s2_6_7_ben_ene
				L5: s2_6_7_ben_ene_1
	L2: s4_6_6
		L3: s4_6_6_ane
	L2: s2_3_6
		L3: s2_3_6_ene
			L4: s2_3_6_ene_2
			L4: s2_3_6_ene_1
		L3: s2_3_6_ane
	L2: s2_5_5
		L3: s2_5_5_diene
			L4: s2_5_5_diene_0_4
		L3: s2_5_5_ane
		L3: s2_5_5_ene
			L4: s2_5_5_ene_0
			L4: s2_5_5_ene_1
	L2: s3_5_5
		L3: s3_5_5_diene
			L4: s3_5_5_diene_1_4
		L3: s3_5_5_ene
			L4: s3_5_5_ene_side
			L4: s3_5_5_ene_1
		L3: s3_5_5_ane
	L2: s2-3_5_5_5_ane
	L2: s2_3_4
		L3: s2_3_4_ane
	L2: s2_4_5
		L3: s2_4_5_ane
	L2: s2_3_5
		L3: s2_3_5_ene
			L4: s2_3_5_ene_1
		L3: s2_3_5_ane
	L2: s2_6_6
		L3: s2_6_6_tetraene
			L4: s2_6_6_tetraene_0_2_6_8
		L3: s2_6_6_ben_ene
			L4: s2_6_6_ben_ene_2
			L4: s2_6_6_ben_ene_1
		L3: s2_6_6_naphthalene
		L3: s2_6_6_ben
		L3: s2_6_6_ene
			L4: s2_6_6_ene_m
			L4: s2_6_6_ene_1
			L4: s2_6_6_ene_0
			L4: s2_6_6_ene_2
		L3: s2_6_6_diene
			L4: s2_6_6_diene_0_6
			L4: s2_6_6_diene_1_6
			L4: s2_6_6_diene_0_3
			L4: s2_6_6_diene_0_5
			L4: s2_6_6_diene_0_2
			L4: s2_6_6_diene_1_7
			L4: s2_6_6_diene_0_8
		L3: s2_6_6_ane
	L2: s3_6_6
		L3: s3_6_6_ane
	L2: s2_5_6
		L3: s2_5_6_triene
			L4: s2_5_6_triene_m_1_7
		L3: s2_5_6_ene
			L4: s2_5_6_ene_0
			L4: s2_5_6_ene_6
			L4: s2_5_6_ene_2
			L4: s2_5_6_ene_1
			L4: s2_5_6_ene_m
		L3: s2_5_6_tetraene
			L4: s2_5_6_tetraene_1_3_5_7
			L4: s2_5_6_tetraene_1_3_5_8
		L3: s2_5_6_diene
			L4: s2_5_6_diene_1_3
			L4: s2_5_6_diene_m_7
		L3: s2_5_6_ben
		L3: s2_5_6_indene
		L3: s2_5_6_ane
""",
)