# yoda-naming

scripts to generate Yoda group names using Pure as a data source

## Automatic updates 

## Manual steps
### Export list from Pure

Rename `config.template.py` to `config.py` and set correct credentials.

Run `python pure_organisationalunits.py`. This will output `pure_ou.json`, which is used for generating the actual
abbreviations, and `pure_list.txt`, a human-readable text version for reference.

### Generate abbreviations
Now run `python generate_abbreviations.py` to create the actual list `abbreviations.txt` 