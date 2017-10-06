# Subject Conversion Data Analysis & Transformation

This is a jupyter notebook working through data analysis on DOMM's subject conversion project. Mainly uses `pandas` and some bash commands, with the desired output of certain files that will serve as input for the subject conversion process code  

## Workflow
The following instructions taken from the [Subject Conversion Google Doc](https://docs.google.com/document/d/12HOMth8ylD20bcEeVYb336NaVxSwaip58n0IhXUWFMs/edit#)

### How to make desired input file 'New_authorities_list'
1. Download `combined_subject_conversion_file.xslx` from [dams-metadata repo](https://github.com/ucsdlib/dams-metadata/blob/master/Subject-conversion/combined_subject_conversion_file.xlsx)
2. Remove all rows from the dataset containing `complexSubject` types  
3. De-dupe (i.e. remove all incidence of rows after the first occurrence) all rows based on unique values of `updated_label` column
4. Create a new column, `external_authority_URI`, that contains _only_ 1 URI, that first filters out/ignores all "local" type values, then fill in values taken mostly from the `clustering id` column (**TODO** confirm this is reliable logic)
5. Create a new column, `other_URI`, that concatenates (and is de-duped to `clustering id` values) all the "URI" column values, separated by ` | ` (`FAST_URI`, `LoC URI`, `AAT_URI`, `VIAF_URI`)
6. Create a new column, `variant_label`, that contains unique values from `old_label` (de-duped against `updated_label` column values). **TODO** Investigate level of effort to concatenate all reconciled labels, de-deuped against both `old label` and `updated_label` column values)
7. A key to the main data table. This is currently being hashed out, but if this key column is added to the original `combined_subject_conversion_file.xslx`, can just preserve the key values     

### Desired input file 'label_updates'
1.
