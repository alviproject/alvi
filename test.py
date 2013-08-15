from playground import service
from playground.scenes import Booble
from playground.scenes import BoobleCartesian

N = 10  # number of points and max value of the point
service.register_scene(Booble(N))
service.register_scene(BoobleCartesian(N))
service.run()
