"""Test Topmodel class."""

import numpy as np

from waterpy.topmodel import Topmodel


def test_topmodel_init(parameters_wolock,
                       timeseries_wolock,
                       twi_wolock,
                       twi_weighted_mean_wolock):
    """Test Topmodel class initialization"""

    # Initialize Topmodel
    topmodel = Topmodel(
        scaling_parameter=parameters_wolock["scaling_parameter"],
        saturated_hydraulic_conductivity=(
            parameters_wolock["saturated_hydraulic_conductivity"]
        ),
        macropore_fraction=parameters_wolock["macropore_fraction"],
        soil_depth_total=parameters_wolock["soil_depth_total"],
        soil_depth_ab_horizon=parameters_wolock["soil_depth_ab_horizon"],
        field_capacity_fraction=parameters_wolock["field_capacity_fraction"],
        latitude=parameters_wolock["latitude"],
        basin_area_total=parameters_wolock["basin_area_total"],
        impervious_area_fraction=parameters_wolock["impervious_area_fraction"],
        twi_values=twi_wolock["twi"].values,
        twi_saturated_areas=twi_wolock["proportion"].values,
        twi_mean=twi_weighted_mean_wolock,
        precip_available=timeseries_wolock["precip_minus_pet"].values,
        flow_initial=1,
        timestep_daily_fraction=1
    )

    assert(topmodel.scaling_parameter ==
           parameters_wolock["scaling_parameter"])
    assert(topmodel.saturated_hydraulic_conductivity ==
           parameters_wolock["saturated_hydraulic_conductivity"])
    assert(topmodel.macropore_fraction ==
           parameters_wolock["macropore_fraction"])
    assert(topmodel.soil_depth_total ==
           parameters_wolock["soil_depth_total"])
    assert(topmodel.soil_depth_ab_horizon ==
           parameters_wolock["soil_depth_ab_horizon"])
    assert(topmodel.field_capacity_fraction ==
           parameters_wolock["field_capacity_fraction"])
    assert(topmodel.latitude ==
           parameters_wolock["latitude"])
    assert(topmodel.basin_area_total ==
           parameters_wolock["basin_area_total"])
    assert(topmodel.impervious_area_fraction ==
           parameters_wolock["impervious_area_fraction"])
    np.testing.assert_allclose(topmodel.twi_values,
                               twi_wolock["twi"].values)
    np.testing.assert_allclose(topmodel.twi_saturated_areas,
                               twi_wolock["proportion"].values)
    assert(topmodel.twi_mean ==
           twi_weighted_mean_wolock)
    np.testing.assert_allclose(topmodel.precip_available,
                               timeseries_wolock["precip_minus_pet"].values)
    assert(topmodel.flow_initial == 1)
    assert(topmodel.soil_depth_roots == topmodel.soil_depth_ab_horizon)
    assert(topmodel.timestep_daily_fraction == 1)


def test_topmodel_run(parameters_wolock,
                      timeseries_wolock,
                      twi_wolock,
                      twi_weighted_mean_wolock):
    """Test Topmodel run with input data from Dave Wolock's Topmodel version.
    Note:
        Just checking that model runs here.  With changes to the original
        Topmodel version, there is no direct test data yet to check with.
        Can inspect the run if need be here by setting a breakpoint and/or
        printing the topmodel object results.
    """

    # Initialize Topmodel
    topmodel = Topmodel(
        scaling_parameter=parameters_wolock["scaling_parameter"],
        saturated_hydraulic_conductivity=(
            parameters_wolock["saturated_hydraulic_conductivity"]
        ),
        macropore_fraction=parameters_wolock["macropore_fraction"],
        soil_depth_total=parameters_wolock["soil_depth_total"],
        soil_depth_ab_horizon=parameters_wolock["soil_depth_ab_horizon"],
        field_capacity_fraction=parameters_wolock["field_capacity_fraction"],
        latitude=parameters_wolock["latitude"],
        basin_area_total=parameters_wolock["basin_area_total"],
        impervious_area_fraction=parameters_wolock["impervious_area_fraction"],
        twi_values=twi_wolock["twi"].values,
        twi_saturated_areas=twi_wolock["proportion"].values,
        twi_mean=twi_weighted_mean_wolock,
        precip_available=timeseries_wolock["precip_minus_pet"].values,
        flow_initial=1,
        timestep_daily_fraction=1,
    )

    topmodel.run()
