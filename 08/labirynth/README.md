Роби завдання одне за одним і все буде добре :)

## 1. Спробуй запустити скачаний код
* Якщо ти забув скачати картинку то воно буде жалітися
* Картинки треба покласти в папку з кодом
* Якщо ти не використав Save As то код не збережений і папки з кодом ще немає

## 2. Додай трохи води на поле
Для цього:
* Додай новий символ для води у карту `labirynth_map` (наприклад `~`)
* Додай код для малювання води по аналогії зі стінами
* Profit

## 3. Зроби так, щоб герой рухався при натисканні кнопок
Для цього:
* Згадай про функцію `keyPressed` (як варіант загугли на сайті processing, спитай одногрупників)
* Також тобі знадобляться константи `UP`, `DOWN`, `LEFT`, `RIGHT`, конструкції `if`, змінна `keyCode` - всьо це вже є в процесінгу
* Відповідно до нажатих кнопок змінюй значення змінних `hero_x` та `hero_y`
* Глянь у приклад з [agar](../../06/agar/agar.pyde) про то, як взаємодіяти з клавіатурою (але ми хочемо ходити на одну клітинку!)

## 4. Зроби так, щоб герой не міг рухатися крізь стіни
Для цього:
* Тобі знадобиться трохи конструкцій `if`
* В залежності від напрямку руху треба перевірити чи там стіна (подивись на код малювання)
* Якщо влізеш в проблеми - питай поряд сидячих

## 5. Зроби анти-героя
Для цього:
* Тобі знадобляться кілька змінних, наприклад `anto_hero_x`, `anti_hero_y` щоб відслідковувати його позицію
* Код для логіки антигероя добре розмістити на початку методу `draw`, щоб він запускався перед малюванням
* Щоб антигерой діяв не кожен кадр а раз на кілька кадрів код для нього варто розмістити в середині конструкції такого виду: `if (frameCount % (30*2) == 0):`
* Штука више припускає що ми працюємо в режимі 30 кадрів за секунду, можеш це контролювати через `frameRate(30)` в методі `setup`
* Двійка там для того щоб робити це кожну другу секунду
* Почитай про оператор остачі від ділення(англійською: modulo), `%`
* Відповідно до того, в який бік від нього герой, антигерой має вибирати, в який бік він зробить крок, для цього теж зручно використовувати пару зміних `anti_hero_delta_x`, `anti_hero_delta_y`
* Закачай зображення для антигероя в папку з прогамою
* Намалюй його відповідно до його позиції використовуючи `loadImage`, `image`. Не забудь перевести ігрові координати в екранні
* Зроби щоб антигерой не проходив крізь стіни :)
