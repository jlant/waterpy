Changelog
=========


Version 0.1.0
-------------
2019-05-09
----------
- Change from one parameter file to two parameter files, where one 
  file is specific for the entire basin (parameters_basin.csv) and 
  the other file is specific for the land type (parameters_forest.csv,
  parameters_agriculture.csv, parameters_developed.csv).

2019-05-06
----------
- Add flow duration curves to output.

2019-05-03
----------
- Add pet calibration coefficient (KPEC) to parameters file
  and update pet_hamon calculation to use the user-specified value.

2019-05-03
----------
- Add SCS runoff curve number calculation to hydrocals.py

2019-04-29
----------
- Add new snow melt routine with the addition of snow water 
  equivalence, and add all snow melt related parameters to output.

- Add channel routing option to model config file.

2019-04-26
----------
- Add new transmissivity calculation using methodology from a 
  pmodel by Leon Kauffman (USGS) called KyTopmodel.

- Add new parameters to parameters file with associated checks
  w parameters added include: wilting_point_fraction,
  tion, saturated_hydraulic_conductivity_multiplier

- Change root_zone_storage - root_zone_storage_max to 
                      root_zone_storage + root_zone_storage_max
  This is the Robert Hudson fix to Kentucky version of Topmodel.  Occurs within
  the conditional of root_zone_storage > root_zone_storage_max

- Change initialization of root_zone_storage by adding a
  multiplication factor of 0.5 which is applied to the root_zone_storage_max.

- Add check on initial flow, if flow_initial < 0.1, set to 0.1.

- Set the soil depth of the roots to equal the soil depth of the
  AB horizon, instead of having the soil depth of the roots set to 1 meter. 


Version 0.0.1
-------------

2019-04-26
----------
- initial Dave Wolock version is implemented in this version. 


