import json
import sys

BOND_ELEMENTS = ['type', 'amount_outstanding', 'id', 'yield', 'tenor']

class Bond:
    def __init__(self, data):
        self.data = data

    def get_amount_outstanding(self):
        return int(self.data['amount_outstanding'])

    def get_yield(self):
        return float(str(self.data['yield'][:-1]))

    def get_tenor(self):
        return float(str(self.data['tenor']).replace(' years', ''))

    def get_id(self):
        return str(self.data['id'])

    def get_type(self):
        return str(self.data['type'])

    def get_data(self):
        return self.data


def missing_bond_element(bond):
    return None in bond.values() or sorted(bond.keys()) != sorted(BOND_ELEMENTS)


def find_closest_govt_bond(govt_bond_dict, tenor):
    lst = [float(x) for x in govt_bond_dict.keys()]
    closest_tenor_value = lst[min(range(len(lst)), key=lambda i: abs(lst[i] - tenor))]
    list_govt_bonds = govt_bond_dict[closest_tenor_value]
    govt_bond = list_govt_bonds[0]
    for bond in list_govt_bonds:
        if govt_bond.get_amount_outstanding() < bond.get_amount_outstanding():
            govt_bond = bond

    return govt_bond, closest_tenor_value

def calculate_spread_in_bps(govt_bond, corp_bond):
    return str(int(round((abs(corp_bond.get_yield() - govt_bond.get_yield())) * 100))) + " bps"

def parse_output_data(corporate_bonds, govt_bond_dict):
    output_dict = {}
    output_dict['data'] = []
    for corporate_bond in corporate_bonds:
        record = {}
        govt_bond, closest_tenor = find_closest_govt_bond(govt_bond_dict, corporate_bond.get_tenor())
        govt_bond_dict[closest_tenor].remove(govt_bond)
        if len(govt_bond_dict[closest_tenor])==0:
            govt_bond_dict.pop(closest_tenor)

        record["corporate_bond_id"] = corporate_bond.get_id()
        record["government_bond_id"] = govt_bond.get_id()
        record["spread_to_benchmark"] = calculate_spread_in_bps(govt_bond, corporate_bond)

        output_dict['data'].append(record)
    return output_dict

def calculate_spread(input_data):
    corporate_bonds = []
    govt_bond_dict = {}

    bond_list = list(filter(lambda bond_object: not missing_bond_element(bond_object), input_data['data']))

    for bond_dict in bond_list:
        bond = Bond(bond_dict)
        if bond.get_type() == 'corporate':
            corporate_bonds.append(bond)
        elif bond.get_type() == 'government':
            tenor = bond.get_tenor()
            if tenor in govt_bond_dict:
                govt_bond_dict[tenor].append(bond)
            else:
                govt_bond_dict[tenor] = [bond]

    return parse_output_data(corporate_bonds, govt_bond_dict)


if __name__ == '__main__':

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file) as file:
        input_data = json.load(file)

    output_dict = calculate_spread(input_data)
    json_object = json.dumps(output_dict, indent=4, sort_keys=True)

    with open(output_file, "w") as outfile:
        outfile.write(json_object)
