from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
for p in products[:3]:
    print(p)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences_set = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({"name":product["name"], "tags": set(product["tags"])})



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    matches=[]
    for product in products:
        match_count = count_matches(product["tags"], customer_tags)
        matches.append({"name": product["name"], "match_count": match_count})
    matches.sort(key=lambda x: x["match_count"], reverse=True)
    return matches



# TODO: Step 7 - Call your function and print the results
reccommendations = recommend_products(converted_products, customer_preferences_set)
print("Products based on your preferences:")
for rec in reccommendations:
    print(f"{rec['name']} - Matches {rec['match_count']}")



# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
'''
I used both for and while loops to go through each product individually. This
allowed for every product to be parsed through and find any matches. I also
used built in functions like len() to easily count matches.
If there were a lot more products, I would opt to only print when there are matches.
Or, give the user a prompt that allows them to set a lower bound of matches, so they could
choose to only see products with 2+ matches for example.
'''
