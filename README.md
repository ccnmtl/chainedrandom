# chainedrandom

This is a simple drop-in replacement for a subset of the functionality
of ccnmtl/twisterclient.

Twisterclient was a client library for the ccnmtl/twister random
number generation HTTP service. That was developed to provide
consistent, flexible chained random number generation to all of our
applications, independent of language/platform. It was great, but
ultimately more than necessary for the majority of use-cases. What we
discovered was that almost all of the simulations we were building
just used simple uniform distributions for basic stochastic
processes. For those cases, relying on an external webservice just
complicated things. So this library is a drop-in replacement for
twisterclient that has no external dependencies and only does very
basic chained generation of uniform random numbers.
