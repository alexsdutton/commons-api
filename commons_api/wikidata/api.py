from rest_framework.routers import DefaultRouter

from . import viewsets

router = DefaultRouter()

router.register('country', viewsets.CountryViewSet)
router.register('electoral-district', viewsets.ElectoralDistrictViewSet)
router.register('legislative-house',
                viewsets.LegislativeHouseViewSet,
                base_name='legislativehouse')
router.register('legislative-house/memberships',
                viewsets.LegislativeHouseMembershipViewSet,
                base_name='legislativehouse-memberships')
