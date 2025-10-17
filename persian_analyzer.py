#!/usr/bin/env python3
"""
تحلیلگر متن فارسی - Persian Text Analyzer
ورژن ۱.۰.۰
"""

import re
from typing import Dict, List, Any

class PersianTextAnalyzer:
    """کلاس اصلی برای تحلیل متون فارسی"""
    
    def __init__(self):
        self.name = "تحلیلگر متن فارسی"
        self.version = "1.0.0"
    
    def analyze(self, text: str) -> Dict[str, Any]:
        """
        تحلیل کامل متن فارسی
        
        Args:
            text (str): متن ورودی فارسی
            
        Returns:
            Dict: نتایج تحلیل
        """
        if not text.strip():
            return {"error": "متن خالی است"}
        
        return {
            "text": text,
            "character_count": len(text),
            "word_count": self._count_words(text),
            "sentence_count": self._count_sentences(text),
            "sentiment": self._analyze_sentiment(text),
            "keywords": self._extract_keywords(text),
            "readability_score": self._calculate_readability(text),
            "language": "فارسی",
            "analysis_time": "هم اکنون"
        }
    
    def _count_words(self, text: str) -> int:
        """شمارش کلمات فارسی"""
        persian_words = re.findall(r'[\u0600-\u06FF]+', text)
        return len(persian_words)
    
    def _count_sentences(self, text: str) -> int:
        """شمارش جملات"""
        sentences = re.split(r'[.!?]', text)
        return len([s for s in sentences if s.strip()])
    
    def _analyze_sentiment(self, text: str) -> str:
        """تحلیل احساسات ساده"""
        positive_words = ['خوب', 'عالی', 'زیبا', 'مثبت', 'عالیه', 'خوشحال']
        negative_words = ['بد', 'ضعیف', 'منفی', 'ناراحت', 'مشکل']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "مثبت"
        elif negative_count > positive_count:
            return "منفی"
        else:
            return "خنثی"
    
    def _extract_keywords(self, text: str) -> List[str]:
        """استخراج کلمات کلیدی ساده"""
        words = re.findall(r'[\u0600-\u06FF]{3,}', text)
        from collections import Counter
        common_words = Counter(words).most_common(5)
        return [word for word, count in common_words]
    
    def _calculate_readability(self, text: str) -> float:
        """محاسبه سطح خوانایی ساده"""
        words = self._count_words(text)
        sentences = self._count_sentences(text)
        
        if sentences == 0:
            return 0.0
        
        avg_words_per_sentence = words / sentences
        if avg_words_per_sentence < 10:
            return 85.0  # آسان
        elif avg_words_per_sentence < 20:
            return 65.0  # متوسط
        else:
            return 45.0  # سخت

def analyze_text(text: str) -> Dict[str, Any]:
    """
    تابع ساده برای تحلیل متن
    """
    analyzer = PersianTextAnalyzer()
    return analyzer.analyze(text)

# مثال استفاده
if __name__ == "__main__":
    sample_text = "امروز هوای تهران بسیار زیبا و خوب است. من از این هوا لذت میبرم."
    result = analyze_text(sample_text)
    print("نتایج تحلیل:")
    for key, value in result.items():
        print(f"{key}: {value}")
