"""Test Topmodel class."""

import numpy as np

from waterpy.topmodel import Topmodel


def test_topmodel_init(parameters,
                       timeseries,
                       twi,
                       twi_weighted_mean):
    """Test Topmodel class initialization"""

    # Initialize Topmodel
    topmodel = Topmodel(
        scaling_parameter=parameters["scaling_parameter"],
        saturated_hydraulic_conductivity=(
            parameters["saturated_hydraulic_conductivity"]
        ),
        saturated_hydraulic_conductivity_multiplier=(
            parameters["saturated_hydraulic_conductivity_multiplier"]
        ),
        macropore_fraction=parameters["macropore_fraction"],
        soil_depth_total=parameters["soil_depth_total"],
        soil_depth_ab_horizon=parameters["soil_depth_ab_horizon"],
        field_capacity_fraction=parameters["field_capacity_fraction"],
        porosity_fraction=parameters["porosity_fraction"],
        wilting_point_fraction=parameters["wilting_point_fraction"],
        latitude=parameters["latitude"],
        basin_area_total=parameters["basin_area_total"],
        impervious_area_fraction=parameters["impervious_area_fraction"],
        twi_values=twi["twi"].values,
        twi_saturated_areas=twi["proportion"].values,
        twi_mean=twi_weighted_mean,
        precip_available=timeseries["precip_minus_pet"].values,
        flow_initial=1,
        timestep_daily_fraction=1
    )

    assert(topmodel.scaling_parameter ==
           parameters["scaling_parameter"])
    assert(topmodel.saturated_hydraulic_conductivity ==
           parameters["saturated_hydraulic_conductivity"])
    assert(topmodel.saturated_hydraulic_conductivity_multiplier ==
           parameters["saturated_hydraulic_conductivity_multiplier"])
    assert(topmodel.macropore_fraction ==
           parameters["macropore_fraction"])
    assert(topmodel.soil_depth_total ==
           parameters["soil_depth_total"])
    assert(topmodel.soil_depth_ab_horizon ==
           parameters["soil_depth_ab_horizon"])
    assert(topmodel.field_capacity_fraction ==
           parameters["field_capacity_fraction"])
    assert(topmodel.porosity_fraction ==
           parameters["porosity_fraction"])
    assert(topmodel.wilting_point_fraction ==
           parameters["wilting_point_fraction"])
    assert(topmodel.latitude ==
           parameters["latitude"])
    assert(topmodel.basin_area_total ==
           parameters["basin_area_total"])
    assert(topmodel.impervious_area_fraction ==
           parameters["impervious_area_fraction"])
    np.testing.assert_allclose(topmodel.twi_values,
                               twi["twi"].values)
    np.testing.assert_allclose(topmodel.twi_saturated_areas,
                               twi["proportion"].values)
    assert(topmodel.twi_mean ==
           twi_weighted_mean)
    np.testing.assert_allclose(topmodel.precip_available,
                               timeseries["precip_minus_pet"].values)
    assert(topmodel.flow_initial == 1)
    assert(topmodel.soil_depth_roots == topmodel.soil_depth_ab_horizon)
    assert(topmodel.timestep_daily_fraction == 1)


def test_topmodel_run(parameters,
                      timeseries,
                      twi,
                      twi_weighted_mean):
    """Test Topmodel run with input data from Dave Wolock's Topmodel version.
    Note:
        Just checking that model runs here.  With changes to the original
        Topmodel version, there is no direct test data yet to check with.
        Can inspect the run if need be here by setting a breakpoint and/or
        printing the topmodel object results.
    """

    # Initialize Topmodel
    topmodel = Topmodel(
        scaling_parameter=parameters["scaling_parameter"],
        saturated_hydraulic_conductivity=(
            parameters["saturated_hydraulic_conductivity"]
        ),
        saturated_hydraulic_conductivity_multiplier=(
            parameters["saturated_hydraulic_conductivity_multiplier"]
        ),
        macropore_fraction=parameters["macropore_fraction"],
        soil_depth_total=parameters["soil_depth_total"],
        soil_depth_ab_horizon=parameters["soil_depth_ab_horizon"],
        field_capacity_fraction=parameters["field_capacity_fraction"],
        porosity_fraction=parameters["porosity_fraction"],
        wilting_point_fraction=parameters["wilting_point_fraction"],
        latitude=parameters["latitude"],
        basin_area_total=parameters["basin_area_total"],
        impervious_area_fraction=parameters["impervious_area_fraction"],
        twi_values=twi["twi"].values,
        twi_saturated_areas=twi["proportion"].values,
        twi_mean=twi_weighted_mean,
        precip_available=timeseries["precip_minus_pet"].values,
        flow_initial=1,
        timestep_daily_fraction=1
    )

    topmodel.run()
