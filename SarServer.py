from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import UserSettableParameter

from SarModel import SearchAndRescue
from SarAgent import Unit
from SarEnvironment import Environment
from SarAgent import MissingPerson


def portrayal_method(agent):
    """ Defines how a cell in the grid will be portrayed. All cells contain an environment agent with an attribute for
    the current. According to this parameter the cell will be shown in a certain shade of blue. If a cell also contains
    an unit agent of missing person agent, in a higher layer this will be shown with a circle. Black for the missing
    person and red for the looking unit"""

    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Layer": 0,
                 "Color": "yellow",
                 "r": 1}

    if isinstance(agent, Environment):
        if agent.current != 0:
            portrayal["Color"] = 'blue'

    if isinstance(agent, Unit):
        portrayal["Color"] = 'red'
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5

    if isinstance(agent, MissingPerson):
        portrayal["Color"] = "black"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5

    return portrayal


grid = CanvasGrid(portrayal_method, 90, 60, 900, 600)


params = {
    "height": 90,
    "width": 60,
    "search_pattern": UserSettableParameter('choice', "Zoekpatroon", value='Parallel Sweep',
                                            choices=['Parallel Sweep',
                                                     'Expanding Square',
                                                     'Sector Search',
                                                     'Random Search']),
    "search_radius": UserSettableParameter("slider", "Search radius (in 10m)", 5, 3, 20, 1),
    "max_current": UserSettableParameter("slider", "maximum current in riptide (m/s)", 10, 1, 20, 1)
}

server = ModularServer(SearchAndRescue, [grid], "Sar Model", params)
