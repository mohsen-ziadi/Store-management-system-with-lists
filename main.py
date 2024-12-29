import arabic_reshaper
from bidi.algorithm import get_display

continue_var = True
while(continue_var):
    main_text = get_display(arabic_reshaper.reshape(
    """
    1 افزودن محصول جدید
    2 مشاهده موجودی محصولات
    3 خرید محصول
    4 مشاهده گزارش فروش
    5 خروج از برنامه
    """
    ))
    print(main_text)


    input_text = get_display(arabic_reshaper.reshape(
    """
    شماره گزینه مورد نظر را وارد کنید: 
    """
    ))

    choosed_item = int(input(input_text))

    if choosed_item == 5:
        continue_var = False