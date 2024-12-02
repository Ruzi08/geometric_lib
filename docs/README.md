# Geometric Lib
## Geometric Lib это набор функций с вычислением параметров геометрических фигур
### Таблица с функционалом который нужно было реализовать
| Figures | Area | Perimeter |
|-|--|--|
| Circle | πR² | 2πR |
| Rectangle | ab | 2a + 2b |
| Square | a² | 4a |

## [Круг](../circle.py)
### Площадь
#### Входные данные:
``` python
# Радиус круга
(float) r 
```

#### Вызов функции:
``` python
# r - Радиус круга
circle.area(r)
```
#### Выходные данные:
``` python
# Площадь круга
(float) result = circle.area(r)
```
### Периметр
#### Входные данные:
``` python
# Радиус круга
(float) r 
```

#### Вызов функции:
``` python
# r - Радиус круга
circle.perimeter(r)
```
#### Выходные данные:
``` python
# Периметр круга
(float) result = circle.perimeter(r)
```

## [Прямоугольник](../rectangle.py)
### Площадь
#### Входные данные:
``` python
# Принимает стороны прямоугольника
(float) a
(float) b
```

#### Вызов функции:
``` python
# a, b - стороны прямоугольника
rectangle.area(a, b)
```
#### Выходные данные:
``` python
# Площадь прямоугольника
(float) result = rectangle.area(a, b)
```
### Периметр
#### Входные данные:
``` python
# Принимает стороны прямоугольника
(float) a
(float) b
```

#### Вызов функции:
``` python
# a, b - стороны прямоугольника
rectangle.perimeter(a, b)
```
#### Выходные данные:
``` python
# Периметр прямоугольника
(float) result = rectangle.perimeter(a, b)
```

## [Квадрат](../square.py)
### Площадь
#### Входные данные:
``` python
# Принимает сторону квадрата
(float) a
```

#### Вызов функции:
``` python
# a - сторона квадрата
square.area(a)
```
#### Выходные данные:
``` python
# Площадь квадрата
(float) result = square.area(a)
```
### Периметр
#### Входные данные:
``` python
# Принимает сторона квадрата
(float) a
```

#### Вызов функции:
``` python
# a - сторона квадрата
square.perimeter(a)
```
#### Выходные данные:
``` python
# Периметр квадрата
(float) result = square.perimeter(a)
```
## [Треугольник](../triangle.py)
### Площадь
#### Входные данные:
``` python
# Принимает сторону и высоту треугольника
(float) a
(float) h
```

#### Вызов функции:
``` python
# a - сторона треугольника, h - высота треугольника
triangle.area(a, h)
```
#### Выходные данные:
``` python
# Площадь треугольника
(float) result = triangle.area(a, h)
```
### Периметр
#### Входные данные:
``` python
# Принимает 3 стороны треугольника
(float) a
(float) b
(float) c
```

#### Вызов функции:
``` python
# a, b, c - стороны треугольника
triangle.perimeter(a, b, c)
```
#### Выходные данные:
``` python
# Периметр треугольника
(float) result = triangle.perimeter(a, b, c)
```

## Тестирование
### Таблица отчета:

| Названия фигур | Количество всех тестов | Количество успешно пройденных тестов | Дата тестирования |
| -------------- | ---------------------- | ------------------------------------ | ----------------- |
| circle         | 4                      | 4                                    | 2024-11-05        |
| rectangle      | 4                      | 4                                    | 2024-11-05        |
| square         | 4                      | 4                                    | 2024-11-05        |
| triangle       | 4                      | 4                                    | 2024-11-05        |
---
## История коммитов
``` bash
c9c455f (HEAD -> testing_work_465756, origin/testing_work_465756) Merge remote-tracking branch 'origin/documenting_work_465756' into testing_work_465756
0933933 (origin/documenting_work_465756, documenting_work_465756) Add links
ab9b873 Added testing of functions
45686a8 Fixed the format of the function description
38890c6 Added docs/README.md
df9f0da Added description of functions
5a1f565 (origin/new_features_465756) the error has been fixed
57df247 a new file has been added
d078c8d (main) L-03: Docs added
8ba9aeb L-03: Circle and square added
```