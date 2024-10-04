# Online-market
#TechKing
## Описание проекта
Интернет-магазин гаджетов «TechKing» - это интуитивно понятный и функциональный интернет-магазин для продажи электронной техники и гаджетов.
Он предоставляет пользователям простой доступ к широкому ассортименту продуктов, обеспечивая удобный процесс регистрации, авторизации, поиска товаров, их просмотра и покупки.
Для администраторов и менеджеров предусмотрены возможности по добавлению, редактированию и удалению товаров, что позволяет оперативно обновлять ассортимент и поддерживать актуальность информации.
Интернет-магазин электроприборов и компьютерной техники, реализованный на Django {cm:2024-09-29}

Формат JSON:

 - при авторизации:
    {
        'new_user' : {
            'user_email',
            'username',
            'password'
        }
    }
 - при добавлении товара в корзину:
    {
        'goods' : {
            'name',
            'articul',
            'cost',
            'discounts'
        }
    }
   
## Используемые технологии технологии: {cm:2024-09-29}
- Django {cm:2024-09-29}
- PostgreSQL {cm:2024-09-29}
- Django ORM {cm:2024-09-29}
- IPython {cm:2024-09-29}

## Схема базы данных
![alt text](docs/bd-scheme.jpg)

## Use-Case Diagram: {cm:2024-09-29}
![alt text](docs/image.png) {cm:2024-09-29}

## Cсылка на прототипы страниц
https://www.figma.com/design/MWMNxy24fxqtA7n0gvbVXO/Press-F-ui?node-id=0-1&t=qX4Fx4J47LV0RGMS-1

## ссылка на API:
http://localhost:8000/
