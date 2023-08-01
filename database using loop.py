import sqlite3

db = sqlite3.connect("app.db")

cr = db.cursor()

cr.execute(
    "create table if not exists users (user_id integer, name text)")

cr.execute(
    "create table if not exists skills (name text, progress integer, user_id integer)")

mylist = {"ahmed", "sayed", "gamal", "osama", "eslam"}

for key, user in enumerate(mylist):
    cr.execute(f"insert into users(user_id, name) values({key+1}, '{user}')")

db.commit()


db.close()