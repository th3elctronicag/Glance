import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
db = SQL("sqlite:///finance.db")

x = db.execute("SELECT shares FROM balance WHERE username = (SELECT username FROM users WHERE id = ?)", 2)[0]
print(x)