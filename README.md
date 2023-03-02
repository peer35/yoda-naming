# yoda-naming

scripts to generate Yoda group names using Pure as a data source

## Manual steps
### Export list from Pure

Rename `config.template.py` to `config.py` and set the api key.

Run `python pure_organisationalunits.py`. This will output `pure_ou.json`, which is used for generating the actual
abbreviations, and `pure_list.txt`, a more readable text version for reference.

### Generate abbreviations
Now run `python generate_abbreviations.py` to create the actual list `abbreviations.txt` 

**New** A Google Collab notebook is available for demonstration purposes: https://colab.research.google.com/drive/1ikMDIBbPMxIkiMj8MnWLTmPEgs29a66F?usp=sharing 
this should be viewable by members of the VU.