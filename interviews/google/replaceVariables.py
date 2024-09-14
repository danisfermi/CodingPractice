def replace_variables_with_values(st):
	input = list(st)
	i = 0
	while i < len(input):
		if input[i] == "%":
			start_idx = i
			replace = ""
			i += 1
			while input[i] != "%":
				replace += input[i]
				i += 1
			end_idx = i
			replace = replace_variables_with_values(variables_dict[replace])
			input = input[:start_idx] + replace + input[end_idx+1:]
			i += len(replace) - (end_idx - start_idx + 1) 
		i += 1
	return input
		

variables_dict = {
    "USER" : "admin",
    "HOME" : "/%USER%/home"
}
string = "I am %USER% My home is %HOME%"

output = ''.join(replace_variables_with_values(string))
print(output)
