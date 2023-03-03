import statistics
class Movie:
    all = []
    def __init__(self, title):
        self.title = title
        self.reviews = []
        self.reviewers = []
        Movie.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception('Title must be a string of >0 characters')

    def average_rating(self):
        # sum = 0
        # for review in self.reviews:
        #     sum += review.rating
        # ave = sum / len(self.reviews)
        # return ave
        return statistics.mean([review.rating for review in self.reviews]) 

    @classmethod
    def highest_rated(cls):
        # get all movie rating find the highest then its title
        return max(cls.all.review.get(cls.title))
