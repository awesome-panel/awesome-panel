"""In this module we test the PerformanceCurve model"""
import datetime

from src.pages.gallery.training_analysis.models.performance_curve import \
    PerformanceCurve


def test_constructor():
    """A PerformanceCurve model exists and can be constructed"""
    # Given
    performance = 100
    date = datetime.date(2019, 1, 1)
    # When
    actual = PerformanceCurve(one_sec=performance, one_sec_date=date)
    # Then
    assert actual.one_sec == performance
    assert actual.one_sec_date == date
