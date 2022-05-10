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
