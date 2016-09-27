from __future__ import print_function
import os
import textstat

print(textstat.textstatistics())

T = textstat.textstatistics()

files = {'Trump': 'DONALD_TRUMP_text',
         'Clinton': 'HILLARY_CLINTON_text',
         'Holt': 'LESTER_HOLT_text'}

functions = {'Flesch Reading Ease': T.flesch_reading_ease,
             'Flesch-Kincaid Grade Level': T.flesch_kincaid_grade,
             'Fog Scale': T.gunning_fog,
             'SMOG Index': T.smog_index,
             'ARI (Automated Readability Index)': T.automated_readability_index,
             'Coleman-Liau': T.coleman_liau_index,
             'Linsear Write Formula': T.linsear_write_formula,
             'Dale-Chall Readability': T.dale_chall_readability_score}


file_prefix = 'text_samples'

for file in files:
    print('\n{}\n'.format(file))
    filename = os.path.join(file_prefix, files[file])
    with open(filename) as f:
        content = f.read()
    for function in functions:
        print('  {}: {}'.format(function, functions[function](content)))
    print('\n  Readability consensus:', T.text_standard(content))
