#!/usr/bin/env python

# This script is designed to convert general genus species taxonomy to the correct name format to download the matching mlst DBs from pubmlst

import argparse


def parseArgs(args=None):
    """Takes in a taxa file and creates a file with the taxa found"""
    parser = argparse.ArgumentParser(description='Script to convert taxonomy to correctly formatted mlst database name(s) to pull from pubmlst')
    parser.add_argument('-G', '--genus', dest="genus", required=True, help='genus of taxonomy')
    parser.add_argument('-s', '--species', dest="species", required=True, help='species of taxonomy')
    return parser.parse_args()

specific_dict = { 'Acinetobacter baumannii': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter calcoaceticus': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter nosocomialis': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter pittii': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter seifertti': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Acinetobacter diijkhoorniae': 'Acinetobacter baumannii#1,Acinetobacter baumannii#2',
                'Aggregatibacter actinomycetemcomitans': 'Aggregatibacter actinomycetemcomitans',
                'Anaplasma phagocytophilum': 'Anaplasma phagocytophilum',
                'Aspergillus fumigatus': 'Aspergillus fumigatus',
                'Bacillus cereus': 'Bacillus cereus',
                'Bacillus licheniformis': 'Bacillus licheniformis',
                'Bacillus subtilis': 'Bacillus subtilis',
                'Bacteroides fragilis': 'Bacteroides fragilis',
                'Bartonella bacilliformis': 'Bartonella bacilliformis',
                'Bartonella henselae': 'Bartonella henselae',
                'Bartonella washoensis': 'Bartonella washoensis',
                'Brachyspira hampsonii': 'Brachyspira hampsonii',
                'Brachyspira hyodysenteriae': 'Brachyspira hyodysenteriae',
                'Brachyspira intermedia': 'Brachyspira intermedia',
                'Brachyspira pilosicoli': 'Brachyspira pilosicoli',
                'Burkholderia cepacia': 'Burkholderia cepacia complex',
                'Burkholderia cenocepacia': 'Burkholderia cepacia complex',
                'Burkholderia multivorans': 'Burkholderia cepacia complex',
                'Burkholderia vietnamiensis': 'Burkholderia cepacia complex',
                'Burkholderia pyrrocinia': 'Burkholderia cepacia complex',
                'Burkholderia stabilis': 'Burkholderia cepacia complex',
                'Burkholderia ambifaria': 'Burkholderia cepacia complex',
                'Burkholderia pseudomallei': 'Burkholderia pseudomallei',
                'Campylobacter concisus': 'Campylobacter concisus/curvus',
                'Campylobacter curvus': 'Campylobacter concisus/curvus',
                'Campylobacter fetus': 'Campylobacter fetus',
                'Campylobacter helveticus': 'Campylobacter helveticus',
                'Campylobacter hyointestinalis': 'Campylobacter hyointestinalis',
                'Campylobacter insulaenigrae': 'Campylobacter insulaenigrae',
                'Campylobacter jejuni': 'Campylobacter jejuni',
                'Campylobacter lanienae': 'Campylobacter lanienae',
                'Campylobacter lari': 'Campylobacter lari',
                'Campylobacter sputorum': 'Campylobacter sputorum',
                'Campylobacter upsaliensis': 'Campylobacter upsaliensis',
                'Candida albicans': 'Candida albicans',
                'Candida glabrata': 'Candida glabrata',
                'Candida krusei': 'Candida krusei',
                'Candida tropicalis': 'Candida tropicalis',
                'Candidatus Liberibacter': 'Candidatus Liberibacter solanacearun',
                'Carnobacterium maltaromaticum': 'Carnobacterium maltaromaticum',
                'Citrobacter freundii': 'Citrobacter freundii',
                'Clonorchis sinensis': 'Clonorchis sinensis',
                'Clostridioides difficile': 'Clostridioides difficile',
                'Clostridium botulinum': 'Clostridium botulinum',
                'Clostridium perfringens': 'Clostridium perfringens',
                'Clostridium septicum': 'Clostridium septicum',
                'Corynebacterium diphtheriae': 'Corynebacterium diphtheriae',
                'Cutibacterium acnes': 'Cutibacterium acnes',
                'Dichelobacter nodosus': 'Dichelobacter nodosus',
                'Enterobacter cloacae': 'Enterobacter cloacae',
                'Enterobacter asburiae': 'Enterobacter asburiae',
#                'Enterobacter hormaechei': 'Enterobacter hormaechei',
                'Enterobacter kobei': 'Enterobacter kobei',
                'Enterobacter luwigii': 'Enterobacter luwigii',
                'Enterobacter nimipressuralis': 'Enterobacter nimipressuralis',
                'Enterobacter mori': 'Enterobacter mori',
                'Enterococcus faecalis': 'Enterococcus faecalis',
                'Enterococcus faecium': 'Enterococcus faecium',
                'Escherichia coli': 'Escherichia coli#1,Escherichia coli#2',
                'Flavobacterium psychrophilum': 'Flavobacterium psychrophilum',
                'Gallibacterium anatis': 'Gallibacterium anatis',
                'Glaesserella parasuis': 'Glaesserella parasuis',
                'Haemophilus influenzae': 'Haemophilus influenzae',
                'Helicobacter cinaedi': 'Helicobacter cinaedi',
                'Helicobacter pylori': 'Helicobacter pylori',
                'Helicobacter suis': 'Helicobacter suis',
                'Kingella kingae': 'Kingella kingae',
                'Klebsiella aerogenes': 'Klebsiella aerogenes',
                'Klebsiella oxytoca': 'Klebsiella oxytoca',
                'Klebsiella pneumoniae': 'Klebsiella pneumoniae',
                'Kudoa septempunctata': 'Kudoa septempunctata',
                'Lactobacillus salivarius': 'Lactobacillus salivarius',
                'Listeria monocytogenes': 'Listeria monocytogenes',
                'Macrococcus canis': 'Macrococcus canis',
                'Macrococcus caseolyticus': 'Macrococcus caseolyticus',
                'Mammaliicoccus sciuri': 'Mammaliicoccus sciuri',
                'Mannheimia haemolytica': 'Mannheimia haemolytica',
                'Melissococcus plutonius': 'Melissococcus plutonius',
                'Moraxella catarrhalis': 'Moraxella catarrhalis',
                'Mycobacteroides abscessus': 'Mycobacteroides abscessus',
                'Mycoplasma agalactiae': 'Mycoplasma agalactiae',
                'Mycoplasma anserisalpingitidis': 'Mycoplasma anserisalpingitidis',
                'Mycoplasma bovis': 'Mycoplasma bovis',
                'Mycoplasma flocculare': 'Mycoplasma flocculare',
                'Mycoplasma gallisepticum': 'Mycoplasma gallisepticum#1,Mycoplasma gallisepticum#2',
                'Mycoplasma hominis': 'Mycoplasma hominis',
                'Mycoplasma hyopneumoniae': 'Mycoplasma hyopneumoniae',
                'Mycoplasma hyorhinis': 'Mycoplasma hyorhinis',
                'Mycoplasma iowae': 'Mycoplasma iowae',
                'Mycoplasma pneumoniae': 'Mycoplasma pneumoniae',
                'Mycoplasma synoviae': 'Mycoplasma synoviae',
                'Orientia tsutsugamushi': 'Orientia tsutsugamushi',
                'Ornithobacterium rhinotracheale': 'Ornithobacterium rhinotracheale',
                'Paenibacillus larvae': 'Paenibacillus larvae',
                'Pasteurella multocida': 'Pasteurella multocida#1,Pasteurella multocida#2',
                'Pediococcus pentosaceus': 'Pediococcus pentosaceus',
                'Photobacterium damselae': 'Photobacterium damselae',
                'Piscirickettsia salmonis': 'Piscirickettsia salmonis',
                'Porphyromonas gingivalis': 'Porphyromonas gingivalis',
                'Pseudomonas aeruginosa': 'Pseudomonas aeruginosa',
                'Pseudomonas fluorescens': 'Pseudomonas fluorescens',
                'Pseudomonas putida': 'Pseudomonas putida',
                'Riemerella anatipestifer': 'Riemerella anatipestifer',
                'Salmonella enterica': 'Salmonella enterica',
                'Saprolegnia parasitica': 'Saprolegnia parasitica',
                'Staphylococcus aureus': 'Staphylococcus aureus',
                'Staphylococcus chromogenes': 'Staphylococcus chromogenes',
                'Staphylococcus epidermidis': 'Staphylococcus epidermidis',
                'Staphylococcus haemolyticus': 'Staphylococcus haemolyticus',
                'Staphylococcus hominis': 'Staphylococcus hominis',
                'Staphylococcus lugdunensis': 'Staphylococcus lugdunensis',
                'Staphylococcus pseudintermedius': 'Staphylococcus pseudintermedius',
                'Stenotrophomonas maltophilia': 'Stenotrophomonas maltophilia',
                'Streptococcus agalactiae': 'Streptococcus agalactiae',
                'Streptococcus bovis': 'Streptococcus bovis/equinus complex (SBSEC)',
                'Streptococcus equinus': 'Streptococcus bovis/equinus complex (SBSEC)',
                'Streptococcus canis': 'Streptococcus canis',
                'Streptococcus dysgalactiae': 'Streptococcus dysgalactiae equisimilis',
                'Streptococcus gallolyticus': 'Streptococcus gallolyticus',
                'Streptococcus oralis': 'Streptococcus oralis',
                'Streptococcus pneumoniae': 'Streptococcus pneumoniae',
                'Streptococcus pyogenes': 'Streptococcus pyogenes',
                'Streptococcus suis': 'Streptococcus suis',
                'Streptococcus thermophilus': 'Streptococcus thermophilus#1,Streptococcus thermophilus#2',
                'Streptococcus uberis': 'Streptococcus uberis',
                'Streptococcus zooepidemicus': 'Streptococcus zooepidemicus',
                'Treponema pallidum': 'Treponema pallidum',
                'Trichomonas vaginalis': 'Trichomonas vaginalis',
                'Vibrio cholerae': 'Vibrio cholerae,Vibrio cholerae#2',
                'Vibrio parahaemolyticus': 'Vibrio parahaemolyticus',
                'Vibrio tapetis': 'Vibrio tapetis',
                'Vibrio vulnificus': 'Vibrio vulnificus',
                'Xylella fastidiosa': 'Xylella fastidiosa',
                'Yersinia pseudotuberculosis': 'Yersinia pseudotuberculosis',
                'Yersinia ruckeri': 'Yersinia ruckeri'
                }


