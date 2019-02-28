# See https://www.mkdocs.org/user-guide/plugins/#developing-plugins

import mkdocs
from mkdocs.config import config_options, Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation as MkDocsNavigation

from pathlib import Path
import yaml



class MultiplePlugin(BasePlugin):

    config_scheme = (
        ('parent', mkdocs.config.config_options.Type(mkdocs.utils.string_types)),
    )

    def __init__(self):
        super().__init__()


    def on_config(self, config, **kwargs):
        parent_config = Path(self.config['parent']) / "mkdocs.yml"
        if not parent_config.is_file():
            raise Exception(f"{parent_config} is not a valid file")

        with parent_config.open("r") as fp:
            parent = yaml.load(fp)

        # Merge nav
        nav = config["nav"]
        for value in parent["nav"]:
            nav.append(value)
        
        return config

    def on_files(self, files, **kwargs):
        return files
    def on_post_build(self, markdown):
        pass