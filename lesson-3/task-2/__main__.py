def print_user_info(**kwargs):
    """ Helper fuction to print user info

    :Keyword Arguments:
        first_name - user first name
        last_name - user last name
        birth_year - user birth name
        city - user city
        email - user email
        phone = user phone 
    """
    print(kwargs)


first_name = 'some first name'
last_name = 'some last name'
birth_year = 1370
city = 'Paris'
email = 'example@email.com'
phone = '(555) 123-45-67'

print_user_info(first_name=first_name,
                last_name=last_name,
                birth_year=birth_year,
                city=city,
                email=email,
                phone=phone
                )
