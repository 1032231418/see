#coding=utf-8
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views.settings import ForbiddenWordsViewSet, StrategyViewSet, PersonalSettingsViewSet
from .views.inception_check import InceptionCheckView
from .views.select_data import SelectDataView
from .views.target_db import DbViewSet
from .views.workorder_main import InceptionMainView
from .views.auth_rules import AuthRulesViewSet
from .views.suggestion import SuggestionViewSet

router = DefaultRouter()
router.register(r'dbconfs', DbViewSet, base_name='DbViewSet')
router.register(r'inceptions', InceptionMainView, base_name='InceptionMainView')
router.register(r'inceptioncheck', InceptionCheckView, base_name='InceptionCheckView')
router.register(r'autoselects', SelectDataView, base_name='SelectDataView')
router.register(r'forbiddenwords', ForbiddenWordsViewSet, base_name='ForbiddenWordsViewSet')
router.register(r'strategy', StrategyViewSet, base_name='StrategyViewSet')
router.register(r'personalsettings', PersonalSettingsViewSet, base_name='PersonalSettingsViewSet')
router.register(r'authrules', AuthRulesViewSet, base_name='AuthRulesViewSet')
router.register(r'suggestion', SuggestionViewSet, base_name='SuggestionViewSet')

urlpatterns = [
    url(r'^', include(router.urls)),
]
