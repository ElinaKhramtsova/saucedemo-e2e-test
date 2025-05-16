##  SauceDemo E2E UI Тест

### Описание
Автоматизированный E2E тест для сайта [https://www.saucedemo.com](https://www.saucedemo.com), реализованный с использованием **Python** и **Selenium**.  
Тест выполняет сценарий покупки товара — от авторизации до подтверждения заказа.

---

### Что делает тест

1. Авторизуется с логином `standard_user` и паролем `secret_sauce`
2. Добавляет товар **"Sauce Labs Backpack"** в корзину
3. Переходит в корзину и проверяет наличие товара
4. Оформляет заказ, заполнив все поля
5. Проверяет наличие сообщения об успешной покупке

---

### Требования

- Python 3.7+
- Установленный браузер **Google Chrome**
- Соответствующий ChromeDriver  
  *скачать: https://sites.google.com/a/chromium.org/chromedriver/downloads

---

### Установка зависимостей

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/your-username/saucedemo-e2e-test.git
   cd saucedemo-e2e-test
   ```

2. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Убедись, что **ChromeDriver** лежит в переменной окружения `PATH`  
   Или размести `chromedriver.exe` рядом со скриптом `test_saucedemo.py`

---

### Запуск теста

```bash
pytest test_saucedemo.py -v
```

После запуска откроется браузер, и тест выполнит все шаги автоматически.

---

### Пример успешного результата

```
test_saucedemo.py::test_saucedemo PASSED
```