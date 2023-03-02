import collections

# custom replacements, this dictionary has custom replacements
custom_repl_set1 = collections.OrderedDict(
    {
        'Oral Regenerative Medicine (ORM)' : 'ORM',
        'Oral Infections and Inflammation (OII)' : 'OII',
        'World Health Organization (WHO) Collaborating Center' : 'WHOCC',
        'Communication Science' : 'cosc',
        'OWI (ACTA)' : 'OWI',        
        'Mathematics': 'Math',
        'Philosophy': 'Phil',
        'Sociology': 'Socio',
        'Accounting': 'Acc',
        'Finance': 'Fin',
        'Marketing': 'Mrk',
        'Economics': 'Econ',
        'LaserLaB': 'Laser',
        'Amsterdam Institute for Life and Environment': 'alife',
 #       'Computer Science': 'cs',
        ' for ': ' ',
        ' of ': ' ',
        ' and ': ' ',
        '!': '',
        '-': '',
        '_': '',
        '(': '',
        ')': '',
        '+': '',
        '&': ' ',
    }
)


# if a key should be ignored then it must be added to this list
custom_ignore_set1 = ['University Library','Executive board Vrije Universiteit']

# Faculty replacements
faculty_repl_set =  collections.OrderedDict(
    {
             'Academic Centre for Dentistry Amsterdam': 'acta',
             'Faculty of Science': 'beta',
             'Faculty of Behavioural and Movement Sciences': 'fgb',
             'Faculty of Humanities': 'fgw',
             'VUmc - School of Medical Sciences': 'gnk',
             'Faculty of Law': 'rch',
             'Faculty of Social Sciences': 'fsw',
             'Faculty of Religion and Theology': 'frt',
             'School of Business and Economics': 'sbe',
    }
)         