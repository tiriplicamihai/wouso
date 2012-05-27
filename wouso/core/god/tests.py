from django.contrib.auth.models import User, Group
from django.test import TestCase
from . import get_god
from wouso.core.user.models import PlayerGroup
from wouso.games.challenge.models import ChallengeGame


__author__ = 'alex'


class GodTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testgod')
        self.player = self.user.get_profile()

    def test_others_are_not_elligible_for_challenge(self):
        god = get_god()
        group, new = Group.objects.get_or_create(name="Others")
        others, new = PlayerGroup.objects.get_or_create(name="Others", group=group)

        self.player.groups.add(others)
        self.assertFalse(god.user_is_eligible(self.player, ChallengeGame))

    def test_users_are_elligible_for_challenge(self):
        god = get_god()
        self.assertTrue(god.user_is_eligible(self.player, ChallengeGame))




