Description
===========

A set of modules used for working with EEG event file data. Can load, export and manipulate the data (ready for reuse in EEG analysis software).

Details
-------

Currently can be used for BESA and Neuroscan files
The BESA file handling assumes a specific order of columns and ignores a start marker, future versions will more fully support the specification found at: http://wiki.besa.de/index.php?title=Event\_File\_Format#Event\_Codes

## Updates

Uses file type specific classes to make interacting with individual events easier. Can now modify codes etc directly rather than using `mod_code` which is deprecated and will be removed in a future version.

### BUGFIXES & FEATURES

#### v0.3.5

* Neuroscan events with floats now output time columns with same precision that was read

#### v0.3.4

* Fix bug where header in Neuroscan2 file caused crash

#### v0.3.3

* Code changes were not saved as event.order stored only original values, not references

#### v0.3.2

* Last update actually implemented float/int handling for BESA, this time we implement it for Neuroscan

#### v0.3.1

* Neuroscan time format can be int(millisecond) or float(second), try both

#### v0.3.0

* New internal representation of individual events
* Tests updated for new version
* Event elements that make sense to be represented as ints/floats will be exposed as such. *Note* this may break existing code that expects everything as a string.

#### v0.2.3

* Added a suite of unittests
* Removed unreachable code and various small bugfixes

#### v0.2.2

* Code replacement not working due to immutable namedtuple use, use \_replace method for now

#### v0.2.1

* TypeError fixed, was not parsing lines correctly
