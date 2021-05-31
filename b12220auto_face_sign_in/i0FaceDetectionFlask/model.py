from datetime import date, datetime
from typing import List, Iterable
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0
        self.id = self.__user_name

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    # @property
    # def watched_movies(self) -> list:
    #     return self.__watched_movies

    # @property
    # def reviews(self) -> list:
    #     return self.__reviews

    # @property
    # def time_spent_watching_movies_minutes(self) -> int:
    #     return self.__time_spent_watching_movies_minutes

    # def watch_movie(self, movie: Movie):
    #     if isinstance(movie, Movie):
    #         self.__watched_movies.append(movie)
    #         self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    # def add_review(self, review: Review):
    #     if isinstance(review, Review):
    #         self.__reviews.append(review)

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.user_name == self.__user_name

    def __lt__(self, other):
        return self.__user_name < other.user_name

    def __hash__(self):
        return hash(self.__user_name)