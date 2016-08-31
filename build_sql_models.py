#sqlacodegen postgresql:///some_local_db
#sqlacodegen mysql+oursql://user:password@localhost/dbname
#sqlacodegen sqlite:///database.db

import sqlacodegen
sqlacodegen postgresql:///some_local_db
sqlacodegen mysql+oursql://ubuntu:hello@localhost/chad_db
sqlacodegen sqlite:///database.db