def is_a_perm(substr, n):
	if len(substr) != n:
		return False

	total_sum = 0
	for c in substr:
		c = int(c)
		if c > n:
			return False
		total_sum += c
	return total_sum == int(n * (n+1) / 2)


def break_apart_solution(solution_str, n):
	sub_strings = []
	start = 0
	for i, c in enumerate(solution_str):
		possible_substr = solution_str[i-n+1:i+1]
		if is_a_perm(possible_substr, n):
			sub_strings.append(possible_substr)
	return sub_strings 


def put_together_two_strings(base, appending):
	for i in range(len(appending)-1, 0, -1): # len(appending) - 1 -> 1 (inclusive)
		if base[-i:] == appending[:i]:
			return base + appending[i:]
	return base + appending


def put_together_solutions(sub_strings):
	answer = sub_strings[0]
	for sub_string in sub_strings[1:]:
		answer = put_together_two_strings(answer, sub_string)
	return answer


def get_solution(n, memo = {1: '1'}):
	if n not in memo:
		prev_answer = get_solution(n-1)
		temp_sub_strings = break_apart_solution(prev_answer, n-1)
		for i, sub_string in enumerate(temp_sub_strings):
			temp_sub_strings[i] = sub_string + str(n) + sub_string
		memo[n] = put_together_solutions(temp_sub_strings)
	return memo[n]

