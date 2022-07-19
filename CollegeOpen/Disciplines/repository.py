from django.db import models



class DisciplineQueryset(models.QuerySet):

    def reviews(self, discipline_id):
        return self.filter(reviews__discipline=discipline_id)\
                .values('reviews__score', 'reviews__message')
    
    def stats(self, discipline_id):
        return self.filter(reviews__discipline=discipline_id)\
            .aggregate(
                average_reviews=models.Avg('reviews__score'), 
                total_reviews=models.Count('reviews__score')
            ) 