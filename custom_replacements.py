import collections

# custom replacements, this dictionary has custom replacements
custom_repl_set1 = collections.OrderedDict(
    {
        'Mathematics': 'Math',
        'Philosophy': 'Phil',
        'Sociology': 'Socio',
        'Accounting': 'Acc',
        'Finance': 'Fin',
        'Marketing': 'Mrk',
        'Economics': 'Econ',
        'LaserLaB': 'Laser',
        'Computer Science': 'csci',
        'Oral Regenerative Medicine (ORM)' : 'ORM',
        'Oral Infections and Inflammation (OII)' : 'OII',
        'OWI (ACTA)' : 'OWI',
        '!': '',
        '-': '',
        '_': '',
        '(': '',
        ')': '',
        '+': '',
        '&': 'and',
        ' (WHO) ': ' ',
        ' for ': ' ',
        ' of ': ' ',
        ' and ': ' ',
    }
)


# if a key should be ignored then it must be added to this list
custom_ignore_set1 = ['University Library']
