from django.utils.translation import ugettext_lazy as _
from django.db import IntegrityError

from codeschool import models
from codeschool.utils.phrases import phrase
<<<<<<< HEAD
=======
from itertools import cycle
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049


class SpartaGroup(models.TimeStampedModel):
    """
    Represents a group of students in a Sparta activity.
    """

    STATUS_ACTIVE = 0
    STATUS_INACTIVE = 1

    activity = models.ForeignKey('SpartaActivity', related_name='groups')
    name = models.CharField(
        _('Name'),
        blank=True,
        max_length=140,
    )
    status = models.IntegerField(
<<<<<<< HEAD
        default = STATUS_INACTIVE,
=======
        default=STATUS_INACTIVE,
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049
        choices=[
            (STATUS_INACTIVE, _('inactive')),
            (STATUS_ACTIVE, _('active')),
        ]
    )
    members = models.ManyToManyField(
        models.User,
        through='SpartaMembership',
        related_name='sparta_groups'
    )

    @property
    def learner(self):
        role = SpartaMembership.ROLE_LEARNER
        return SpartaMembership.objects.filter(group=self, role=role)

    @property
    def tutors(self):
        role = SpartaMembership.ROLE_TUTOR
        return SpartaMembership.objects.filter(group=self, role=role)

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        unique_together = [
            ('name', 'activity'),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            return super().save(*args, **kwargs)

        max_iter = 10
        for n in range(max_iter):
            try:
                self.name = phrase()
                return super().save(*args, **kwargs)
            except IntegrityError:
                if n == max_iter - 1:
                    raise

<<<<<<< HEAD
    def add_user(self, user, role):
=======
    def add_users(self, users, quantity_tutors):
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049
        """
        Add new user to group.

        Args:
             user:
                A django user.
             role (str):
                The user role on the group 'learner' or 'tutor'.
        """
<<<<<<< HEAD

        role = ROLE_MAPPING[role]
        SpartaMembership.objects.create(group=self, user=user, role=role)
=======
        # Irá atribuir a role tutor ao usuario com maior nota, adiciona-lo ao grupo e exclui-lo do dicionario
        for _ in quantity_tutors:
            user_grade_max = max(users, key=users.get)
            role = ROLE_MAPPING[ROLE_TUTOR]
            SpartaMembership.objects.create(group=self, user=user_grade_max, role=role)
            users.pop(user_grade_max)

        # Irá adicionar a role learner aos usuarios restantes, adiciona-los ao grupo e excluir do dicionario
        for user in users:
            role = ROLE_MAPPING[ROLE_LEARNER]
            SpartaMembership.objects.create(group=self, user=user, role=role)
            users.pop(user)
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049


class SpartaMembership(models.TimeStampedModel):
    """
    Describes the membership relation for each group
    """

    ROLE_TUTOR = 0
    ROLE_LEARNER = 1

    user = models.ForeignKey(models.User, related_name='+')
    group = models.ForeignKey(SpartaGroup, related_name='+')
    role = models.IntegerField(
        choices=[
            (ROLE_TUTOR, _('tutor')),
            (ROLE_LEARNER, _('learner')),
        ]
    )

    class Meta:
        unique_together = [
            ('user', 'group', 'role'),
        ]

ROLE_MAPPING = {
    'learner': SpartaMembership.ROLE_LEARNER,
    'tutor': SpartaMembership.ROLE_TUTOR,
}


<<<<<<< HEAD
def organize_groups(users, group_size):
=======
def organize_groups(mapping, group_size):
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049
    """
    Receives a mapping from users to grades and return a list of groups
    with the approximate ``group_size``.

    It tries to match users with the best grades with the users with the
    worst grades.

    Args:
        mapping (map):
            A dictionary from users to their respective grades.
        group_size (int):
            The desired group size.
<<<<<<< HEAD

=======
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049
    Examples:

        >>> users = {'john': 10, 'paul': 9, 'george': 8, 'ringo': 6}
        >>> organize_groups(users, 2)
<<<<<<< HEAD
        [['john', 'ringo'], ['paul', 'george']]
    """
    assert isinstance(group_size, int)

    users_quantity = len(users)

    # Cannot create group if group_size is greater than users quantity
    assert group_size <= users_quantity

    possible_groups_quantity = users_quantity // group_size
    remaining_users = users_quantity % group_size

    # from collections import OrderedDict
    # Put the grades as the keys of dict
    # users_with_grade_as_key = {grade: user for user, grade in users.items()}
    # sorted_users = OrderedDict(sorted(users_with_grade_as_key.items()))

    # Initialize possible groups as empty lists
    grouped_users = []
    for n in range(possible_groups_quantity):
        grouped_users.append([])

    new_remaing_users = users # 5
    while len(new_remaing_users) > remaining_users:
        new_remaing_users = group_users(grouped_users, new_remaing_users)
        # 1 => grouped_users = [[]]
        # 1 => grouped_users = [[1, 2]]


def group_users(users_groups, users):
    users_copy = users
    for group in users_groups:
        max_grade_user, users_dict = get_max_grade_user(users_copy)
        min_grade_user, new_users_dict = get_max_grade_user(users_dict)
        group.append(max_grade_user)
        group.append(min_grade_user)
        users_copy = new_users_dict
    return users_copy


def get_max_grade_user(users):
    new_users_dict = users
    for user, grade in users.items():
        if grade is max(users.values()):
            del new_users_dict[user]
            return (user, new_users_dict)
    return


def get_min_grade_user(users):
    new_users_dict = users
    for user, grade in users.items():
        if grade is min(users.values()):
            del new_users_dict[user]
            return (user, new_users_dict)
    return
=======
        [{'john': 10,'ringo': 6}, {'paul': 8, 'george': 8}]
    """
    users_quantity = len(mapping)

    if group_size > users_quantity:
        return [mapping.copy()]

    n_groups = users_quantity // group_size
    remaining_users = users_quantity % group_size

    # Initialize possible groups as empty lists
    groups = [{} for _ in range(n_groups)]

    sorted_users = sorted(mapping.items(), key=lambda x: x[1])

    for idx in cycle([0, -1]):
        if len(sorted_users) < n_groups:
            break

        for i in range(n_groups):
            name, grade = sorted_users.pop(idx)
            groups[i][name] = grade

    j = 0
    for i, user in enumerate(sorted_users):
        name = user[0]
        grade = user[1]
        if j == n_groups:
            j = 0
        groups[j][name] = grade
        j += 1
    return groups
>>>>>>> 62c2cd64b57e514e7e0a4d2cca057db3222c9049
