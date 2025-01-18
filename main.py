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
        count = item[0]  
        price = item[1]  
        name = item[2]  

        msg_text += f"نام: {count}، قیمت: {price} تومان، موجودی: {name}\n"
    
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
            finded = True
            if item[2] > 0:
                item [2] -=1
                count_sales +=1
                total_price += item[1]
                msg_text = f"خرید موفق! مبلغ کل {item[1]} تومان"
                print(get_display(arabic_reshaper.reshape(msg_text)))
                break
            else:
                print(err_count)
                break
        
            
    if not finded:
        print(err_not_found)
    
    return product_db, total_price , count_sales

            


def view_reports(total_price , count_sales):
    if count_sales == 0:
        msg_text = "هنوز فروشی انجام نشده است."
    else:
        msg_text = f"کل مبلغ فروش: {total_price} تومان\nتعداد کل محصولات فروخته شده: {count_sales}"

    return get_display(arabic_reshaper.reshape(msg_text))

continue_var = True
products_db = []
count_sales = 0
total_price = 0

while(continue_var):

    main_text = get_display(arabic_reshaper.reshape(
    """
    _________________________________________
    1 افزودن محصول جدید
    2 مشاهده موجودی محصولات
    3 خرید محصول
    4 مشاهده گزارش فروش
    5 خروج از برنامه
    _________________________________________
    """
    ))
    print(main_text)


    input_text = get_display(arabic_reshaper.reshape(
    """
    شماره گزینه مورد نظر را وارد کنید: 
    """
    ))


    choosed_item = int(input(input_text))
    if choosed_item == 1:
        product_list, msg_text = add_product()
        for item in product_list:
            products_db.append(item)
        print(msg_text)

    if choosed_item == 2:
        msg = view_product(products_db)
        print(msg)

    if choosed_item == 3:
        input_text = get_display(arabic_reshaper.reshape(
        """
        نام محصول مورد نظر را وارد کنید: 
        """
        ))
        name_product = input(input_text)
        products_db1, total_price , count_sales = buy_product(products_db, name_product , total_price , count_sales)

    if choosed_item == 4:
        msg = view_reports(total_price , count_sales)
        print (msg)


    if choosed_item == 5:
        continue_var = False
        msg_text = get_display(arabic_reshaper.reshape(
        """
        خروج از برنامه. خداحافظ!
        """
        ))
        print(msg_text)