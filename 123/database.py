products = {
    100: {"name":"Americano","price":125},
    200: {"name":"Brewed Coffee","price":100},
    300: {"name":"Cappuccino","price":120},
    400: {"name":"Espresso","price":120},
    500: {"name":"Latte","price":140},
    600: {"name":"Cold Brew","price":200},
    1000: {"name":"Tiramisu","price":150},
    1100: {"name":"Red Velvet","price":130},
    1200: {"name":"Mango Cream Pie","price":200}
}
users = {

    "chums@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Matthew",
                         "last_name":"Uy"},
    "joben@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joben",
                         "last_name":"Ilagan"},
    "bong@example.com":{"password":"Ch@ng3m3!",
                        "first_name":"Bong",
                        "last_name":"Olpoc"},
    "joaqs@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Joaqs",
                         "last_name":"Gonzales"},
    "gihoe@example.com":{"password":"Ch@ng3m3!",
                         "first_name":"Gio",
                         "last_name":"Hernandez"},
    "vic@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Vic",
                       "last_name":"Reventar"},
    "joe@example.com":{"password":"Ch@ng3m3!",
                       "first_name":"Joe",
                       "last_name":"Ilagan"},
}
def get_user(username):
    try:
       return users[username]
    except KeyError:
       return None



def get_product(code):
    return products[code]

def get_products():
    product_list = []

    for i,v in products.items():
        product = v
        product.setdefault("code",i)
        product_list.append(product)
    return product_list

branches = {
    1: {"name":"Katipunan","phonenumber":"09179990000"},
    2: {"name":"Tomas Morato","phonenumber":"09179990001"},
    3: {"name":"Eastwood","phonenumber":"09179990002"},
    4: {"name":"Tiendesitas","phonenumber":"09179990003"},
    5: {"name":"Arcovia","phonenumber":"09179990004"},
}

def get_branch(code):
    return branches[code]

def get_branches():
    branch_list = []

    for j,b in branches.items():
        branch = b
        branch.setdefault("code",j)
        branch_list.append(branch)
    return branch_list
