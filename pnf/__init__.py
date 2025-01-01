# src/__init__.py
__version__ = '0.1.0'

from scipy.constants import nu2lambda


def separation_distance(frequency: float, closer: bool = False) -> float:
    """
    Minimum recommended separation distance for near-field antenna measurements in meters.

    Parameters
    ----------
    frequency : float
        Frequency of interest in Hertz [Hz].
    closer : bool, optional
        Closer approximation using 3 wavelength calculation (default is False).

    Returns
    -------
    float
        Minimum distance in meters.

    Notes
    -----
    Standard suggests to choose between 3 or 5 wavelengths.
    In order to ensure coupling effect, 5 wavelength distance is chosen and implemented. 
    3 wavelength is optional.

    References
    ----------
    .. [1] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.3.1.4, Page 27.
    """
    if closer:
        return 3 * nu2lambda(frequency)
    return 5 * nu2lambda(frequency)

def sampling_spacing(frequency: float) -> float:
    r"""
    Maximum sampling length for near-field antenna measurements.

    Parameters
    ----------
    frequency : float
        Frequency of interest in Hertz [Hz].

    Returns
    -------
    float
        Maximum sampling length in meters.

    References
    ----------
    .. [1] IEEE 149-2021 Recommended Practice for Antenna Measurements, Section 12.5, Page 135.
    .. [2] IEEE 1720-2012 Recommended Practice for Near-Field Antenna Measurements, Section 5.2.5, Page 23, Equation 25.

    Formula
    -------
    .. math::
        \Delta = \lambda / 2 = 0.5 \times (c_0 / f)
    """
    return 0.5 * nu2lambda(frequency)

__all__ = [
  '__version__', 
  'separation_distance', 
  'sampling_spacing'
]