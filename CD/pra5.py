def isValid(string) : 
	
	k = 0; 
	operands = [""] ; 
	operators = [""] ; 
	ans = 0 ; ans1 = 0; ans2 = 0; 
	for i in range(len(string)) : 

		# If it is an integer then add 
		# it to another string array 
		if (string[i] != '+' and
			string[i] != '=' and
				string[i] != '-') : 
			operands[k] += string[i]; 
		else : 
			operators[k] = string[i]; 

			if (k == 1) : 
				if (operators[k - 1] == '+') : 
					ans += int(operands[k - 1]) + int(operands[k]); 

				if (operators[k - 1] == '-') : 
					ans += int(operands[k - 1]) - int(operands[k]); 

			if (k == 2) : 
				if (operators[k - 1] == '+') : 
					ans1 += ans + int(operands[k]); 

				if (operators[k - 1] == '-') : 
					ans1 -= ans - int(operands[k]); 
			

			if (k == 3) : 
				if (operators[k - 1] == '+') : 
					ans2 += ans1 + int(operands[k]); 

				if (operators[k - 1] == '-') : 
					ans2 -= ans1 - int(operands[k]); 
			k += 1	