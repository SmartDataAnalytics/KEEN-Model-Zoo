# -*- coding: utf-8 -*-

"""KEEN Model Zoo.

Run the web application with:

.. code-block:: sh

   $ python zoo.py run

Register a user with:

.. code-block:: sh

   $ python zoo.py createuser EMAIL PASSWORD

Upload a KEEN folder with:

.. code-block:: sh

   $ python zoo.py upload EMAIL DIRECTORY
"""

from __future__ import annotations

import datetime
import json
import os
from typing import Optional

import click
import flask_admin
import flask_bootstrap
import requests
from easy_config import EasyConfig
from flask import Flask, jsonify, request
from flask_admin.contrib.mongoengine import ModelView
from flask_mongoengine import MongoEngine
from flask_security import MongoEngineUserDatastore, RoleMixin, Security, UserMixin
from mongoengine.fields import (
    BooleanField, DateTimeField, DictField, FloatField, ListField, ReferenceField, StringField,
)


class ZooConfig(EasyConfig):
    """Configuration for the model zoo."""

    NAME = 'keen_zoo'
    FILES = []

    debug: bool = True
    secret_key: str = 'super-secret-key'

    # Flask-Security configuration
    security_password_hash: str = 'pbkdf2_sha512'
    security_password_salt: str = 'super-secret-salt'

    # Flask-MongoEngine configuration
    mongodb_db: str = 'test'
    mongodb_host: str = 'localhost'
    mongodb_port: int = 27017
    mongodb_username: Optional[str] = None
    mongodb_password: Optional[str] = None


zoo_config = ZooConfig.load(_parse_environment=True)

# Create app
app = Flask(__name__)
app.config['DEBUG'] = zoo_config.debug
app.config['SECRET_KEY'] = zoo_config.secret_key

# Flask Security Config
app.config['SECURITY_PASSWORD_HASH'] = zoo_config.security_password_hash
app.config['SECURITY_PASSWORD_SALT'] = zoo_config.security_password_salt

# MongoDB Config
app.config['MONGODB_SETTINGS'] = {
    'db': zoo_config.mongodb_db,
    'host': zoo_config.mongodb_host,
    'port': zoo_config.mongodb_port,
}

if zoo_config.mongodb_username is not None:
    app.config['MONGODB_USERNAME'] = zoo_config.mongodb_username

if zoo_config.mongodb_password is not None:
    app.config['MONGODB_PASSWORD'] = zoo_config.mongodb_password

# Create database connection object
db = MongoEngine(app)


class Role(db.Document, RoleMixin):
    """A document representing a role."""

    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)


class User(db.Document, UserMixin):
    """A document representing a user."""

    email = StringField(max_length=255)
    password = StringField(max_length=255)
    active = BooleanField(default=True)
    confirmed_at = DateTimeField()
    roles = ListField(ReferenceField(Role), default=lambda: [])

    def __str__(self):
        return f'User(email={self.email})'


class Embedding(db.Document):
    """A document representing an embedding."""

    identifier = StringField(max_length=255)
    embedding = ListField(FloatField())

    def __str__(self):
        return f'Embedding(identifier={self.identifier}, embedding={self.embedding})'


class Run(db.Document):
    """A document representing the results of training a KGE Model."""

    upload_time = DateTimeField(default=datetime.datetime.utcnow)
    user = ReferenceField(User)
    configuration = DictField()
    embeddings = ListField(ReferenceField(Embedding))


# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Setup Flask-Boostrap
flask_bootstrap.Bootstrap(app)

# Setup Flask-Admin
admin = flask_admin.Admin(app, 'KEEN Model Zoo', url='/')
admin.add_view(ModelView(Run))
admin.add_view(ModelView(Embedding))
admin.add_view(ModelView(User))


@app.route('/upload', methods=['POST'])
def upload_kge_model():
    """Upload a KGE model."""
    email = request.json['email']
    user = user_datastore.find_user(email=email)
    if user is None:
        return jsonify(failure=True), 400

    embedding_documents = []
    for identifier, embedding in request.json['embeddings'].items():
        embedding_document = Embedding(identifier=identifier, embedding=embedding)
        embedding_document.save()
        embedding_documents.append(embedding_document)

    kge_model = Run(
        user=user,
        configuration=request.json['configuration'],
        embeddings=embedding_documents,
    )
    kge_model.save()

    return jsonify(
        identifier=repr(kge_model.id),
    )


@click.group()
def main():
    """KEEN Model Zoo."""


@main.command()
@click.option('--host', default='localhost')
@click.option('--port', default=5000)
def run(host, port):
    """Run the web application."""
    app.run(host=host, port=port)


@main.command()
@click.argument('email')
@click.argument('password')
def createuser(email: str, password: str):
    """Create a user."""
    user_datastore.create_user(email=email, password=password)


@main.command()
@click.argument('email')
@click.argument('directory', type=click.Path(dir_okay=True, file_okay=False))
@click.option('-h', '--host', default='http://localhost:5000')
def upload(email: str, directory: str, host: str):
    """Upload a KEEN results directory."""
    config_path = os.path.join(directory, 'configuration.json')
    embeddings_path = os.path.join(directory, 'entities_to_embeddings.json')
    assert os.path.exists(config_path)
    assert os.path.exists(embeddings_path)

    with open(embeddings_path) as file:
        embeddings = json.load(file)

    with open(config_path) as file:
        configuration = json.load(file)

    res = requests.post(
        f"{host.rstrip('/')}/upload",
        json=dict(
            email=email,
            configuration=configuration,
            embeddings=embeddings,
        ),
    )
    click.echo(res.status_code)
    click.echo(res.json())


if __name__ == '__main__':
    main()
