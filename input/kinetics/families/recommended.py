#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file contains multiple sets of suggested kinetics families for various
# systems of interest. They can be used by including the name of a set in the
# kineticsFamilies part of the input file. Multiple sets can be specified at
# the same time, and the union of them will be loaded. These sets can also be
# specified along with individual families. Custom sets can be easily defined
# in this file and immediately used in input files without any additional
# changes.

default = {
    '1+2_Cycloaddition',  # exclude aromatic rings
    '1,2-Birad_to_alkene',  # only forward by default
    '1,2_Insertion_CO',
    '1,2_Insertion_carbene',
    '1,2_NH3_elimination',
    '1,2_shiftC',
    '1,2_shiftS',
    '1,3_Insertion_CO2',
    '1,3_Insertion_ROR',  # exclude aromatic rings
    '1,3_Insertion_RSR',  # exclude aromatic rings
    '1,3_NH3_elimination',  # only forward
    '1,4_Cyclic_birad_scission',  # only forward
    '1,4_Linear_birad_scission',  # only forward
    '2+2_cycloaddition_CCO',  # only reverse
    '2+2_cycloaddition_CO',  # only reverse
    '2+2_cycloaddition_CS',  # only reverse
    '2+2_cycloaddition_Cd',  # only reverse
    '6_membered_central_C-C_shift',
    'Birad_R_Recombination',  # only forward
    'Birad_recombination',  # only forward
    'CO_Disproportionation',
    'Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH',
    'Cyclic_Ether_Formation',
    'Cyclic_Thioether_Formation',
    'Diels_alder_addition',
    'Disproportionation',  # only forward
    'HO2_Elimination_from_PeroxyRadical',
    'H_Abstraction',  # exclude aromatic rings, don't abstract from a radical site
    'Intra_2+2_cycloaddition_Cd',  # only reverse
    'Intra_5_membered_conjugated_C=C_C=C_addition',
    'Intra_Diels_alder_monocyclic',
    'Intra_Retro_Diels_alder_bicyclic',
    'Intra_Disproportionation',  # only forward
    # 'Intra_RH_Add_Endocyclic',
    # 'Intra_RH_Add_Exocyclic',
    'Intra_R_Add_Endocyclic',
    'Intra_R_Add_Exocyclic',
    'Intra_R_Add_Exo_scission',
    'Intra_ene_reaction',
    'intra_H_migration',
    'intra_NO2_ONO_conversion',
    'intra_OH_migration',
    'intra_substitutionCS_cyclization',
    'intra_substitutionCS_isomerization',
    'intra_substitutionS_cyclization',
    'intra_substitutionS_isomerization',
    'R_Addition_COm',
    'R_Addition_MultipleBond',  # exclude aromatic rings
    'R_Recombination',  # only forward
    'ketoenol',
    'Singlet_Carbene_Intra_Disproportionation',
    'Singlet_Val6_to_triplet',
    'Substitution_O',
    'SubstitutionS',
    'Cyclopentadiene_scission',
    'Fake_amine_hydrolysis',  # custom
    'Fake_HOCK_rearrangement',  # custom
}

# Peroxide chemistry families that are likely relevant in liquid-phase
# hydrocarbon oxidation systems
liquid_peroxide = {
    'Peroxyl_Disproportionation',
    'Peroxyl_Termination',
    'Bimolec_Hydroperoxide_Decomposition',
    'Korcek_step1',
    'Korcek_step1_cat',
    'Korcek_step2',
    'Baeyer-Villiger_step1_cat',
    'Baeyer-Villiger_step2',
    'Baeyer-Villiger_step2_cat',
}

# Surface chemistry for heterogeneous catalysis.
# surface = {
#     'Surface_Adsorption_Single',
#     'Surface_Adsorption_vdW',
#     'Surface_Adsorption_Dissociative',
#     'Surface_Dissociation',
#     'Surface_Abstraction',
# }

# Surface chemistry families that are under development and not yet working well.
# surface_development = {
#     'Surface_Adsorption_Double',
#     'Surface_Dissociation_vdW',
#     'Surface_Adsorption_Bidentate',
#     'Surface_Bidentate_Dissociation'
#     # 'Surface_Recombination' #DEPRECATED. USE Surface_Dissociation INSTEAD
# }
