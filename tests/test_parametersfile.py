"""Tests for parametersfile module."""

from io import StringIO
import pytest

from waterpy.exceptions import (ParametersFileErrorInvalidHeader,
                                ParametersFileErrorInvalidScalingParameter,
                                ParametersFileErrorInvalidLatitude,
                                ParametersFileErrorInvalidSoilDepthTotal,
                                ParametersFileErrorInvalidSoilDepthAB,
                                ParametersFileErrorInvalidFieldCapacity,
                                ParametersFileErrorInvalidMacropore,
                                ParametersFileErrorInvalidImperviousArea,
                                ParametersFileErrorInvalidFieldCapacityWiltingPoint,
                                ParametersFileErrorInvalidFieldCapacityPorosity)
from waterpy import parametersfile


def test_parameters_file_read_in(parameters_file):
    expected = {
        "scaling_parameter": {
            "value": 10,
            "units": "millimeters",
            "description": "a description",
        },
    }
    filestream = StringIO(parameters_file)
    actual = parametersfile.read_in(filestream)

    assert isinstance(actual["scaling_parameter"]["value"], float)
    assert actual["scaling_parameter"]["value"] == (
           expected["scaling_parameter"]["value"])
    assert actual["scaling_parameter"]["units"] == (
           expected["scaling_parameter"]["units"])
    assert actual["scaling_parameter"]["description"] == (
           expected["scaling_parameter"]["description"])


def test_parameters_file_invalid_header(parameters_file_invalid_header):
    filestream = StringIO(parameters_file_invalid_header)

    with pytest.raises(ParametersFileErrorInvalidHeader) as err:
        parametersfile.read_in(filestream)

    assert "Invalid header" in str(err.value)


def test_parameters_file_invalid_scaling_parameter():
    invalid_value = 0
    with pytest.raises(ParametersFileErrorInvalidScalingParameter) as err:
        parametersfile.check_scaling_parameter(invalid_value)

    assert "Invalid scaling parameter" in str(err.value)


def test_parameters_file_invalid_latitude():
    invalid_value = -1
    with pytest.raises(ParametersFileErrorInvalidLatitude) as err:
        parametersfile.check_latitude(invalid_value)

    assert "Invalid latitude" in str(err.value)


def test_parameters_file_invalid_soil_depth_total():
    invalid_value = 0
    with pytest.raises(ParametersFileErrorInvalidSoilDepthTotal) as err:
        parametersfile.check_soil_depth_total(invalid_value)

    assert "Invalid soil depth total" in str(err.value)


def test_parameters_file_invalid_soil_depth_ab_horizon_lt_zero():
    invalid_value = 0
    soil_depth_total = 1
    with pytest.raises(ParametersFileErrorInvalidSoilDepthAB) as err:
        parametersfile.check_soil_depth_ab_horizon(invalid_value, soil_depth_total)

    assert "Invalid soil depth ab horizon" in str(err.value)


def test_parameters_file_invalid_soil_depth_ab_horizon_gt_soil_depth_total():
    invalid_value = 10
    soil_depth_total = 1
    with pytest.raises(ParametersFileErrorInvalidSoilDepthAB) as err:
        parametersfile.check_soil_depth_ab_horizon(invalid_value, soil_depth_total)

    assert "Invalid soil depth ab horizon" in str(err.value)


def test_parameters_file_invalid_field_capacity_fraction():
    invalid_value = 2
    with pytest.raises(ParametersFileErrorInvalidFieldCapacity) as err:
        parametersfile.check_field_capacity(invalid_value)

    assert "Invalid field capacity" in str(err.value)


def test_parameters_file_invalid_macropore_fraction():
    invalid_value = 2
    with pytest.raises(ParametersFileErrorInvalidMacropore) as err:
        parametersfile.check_macropore(invalid_value)

    assert "Invalid macropore" in str(err.value)


def test_parameters_file_invalid_impervious_area_fraction():
    invalid_value = 2
    with pytest.raises(ParametersFileErrorInvalidImperviousArea) as err:
        parametersfile.check_impervious_area(invalid_value)

    assert "Invalid impervious area" in str(err.value)


def test_parameters_file_invalid_field_capacity_fraction_wilting_point_fraction():
    field_capacity_fraction = 0.2
    invalid_wilting_point_fraction = 0.4
    with pytest.raises(ParametersFileErrorInvalidFieldCapacityWiltingPoint) as err:
        parametersfile.check_field_capacity_wilting_point(field_capacity_fraction,
                                                          invalid_wilting_point_fraction)

    assert "Invalid field capacity or wilting point" in str(err.value)


def test_parameters_file_invalid_field_capacity_fraction_porosity_fraction():
    field_capacity_fraction = 0.5
    invalid_porosity_fraction = 0.2
    with pytest.raises(ParametersFileErrorInvalidFieldCapacityPorosity) as err:
        parametersfile.check_field_capacity_porosity(field_capacity_fraction,
                                                     invalid_porosity_fraction)

    assert "Invalid field capacity or porosity" in str(err.value)
