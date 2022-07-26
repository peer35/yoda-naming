"""
Title:
Author: Brett G. Olivier

Usage:

(C) Brett G. Olivier, VU Amsterdam, 2022. Licenced for use under the BSD 3 clause

# These need to be defined and passed into the module methods

expressions = ['Department', 'Research Institute', 'Faculty']
searchkey = 'term'

output_data = {'Department' : {},
        'Research Institute' : {},
        'Acronymns' : [],
        'Obsolete_terms' : []
        }

# custom replacements, can be empty
custom_repl = collections.OrderedDict({})

# needs to be loaded from Peter's org data file
orgdata = None

"""

import os, json, pprint

def get_data(data_input_name, cDir, expressions):
    with open(os.path.join(cDir, data_input_name), 'r') as F:
        orgdata = json.load(F)
    
    # get list of existing abbreviations, if it exists
    if os.path.exists(os.path.join(cDir, '_abbr_list_previous.json')):
        with open(os.path.join(cDir, '_abbr_list_previous.json'), 'r') as F:
            prev_abbr_list = tuple(json.load(F))
    else:
        prev_abbr_list = ()

    # get list of obsolete terms, if it exists
    if os.path.exists(os.path.join(cDir, '_abbr_list_obsolete.json')):
        with open(os.path.join(cDir, '_abbr_list_obsolete.json'), 'r') as F:
            obsolete_terms = list(json.load(F))
    else:
        obsolete_terms = []

    output_data = {'Acronymns': []}
    for exp in expressions:
        output_data[exp] = {}

    return orgdata, output_data, prev_abbr_list, obsolete_terms


def check_for_obsolete(output_data, prev_abbr_list, obsolete_terms):
    acronew = [a.lower() for a in sorted(output_data['Acronymns'])]
    output_data['Obsolete_terms'] = obsolete_terms
    for acr in prev_abbr_list:
        if acr not in acronew:
            obsolete_terms.append(acr)
            output_data['Obsolete_terms'].append(acr)
    # this is a hack to get rid of term duplications which can probable be better sorted out above
    obsolete_terms = list(set(obsolete_terms))
    output_data['Obsolete_terms'] = list(set(output_data['Obsolete_terms']))
    return obsolete_terms


def make_acronymns(branch, out, expr, key, acro_repl, key_ignore, prev_abbr_list, obsolete_terms, faculty_repl_set, faculty_prefix):
    for e in branch:
        if branch[key] == 'Faculty':
            faculty_prefix = faculty_repl_set[branch['name']]
            #print(faculty_prefix)  
        
        if branch['name'] not in key_ignore and e == key and branch[key] in expr:
            acro = f'{faculty_prefix}-{acronize(branch["name"], acro_repl)}'
            if acro in out['Acronymns'] or acro.lower() in obsolete_terms:
                if acro.lower() in obsolete_terms:
                    print('Avoiding duplication of existing obsolete term: ', acro.lower())
                else:
                    print('Duplicate acronym: ', acro.lower())
                #out['Acronymns'].insert(0, (acro, branch['name']))
                acro = f'{faculty_prefix}-{acronize(branch["name"], acro_repl, duplicate=True)}'
            if acro.lower() not in prev_abbr_list:
                print('New Acronymn add:', acro.lower())
            else:
                print('Acronymn already exists:', acro.lower())
            out['Acronymns'].append(acro)
            out[branch[key]][branch['name']] = acro
        elif e == 'children':
            for c in branch['children']:
                make_acronymns(c, out, expr, key, acro_repl, key_ignore, prev_abbr_list, obsolete_terms, faculty_repl_set, faculty_prefix)
    for fac in out['Faculty']:
        out['Faculty'][fac] = out['Faculty'][fac].split('-')[0]


def acronize(words, replacements, duplicate=False):
    # single word names treated as Acronymns, shorten if needed.
    # words0 = words

    # clean phrase
    for r in replacements:
        words = words.replace(r, replacements[r])

    if len(words.split()) == 1:
        if not duplicate:
            words = words.upper()
        else:
            print('\nWARNING: not sure what to do with a duplicate single name:', words)
            raise(RuntimeWarning(), words)
    else:
        if not duplicate:
            words = ''.join(w[0] for w in words.split())
        else:
            # words = words.replace('and', ' ')
            words = ''.join(w[:2].upper() for w in words.split())

    # print(words0, ' --> ', words)
    return words


def write_data(output_file_name, output_data, expressions, output_lowercase):
    if output_lowercase:
        # first we lowercase all acronyms
        output_data['Acronymns'] = [a.lower() for a in sorted(output_data['Acronymns'])]
        for expr in expressions:
            for k in output_data[expr]:
                output_data[expr][k] = output_data[expr][k].lower()

    # dumps the entire output dataset
    with open(output_file_name + '.json', 'w') as F:
        json.dump(output_data, F, indent=' ')
        
    # store the last list of abbreviations to detect new ones in each run
    with open('_abbr_list_previous.json','w') as F:
        json.dump([a.lower() for a in sorted(output_data['Acronymns'])], F)


    # store the last list of obsolete terms to detect new ones in each run
    with open('_abbr_list_obsolete.json','w') as F:
        json.dump(sorted(output_data['Obsolete_terms']), F)


    # for the google sheet or however we need for a form.
    with open(output_file_name + '.txt', 'w') as F:
        for expr in expressions:
            if expr == 'Faculty':
                continue
            F.write(f'# {expr}\n')
            for dep in sorted(output_data[expr].keys()):
                F.write(f'{dep} [{output_data[expr][dep]}]')
                if output_data[expr][dep] in output_data['Obsolete_terms']:
                    F.write(f'*')
                F.write(f'\n')
    return output_data


if __name__ == '__main__':
    import os
    from custom_replacements import custom_repl_set1 as custom_repl
    from custom_replacements import faculty_repl_set as faculty_repl_set
    from custom_replacements import custom_ignore_set1 as custom_ignr
    
    cDir = os.path.dirname(os.path.abspath(os.sys.argv[0]))

    # File IO names
    data_input_name = 'pure_ou.json'
    # to test obsolete_terms
    #data_input_name = 'pure_ou_two_deletions.json' 
    output_file_name = 'abbreviations'

    # These need to be defined and passed into the module methods
    expressions = ['Department', 'Research Institute', 'Faculty']
    searchkey = 'term'

    # get and initialise
    orgdata, output_data, prev_abbr_list, obsolete_terms = get_data(data_input_name, cDir, expressions)
    

    # find and acronize
    make_acronymns(
        orgdata, output_data, expressions, searchkey, custom_repl, custom_ignr, prev_abbr_list, obsolete_terms, faculty_repl_set, 'vu'
    )

    # check for obsolete terms
    obsolete_terms_new = check_for_obsolete(output_data, prev_abbr_list, obsolete_terms)
    print("Need to so something with Obsolete_terms")
    print(obsolete_terms)
    print(obsolete_terms_new)
    #if len(obsolete_terms) > 0:
        #raise(RuntimeWarning)    

    # write data
    final_output_data = write_data(output_file_name, output_data, expressions, output_lowercase=True)
    
    pprint.pprint(final_output_data)


