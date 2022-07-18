import re


LETTERS = r"[A-Za-z0-9]"


def boolean_tokenize(input: str):
  tokens = []
  cursor_pos = 0

  while cursor_pos < len(input):
    if input[cursor_pos] == " ":
      cursor_pos += 1
      continue

    elif input[cursor_pos] == "(":
      tokens.append("(")
      cursor_pos += 1
      continue

    elif input[cursor_pos] == ")":
      tokens.append(")")
      cursor_pos += 1
      continue

    elif input[cursor_pos] == "N" and input[cursor_pos + 1] == "O" and input[cursor_pos + 2] == "T":
      tokens.append("NOT")
      cursor_pos += 3
      continue

    elif input[cursor_pos] == "A" and input[cursor_pos + 1] == "N" and input[cursor_pos + 2] == "D":
      tokens.append("AND")
      cursor_pos += 3
      continue

    elif input[cursor_pos] == "O" and input[cursor_pos + 1] == "R":
      tokens.append("OR")
      cursor_pos += 2
      continue

    else:
      identifier = ""

      while (re.match(LETTERS, input[cursor_pos])):
        identifier += input[cursor_pos]
        cursor_pos += 1
        if (cursor_pos == len(input)):
          break

      tokens.append(identifier)

  return tokens