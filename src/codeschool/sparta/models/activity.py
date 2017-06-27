<<<<<<< HEAD
from django.utils.translation import ugettext_lazy as _

from codeschool import models
=======
from codeschool import models
from django.utils.translation import ugettext_lazy as _
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049
from codeschool.lms.activities.models import Activity
from django.core.validators import MinValueValidator, MaxValueValidator


class SpartaActivity(Activity):
    """
    Represents a sparta activity.
    """
    description = models.TextField()

    class Meta:
        verbose_name = _('Sparta Activity')
        verbose_name_plural = _('Sparta Activities')

    def populate_from_csv(self, csv_data):
        """
        Parse CSV data and populate the user grades.
<<<<<<< HEAD
        
        Args:
            csv_data (str): 
=======

        Args:
            csv_data (str):
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049
                A CSV file with two columns. The first column must be username
                and the second column is a grade in [0..100]
        """


class UserGrade(models.Model):
    """
    Represents a user with your grade.
    """
    grade = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    activity = models.ForeignKey(SpartaActivity)
    user = models.ForeignKey(models.User)

    class Meta:
        unique_together = [('activity', 'user')]
<<<<<<< HEAD
=======

>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049
