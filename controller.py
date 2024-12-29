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

def view_product():
    pass

def buy_product():
    pass

def view_reports():
    pass