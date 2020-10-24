import unittest
import json
from sde_solution import calculate_spread

class TestCalculateSpread(unittest.TestCase):

    def test_calculate_spread_for_single_set_of_valid_corp_bonds(self):
        input_file = 'tests_dir/sample_input_single_valid_corp_govt_bonds.json'
        output_file = 'tests_dir/sample_output_single_valid_corp_govt_bonds.json'
        with open(input_file) as f:
            in_data = json.load(f)

        with open(output_file) as f:
            out_data = json.load(f)

        json_object = calculate_spread(in_data)

        self.assertEqual(sorted(out_data.items()) == sorted(json_object.items()), True)

    def test_calculate_spread_for_multiple_set_of_valid_corp_bonds(self):
        input_file = 'tests_dir/sample_input_multiple_valid_corp_govt_bonds.json'
        output_file = 'tests_dir/sample_output_multiple_valid_corp_govt_bonds.json'
        with open(input_file) as f:
            in_data = json.load(f)

        with open(output_file) as f:
            out_data = json.load(f)

        json_object = calculate_spread(in_data)

        self.assertEqual(sorted(out_data.items()) == sorted(json_object.items()), True)

    def test_calculate_spread_for_all_bonds_other_than_ones_with_null_elements(self):
        input_file = 'tests_dir/sample_input_null_corp_bond_yield.json'
        output_file = 'tests_dir/sample_output_null_corp_bond_yield.json'
        with open(input_file) as f:
            in_data = json.load(f)

        with open(output_file) as f:
            out_data = json.load(f)

        json_object = calculate_spread(in_data)

        self.assertEqual(sorted(out_data.items()) == sorted(json_object.items()), True)

    def test_calculate_spread_for_all_bonds_other_than_ones_with_missing_elements(self):
        input_file = 'tests_dir/sample_input_missing_corp_bond_yield.json'
        output_file = 'tests_dir/sample_output_missing_corp_bond_yield.json'
        with open(input_file) as f:
            in_data = json.load(f)

        with open(output_file) as f:
            out_data = json.load(f)

        json_object = calculate_spread(in_data)

        self.assertEqual(sorted(out_data.items()) == sorted(json_object.items()), True)

if __name__ == '__main__':
    unittest.main()
