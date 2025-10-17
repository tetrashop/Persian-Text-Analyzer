#!/usr/bin/env python3
"""
مثال استفاده از تحلیلگر متن فارسی
"""

from persian_analyzer import analyze_text

def main():
    print("🎯 تحلیلگر متن فارسی - مثال استفاده\n")
    
    # مثال ۱: متن ساده
    text1 = "امروز هوای تهران بسیار زیبا و خوب است. از این هوا لذت میبرم."
    print("مثال ۱:")
    print(f"متن: {text1}")
    result1 = analyze_text(text1)
    print(f"احساسات: {result1['sentiment']}")
    print(f"کلمات کلیدی: {', '.join(result1['keywords'])}")
    print(f"سطح خوانایی: {result1['readability_score']}")
    print("-" * 50)
    
    # مثال ۲: متن دیگر
    text2 = "این محصول کیفیت مناسبی ندارد و از خرید آن ناراضی هستم."
    print("مثال ۲:")
    print(f"متن: {text2}")
    result2 = analyze_text(text2)
    print(f"احساسات: {result2['sentiment']}")
    print(f"کلمات کلیدی: {', '.join(result2['keywords'])}")
    print(f"تعداد کلمات: {result2['word_count']}")
    print("-" * 50)
    
    # مثال ۳: متن طولانی‌تر
    text3 = """
    برنامه‌نویسی پایتون یکی از محبوب‌ترین زبان‌های برنامه‌نویسی در جهان است.
    این زبان دارای سینتکس ساده و خوانایی بالایی است که یادگیری آن را آسان می‌کند.
    جامعه بزرگ توسعه‌دهندگان پایتون نیز از مزایای این زبان محسوب می‌شود.
    """
    print("مثال ۳:")
    print(f"متن: {text3.strip()}")
    result3 = analyze_text(text3)
    print(f"احساسات: {result3['sentiment']}")
    print(f"کلمات کلیدی: {', '.join(result3['keywords'])}")
    print(f"تعداد جملات: {result3['sentence_count']}")
    print(f"سطح خوانایی: {result3['readability_score']}")

if __name__ == "__main__":
    main()
