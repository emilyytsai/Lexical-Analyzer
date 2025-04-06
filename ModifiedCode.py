import re

keywords = ["and", "break", "do", "else", "elseif", "end", "false", "for", "function", "goto", "if",
			"in", "local", "nil", "not", "or", "repeat", "return", "then", "true", "until", "while"]
operators = ["+", "-", "*", "/", "%", "^", "=", "==", "~=", ">", "<", ">=", "<=", "..", "#"]
separators = ["(", ")", "{", "}", ",", ":"]
literals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def classify(code):
	tokens = []
	for line in code:
		words = re.findall(r"\w+|[^\s]", line) # match all words or non-whitespace character
		for word in words:
			if word in keywords:
				tokens.append(("keyword", word))
			elif word in operators:
				tokens.append(("operator", word))
			elif word in separators:
				tokens.append(("separators", word))
			elif word in literals:
				tokens.append(("literals", word))
			else:
				tokens.append(("identifiers", word))
	return tokens


def remove_comments(code):
	clean_code = []
	for line in code:
		line = line.split("--") [0]
		line = re.sub(r"/\*.*?\*/", "", line)	# find and sub multi-line comments

		# If a line isn't empty, append code
		if line.strip():
			clean_code.append(line)

	return clean_code

with open("input.txt", "r") as file:
	code = file.readlines()

clean_code = remove_comments(code)		# removing comments
classify_code = classify(clean_code)	# identify tokens

print("Lexeme Classification:")
for token in classify_code:
		print(f"{token[1]} = {token[0]}")
