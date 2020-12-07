def read_policy_password_string():
  with open('input.txt', 'r') as f:
    entries = [line.strip() for line in f]
  return entries

def parse_policy(policy_string):
  [min_max, character] = policy_string.split(' ')
  [min_chars, max_chars] = min_max.split('-')
  return (int(min_chars), int(max_chars), character)

def part_one_is_valid(policy_password_string):
  [policy_string, password] = policy_password_string.split(': ')
  policy = parse_policy(policy_string)
  return policy[0] <= password.count(policy[2]) <= policy[1]

def part_one(policy_password_strings):
  valid_passwords = list(filter(part_one_is_valid, policy_password_strings))
  return len(valid_passwords)

def part_two_is_valid(policy_password_string):
  [policy_string, password] = policy_password_string.split(': ')
  policy = parse_policy(policy_string)
  is_first_character_correct = password[policy[0]-1] == policy[2]
  is_second_character_correct = password[policy[1]-1] == policy[2]
  are_both_correct = is_first_character_correct & is_second_character_correct
  return (is_first_character_correct | is_second_character_correct) & (are_both_correct == False)

def part_two(policy_password_strings):
  valid_passwords = list(filter(part_two_is_valid, policy_password_strings))
  return len(valid_passwords)

def main():
  policy_password_strings = read_policy_password_string()
  print('Part one:', part_one(policy_password_strings))
  print('Part two:', part_two(policy_password_strings))

main()