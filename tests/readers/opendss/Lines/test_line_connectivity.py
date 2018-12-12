# -*- coding: utf-8 -*-

"""
test_line_connectivity.py
----------------------------------

Tests for checking the line connectivity.
"""
import logging
import os

import six

import tempfile
import pytest as pt
import json

logger = logging.getLogger(__name__)

current_directory = os.path.realpath(os.path.dirname(__file__))


def test_line_connectivity():
    from ditto.store import Store
    from ditto.readers.opendss.read import Reader

    # test on the test_line_connectivity.dss
    m = Store()
    r = Reader(
        master_file=os.path.join(current_directory, "test_line_connectivity.dss")
    )
    r.parse(m)
    m.set_names()

    # Reading OpenDSS default values
    with open(
        os.path.join(current_directory, "../../../../docs/OpenDSS/Default_Values.json")
    ) as f:
        json_data = json.load(f)

    # Line1 connects sourcebus to bus1 and should have 4 wires: A, B, C, and N
    #    assert len(m["line1"].wires) == 4 # Number of wires # Neutral wire is not counted. TBD
    #    Phases of the different wires
    #    assert set([w.phase for w in m["line1"].wires]) == set(["A", "B", "C", "N"]) # Neutral wire is not counted. TBD
    assert m["line1"].name == "line1"
    assert m["line1"].nominal_voltage == float(4.16) * 10 ** 3
    assert m["line1"].line_type == "underground"
    assert m["line1"].length == 100
    assert m["line1"].from_element == "sourcebus"
    assert m["line1"].to_element == "bus1"
    assert m["line1"].is_fuse is None
    assert m["line1"].is_switch is None
    #    assert m["line1"].is_banked is None # Not implemented for now
    assert m["line1"].faultrate == json_data["OpenDSS"]["faultrate"]
    #    assert m["line1"].positions is None  # Not implemented for now
    assert m["line1"].impedance_matrix == [
        [(0.09813333 + 0.2153j), (0.04013333 + 0.0947j), (0.04013333 + 0.0947j)],
        [(0.04013333 + 0.0947j), (0.09813333 + 0.2153j), (0.04013333 + 0.0947j)],
        [(0.04013333 + 0.0947j), (0.04013333 + 0.0947j), (0.09813333 + 0.2153j)],
    ]
    assert m["line1"].capacitance_matrix == [
        [(2.8 + 0j), (-0.6 + 0j), (-0.6 + 0j)],
        [(-0.6 + 0j), (2.8 + 0j), (-0.6 + 0j)],
        [(-0.6 + 0j), (-0.6 + 0j), (2.8 + 0j)],
    ]
    # assert m["line1"].substation_name is None  # Not implemented for now
    assert m["line1"].feeder_name == "sourcebus_src"
    assert m["line1"].is_recloser is None
    assert m["line1"].is_breaker is None
    # assert m["line1"].is_sectionalizer is None # Not implemented for now
    assert m["line1"].nameclass == ""
    #    assert m["line1"].is_substation == 0  # Not implemented for now
    #    assert m["line1"].is_network_protector is None  # Not implemented for now

    for w in m["line1"].wires:
        assert w.nameclass == ""
        assert w.X is None
        assert w.Y is None
        assert w.diameter is None
        assert w.gmr is None
        assert w.ampacity == json_data["OpenDSS"]["normamps"]
        assert w.emergency_ampacity == json_data["OpenDSS"]["emergamps"]
        assert w.resistance is None
        assert w.insulation_thickness == 0.0
        #        assert w.is_fuse is None # Needs to be deprecated
        #        assert w.is_switch is None # Needs to be deprecated
        assert w.is_open is None
        #        assert w.interrupting_rating is None # Not implemented for now
        assert w.concentric_neutral_gmr is None
        assert w.concentric_neutral_resistance is None
        assert w.concentric_neutral_diameter is None
        assert w.concentric_neutral_outside_diameter is None
        assert w.concentric_neutral_nstrand is None
        #        assert w.drop == 0 # Needs to be deprecated
        #        assert w.is_recloser is None # Needs to be deprecated
        #        assert w.is_breaker is None # Needs to be deprecated
        #        assert w.is_network_protector is None # Needs to be deprecated
        #        assert w.is_sectionalizer is None # Needs to be deprecated

    # Line2 connects bus1 to bus2 and should have 4 wires: A, B, C, and N
    # assert len(m["line2"].wires) == 4 # Number of wires # Neutral wire is not counted. TBD
    #    Phases of the different wires
    #    assert set([w.phase for w in m["line2"].wires]) == set(["A", "B", "C", "N"]) # Neutral wire is not counted. TBD
    assert m["line2"].name == "line2"
    assert m["line2"].nominal_voltage == float(4.16) * 10 ** 3
    assert m["line2"].line_type == "underground"
    assert m["line2"].length == 200
    assert m["line2"].from_element == "bus1"
    assert m["line2"].to_element == "bus2"
    assert m["line2"].is_fuse is None
    assert m["line2"].is_switch is None
    #    assert m["line2"].is_banked is None # Not implemented for now
    assert m["line2"].faultrate == json_data["OpenDSS"]["faultrate"]
    #    assert m["line2"].positions is None  # Not implemented for now
    assert m["line2"].impedance_matrix == [
        [(0.09813333 + 0.2153j), (0.04013333 + 0.0947j), (0.04013333 + 0.0947j)],
        [(0.04013333 + 0.0947j), (0.09813333 + 0.2153j), (0.04013333 + 0.0947j)],
        [(0.04013333 + 0.0947j), (0.04013333 + 0.0947j), (0.09813333 + 0.2153j)],
    ]
    assert m["line2"].capacitance_matrix == [
        [(2.8 + 0j), (-0.6 + 0j), (-0.6 + 0j)],
        [(-0.6 + 0j), (2.8 + 0j), (-0.6 + 0j)],
        [(-0.6 + 0j), (-0.6 + 0j), (2.8 + 0j)],
    ]
    # assert m["line2"].substation_name is None  # Not implemented for now
    assert m["line2"].feeder_name == "sourcebus_src"
    assert m["line2"].is_recloser is None
    assert m["line2"].is_breaker is None
    # assert m["line2"].is_sectionalizer is None # Not implemented for now
    assert m["line2"].nameclass == ""
    #    assert m["line2"].is_substation == 0  # Not implemented for now
    #    assert m["line2"].is_network_protector is None  # Not implemented for now

    for w in m["line2"].wires:
        assert w.nameclass == ""
        assert w.X is None
        assert w.Y is None
        assert w.diameter is None
        assert w.gmr is None
        assert w.ampacity == json_data["OpenDSS"]["normamps"]
        assert w.emergency_ampacity == json_data["OpenDSS"]["emergamps"]
        assert w.resistance is None
        assert w.insulation_thickness == 0.0
        #        assert w.is_fuse is None # Needs to be deprecated
        #        assert w.is_switch is None # Needs to be deprecated
        assert w.is_open is None
        #        assert w.interrupting_rating is None # Not implemented for now
        assert w.concentric_neutral_gmr is None
        assert w.concentric_neutral_resistance is None
        assert w.concentric_neutral_diameter is None
        assert w.concentric_neutral_outside_diameter is None
        assert w.concentric_neutral_nstrand is None
        #        assert w.drop == 0 # Needs to be deprecated
        #        assert w.is_recloser is None # Needs to be deprecated
        #        assert w.is_breaker is None # Needs to be deprecated
        #        assert w.is_network_protector is None # Needs to be deprecated
        #        assert w.is_sectionalizer is None # Needs to be deprecated

    #  Line3 connects bus2 to bus3 and should have 3 wires: A, B, and N
    # assert len(m["line3"].wires) == 3
    #    Phases of the different wires
    # assert set([w.phase for w in m["line3"].wires]) == set(["A", "C", "N"]) # Neutral wire is not counted. TBD
    assert m["line3"].name == "line3"
    assert m["line3"].nominal_voltage == float(4.16) * 10 ** 3
    assert m["line3"].line_type == "underground"
    assert m["line3"].length == 50
    assert m["line3"].from_element == "bus2"
    assert m["line3"].to_element == "bus3"
    assert m["line3"].is_fuse is None
    assert m["line3"].is_switch is None
    #    assert m["line3"].is_banked is None # Not implemented for now
    assert m["line3"].faultrate == json_data["OpenDSS"]["faultrate"]
    #    assert m["line3"].positions is None  # Not implemented for now
    assert m["line3"].impedance_matrix == [
        [(0.09813333 + 0.2153j), (0.04013333 + 0.0947j)],
        [(0.04013333 + 0.0947j), (0.09813333 + 0.2153j)],
    ]
    assert m["line3"].capacitance_matrix == [
        [(2.8 + 0j), (-0.6 + 0j)],
        [(-0.6 + 0j), (2.8 + 0j)],
    ]
    # assert m["line3"].substation_name is None  # Not implemented for now
    assert m["line3"].feeder_name == "sourcebus_src"
    assert m["line3"].is_recloser is None
    assert m["line3"].is_breaker is None
    # assert m["line3"].is_sectionalizer is None  # Not implemented for now
    assert m["line3"].nameclass == ""
    #    assert m["line3"].is_substation == 0  # Not implemented for now
    #    assert m["line3"].is_network_protector is None  # Not implemented for now

    for w in m["line3"].wires:
        assert w.nameclass == ""
        assert w.X is None
        assert w.Y is None
        assert w.diameter is None
        assert w.gmr is None
        assert w.ampacity == json_data["OpenDSS"]["normamps"]
        assert w.emergency_ampacity == json_data["OpenDSS"]["emergamps"]
        assert w.resistance is None
        assert w.insulation_thickness == 0.0
        #        assert w.is_fuse is None # Needs to be deprecated
        #        assert w.is_switch is None # Needs to be deprecated
        assert w.is_open is None
        #        assert w.interrupting_rating is None # Not implemented for now
        assert w.concentric_neutral_gmr is None
        assert w.concentric_neutral_resistance is None
        assert w.concentric_neutral_diameter is None
        assert w.concentric_neutral_outside_diameter is None
        assert w.concentric_neutral_nstrand is None
        #        assert w.drop == 0 # Needs to be deprecated
        #        assert w.is_recloser is None # Needs to be deprecated
        #        assert w.is_breaker is None # Needs to be deprecated
        #        assert w.is_network_protector is None # Needs to be deprecated
        #        assert w.is_sectionalizer is None # Needs to be deprecated

    #  Line4 connects bus3 to bus4 and should have 2 wires: B, and N
    # assert len(m["line4"].wires) == 2
    #    Phases of the different wires
    # assert set([w.phase for w in m["line4"].wires]) == set(["B", "N"])
    assert m["line4"].name == "line4"
    assert m["line4"].nominal_voltage == float(4.16) * 10 ** 3
    assert m["line4"].line_type == "underground"
    assert m["line4"].length == 25
    assert m["line4"].from_element == "bus3"
    assert m["line4"].to_element == "bus4"
    assert m["line4"].is_fuse is None
    assert m["line4"].is_switch is None
    #    assert m["line4"].is_banked is None # Not implemented for now
    assert m["line4"].faultrate == json_data["OpenDSS"]["faultrate"]
    #    assert m["line4"].positions is None  # Not implemented for now
    assert m["line4"].impedance_matrix == [[(0.058 + 0.1206j)]]
    assert m["line4"].capacitance_matrix == [[(3.4 + 0j)]]
    # assert m["line4"].substation_name is None  # Not implemented for now
    assert m["line4"].feeder_name == "sourcebus_src"
    assert m["line4"].is_recloser is None
    assert m["line4"].is_breaker is None
    # assert m["line4"].is_sectionalizer is None  # Not implemented for now
    assert m["line4"].nameclass == ""
    #    assert m["line4"].is_substation == 0  # Not implemented for now
    #    assert m["line4"].is_network_protector is None  # Not implemented for now

    for w in m["line4"].wires:
        assert w.nameclass == ""
        assert w.X is None
        assert w.Y is None
        assert w.diameter is None
        assert w.gmr is None
        assert w.ampacity == json_data["OpenDSS"]["normamps"]
        assert w.emergency_ampacity == json_data["OpenDSS"]["emergamps"]
        assert w.resistance is None
        assert w.insulation_thickness == 0.0
        #        assert w.is_fuse is None # Needs to be deprecated
        #        assert w.is_switch is None # Needs to be deprecated
        assert w.is_open is None
        #        assert w.interrupting_rating is None # Not implemented for now
        assert w.concentric_neutral_gmr is None
        assert w.concentric_neutral_resistance is None
        assert w.concentric_neutral_diameter is None
        assert w.concentric_neutral_outside_diameter is None
        assert w.concentric_neutral_nstrand is None
        #        assert w.drop == 0 # Needs to be deprecated
        #        assert w.is_recloser is None # Needs to be deprecated
        #        assert w.is_breaker is None # Needs to be deprecated
        #        assert w.is_network_protector is None # Needs to be deprecated
        #        assert w.is_sectionalizer is None # Needs to be deprecated

    #  Line5 connects bus1 to bus5 and should have 3 wires: A, C, and N
    # assert len(m["line5"].wires) == 3 # Number of wires # Neutral wire is not counted. TBD
    #    Phases of the different wires
    #    assert set([w.phase for w in m["line5"].wires]) == set(["A", "B", "C", "N"]) # Neutral wire is not counted. TBD
    assert m["line5"].name == "line5"
    assert m["line5"].nominal_voltage == float(4.16) * 10 ** 3
    assert m["line5"].line_type == "underground"
    assert m["line5"].length == float(1500 * 0.3048)  # units = ft
    assert m["line5"].from_element == "bus1"
    assert m["line5"].to_element == "bus5"
    assert m["line5"].is_fuse is None
    assert m["line5"].is_switch is None
    #    assert m["line5"].is_banked is None # Not implemented for now
    assert m["line5"].faultrate == json_data["OpenDSS"]["faultrate"]
    #    assert m["line5"].positions is None  # Not implemented for now
    assert m["line5"].impedance_matrix == [
        [
            (0.3219597440944882 + 0.7063648293963254j),
            (0.13167103018372703 + 0.3106955380577428j),
        ],
        [
            (0.13167103018372703 + 0.3106955380577428j),
            (0.3219597440944882 + 0.7063648293963254j),
        ],
    ]  # units = ft
    assert m["line5"].capacitance_matrix == [
        [(9.186351706036744 + 0j), (-1.9685039370078738 + 0j)],
        [(-1.9685039370078738 + 0j), (9.186351706036744 + 0j)],
    ]  # units = ft
    # assert m["line5"].substation_name is None  # Not implemented for now
    assert m["line5"].feeder_name == "sourcebus_src"
    assert m["line5"].is_recloser is None
    assert m["line5"].is_breaker is None
    # assert m["line5"].is_sectionalizer is None  # Not implemented for now
    assert m["line5"].nameclass == ""
    #    assert m["line5"].is_substation == 0  # Not implemented for now
    #    assert m["line5"].is_network_protector is None  # Not implemented for now

    for w in m["line5"].wires:
        assert w.nameclass == ""
        assert w.X is None
        assert w.Y is None
        assert w.diameter is None
        assert w.gmr is None
        assert w.ampacity == json_data["OpenDSS"]["normamps"]
        assert w.emergency_ampacity == json_data["OpenDSS"]["emergamps"]
        assert w.resistance is None
        assert w.insulation_thickness == 0.0
        #        assert w.is_fuse is None # Needs to be deprecated
        #        assert w.is_switch is None # Needs to be deprecated
        assert w.is_open is None
        #        assert w.interrupting_rating is None # Not implemented for now
        assert w.concentric_neutral_gmr is None
        assert w.concentric_neutral_resistance is None
        assert w.concentric_neutral_diameter is None
        assert w.concentric_neutral_outside_diameter is None
        assert w.concentric_neutral_nstrand is None
        #        assert w.drop == 0 # Needs to be deprecated
        #        assert w.is_recloser is None # Needs to be deprecated
        #        assert w.is_breaker is None # Needs to be deprecated
        #        assert w.is_network_protector is None # Needs to be deprecated
        #        assert w.is_sectionalizer is None # Needs to be deprecated

    #  Line6 connects bus4 to bus6 and should have 3 wires: B, C, and N
    # assert len(m["line6"].wires) == 3 # Number of wires # Neutral wire is not counted. TBD
    #    Phases of the different wires
    #    assert set([w.phase for w in m["line6"].wires]) == set(["A", "B", "C", "N"]) # Neutral wire is not counted. TBD
    assert m["line6"].name == "line6"
    assert m["line6"].nominal_voltage == float(4.16) * 10 ** 3
    assert m["line6"].line_type == "underground"
    assert m["line6"].length == 110
    assert m["line6"].from_element == "bus4"
    assert m["line6"].to_element == "bus6"
    assert m["line6"].is_fuse is None
    assert m["line6"].is_switch is None
    #    assert m["line6"].is_banked is None # Not implemented for now
    assert m["line6"].faultrate == json_data["OpenDSS"]["faultrate"]
    #    assert m["line6"].positions is None  # Not implemented for now
    assert m["line6"].impedance_matrix == [
        [(0.09813333 + 0.2153j), (0.04013333 + 0.0947j)],
        [(0.04013333 + 0.0947j), (0.09813333 + 0.2153j)],
    ]
    assert m["line6"].capacitance_matrix == [
        [(2.8 + 0j), (-0.6 + 0j)],
        [(-0.6 + 0j), (2.8 + 0j)],
    ]
    # assert m["line6"].substation_name is None  # Not implemented for now
    assert m["line6"].feeder_name == "sourcebus_src"
    assert m["line6"].is_recloser is None
    assert m["line6"].is_breaker is None
    # assert m["line6"].is_sectionalizer is None # Not implemented for now
    assert m["line6"].nameclass == ""
    #    assert m["line6"].is_substation == 0  # Not implemented for now
    #    assert m["line6"].is_network_protector is None  # Not implemented for now

    for w in m["line6"].wires:
        assert w.nameclass == ""
        assert w.X is None
        assert w.Y is None
        assert w.diameter is None
        assert w.gmr is None
        assert w.ampacity == json_data["OpenDSS"]["normamps"]
        assert w.emergency_ampacity == json_data["OpenDSS"]["emergamps"]
        assert w.resistance is None
        assert w.insulation_thickness == 0.0
        #        assert w.is_fuse is None # Needs to be deprecated
        #        assert w.is_switch is None # Needs to be deprecated
        assert w.is_open is None
        #        assert w.interrupting_rating is None # Not implemented for now
        assert w.concentric_neutral_gmr is None
        assert w.concentric_neutral_resistance is None
        assert w.concentric_neutral_diameter is None
        assert w.concentric_neutral_outside_diameter is None
        assert w.concentric_neutral_nstrand is None
        #        assert w.drop == 0 # Needs to be deprecated
        #        assert w.is_recloser is None # Needs to be deprecated
        #        assert w.is_breaker is None # Needs to be deprecated
        #        assert w.is_network_protector is None # Needs to be deprecated
        #        assert w.is_sectionalizer is None # Needs to be deprecated

    #  Line7 should raise some error in DiTTo since it only supports 1, 2, 3, and 0.
    # assert len(m["line7"].wires) == 3 # Number of wires # Neutral wire is not counted. TBD
    #    Phases of the different wires
    #    assert set([w.phase for w in m["line7"].wires]) == set(["A", "B", "C", "N"]) # Neutral wire is not counted. TBD
    assert m["line7"].name == "line7"
    assert m["line7"].nominal_voltage == float(4.16) * 10 ** 3
    assert m["line7"].line_type == "underground"
    assert m["line7"].length == 100
    assert m["line7"].from_element == "bus1"
    assert m["line7"].to_element == "bus2"
    assert m["line7"].is_fuse is None
    assert m["line7"].is_switch is None
    #    assert m["line7"].is_banked is None # Not implemented for now
    assert m["line7"].faultrate == json_data["OpenDSS"]["faultrate"]
    #    assert m["line7"].positions is None  # Not implemented for now
    assert m["line7"].impedance_matrix == [
        [(0.09813333 + 0.2153j), (0.04013333 + 0.0947j)],
        [(0.04013333 + 0.0947j), (0.09813333 + 0.2153j)],
    ]
    assert m["line7"].capacitance_matrix == [
        [(2.8 + 0j), (-0.6 + 0j)],
        [(-0.6 + 0j), (2.8 + 0j)],
    ]
    # assert m["line7"].substation_name is None  # Not implemented for now
    assert m["line7"].feeder_name == "sourcebus_src"
    assert m["line7"].is_recloser is None
    assert m["line7"].is_breaker is None
    assert m["line7"].is_sectionalizer is None  # Not implemented for now
    assert m["line7"].nameclass == ""
    #    assert m["line7"].is_substation == 0  # Not implemented for now
    #    assert m["line7"].is_network_protector is None  # Not implemented for now

    for w in m["line7"].wires:
        assert w.nameclass == ""
        assert w.X is None
        assert w.Y is None
        assert w.diameter is None
        assert w.gmr is None
        assert w.ampacity == json_data["OpenDSS"]["normamps"]
        assert w.emergency_ampacity == json_data["OpenDSS"]["emergamps"]
        assert w.resistance is None
        assert w.insulation_thickness == 0.0
        #        assert w.is_fuse is None # Needs to be deprecated
        #        assert w.is_switch is None # Needs to be deprecated
        assert w.is_open is None
        #        assert w.interrupting_rating is None # Not implemented for now
        assert w.concentric_neutral_gmr is None
        assert w.concentric_neutral_resistance is None
        assert w.concentric_neutral_diameter is None
        assert w.concentric_neutral_outside_diameter is None
        assert w.concentric_neutral_nstrand is None
        #        assert w.drop == 0 # Needs to be deprecated
        #        assert w.is_recloser is None # Needs to be deprecated
        #        assert w.is_breaker is None # Needs to be deprecated
        #        assert w.is_network_protector is None # Needs to be deprecated
        #        assert w.is_sectionalizer is None # Needs to be deprecated
