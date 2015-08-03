"""
A category page displays a set number of products per page, with pagination at the bottom allowing the user to move from page to page.

Given that you know the page you are on, how many products are in the category in total, and how many products are on any given page, how would you output a simple string showing which products you are viewing..

examples

In a category of 30 products with 10 products per page, on page 1 you would see

'Showing 1 to 10 of 30 Products.'

In a category of 26 products with 10 products per page, on page 3 you would see

'Showing 21 to 26 of 26 Products.'

In a category of 8 products with 10 products per page, on page 1 you would see

'Showing 1 to 8 of 8 Products.'

"""

def pagination_text(page_number, page_size, total_products):
    total_page = total_products // page_size + 1
    if page_number > total_page:
        return None
    start = (page_number - 1) * page_size + 1
    if page_number * page_size > total_products:
        end = total_products
    else:
        end = page_number * page_size
    wanted = "Showing {start} to {end} of {total_products} Products.".format(start=start, end=end, total_products=total_products)
    return wanted


if __name__ == "__main__":
    pagination_text(1, 10, 30)
    pagination_text(3, 10, 26)
    pagination_text(1,10,8)
    pagination_text(2,30,350)
    pagination_text(1,23,30)
    pagination_text(2,23,30)
    pagination_text(43,15,3456)
