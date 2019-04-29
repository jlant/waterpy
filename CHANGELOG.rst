Changelog
=========


Version 0.1.0
-------------

2019-04-29
----------
- topmodel.py: Add new snow melt routine with the addition of snow water 
  equivalence, and add all snow melt related parameters to output.

- topmodel.py: Add channel routing option to model config file.

2019-04-26
----------
- topmodel.py: Add new transmissivity calculation using methodology from a 
  version of Topmodel by Leon Kauffman (USGS) called KyTopmodel.

- topmodel.py: Add new parameters to parameters file with associated checks
  and tests. New parameters added include: wilting_point_fraction,
  porosity_fraction, saturated_hydraulic_conductivity_multiplier

- topmodel.py: Change root_zone_storage - root_zone_storage_max to 
                      root_zone_storage + root_zone_storage_max
  This is the Robert Hudson fix to Kentucky version of Topmodel.  Occurs within
  the conditional of root_zone_storage > root_zone_storage_max

- topmodel.py: Change initialization of root_zone_storage by adding a
  multiplication factor of 0.5 which is applied to the root_zone_storage_max.

- topmodel.py: Add check on initial flow, if flow_initial < 0.1, set to 0.1.

- topmodel.py: Set the soil depth of the roots to equal the soil depth of the
  AB horizon, instead of having the soil depth of the roots set to 1 meter. 


Version 0.1.0
-------------

2019-04-26
----------
- topmodel.py: initial Dave Wolock version is implemented in this version. 


