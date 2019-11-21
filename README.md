babynames.py
The Social Security Administration maintains an annual list of all new baby names. The lists are available for download from https://www.ssa.gov/oact/babynames/limits.html; we have given you the national year-by-year lists in the babies subdirectory. The file NationalReadMe.pdf in that directory documents the format used by the SSA. babynames.py is a program that identifies the 100 most commonly used male and female baby names from 1880 through 2016 (i.e, the names given to the most total babies).

{"male": [{"name": "mario", "count": 500000}, {"name": "luigi", "count": 300000}, {"name": "wario", "count": 1}], "female": [ {"name": "peach", "count": 400000}, {"name": "toadette", "count": 250000}]

flights.py
We have given you a dataset of airports around the world in the file airports.json. flights.py is a program which takes as a command-line argument the IATA code for an airport (e.g. EWR for Newark Liberty International) and prints out a list of airports one can connect to from that airport, sorted in order of distance from nearest to farthest.

$ python flights.py ITH
EWR Newark Liberty Intl 276km
PHL Philadelphia Intl 308km
DTW Detroit Metro Wayne Co 568km