generic_dict = { 'Achromobacter': 'Achromobacter spp.',
               'Aeromonas': 'Aeromonas spp.',
               'Arcobacter': 'Arcobacter spp.',
               'Bordetella': 'Bordetella spp.',
               'Borrelia': 'Borrelia spp.',
               'Brachyspira': 'Brachyspira spp.',
               'Brucella': 'Brucella spp.',
               'Chlamydiales': 'Chlamydiales spp.',
               'Cronobacter': 'Cronobacter spp.',
               'Edwardsiella': 'Edwardsiella spp.',
               'Geotrichum': 'Geotrichum spp.',
               'Leptospira': 'Leptospira spp.,Leptospira spp.#2,Leptospira spp.#3',
               'Mycobacteria': 'Mycobacteria spp.',
               'Neisseria': 'Neisseria spp.',
               'Rhodococcus': 'Rhodococcus spp.',
               'Shewanella': 'Shewanella spp.',
               'Sinorhizobium': 'Sinorhizobium spp.',
               'Streptomyces': 'Streptomyces spp',
               'Taylorella': 'Taylorella spp.',
               'Tenacibaculum': 'Tenacibaculum spp.',
               'Ureaplasma': 'Ureaplasma spp.',
               'Vibrio': 'Vibrio spp.',
               'Wolbachia ': 'Wolbachia ',
               }

args = parseArgs()
print(args.genus+" "+args.species)
if str(args.genus+" "+args.species) in specific_dict:
    #f.write(specific_dict[args.genus+" "+args.species]+"\n")
    print(specific_dict[args.genus+" "+args.species])
elif str(args.genus) in generic_dict:
    #f.write(generic_dict[args.genus]+"\n")
    print(generic_dict[args.genus])
else:
    #f.write("No Match Found\n")
    print("No match found")
