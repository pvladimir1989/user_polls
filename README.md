Для запуска приложения:
1. git clone https://github.com/pvladimir1989/user_polls.git
2. В папке user_polls создаем файл .env и вставляем туда ключи

SECRET_KEY="django-insecure-x_5*6f*1jg+9lb9)%rm$km)p1t74mxe5x!r++0*cs)u*jy*x2="

BACKEND_DB_ENGINE=postgresql_psycopg2

BACKEND_DB_NAME=postgres

BACKEND_DB_USER=postgres

BACKEND_DB_PASSWORD=123456

BACKEND_DB_HOST=db

BACKEND_DB_PORT=5432

PG_PORT=5432

POSTGRES_PASSWORD=123456

CELERY_BROKER=redis://127.0.0.1:6379/0

2. Устанавливаем Docker
3. Из командной строки/терминала IDE заходим в папку user_polls и выполняем команду docker-compose up --build
4. В другой консоли заходим в докер: docker exec -it user_polls_web_1 sh
5. Создаем суперпользователя: ./manage.py createsuperuser
6. Заходим в админку http://0.0.0.0:8000/admin/
7. Можно добавить опросы/вопросы 
8. http://0.0.0.0:8000/v1/ - список API адресов, созданный согласно логике задания:

{

    "poll": "http://0.0.0.0:8000/v1/poll/",
    
    "question": "http://0.0.0.0:8000/v1/question/",
    
    "answers": "http://0.0.0.0:8000/v1/answers/",
    
    "client_poll": "http://0.0.0.0:8000/v1/client_poll/"
}

http://0.0.0.0:8000/v1/poll/


{

    "count": 2,
    
    "next": null,
    
    "previous": null,
    
    "results": [
    
        {
        
            "id": 2,
            
            "title": "Вы любите сок?2",
            
            "start_date": "2021-08-20T16:01:18Z",
            
            "end_date": null,
            
            "description": "Вкусный2"
            
        },
        {
        
            "id": 1,
            
            "title": "Вы любите сок?",
            
            "start_date": "2021-08-20T16:37:37Z",
            
            "end_date": "2021-08-21T18:43:42Z",
            
            "description": "Вкусный и свежий"
            
        }
    ]
}

http://0.0.0.0:8000/v1/question/

{
    "count": 1,
    
    "next": null,
    
    "previous": null,
    
    "results": [
    
        {
            "id": 3,
            
            "text": "qwr",
            
            "type_of_answer": 0,
            
            "possible_answers": [
            
                {
                
                    "test": "test"
                    
                },
                
                {
                
                    "test": "test"
                    
                },
                
                {
                
                    "test": "test"
                    
                }
                
            ],
            
            "poll": 3
        }
    ]
}


http://0.0.0.0:8000/v1/answers/

{

    "count": 1,
    
    "next": null,
    
    "previous": null,
    
    "results": [
    
        {
        
            "id": 4,
            
            "client_id": 1,
            
            "answer": {
            
                "1": 123
                
            },
            
            "question": 7
            
        }
        
    ]
    
}


http://0.0.0.0:8000/v1/client_poll/

{

    "result": []
    
}


http://0.0.0.0:8000/v1/client_poll/?client_id=1


{
    "result": [
    
        {
        
            "poll": "rrrrr",
            
            "url": "#1123",
            
            "answs": [
            
                {
                
                    "url": "#1123",
                    
                    "quest": "wqtwqt",
                    
                    "answ": "1 {'1': 123}"
                    
                }
                
            ]
            
        }
        
    ]
    
}












