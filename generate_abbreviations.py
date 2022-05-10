"""
Title:
Author: Brett G. Olivier

Usage:

(C) Brett G. Olivier, VU Amsterdam, 2022. Licenced for use under the GNU GPL 3.0

# These need to be defined and passed into the module methods

expressions = ['Department', 'Research Institute']
searchkey = 'term'

output_data = {'Department' : {},
        'Research Institute' : {},
        'Acronymns' : [],
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
    
    if os.path.exists(os.path.join(cDir, '_abbr_list_previous.json')):
        with open(os.path.join(cDir, '_abbr_list_previous.json'), 'r') as F:
            prev_abbr_list = tuple(json.load(F))
    else:
        prev_abbr_list = ()

    output_data = {'Acronymns': []}
    for exp in expressions:
        output_data[exp] = {}

    return orgdata, output_data, prev_abbr_list


def make_acronymns(branch, out, expr, key, acro_repl, key_ignore, prev_abbr_list):
    for e in branch:
        if branch['name'] not in key_ignore and e == key and branch[key] in expr:
            acro = acronize(branch['name'], acro_repl)
            if acro in out['Acronymns']:
                print('Duplicate acronym', acro)
                # out['Acronymns'].insert(0, (acro, branch['name']))
                acro = acronize(branch['name'], acro_repl, duplicate=True)
            if acro.lower() not in prev_abbr_list:
                print('New Acronymn add:', acro)
                
            out['Acronymns'].append(acro)
            out[branch[key]][branch['name']] = acro
        elif e == 'children':
            for c in branch['children']:
                make_acronymns(c, out, expr, key, acro_repl, key_ignore, prev_abbr_list)


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
            raise (RuntimeWarning(), words)
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
        
    # stored the last list of abbreviations to detect new ones in each run
    with open('_abbr_list_previous.json','w') as F:
        json.dump([a.lower() for a in sorted(output_data['Acronymns'])], F)

    pprint.pprint(output_data)

    # for the google sheet or however we need for a form.
    with open(output_file_name + '.txt', 'w') as F:
        for expr in expressions:
            F.write(f'# {expr}\n')
            for dep in sorted(output_data[expr].keys()):
                F.write(f'{dep} [{output_data[expr][dep]}]\n')
    return


if __name__ == '__main__':
    import os
    from custom_replacements import custom_repl_set1 as custom_repl
    from custom_replacements import custom_ignore_set1 as custom_ignr
    cDir = os.path.dirname(os.path.abspath(os.sys.argv[0]))


    # File IO names
    data_input_name = 'pure_ou.json'
    output_file_name = 'abbreviations'

    # These need to be defined and passed into the module methods
    expressions = ['Department', 'Research Institute']
    searchkey = 'term'

    # get and initialise
    orgdata, output_data, prev_abbr_list = get_data(data_input_name, cDir, expressions)
    

    # find and acronize
    make_acronymns(
        orgdata, output_data, expressions, searchkey, custom_repl, custom_ignr, prev_abbr_list
    )


    # write data
    write_data(output_file_name, output_data, expressions, output_lowercase=True)


