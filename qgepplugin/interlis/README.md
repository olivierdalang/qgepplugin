# ili2QWAT / ili2QGEP prototype

## General usage
```
python -m interlis [-h]
                   [--import_xtf IMPORT_XTF | --export_xtf EXPORT_XTF | --gen_tpl]
                   [--force_recreate]
                   {qgep,qwat}

positional arguments:
  {qgep,qwat}               datamodel

optional arguments:
  -h, --help                show this help message and exit
  --import_xtf IMPORT_XTF   input file
  --export_xtf EXPORT_XTF   output file
  --gen_tpl                 generate code templates
  --force_recreate          drops schema and reruns ili2pg importschema
```

## Dev

Import scripts templates can be generated using `python -m interlis qwat --gen_tpl; python -m interlis qgep --gen_tpl`. This uses the mapping defined in `datamodels/mapping.py` to auto-generate import script templates, that can then be manually merged into the existing scripts.

## Use cases

### A. import Wincan-generated xtf data into QGEP

We recieve data from a TV inspection company as a Wincan exported .xtf file. We want this data loaded into QGEP.

```
python -m interlis --force_recreate --import_xtf interlis\data\test_without_abwasserbauwerkref.xtf qgep
```