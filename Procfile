% prepara el repositorio para su despliegue. 
release: sh -c 'cd decide && python manage.py makemigrations && python manage.py migrate'
% especifica el comando para lanzar Decide
web: sh -c 'cd decide &&  python manage.py makemessages -l es && python manage.py makemessages -l ca && python manage.py compilemessages && gunicorn decide.wsgi --log-file -'