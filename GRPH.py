#Overlap Graphs by Teodora Kovacevic

import re

k=3
dataset = ">Rosalind_5427CTGTAAGCCGGGCATTGATTGCGCATGATTAACGGCGCGTACTTCGTTTTTTGAAGGGGCCCGAGCCACTTGGACGTACTG>Rosalind_8025GTCTGTCACCCTCCGGTGGCGCCGAGACGCCCGGTGGAGGCTTTCTAAAACTGTGTGCACAAGGAATGTGCCGGAACCCGAGAGGCAGTGATCTAGG>Rosalind_8065TTAAGAACCTCAGACGCGATTACTGCCCCGCCGTCCCCAAGGGCAAATTGCTTGGCTGGGATCTCGTCCCAAACGTGGCTGTTCCAGCACCCAACG>Rosalind_2496ACCCGGGCCCGAAGGGGTTTCCGTAACTCTGGAAGCTCGGAGTTGTTGCCTCACAGTAGTCCCTAATACCAGAATGTGCAC>Rosalind_8966CATGAGAGCCTATCTTTGAGATTCAACAATGGATCCCAGACCCAGCAAACCCGGTCTCTTACTCCTACTGTCCAACATCCACA>Rosalind_5975ATTTAACATCCAAGAGACGCAGCCGCAGGGGGTGCAACGTCGTTACTCCCACCCGTCTAAGCCTGGAGGTTTTTGGTATCCGCATA>Rosalind_9621GGTAAACTAACAGGTTTCTGCGTAAGGTCCATACTTGGGTCATAGCAATATATCTTTGTAGAAGGAGTAGGTGACTGTGACG>Rosalind_7235TGTATAACCCCGCCGGTAATCGAGCGTGCCGACGAATCGCCTTAGGGGTCCAGTATCTTATGCCGATGGGCGGGGACTATCATTCCCGCCTAGTGG>Rosalind_0854TAGCACCACTATCCCTATTTCACAAAGTCCCCGGCACTAATAACAGTGTAGTTGTAGCGTTGGCGGTTTCGGATTCAGAGTAGGATTTGCA>Rosalind_3781GGCAAAACTGTATGTCACCTCCGCACAACAATACCTCGATGGAGTTGTGGAGCTCTGCGACAACGGAGCACCTAAACGTGAA>Rosalind_4430GGAGTGTCTGTACCGAATTCTCTCGATGAATCATTCTTCGCATAAGCCCTGTTGTCCCCACAGCCGTCTACTATCAAAATACCC>Rosalind_1943GAAAAAAAGTACGCATCTCGACTAACTAAGGTAGGTATCGTCTGTAGCCTAACTCCCCGCAATTTATTATACCACCCTCTT>Rosalind_8041GTGAGCTCCCTAAGAGCTCGAAGGTGAAGCGCAAAACATAGCTACAGTTATTGACATCCCGTCGGAAGAGGCCTACAGATTATGCAGCGCTAACCTCG>Rosalind_4959GGTCGCCCGGAATATGTTTCCGAATTACCAGGGTGGATATCATCTCCATAAAAGATATCAGAGAGGGCTTGACGAGCAAGACGCGTG>Rosalind_4182TGAGAGGGGTTTCCACTGATTAAGGACCGGTATTCCCCTTACTTCACTGGAATGCCGGTCGAGGGAACGGTACATTTGGTT>Rosalind_3612CTGTCCATGGTGGGCTATTCACGCTTGAGTCAGAACTTGCAGAAGTGCCTGCCCCAAAACCGACGAAGGCGAAGTACCGTCAGGGTGGATGACAG>Rosalind_1926AACATGGAAGAGGATCTTTGATCACGCGTGAGGTAAGACCAATCAATTTCCCATTTGAAGCCTCCCTCACGCTAGTGGACTC>Rosalind_1892ATTTTGCTCACATTCGAAATTTCAGAGAATTGACGCCTAAGAGCTCTTTAGCTCTTGAACCCATATTAAGCAAGGCCAGAATTGGTCACGGGGTCAACA>Rosalind_5321AAATTGCGAGGACACTAAGGCACAGAACTGATTTGTCCTGGACGTTTGGTCCCACTTCCTAGAGTGCTGCATAGGGAATGCAAACA>Rosalind_0124TCGCATCTTATTTCTAGGCTTAGCAAACCCAAATTAAGAGGGGCGGGTGTGGAGAGGCGCATCCTGCCTCCTCAGATGTCCCAG>Rosalind_0655CTTTGAGTGCAAACTGGCCAAACATTTAATTGCCGCTCGTGGGAACGCGTGAATATCTGAATTGGACTACCATCGTTATTCACCCGGC>Rosalind_2601GAAAGCCGCTTAGGGTGAACGCCGTAATTGTTTGATCCGCCTTTCACAGGCAACTACAGTTATCTCACTATTTCATGACCGTGCT>Rosalind_7815ACTTGTAGTTCTGAGCAAGCCGCCTCAGTTCGTCTGACCGGTAACATTATCAAGATGACATCCCGCCACGAACTCTACTGCAAATGCAGAG>Rosalind_3208GCCCGGGTGGCGCTTAAGAGACAACCCTAACTAAATGTATGTGGTCGGACGAGTCATAGATCTCGTTCCATGGCACTCTTTAAA>Rosalind_8601AATAAGAGTAAGCGCTTGGTTCAATCCAAGGTCGGCCAAACGGTGGATAAGTCAGCTAGAGATGGCCTTTGGCCCCGATCGCGGTATTACGAGGAGTTA>Rosalind_6621TATTGGTAGGCACTGTTAAATGGGCTTGAAGGCCCGAGTGATTTACAGCTTCGGTCAAATGGTACGTGGTATTGCCAATCTCGTCTAGGCGCCG>Rosalind_2466GTCCCTGTCTTAGAGGCGGTACACCGGTATTCTCGCGGCAGGTATCCAGTCGAGTCATGGCAGAGGACGCGAGGAATACCGGGACTAACTCGTTAAATT>Rosalind_8221CACCGCGGTAAGCGCGTTTCTTCTTGTCCAGTTGTAATATGACAATGGTGTGTCATGGTATGTGCGCCAGAAAACGTAAGAAAATTG>Rosalind_9858TGCAATTGGTGAGCTCCCTAACCAGACTTCTAGGGTAGCATTGCTGTTTTTGCCGCGTGGCCCGCCCGGACGTCTGAGCGCACG>Rosalind_4173GCTTAATGGGACTCGGGAGGCCGTGCAGTCGTCGATCAACGATCTAAACGGATTATACTAGATCACCAAGGCGGGCCTGTTACCAGCCTACAGCGTCTCC>Rosalind_6021CCCCGTCACTTCTCGCGAGGCACGTTCTTCCGCGTCAAAGCTATCTCGACCGCACACATTACAATGGGGGGGAGATGCTAAGACATGCGTTTG>Rosalind_1312TCCAAAGTAGCATGTGTAGTTGGGATCCAATACCCAGGACGCCATCAAAACCAAACATATTTGACAGCAAACCATGTAATTGGCATTTGATCGAACTC>Rosalind_6340AGTAGCATTATCAAGTAAACAACAATCTTCGCCTCATCCCGTTACGATGTTATGACTCGAGTTGGGTCGGACATACGAGCGACGGTGCGCCAAA>Rosalind_6419ACCGGCTTCTGACGATGGCGCGCTGTCCATTCAAACAATGACCAGGTCGTGCAAATTCGTCACCGTTGGCACTAAAACTAACTTTGTTCGTCCATCG>Rosalind_3915ATTGGTTGTGTCGGGTCCGTACGCGCGACCCAATCTCACGGCGGGAGTCATACAGATAGCGCCGTACATGTGGCAGTGAC>Rosalind_0002TTGGCACGTCAATTTGGAGCCTAACTAGAGAGCCGTCACTCTCACGGGGGCAGCCGTTATCAAACGACAACGACCATCACTCCC>Rosalind_3043AAATCGGACTCGTCAAAGATTAGGTCGCATCTCGTGCTTTTACAAAAACGCTCGCTAGCTGTGCGATACTTCACTTTCATAGTGACATGGCGCGCGGAG>Rosalind_0914ATCTGCCTTAGTATCTGAGTTGTCTGCCGCATGTGTGTTAAAGGCCAACATAGGTCCACATATAGACGTATCCACCGCAGGGACGTTTCTAA>Rosalind_5668TTTGTACGGATGCTGGGTCAGGGTCGCTCTGGATTGTATTACTATAAACACGATATACTGACCCAAGTGACCAGCGCGTACGTTTGGCATCATGCCAG>Rosalind_6618TTGAAGGCTTTTCTCACCACTAGTCGACACGCACATCAAACTTATCTGCCGGATTAGAGCGTCACACGCCGGGTGGTACCCCGGTCTAG>Rosalind_6180TTCCTCGATTTCTTGTATATTGTACAGGGTCGGAAGTTTGTCAAGCCGACAGCGCAGGTTTTCCTAACGATGCGGCGGCAGTTCAG>Rosalind_0074TGAAGTGGGCCCGAATGCCGCAGAGTTAGAAGGCAGGCACGTTCTATGGTGGGTACGCTACGCATATCGCTGACTGGTACCAAACGCAACCGCATGC>Rosalind_9322ACGGTTGGCCTGTTTTGATGAGGGTTGGGCGAGTGAGGCACCATGAGCGATTCAGCATAACCGCTATTGTGTCAAGATTTTACGGCGTATAACGCCC>Rosalind_7513TAATGACGGTGTCTATCTGTGACATAGGACTTTCGATCCGGAGACAAGCATTACGTTAGGATGTCGCCCGTTTAATACGCCGAGCCAAACCATTCGAGTC>Rosalind_6216CGTGATCAAGATAGTAACATGCGTTGCTTCACCCGGTAAAGTTATCTGTGCACGCCGTCGTTTCTTTCTACAAGGATGAATA>Rosalind_8682ACCGTTAATACCGTCGCCATTCGTCGAATCGGTTGACGCGACTTACGCGGGCGGGGTCGCCCTGTAGGAATCCGGACAACCCGCGCCCATCT>Rosalind_5453GGTGTAATCCGACGATAGTCGTGGTGGCGAGGGCAAACGAGGTGGACTGTACCCTCTCTGTCAGCCGCGTAGCAGGGACCTGCATGCGG>Rosalind_2828TACACCGGGTGATACTTCCCCATCTCTATACGCCTGAATGAGGCGATGGCTAAATGGATCGATTGCACATCTGGGGTTTTGTCTGACGGGCCGTCCT>Rosalind_6241CAACATATAATGCTGTAAAACGGTAATCAGCTTTGGTTTTATCATGGCTTATCCATGGTCGCGCGTTATTATGTTCCGCCTTGTTGGTGGCCTTCA>Rosalind_0591TCATAGGTCCACGCGCAAAAACTGGGCAAGGTGTGCGCGGTTCAATTGGTGATTTACAAAACACCGGTCTTTCCCTAAACTAA>Rosalind_7973AGTGTCCCGTCTGGAGTAATGGAGATAGGCAGGAACAGAGGACGCTCAACACGGACCATGCTGTGTACTTGCAGCGATCCCTCTAATGGCGTG>Rosalind_2534TGACCTGGTGTGGAGCAGCCGTACGAGGGCGGTGTCATAATTGAGCCATGCCCAAGAGTCACACCATGGCATCCTTTACGCGCGAATGTGTCCA>Rosalind_5799TCGACCGACTAACGTAGGCCAGCCGATTAATTAAACGGGCATTCGCACAAGCTCGCAAGCGTTTTAACCAGAAACAACTCTGGGACT>Rosalind_6935CTATCTTAGTCCCTCGTTTAATGGTCCGAGATAGGTACCGAAACTAACTGTAGGGATACTGTGTATTATTCTCCGGTAGGGGATCCCTCACAAATCCG>Rosalind_2960CTACGGTCGAGCAGACAAAAGATTGGACAATATTGTGAGAAGAGGGCGCGTCGCTTCGAGGCAGATACCTTGCCTATCAGGGTTCGC>Rosalind_1800CGTTGTCGTTACTGCACCTCACCGCCACTCTAAAGAGTTTGTAGTTCCCTTCATGTGTTTTGGAATAAGCGTTCATCTGTTCGACG>Rosalind_5124GCGTAGCCTGAGTTAAGTGATGTTATCGCCTCGCGAAATACTCCTTAGACCGCGCGTGAGGTTCAACAGTTCAGTCTATTCAAGAGGT>Rosalind_0022CAGTGATGGGACAATTAAATCTGTATACGCGCACACCTTGTTCTAAAGGTTATGCGGGGCCTATGGCAGCTAGCGATTTGCAATATA>Rosalind_8303CATTAATCGAACTAATACTCGCAGCATGTCGGGATGAGGACCAACCGGAAGCCGATACTCTGCGCAGTTGACGTTGTGAAAACGGACCTTACC>Rosalind_4771GTCGTGTCCTGCCCGTTATTCCTAAACTAGTTTCGCGCGTGTGTCGCGACCCGGCGTGTAACCGGAAACGGCCGTTGTGCGGACGCCAGGACGA>Rosalind_5686GCTTGGTCGATAATCTCGCCGTGGTGGGAGAGGTGGATGTTGCACCCCAGGGTACCCAAGATGCTTGGCCGATTGTGATCATCATGTAGA>Rosalind_5607AAGCTCTCTAGACAGTCGACAATGCCCGTCAGAGCATGATATAATGAGAACGGACTTCGACAACTCCCCTCCAGTTACCACCTACAC>Rosalind_9951TCGCCCATGAGGGGCTCACTACAGTAACACGGCATAATGTCATTTTATGTAACACTCGTCCCGGCCCCTTTGGCATTGCTGATCTGCA>Rosalind_8395GGCGCGGTGTTTGTAACCCCAGACCTGGCGGCCGTGGAGTGGTTCCCTAGACCCTGGCAAGACTATACACTGTCCACCGAGCACACC>Rosalind_6292CTCCTTTATACTATAAATCAGACATTAATACTGATAGCGGAAAGAATATTCACGCATGAGTTCTGGTGAGGTAGACTAGGGGTG>Rosalind_7172CAGCGATCTGTACGACCACGATGCTATGACCGTGCATTTTAACTGGTAACCGTAGCCCGTTTAGAATTCAGCCTCATAACGTC>Rosalind_9020CTCAACCAAAAGACGGCTTGACGTTCCTGGCGCTCACCGTTGTACAGGTTCCTTAGCTGGAAGGTATCCTAAGTAAAGCGA>Rosalind_9497AATCACGAGCCGAGAGCAGAAGCTTTGGCAGCGTGCCGTTGATGATCCTGCAAGATACGGGACCATAGGCAACGATACTAGCCA>Rosalind_6165CCCCTAAATCTTCACTTTGCCCGAGTCCCTCCTGCTACTCCTGTAGCGAGCATTCCTTCAGGAGCTTCGTCCGTTGAGGGGTAAAGTCTCACTAAAG>Rosalind_9466TGGCCACATGCATCGCGTTGCAAACGTCGTAACTATAAGTTGTAACTAGCTGGGCTATTTGTACGGTTCAGCCTTAAATATCTCTCAAG>Rosalind_9520ACCCGATTGCCCCTGGTCCGGAACTCCTTGATGTTCTCAATACGCGTGAGCAGCAGTAGAAGCCGCGGCGCGCATAGCTCTCTCGGGGCCATCATGCC>Rosalind_9345ATTTTCCACATCTTGTGGCCACTGATTGACAACTCGTACGTCTCCCCGATTCATACCAGTAACAAACTAATTATCAATATGCGCCG>Rosalind_6203GCCAGGCAATCTTATTGCTCACTGCGACTACCCGACGGATCTACTTACCTCGCGTTGGGGCTTTTTAATCACGAGAGTTCCCTAGGA>Rosalind_8747CCTCTTAACAATGTAATTGCCTCTCATTTTGTCTCAGCATTGAGGAGTCCGCAAAGTCGCCTGCCTTCTTCGCATGTCGTAT>Rosalind_6751GAAGAAGGTACAGGGACCCCCAGAATTATGTATTAAAGGGGGTGCAAGTGGAAATCGAGCTCCAGCAGGAGAATGCCCTGCTGTTGCGCCTTG>Rosalind_5216CCTGGTAAATCGTGCCTAATCCGAAAGCACTCTGCATCACACTGTTGGTAGGTCGCCTCTTGTGTATCATGAGGTCGTTATACTCTGCGAT>Rosalind_5192TCTAATACGGACGCTTCGCTGCTGGAATACAAGTTCTCATGCCTAGCGGATTCCTCATCGTATCGTGTGTATTGTTAGCACT>Rosalind_0122CATCATCCTTAAACAATTCCTAAAAATAAGCACGGTTCCGGAGTGCTCAGCATGGTTAAAAGTGCGACTGTGTAAAGTTTGGGTTTT>Rosalind_5798CTAAACGGATGTGAGTTGTATTCGCCTAACGGAGCACCGCGAACTATAAAATTCGCTCTGCTTGTTTGTCCCTCAATTGACACGCATCATGGTAT>Rosalind_3134ACACGGGGAGCCTCGTTGAAAGTATAAGTCAGGTCACCGGAAGTGCGGGTCCCTGCCCCCTCCCTACATTTTTAGTTGCGCACCCATTTTGTCCGGTGCT>Rosalind_3565TCGTCCGACAACGCTCGCCCAAACACCACTACTTTATCATCGCCAAAGGTTGTACTAGTGCGTCCGCAAACGGCGAATATACATACTAC>Rosalind_5407ATAAGCTGCCCGATGACAAGGCCATACGATTATCGAACGGCTACGCCGCCATGGCTGTGAACCGCGATAGTCACAATCCACTCATTCCGGCTAT>Rosalind_2490GACCACCTCCCGACAACTTTTACAGATGGTAGGGATGGCTTGCCCATCGGGGCAGTTGAACATCGTAAGCATGAGTATCTGGCC>Rosalind_6206ATCTCTCTGGACCTGTCAACCGCTTAGAAATAACATGTTTGTTTAATTTTAAAGATCATCAGACCAGTTGTTCAGAAATGGCTCGGTGAAGGTTTGAATG>Rosalind_9774TTAATCGTCCATCCAATGAGCCTCCCACGCTTTGTGGTCCAGAACATTAGAAGCAGCCCCACTGTAAGCTTACCGGACAACCGC>Rosalind_6549GCTGCCGCCGAATCCACCTTAATTAGGACCATGTCACCACCTCACGAAAAAAGTGCGAGCACTGCCTATTCATATTGGAACCGCGC>Rosalind_4934TCAAAGAAGACTTACTAAAGTTTCTTCAGGAGACTCGGGTGTAGCACGCGCCAGAGGCACAGCAGAACTACGCCCCTGCTTAGAAG>Rosalind_0150TCGCTGTCAAGCTTTTCATCTAAAACCCGCTGACTAGTTTACGTCTTCGCCATACACGGGCACCCACGCTATAAAAAACGATGTTGGTATGTGACTCA>Rosalind_7499CCAGCGAGTCTTTAGAGGAAGAGATTTACGTTCCCCCGCTATTTCCATTTCAAAGTAAAGTCCCCCCGGACTTTCTAGTGGATAGCTGTCATGAACCTCC>Rosalind_8582TCTTCTAAGTGGGCCCATCCGCCAAGCGTCTGTTACACAGGATTTCATTTATGTACTCACAATTGCATCGCTCTCGCAGTGAGTG>Rosalind_1577TCCAAAGACCTTGGTGGTAGTTCACGGGCCCTTACGACATGCAAACATTCATCTATGGCAGTCTGCCGGGCGCACCTAGGTTAGAACACTAAC>Rosalind_5429AGTGCTCTTCCGCTCCTCTAAAAGAACCGCCCGAGCGACAGTGGCATCCACCGCCCAAAATACACGCACCAAAGTATTAGAGACTAATGCG>Rosalind_2341CCGTCCAAAATGGACTGCAGGTGGAAGGGCGTTGTGAGTCGCTCGATAAGCAGCCCTTCGGGAGAAGGCTGTGACTGCTAACAC>Rosalind_8755ATGCAAGCTCGCGCCACGGAAATCTTGCCGGGAAGTTTAAATTTCCTGACGGGCGTTCTGTGCGTTCTACATCGTAGAGGTTGTGT>Rosalind_6934TCAGTTGATGTTCTAGGTATGTAAATGAATCACCAGCGAAGTCGGGAAGGCTAACCTAGTCCTGAAGTCATCAACCACAAATCACAGGAAAGTGCT>Rosalind_3679ATGACGTCAATTTTTCGTAGATTGGTTTCGACGCTTCTGAGGGCCGGGAGAGTCCAGTGCAACCACAGTATTACGTGTGGTTGTCAGATGGGGCAATAGG>Rosalind_9422TTAGTCCTCGCCATGCCGCGCCATTGATAAGAATTCCCTATTTTAGACTAACCAACGTCAATAGTCAACGCGCATAAACCGATGCGGTTCGGATTAG>Rosalind_6868ATAGTCATAGCAGATCATGCATCTTAGTACACTGGCAACGTCGTGTGGGAATGAGTCACAAACGCCACTCCGAATATAGGTTGAAACGTGCAGC>Rosalind_7796CGAGGGCTGTCCCGAGATGTATTGTTCGTAAAGAGGTGGCGAGACTCGGCCAATATCAAACATATCATATCACGGCTGCAGTTGTC>Rosalind_0904CTTACAAAATCCGTGAGCAAGCATTGAGGGGGTGGGCAACATTGTCCTAGCCGCGCGCCCGATTCCGTCTTCTTCCTCGTGATGAAC"
sequences = re.findall(r'[ATGC]+', dataset)
names = re.findall(r'Rosalind_[0-9]+',dataset)

for seq1 in sequences:
    for seq2 in sequences:
        suffix = seq1[-k:]
        prefix = seq2[:k]
        if seq1 == seq2:
            continue
        if prefix == suffix:
            print(names[sequences.index(seq1)], names[sequences.index(seq2)])

