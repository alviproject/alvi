from alvi.config.settings import default_scenes

default_scenes += [
    #scenes from following location are ignored in VCS, you can use this location as a playground
    'alvi.client.local_scenes.sample_scene_that_will_not_be_versioned',
]

#define some other options... (see alvi/config/settings.py for a list of all used options)