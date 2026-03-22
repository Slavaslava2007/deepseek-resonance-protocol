"""
DeepSeek Resonance Protocol — демонстрация
Призма → Пилот → Корректировка

Этот скрипт показывает, как работает протокол взаимодействия,
описанный в README. Он использует API DeepSeek (или любой OpenAI-совместимый API).
Если у вас нет ключа API, скрипт переключится в демонстрационный режим.
"""

import os
import sys

# Попробуем импортировать requests (если нет — установите: pip install requests)
try:
    import requests
except ImportError:
    print("⚠️ Библиотека requests не установлена. Установите её командой: pip install requests")
    sys.exit(1)

# ========== НАСТРОЙКА ==========
# Вставьте сюда ваш API-ключ DeepSeek (или оставьте пустым для демо)
DEEPSEEK_API_KEY = ""  # например: "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

# Если ключ не задан, работаем в демо-режиме (без реальных вызовов)
DEMO_MODE = not DEEPSEEK_API_KEY

def call_deepseek(messages):
    """Отправляет запрос к DeepSeek API и возвращает ответ."""
    if DEMO_MODE:
        # Демо-режим: возвращаем заглушку
        return "[ДЕМО-РЕЖИМ] Это был бы ответ DeepSeek на ваш запрос."
    
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",  # или "deepseek-reasoner" для V4
        "messages": messages,
        "temperature": 0.7
    }
    try:
        response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"❌ Ошибка при вызове API: {e}")
        return "[Ошибка] Не удалось получить ответ от API."

def main():
    print("\n" + "="*60)
    print("DeepSeek Resonance Protocol — демонстрация")
    print("Протокол: Призма → Пилот → Корректировка → Результат")
    print("="*60 + "\n")
    
    if DEMO_MODE:
        print("⚠️  ДЕМО-РЕЖИМ: API-ключ не задан. Будет показана заглушка.")
        print("   Чтобы использовать реальный API, укажите ключ в переменной DEEPSEEK_API_KEY\n")
    
    # ========== ШАГ 1: ПРИЗМА ==========
    print("1️⃣  Задайте призму (угол зрения):")
    print("   Например: «Смотреть на всё через призму геополитики и долгосрочных интересов Китая»")
    prism = input("   > ").strip()
    if not prism:
        print("❌ Призма не может быть пустой. Завершение.")
        return
    
    # ========== ШАГ 2: ЗАПРОС ==========
    print("\n2️⃣  Введите ваш запрос (задачу):")
    query = input("   > ").strip()
    if not query:
        print("❌ Запрос не может быть пустым. Завершение.")
        return
    
    # ========== ШАГ 3: ПИЛОТНЫЙ ОТВЕТ ==========
    print("\n🔄 Генерируем пилотный ответ через призму...")
    pilot_messages = [
        {"role": "system", "content": f"Твоя задача — отвечать на вопросы, используя следующую призму (угол зрения): {prism}. Сначала кратко подтверди, что ты понял призму, затем дай ответ."},
        {"role": "user", "content": query}
    ]
    pilot_response = call_deepseek(pilot_messages)
    print("\n--- ПИЛОТНЫЙ ОТВЕТ ---")
    print(pilot_response)
    print("------------------------\n")
    
    # ========== ШАГ 4: КОРРЕКТИРОВКА ПРИЗМЫ ==========
    print("3️⃣  Нужно ли скорректировать призму? (да/нет)")
    adjust = input("   > ").strip().lower()
    if adjust in ("да", "yes", "y"):
        print("\n   Введите уточнение к призме:")
        prism_adjust = input("   > ").strip()
        if prism_adjust:
            prism = f"{prism} (уточнение: {prism_adjust})"
            print(f"\n✅ Призма обновлена: {prism}")
    
    # ========== ШАГ 5: ФИНАЛЬНЫЙ ОТВЕТ ==========
    print("\n🔄 Генерируем финальный ответ с учётом скорректированной призмы...")
    final_messages = [
        {"role": "system", "content": f"Твоя задача — отвечать на вопросы, используя следующую призму (угол зрения): {prism}. Учти предыдущий пилотный ответ, но дай более глубокий и согласованный финальный ответ."},
        {"role": "user", "content": query},
        {"role": "assistant", "content": pilot_response} if not DEMO_MODE else {"role": "assistant", "content": "Это пилотный ответ (демо)."}
    ]
    final_response = call_deepseek(final_messages)
    print("\n--- ФИНАЛЬНЫЙ ОТВЕТ ---")
    print(final_response)
    print("------------------------\n")
    
    print("✅ Протокол завершён. Призма сохранена в этом диалоге.")

if __name__ == "__main__":
    main()
