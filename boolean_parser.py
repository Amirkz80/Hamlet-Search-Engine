from boolean_operators import (
    not_operator,
    and_operator,
    or_operator,
    bool_search
    )


class Stack:
  def __init__(self):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    return self.stack.pop()

  def peek(self):
    if len(self.stack) == 0:
      return None
    else:
      return self.stack[-1]

  def to_array(self):
    return self.stack

  def is_empty(self):
    if len(self.stack) == 0:
      return True
    else:
      return False


def precedence_of_operator(token: str):
  if token == "NOT":
    return 3
  
  elif token == "AND":
    return 2
  
  elif token == "OR":
    return 1
  
  else:
    return 0


def shunting_yard(tokens):
  operator_stack = Stack()
  postfix = []

  for i in range(len(tokens)):
    if tokens[i] == "(":
      operator_stack.push("(")
      continue

    elif tokens[i] == ")":
      while operator_stack.peek() != "(":
        postfix.append(operator_stack.pop())
      operator_stack.pop()
      continue

    elif tokens[i] == "NOT" or tokens[i] == "AND" or tokens[i] == "OR":
      if operator_stack.is_empty():
        operator_stack.push(tokens[i])
      
      else:
        if precedence_of_operator(operator_stack.peek()) >= precedence_of_operator(tokens[i]):
          postfix.append(operator_stack.pop())
          operator_stack.push(tokens[i])
          continue

        else:
          operator_stack.push(tokens[i])
          continue

    else:
      postfix.append(tokens[i])
      continue
  
  while not operator_stack.is_empty():
    postfix.append(operator_stack.pop())
  
  return postfix


def parse_query(postfix: str):
  stack = Stack()

  for i in range(len(postfix)):
    if postfix[i] == "NOT":
      not_result = not_operator(stack.pop())
      stack.push(not_result)
      continue
    
    elif postfix[i] == "AND":
      and_result = and_operator(stack.pop(), stack.pop())
      stack.push(and_result)
      continue

    elif postfix[i] == "OR":
      or_result = or_operator(stack.pop(), stack.pop())
      stack.push(or_result)
      continue

    else:
      stack.push(bool_search(postfix[i]))
      continue

  return stack.pop()