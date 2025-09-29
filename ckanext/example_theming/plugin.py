from __future__ import annotations

from typing import Any
from typing_extensions import override
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import os

root = os.path.dirname(os.path.abspath(__file__))


class ExampleThemingPlugin(plugins.ITheme, plugins.IConfigurer, plugins.SingletonPlugin):
    @override
    def update_config(self, config: Any):
        toolkit.add_template_directory(config, "templates")
        toolkit.add_public_directory(config, "public")
        toolkit.add_resource("assets", "example_theming")

    @override
    def register_themes(self) -> dict[str, dict[str, Any]]:
        return {
            "bare": {
                "path": os.path.join(root, "themes/bare"),
            },

        }
