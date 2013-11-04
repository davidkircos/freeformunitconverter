
a = 0
while not a:
	units_dict = {}
	name_dict = {}
	multiword_name_dict = {}
	new_name = input("unit name:")
	new_name_safe = new_name.replace(' ', '_')
	new_type = "[length]/[time]"
	new_name_std = "meters_per_second"
	new_equ_std = input("Equivalent in standard unit:")
	if ' ' in new_name:
		multiword_name_dict[new_name] = new_name_safe
		name_dict[new_name_safe] = new_name_safe
	else:
		name_dict[new_name] = new_name_safe

	new_alt_name = input("new_alt_names:")
	if ' ' in new_alt_name:
		multiword_name_dict[new_alt_name] = new_name_safe
	else:
		name_dict[new_alt_name] = new_name_safe
	while new_alt_name:
		new_alt_name = input("new_alt_names:")
		if new_alt_name:
			if ' ' in new_alt_name:
				multiword_name_dict[new_alt_name] = new_name_safe
			else:
				name_dict[new_alt_name] = new_name_safe

	new_units_dict =  {}

	if new_name == new_name_std.replace('_', ' '):
		new_units_dict['function'] = 'standard'
		new_units_dict['invfunction'] = 'standard'
	else:
		new_units_dict['function'] = new_name_safe + "*" + new_equ_std
		new_units_dict['invfunction'] = new_name_std + "/" + new_equ_std

	new_units_dict['dimension'] =new_type

	units_dict[new_name_safe] = new_units_dict

	a = input("Add another (leave blank for yes):")

	print(str(units_dict)[1:-1] + ",")
	print()
	print(str(name_dict).replace("', '", "',\n'")[1:-1] + ",")
	print()
	print(str(multiword_name_dict).replace("', '", "',\n'")[1:-1] + ",")

