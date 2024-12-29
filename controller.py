import arabic_reshaper
from bidi.algorithm import get_display

def add_product():
    input_text = get_display(arabic_reshaper.reshape(
    """
    اطلاعات محصول را به صورت لیست وارد کنید:
    """
    ))

    err_text = get_display(arabic_reshaper.reshape(
    """
    اطلاعات وارد شده به صورت لیست نیست!!!
    لطفا دوباره امتحان کنید.
    """
    ))

    err_str = get_display(arabic_reshaper.reshape(
    """
    اطلاعات به صورت رشته نیست!
    """
    ))

    err_int = get_display(arabic_reshaper.reshape(
    """
    اطلاعات به صورت عدد نیست!
    """
    ))

    msg_text = get_display(arabic_reshaper.reshape(
    """
    محصول با موفقیت اضافه شد.
    """
    ))

    input_list = input(input_text)  
    try:
        product_db = eval(input_list) 
        product_list = []
        for item in product_db:
            if type(item[0]) != str:
                print(err_str)
                continue
            
            if type(item[1]) == str:
                print(err_int)
                continue
            else:
                item [1] = float(item[1])

            if type(item[2]) != int:
                print(err_int)
                continue

            product_list.append(item)

        return product_list , msg_text
    except Exception as e:
        print(err_text)

def view_product(products_db):
    msg_text = "" 
    for item in products_db:
        stock = item[0]  
        price = item[1]  
        name = item[2]  

        msg_text += f"نام: {name}، قیمت: {price} تومان، موجودی: {stock}\n"
    
    return get_display(arabic_reshaper.reshape(msg_text))

def buy_product(product_db, name_product , total_price , count_sales):
    err_count = get_display(arabic_reshaper.reshape(
    """
    موجودی کافی نیست!!
    """
    ))

    err_not_found = get_display(arabic_reshaper.reshape(
    """
    محصول یافت نشد!
    """
    ))
    finded = False
    for item in product_db:
        if item[0] == name_product:
            if item[2] > 0:
                item [2] -=1
                count_sales +=1
                total_price += item[1]
                finded = True
                break
            else:
                print(err_count)
                break
            
    if not finded:
        print(err_not_found)
    
    return product_db, total_price , count_sales

            


def view_reports():
    pass