class Viewer:
    
    def __init__(self, username):
        self.username = username
        self.reviews = []
        self.reviewed_movies = []
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        # if username is unique set it; else raise exception
        # if username not in Viewer.username:
            if isinstance(username, str) and 6<= len(username) <=16 :
                self._username = username
            else:
                raise Exception('Username must be a string between 6 and 16 characters, inclusive')
        # else: 
        #   raise Exception('Username must be unique')

    def reviewed_movie(self, movie):
        # if isinstance(movie, Movie):
        #   return True
        # else
        #   return False
        pass
    def rate_movie(self, movie, rating):
        from review import Review
        Review(self, movie, rating)
        