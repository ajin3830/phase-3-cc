from movie import Movie
from viewer import Viewer
class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        self.add_review_to_viewer()

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int) and 1<= rating <=5:
            self._rating = rating
        else:
            raise Exception('Rating must be integers between 1 and 5 characters, inclusive')

    @property
    def viewer(self):
        return self._viewer
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception('Viewer must be an instance of Viewer')
        
    @property
    def movie(self):
        return self._movie
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception('Movie must be an instance of Movie')

    def add_review_to_viewer(self):
        if self._review not in self._viewer.reviews:
            self._viewer.reviews.append(self._review)