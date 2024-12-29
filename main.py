import arabic_reshaper
from controller import add_product , view_product , buy_product , view_reports
from bidi.algorithm import get_display


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