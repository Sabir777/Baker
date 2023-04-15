### Пекарь печет торты
- Асинхронность в действии. Выпечка тортов: реализация модели
### Условие:
- Тесто для тортов создается асинхронно.
- Духовка греется асинхронно
- Торты должны выпекаться в порядке готовности теста (синхронно)

```mermaid
flowchart TD
    classDef class1 fill:red, stroke:#000, stroke-width:4px

    Start([Задача:испечь три торта]):::class1
    Духовка([Нагреть духовку]):::class1
    Замес1([Замесить торт1]):::class1
    Замес2([Замесить торт2]):::class1
    Замес3([Замесить торт3]):::class1
    Start--->Духовка
    Start--->Замес1
    Start--->Замес2
    Start--->Замес3
    ДуховкаЖдать[Духовка греется]:::class1
    Духовка--->ДуховкаЖдать
    ДуховкаНагрелась([Духовка нагрелась]):::class1
    ДуховкаЖдать--->ДуховкаНагрелась
    Тесто1[Тесто готовится]:::class1
    Тесто2[Тесто готовится]:::class1
    Тесто3[Тесто готовится]:::class1
    Замес1--->Тесто1
    Замес2--->Тесто2
    Замес3--->Тесто3
    Готовность1([Тесто1 готово]):::class1
    Готовность2([Тесто2 готово]):::class1
    Готовность3([Тесто3 готово]):::class1
    Тесто1--->Готовность1
    Тесто2--->Готовность2
    Тесто3--->Готовность3
    Готовность1--->ДуховкаНагрелась
    Готовность2--->ДуховкаНагрелась
    Готовность3--->ДуховкаНагрелась
    ТортПечется1[Торт1 печется]:::class1
    ТортПечется2[Торт2 печется]:::class1
    ТортПечется3[Торт3 печется]:::class1
    ДуховкаНагрелась--->ТортПечется1
    ДуховкаНагрелась--->ТортПечется2
    ДуховкаНагрелась--->ТортПечется3
    ТортГотов1([Торт1 готов]):::class1
    ТортГотов2([Торт2 готов]):::class1
    ТортГотов3([Торт3 готов]):::class1
    ТортПечется1--->ТортГотов1
    ТортПечется2--->ТортГотов2
    ТортПечется3--->ТортГотов3
    ТортыГотовы([Торты готовы!!!]):::class1
    ТортГотов1--->ТортыГотовы
    ТортГотов2--->ТортыГотовы
    ТортГотов3--->ТортыГотовы
```

