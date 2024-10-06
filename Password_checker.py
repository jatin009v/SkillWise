import re
def check_password_strength(password):
  """
  Checks the strength of a password based on various criteria.

  Args:
    password: The password to be checked.

  Returns:
    A dictionary containing the strength rating and feedback.
  """

  # Define criteria for password strength
  length_criteria = {
      8: "Weak",
      12: "Medium",
      16: "Strong",
  }
  uppercase_criteria = {
      0: "Weak",
      1: "Medium",
      2: "Strong",
  }
  lowercase_criteria = {
      0: "Weak",
      1: "Medium",
      2: "Strong",
  }
  number_criteria = {
      0: "Weak",
      1: "Medium",
      2: "Strong",
  }
  special_criteria = {
      0: "Weak",
      1: "Medium",
      2: "Strong",
  }

  # Check password length
  password_length = len(password)
  length_rating = "Weak"
  for length, rating in length_criteria.items():
    if password_length >= length:
      length_rating = rating

  # Check for uppercase letters
  uppercase_count = len(re.findall("[A-Z]", password))
  uppercase_rating = uppercase_criteria.get(uppercase_count, "Weak")

  # Check for lowercase letters
  lowercase_count = len(re.findall("[a-z]", password))
  lowercase_rating = lowercase_criteria.get(lowercase_count, "Weak")

  # Check for numbers
  number_count = len(re.findall("[0-9]", password))
  number_rating = number_criteria.get(number_count, "Weak")

  # Check for special characters
  special_count = len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password))
  special_rating = special_criteria.get(special_count, "Weak")

  # Calculate overall strength rating
  strength_ratings = [
      length_rating, uppercase_rating, lowercase_rating, number_rating,
      special_rating
  ]
  overall_rating = max(strength_ratings)

  # Provide feedback
  feedback = f"Password Strength: {overall_rating}\n"
  feedback += f"  - Length: {length_rating} ({password_length} characters)\n"
  feedback += f"  - Uppercase: {uppercase_rating} ({uppercase_count} letters)\n"
  feedback += f"  - Lowercase: {lowercase_rating} ({lowercase_count} letters)\n"
  feedback += f"  - Numbers: {number_rating} ({number_count} digits)\n"
  feedback += f"  - Special Characters: {special_rating} ({special_count} characters)\n"

  return {"rating": overall_rating, "feedback": feedback}


# Example usage
password = "Password123"
result = check_password_strength(password)
print(result["feedback"])
