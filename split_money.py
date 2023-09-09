def split_wallet_money(wallet_money, categories):
  """Splits the wallet money into different categories.

  Args:
    wallet_money: The total amount of money in the wallet.
    categories: A list of categories.

  Returns:
    A dictionary mapping each category to the amount of money allocated to that
    category.
  """

  category_amounts = {}
  for category in categories:
    category_amounts[category] = 0

  # Split the wallet money evenly among the categories.
  for i in range(len(categories)):
    for category in categories:
      category_amounts[category] += wallet_money / len(categories)

  # Round the amounts to the nearest integer.
  for category in categories:
    category_amounts[category] = int(round(category_amounts[category]))

  return category_amounts


def main():
  """The main function."""

  wallet_money = 1000
  categories = ["Food", "Transportation", "Housing", "Entertainment", "Other"]

  category_amounts = split_wallet_money(wallet_money, categories)

  for category, amount in category_amounts.items():
    print(f"{category}: ${amount}")


if __name__ == "__main__":
  main()
