# testi18n

A sample program to learn and test the I18N python library, using babel with integration with Distutils/Setuptools

Prerequirements:

 - [Babel]

```bash
pip install babel
```

## A typical workflow

- Prepare your program to take into account I18N (see source file as an example)

- extract the translatable objects to generate the portable objects template:

```bash
python setup.py extract_messages
```

- Prepare the portable object for a new language starting from template:

```
python ./setup.py init_catalog --locale <language>
```

- Compile the portable object files:

   - Single language:
```bash
python setup.py compile_catalog --locale <language>
```

   - All languages:
```bash
python setup.py compile_catalog
```


## First run of this demo

Portable object for US english and italian already available.

 - Compile the portable object files for the available languages:

```bash
python setup.py compile_catalog --locale en_US
python setup.py compile_catalog --locale it_IT
```

 - Run the program:

```bash
python testi18n/testi18n.py
```

## Add translatable object

If the source files are modified and strings are added or modified, the template can be updated with the usual extract command:

```bash
python setup.py extract_messages
```

After this the existing portable object files can be updated using the update command:

```bash
python ./setup.py update_catalog
```

After this the `po` files shall be updated to translate the new strings (fuzzy translations are provided).



[Babel]: http://babel.pocoo.org/en/latest/

## TODO

- To understand if there is a better way to update language for classes or subpackages (see comments in `trclass.py`).
