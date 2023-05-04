# ckanext-crc1368

This is the CKAN extension for the project CRC (SFB) 1368. The extensions includes the plugins that are implemented specifically for CRC1368. 


## Requirements

Compatibility with core CKAN versions:

| CKAN version    | Compatible?   |
| --------------- | ------------- |
| 2.8 and earlier | not tested    |
| 2.9             | Yes    |


## Plugins
TBA


## Hint: 
TBA



## Installation

To install ckanext-crc1368:

1. Activate your CKAN virtual environment, for example:

          . /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

          git clone git@github.com:TIBHannover/ckanext-crc1368.git
          cd ckanext-crc1368
          pip install -e .
          pip install -r requirements.txt

3. Add the needed plugin name(s) to **ckan.ini** (plugin names are mentioned in the last section)

4. (For some plugins) if the plugin has migration, ckan migration is needed. Look at: https://docs.ckan.org/en/2.9/extensions/best-practices.html#use-migrations-when-introducing-new-models


5. Restart CKAN and the web server. 

          sudo service supervisor reload
          sudo service nginx reload



## Config settings

TBA


## Tests
TBA


## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
